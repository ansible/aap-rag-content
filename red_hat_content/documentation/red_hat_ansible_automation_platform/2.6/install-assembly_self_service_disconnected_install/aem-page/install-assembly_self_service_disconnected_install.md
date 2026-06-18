+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_self_service_disconnected_install"
title = "Install Ansible automation portal in air-gapped OpenShift Container Platform environments - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_self_service_about/", "Install Ansible automation portal (OpenShift Container Platform only)"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_self_service_disconnected_install/aem-page/install-assembly_self_service_disconnected_install.html"
last_crumb = "Install Ansible automation portal in air-gapped OpenShift Container Platform environments"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Install Ansible automation portal in air-gapped OpenShift Container Platform environments"
oversized = "false"
page_slug = "install-assembly_self_service_disconnected_install"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_self_service_disconnected_install"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_self_service_disconnected_install/toc/toc.json"
type = "aem-page"
+++

# Install Ansible automation portal in air-gapped OpenShift Container Platform environments

You can install Ansible automation portal in a disconnected OpenShift Container Platform environment. For new installations, use OCI container delivery and mirror required container images and plug-in artifacts to your internal registry.

## Prerequisites for disconnected installation

Review the mandatory subscriptions, permissions, and platform access required before starting the disconnected installation of the Ansible automation portal.

Fulfilling these prerequisites helps ensure a successful deployment.

- You have a valid subscription to Red Hat Ansible Automation Platform.
- You have access to an instance of Red Hat Ansible Automation Platform with the appropriate permissions to create an OAuth application.
- You have access to a Red Hat OpenShift Container Platform instance with the appropriate permissions within your project to create an application.
- You have installed `oc`, the OpenShift command-line interface (CLI) tool, on your local machine.
- You have installed Helm 3.10 or newer.
- You have installed `skopeo` and `podman` for mirroring container images and plug-in artifacts.
- You have internet access to pull images and charts from public repositories, including `registry.redhat.io`.
- A Red Hat pull secret that allows you to pull images from `registry.redhat.io`.
- You have a method to provide the Ansible plug-ins in the disconnected environment:
  * For OCI delivery: A method to mirror the OCI artifacts image referenced by `imageTagInfo`.
  * For HTTP plug-in registry: The ability to host the plug-in tarball files.
- You have registry credentials for the registry endpoint used by the dynamic plug-in installer.


Important:

The image versions and compatibility requirements vary between Helm chart releases. Before you begin, consult the [Ansible Automation Portal Lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page for version mappings between the Helm chart, Red Hat Developer Hub, and PostgreSQL.

## Prepare for air-gapped installation

Before you can install Ansible automation portal in a disconnected OpenShift Container Platform environment, you must complete some processes on a connected bastion host.

## Mirror container images

Use `skopeo copy` to mirror the required container images from the Red Hat registry to your disconnected registry for installing the Ansible automation portal in an isolated environment.

### Before you begin

- `skopeo` is installed.
- You have authenticated to `registry.redhat.io`:

```terminal
$ skopeo login registry.redhat.io
```

- You have authenticated to your disconnected registry:

```terminal
$ skopeo login <disconnected_registry_url>
```

### About this task

`skopeo copy` preserves SHA256 digests, so the Helm chart's default digest-based image references work without additional tag overrides.

If you mirror `registry.redhat.io` content to a different registry host (or to a registry prefix such as `quay.io/<org>`), you can set `redhat-developer-hub.global.imageRegistry` so the Helm chart pulls all of its images from that mirrored location. `imageRegistry` is a single override that controls the registry for the base application image, PostgreSQL image, OCI plug-in artifacts, and Ansible Dev Tools sidecar.

The dynamic plug-in init container does not use cluster-level image mirror configuration (for example, `ImageDigestMirrorSet` or `ImageTagMirrorSet`). You must set `imageRegistry` even if your cluster redirects `registry.redhat.io` pulls.

*Table 1. Required container images*

| Image                                                                                                                              | Source registry      | Purpose                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------ |
| `rhdh/rhdh-hub-rhel9:<rhdh_version>`                                                                                               | `registry.redhat.io` | Red Hat Developer Hub application and `install-dynamic-plugins` init container       |
| `rhel9/postgresql-<version>:<tag>`                                                                                                 | `registry.redhat.io` | Built-in PostgreSQL database (skip if using an external database)                    |
| `ansible-automation-platform-25/ansible-dev-tools-rhel8:latest` or `ansible-automation-platform-26/ansible-dev-tools-rhel9:latest` | `registry.redhat.io` | Ansible Dev Tools sidecar (base image varies by Ansible Automation Platform version) |
| `ansible-automation-platform/automation-portal:<plugin-version>`                                                                   | `registry.redhat.io` | Ansible plug-in OCI artifacts (OCI delivery only)                                    |
| `rhdh/rhdh-plugin-catalog-index-rhel9:<rhdh_version>`                                                                              | `registry.redhat.io` | Plug-in catalog index (rebuilt by `mirror-plugins.sh`)                               |


Replace version placeholders with the versions bundled with your Helm chart. See the [Ansible Automation Portal Lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page for version mappings.

### Procedure

1.  Copy the Red Hat Developer Hub hub image to your disconnected registry:
  

```terminal
$ skopeo copy \
    docker://registry.redhat.io/rhdh/rhdh-hub-rhel9:<rhdh_version> \
    docker://<disconnected_registry_url>/rhdh/rhdh-hub-rhel9:<rhdh_version>
```
    This image is used for both the main application container and the `install-dynamic-plugins` init container. Replace `<rhdh_version>` with the Red Hat Developer Hub version bundled with your Helm chart.

2.  If you use the built-in PostgreSQL database, copy the PostgreSQL image.
      An external database is the supported production architecture and does not require this step.

```terminal
$ skopeo copy \
    docker://registry.redhat.io/rhel9/postgresql-<version>:<tag> \
    docker://<disconnected_registry_url>/rhel9/postgresql-<version>:<tag>
```
    Replace `<version>` with the PostgreSQL major version and `<tag>` with the image tag bundled with your Helm chart. See the [Ansible Automation Portal Lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page for version mappings.

3.  Copy the plug-in catalog index image:
  

```terminal
$ skopeo copy \
    docker://registry.redhat.io/rhdh/rhdh-plugin-catalog-index-rhel9:<rhdh_version> \
    docker://<disconnected_registry_url>/rhdh/rhdh-plugin-catalog-index-rhel9:<rhdh_version>
```
    The Mirror dynamic plug-in artifacts procedure rebuilds this image with updated registry references. You must still mirror the original image because the script uses it as its source.

4.  If you use OCI container delivery, copy the Ansible plug-ins OCI artifacts image:
  

```terminal
$ skopeo copy \
    docker://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version> \
    docker://<disconnected_registry_url>/ansible-automation-platform/automation-portal:<plugin-version>
```

5.  Copy the Ansible Dev Tools sidecar image, using the path that matches your Ansible Automation Platform version.
      **Ansible Automation Platform 2.5:**

```terminal
$ skopeo copy \
    docker://registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest \
    docker://<disconnected_registry_url>/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest
```
    **Ansible Automation Platform 2.6:**

```terminal
$ skopeo copy \
    docker://registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest \
    docker://<disconnected_registry_url>/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest
```

### Results

Verify that each image is accessible in your disconnected registry. For example:

```terminal
$ skopeo inspect docker://<disconnected_registry_url>/rhdh/rhdh-hub-rhel9:<rhdh_version>
```
A successful response returns the image manifest metadata. An error indicates the image was not mirrored correctly.

## Mirror dynamic plug-in artifacts

In Red Hat Developer Hub 1.9 and later, dynamic plug-ins are distributed as OCI artifacts referenced by a plug-in catalog index. In a disconnected environment, mirror these artifacts and rebuild the catalog index with updated registry references.

### Before you begin

- `skopeo` 1.20 or later is installed.
- `podman` 5.6 or later is installed.
- `jq` 1.7 or later is installed.
- GNU `tar` 1.35 or later is installed.
- You have authenticated to `registry.redhat.io` and your disconnected registry.

### About this task

Without this step, the `install-dynamic-plugins` init container attempts to pull plug-ins from external registries and fails with `i/o timeout` errors.

Use the `mirror-plugins.sh` script from the Red Hat Developer Hub operator repository to mirror the plug-in artifacts.

### Procedure

1.  Download the `mirror-plugins.sh` script from the Red Hat Developer Hub operator repository:
  

```terminal
$ curl -LO https://raw.githubusercontent.com/redhat-developer/rhdh-operator/release-<rhdh_version>/.rhdh/scripts/mirror-plugins.sh
$ chmod +x mirror-plugins.sh
```
    Replace `<rhdh_version>` with the Red Hat Developer Hub version bundled with your Helm chart. See the [Ansible Automation Portal Lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page for version mappings.

2.  Mirror the plug-in catalog index and all referenced plug-in artifacts to your disconnected registry:
  

```terminal
$ ./mirror-plugins.sh \
  --plugin-index oci://registry.redhat.io/rhdh/rhdh-plugin-catalog-index-rhel9:<rhdh_version> \
  --to-registry <disconnected_registry_url>
```
    The script copies all OCI plug-in artifacts, rewrites the catalog index with your mirror registry URLs, and pushes the updated index to your disconnected registry.

3.  If your disconnected environment has no direct network path to the connected bastion host, use the export-then-import workflow.
  1.  On the connected bastion host, export the plug-in artifacts to a directory:
  

```terminal
$ ./mirror-plugins.sh \
  --plugin-index oci://registry.redhat.io/rhdh/rhdh-plugin-catalog-index-rhel9:<rhdh_version> \
  --to-dir /path/to/plugin-export
```

  2.  Transfer the export directory to a host in the disconnected environment.
  3.  On the disconnected host, import the artifacts into your mirror registry:
  

```terminal
$ ./mirror-plugins.sh \
  --from-dir /path/to/plugin-export \
  --to-registry <disconnected_registry_url>
```

### Results

- Check the `rhdh-plugin-mirroring-summary.txt` file generated by the script. It lists all mirrored artifacts and their destination paths.
- Verify that the catalog index image exists in your disconnected registry:

```terminal
$ skopeo inspect docker://<disconnected_registry_url>/rhdh/rhdh-plugin-catalog-index-rhel9:<rhdh_version>
```

## Download the helm chart package

Download the Helm chart package and modify the internal image references to point to your disconnected registry. This prepares the installation package for the air-gapped environment.

### Procedure

1.  Add the OpenShift Helm charts repository and update your local cache:
  

```
helm repo add openshift-helm-charts https://charts.openshift.io/
helm repo update
```

2.  Pull the required version of the chart:
  

```
helm pull openshift-helm-charts/redhat-rhaap-portal --version x.y.z
```
    The chart is saved as a `.tgz` file (for example, `redhat-rhaap-portal-1.0.1.tgz`).

3.  Extract the chart files:
  

```
tar -xvf redhat-rhaap-portal-x.y.z.tgz
```
    This creates a directory with a name similar to `redhat-rhaap-portal-1.0.1/`.

4.  In the `redhat-rhaap-portal/values.yaml` file, replace all `image:` references with the full path to the images in your disconnected registry.
5.  Repack the chart with your modifications:
  

```
helm package redhat-rhaap-portal-x.y.z
```
    A new `.tgz` file is created containing your changes.

## Transfer assets to the disconnected environment

Transfer the modified Helm chart package from the connected bastion host to a machine inside your disconnected network. This action stages the installation assets for deployment within the isolated OpenShift environment.

### Procedure

1.  Copy the modified Helm chart `.tgz` file or files (for example, `redhat-rhaap-portal-1.0.1.tgz`) from your connected bastion host to a machine or jump box within your disconnected OpenShift network.
2.  If you use the HTTP plug-in registry method, transfer the plug-in tarball files to the disconnected environment.

## Install the Helm chart in the disconnected OpenShift environment

You can install the modified Helm chart using the `helm install` command in your disconnected OpenShift environment. This deploys the Ansible automation portal using the locally available assets.

After preparing the disconnected environment with mirrored images and transferred assets, install the Helm chart to deploy the Ansible automation portal.

## Access the disconnected OpenShift environment

Ensure your disconnected OpenShift cluster is configured to trust the private registry containing the mirrored container images. This step is crucial for successful image pulling during installation.

### Before you begin

- You have the necessary kubeconfig and permissions for setting up image pull secrets or insecure registries.

### Procedure

1.  In a terminal, log in to your disconnected OpenShift cluster using the `oc` CLI.
  

```
oc login --token=<your_token> --server=<your_openshift_api_url>
```
    Use the following command if you have a kubeconfig:

```
export KUBECONFIG=/path/to/your/kubeconfig
oc login
```

2.  Ensure that your OpenShift cluster is configured to trust your disconnected registry.

## Configure plug-in delivery for disconnected environments

Create the registry authentication secret so the dynamic plug-in init container can pull OCI artifacts from your disconnected registry.

### Before you begin

- You have mirrored the required container images and plug-in artifacts to your disconnected registry.
- You have credentials for your disconnected registry.

### Procedure

1.  Create an auth.json file with credentials for your disconnected registry:
  

```
{
  "auths": {
    "<disconnected_registry_url>": {
      "auth": "<base64-encoded-registry-credentials>"
    }
  }
}
```
    Generate the base64-encoded value:

```
$ printf '%s' '<registry_username>:<registry_password>' | base64 -w0
```

2.  Create the registry authentication secret:
  

```
$ oc create secret generic <release-name>-dynamic-plugins-registry-auth \
  --from-file=auth.json=./auth.json \
  -n <project_name>
```
    Replace `<release-name>` with your Helm release name. If you use the default release name from the OpenShift catalog, the secret name is `redhat-rhaap-portal-dynamic-plugins-registry-auth`.

### Results

Verify that the secret exists in the project:

```
$ oc get secret <release-name>-dynamic-plugins-registry-auth -n <project_name>
```

## Install the Helm chart

Install the Ansible automation portal by using the `helm install` command, referencing the local Helm chart file and required configuration values.

### Procedure

1.  On the machine within your disconnected environment, navigate to the directory where you placed the transferred Helm chart `.tgz` file:
  

```terminal
$ cd /path/to/your/transferred/charts/
```

2.  Define your namespace and cluster router base as environment variables:
  

```terminal
$ export MY_NAMESPACE="<your_namespace_name>"
$ export MY_CLUSTER_ROUTER_BASE="<your_cluster_router_base>"
```

3.  If the namespace does not exist, create it:
  

```terminal
$ oc new-project "${MY_NAMESPACE}"
```

4.  Create a custom values file and reuse it for install and upgrade.
      Choose the example that matches your plug-in delivery method.

    **OCI delivery** (`values-oci.yaml`):

```yaml
redhat-developer-hub:
  global:
    clusterRouterBase: <your_cluster_router_base>
    pluginMode: oci
    imageTagInfo: "<plugin-version>"
    # Registry host only. Replaces registry.redhat.io for all images.
    imageRegistry: "<disconnected_registry_url>"
    # Optional. Full OCI plugin image path for mirrors with non-standard
    # repository paths. Overrides imageRegistry for OCI plugin artifacts only.
    # Use when your mirror does not preserve the default repository path
    # (ansible-automation-platform/automation-portal).
    # ociPluginImage: "<disconnected_registry_url>/custom-path/automation-portal"
  catalogIndex:
    image:
      registry: "<disconnected_registry_url>"
  upstream:
    backstage:
      # The Helm chart pins images by SHA256 digest by default.
      # Override with tag-based references if your mirroring method
      # does not preserve digests.
      image:
        repository: rhdh/rhdh-hub-rhel9
        tag: "<rhdh_version>"
      appConfig:
        ansible:
          rhaap:
            checkSSL: true  # Set to false if using self-signed certificates.
        catalog:
          providers:
            rhaap:
              '{{- include "catalog.providers.env" . }}':
                orgs: "<your-aap-organization-name>"
    postgresql:
      image:
        repository: rhel9/postgresql-<version>
        tag: "<postgresql_tag>"
```
  Note:
      The Helm chart pins the PostgreSQL image by SHA256 digest. If your mirroring method does not preserve digests, set `postgresql.image.tag` to the tag you used when mirroring the image.

    **HTTP plug-in registry delivery** (`values-tarball.yaml`):

```yaml
redhat-developer-hub:
  global:
    clusterRouterBase: <your_cluster_router_base>
    pluginMode: tarball
    # Registry host only. Replaces registry.redhat.io for the images.
    imageRegistry: "<disconnected_registry_url>"
  catalogIndex:
    image:
      registry: "<disconnected_registry_url>"
  upstream:
    backstage:
      image:
        repository: rhdh/rhdh-hub-rhel9
        tag: "<rhdh_version>"
      appConfig:
        ansible:
          rhaap:
            checkSSL: true  # Set to false if using self-signed certificates.
        catalog:
          providers:
            rhaap:
              '{{- include "catalog.providers.env" . }}':
                orgs: "<your-aap-organization-name>"
    postgresql:
      image:
        repository: rhel9/postgresql-<version>
        tag: "<postgresql_tag>"
```
  Note:
      Replace `<rhdh_version>` and `<version>` with the versions bundled with your Helm chart. See the [Ansible Automation Portal Lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page for version mappings.

  Important:
      Set `imageRegistry` to the registry host only (for example, `mirror.example.com`). Do not include repository paths. The chart appends the default repository path `ansible-automation-platform/automation-portal` automatically. If your mirror uses a different repository structure, set `ociPluginImage` to the full image path instead.

  Note:
      The `secrets-scm` secret is only required if you use private SCM repositories for importing catalog entities or running software templates that access SCM. If you do not use SCM integration, you can skip creating this secret.

5.  Install the chart using the `helm install` command:
  

```terminal
$ helm install redhat-rhaap-portal \
  redhat-rhaap-portal-x.y.z.tgz \
  --namespace "${MY_NAMESPACE}" \
  -f /path/to/values-oci.yaml
```
    To apply changes after deployment, upgrade the Helm release. If you install from the OpenShift web console, use Developer -> Helm -> select the release -> Actions -> Upgrade -> YAML view.

    To upgrade from the command line:

```terminal
$ helm upgrade redhat-rhaap-portal \
  redhat-rhaap-portal-x.y.z.tgz \
  --namespace "${MY_NAMESPACE}" \
  -f /path/to/values-oci.yaml
```
    Alternatively, you can pass values using `--set` flags.

    **OCI delivery:**

```terminal
$ helm install redhat-rhaap-portal \
  redhat-rhaap-portal-x.y.z.tgz \
  --namespace "${MY_NAMESPACE}" \
  --set redhat-developer-hub.global.clusterRouterBase="${MY_CLUSTER_ROUTER_BASE}" \
  --set redhat-developer-hub.global.imageRegistry="<disconnected_registry_url>" \
  --set redhat-developer-hub.global.pluginMode=oci
```
    To also set `ociPluginImage` via `--set`:

```terminal
--set redhat-developer-hub.global.ociPluginImage="<disconnected_registry_url>/custom-path/automation-portal"
```
    **HTTP plug-in registry delivery:**

```terminal
$ helm install redhat-rhaap-portal \
  redhat-rhaap-portal-x.y.z.tgz \
  --namespace "${MY_NAMESPACE}" \
  --set redhat-developer-hub.global.clusterRouterBase="${MY_CLUSTER_ROUTER_BASE}" \
  --set redhat-developer-hub.global.imageRegistry="<disconnected_registry_url>" \
  --set redhat-developer-hub.global.pluginMode=tarball
```

## Configure CA certificates for private registries

If your private registry uses a certificate signed by an internal or self-signed CA, mount the CA certificate into the `install-dynamic-plugins` init container so that `skopeo` trusts the registry.

### Procedure

1.  Obtain the CA certificate chain that signed your mirror registry's TLS certificate.
      If the registry uses a certificate chain, include the full chain:

```terminal
$ cat registry.crt intermediate.crt root.crt > ca-bundle.crt
```

2.  Create a ConfigMap from the CA certificate:
  

```terminal
$ oc create configmap registry-ca-crt \
  --from-file=ca.crt=ca-bundle.crt -n *namespace*
```

3.  Add the volume and mount to your values file.
      Add the `registry-ca-crt` volume to `extraVolumes`, and add the CA certificate volume mount to the `install-dynamic-plugins` init container:

```yaml
redhat-developer-hub:
  upstream:
    backstage:
      extraVolumes:
        - name: registry-ca-crt
          configMap:
            name: registry-ca-crt
      initContainers:
        - name: install-dynamic-plugins
          volumeMounts:
            - name: registry-ca-crt
              mountPath: /etc/containers/certs.d/*registry-host*
              readOnly: true
```
  Note:
      The `mountPath` for the CA certificate must be the registry hostname only (for example, `/etc/containers/certs.d/mirror.example.com`). Do not include repository paths. If the registry uses a non-standard port, include it in the path (for example, `/etc/containers/certs.d/mirror.example.com:5000`).

### Results

After the deployment restarts, check the `install-dynamic-plugins` init container logs for certificate errors:

```terminal
$ oc logs *pod-name* -c install-dynamic-plugins -n *namespace* | grep -i "x509\|certificate"
```
If the CA certificate is mounted correctly, there are no `x509: certificate signed by unknown authority` errors.

## Verify the disconnected installation

Verify the successful installation of the Helm chart in the disconnected environment. Check the Helm release status, monitor the pods, and verify that the application routes are accessible.

### Procedure

1.  Check the Helm release status:
  

```
$ helm list -n ${MY_NAMESPACE}
```

2.  Monitor the pods in your namespace to ensure they are running:
  

```
$ oc get pods -n ${MY_NAMESPACE}
```

3.  Check for `ImagePullBackOff` or other errors in pod events:
  

```
$ oc describe pod <pod_name> -n ${MY_NAMESPACE}
```

4.  If the chart uses routes to expose services, verify that the routes are created and accessible:
  

```
$ oc get route -n ${MY_NAMESPACE}
```

## Configure the Helm chart for air-gapped OCI delivery

Configure Helm chart values for disconnected OCI plug-in delivery by setting the mirror registry, plug-in mode, and container image references.

### About this task

Set the following values in your Helm values file for a disconnected installation with OCI delivery:

```
redhat-developer-hub:
  global:
    pluginMode: oci
    imageTagInfo: "<plugin-version>"
    imageRegistry: "<your-mirror-registry-host>"
    catalogIndex:
      image:
        registry: "<your-mirror-registry-host>"
  upstream:
    backstage:
      image:
        repository: rhdh/rhdh-hub-rhel9
        tag: "<platform-version>"
    postgresql:
      image:
        repository: rhel9/postgresql-15
        tag: "latest"
```


Note:

Set `imageRegistry` and `catalogIndex.image.registry` to the registry host only (for example, `mirror.example.com` or `mirror.example.com:5000`). Use a hostname that cluster nodes can resolve and pull from. Do not include a repository path in `imageRegistry`. Setting `imageRegistry` does not override the catalog index registry; you must set `catalogIndex.image.registry` separately.

Note:

If your mirror uses a non-standard path for the Ansible plug-in OCI image, set `ociPluginImage` to the full image path (for example, `<your-mirror-registry-host>/custom-path/automation-portal`).

### Procedure

 Complete the standard install steps using these values.

## Troubleshooting disconnected installations

Use this reference to troubleshoot common issues that occur during disconnected Ansible automation portal installations.

| Symptom                                                                                                    | Cause                                                                                                     | Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `authentication required` or `unauthorized` in `install-dynamic-plugins` init container logs               | Auth secret missing or malformed. The init container uses `skopeo` and does not use cluster pull secrets. | Create `<release-name>-dynamic-plugins-registry-auth` secret. Use `base64 -w0` to avoid multiline values that corrupt `auth.json`.                                                                                                                                                                                                                                                                                                                                                  |
| Duplicate path in OCI URL (for example, `.../ansible-automation-platform/ansible-automation-platform/...`) | `imageRegistry` includes a repository path instead of the registry host only.                             | Set `imageRegistry` to the registry host only. If your mirror uses a different repository structure, use `ociPluginImage` to set the full image path.                                                                                                                                                                                                                                                                                                                               |
| `x509: certificate signed by unknown authority` in init container logs                                     | Private registry uses a self-signed or internal CA certificate.                                           | Mount the CA certificate into the init container. See [Configure CA certificates for private registries](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_self_service_disconnected_install#self-service-install-disconnected-configure-ca-certs "If your private registry uses a certificate signed by an internal or self-signed CA, mount the CA certificate into the install-dynamic-plugins init container so that skopeo trusts the registry."). |
