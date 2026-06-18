+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_oci_container_delivery"
title = "OCI container delivery - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_about/", "Install Ansible automation portal (OpenShift Container Platform only)"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_oci_container_delivery/aem-page/install-proc_self_service_oci_container_delivery.html"
last_crumb = "OCI container delivery"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "OCI container delivery"
oversized = "false"
page_slug = "install-proc_self_service_oci_container_delivery"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_oci_container_delivery"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_oci_container_delivery/toc/toc.json"
type = "aem-page"
+++

# OCI container delivery

Use OCI container delivery to pull plug-in artifacts from `registry.redhat.io/ansible-automation-platform/automation-portal`. The plug-in version must match the `imageTagInfo` value in your Helm chart configuration. This is the recommended method for new installations.

## Before you begin

- You have a Red Hat account with access to `registry.redhat.io`.
- You have credentials for `registry.redhat.io`.
- You have access to the OpenShift project where you will install the Helm chart.
- You have installed the OpenShift CLI (`oc`) and logged in to your cluster.
- You have a registry service account token from the Red Hat Customer Portal. For more information, see [Registry Service Accounts](https://access.redhat.com/RegistryAuthentication).

## Procedure

1.  Create an auth.json file on your local machine.
2.  Add registry credentials for `registry.redhat.io` to the auth.json file:
  

```
{
  "auths": {
    "registry.redhat.io": {
      "auth": "<base64-encoded-username-password>"
    }
  }
}
```
      If you pull plug-in artifacts from a private or mirror registry, add an entry for that registry in the same auth.json file:

```
{
  "auths": {
    "registry.redhat.io": {
      "auth": "<base64-encoded-username-password>"
    },
    "<private_registry_url>": {
      "auth": "<base64-encoded-registry-credentials>"
    }
  }
}
```
    For full mirror registry configuration including `imageRegistry`, `ociPluginImage`, and image mirroring procedures, see the disconnected installation chapter.

3.  Generate the base64-encoded authentication value for each registry:
  

```
printf '%s' '<username>:<password>' | base64 -w0
```

4.  Replace the `<base64-encoded-username-password>` and `<base64-encoded-registry-credentials>` placeholders in the auth.json file with the output from the previous step.
5.  Create the authentication secret in the target OpenShift project. The secret name must match your Helm release name.
      If you install from the OpenShift catalog and you use the default release name `redhat-rhaap-portal`:

```
oc create secret generic redhat-rhaap-portal-dynamic-plugins-registry-auth \
  --from-file=auth.json=./auth.json
```
    If you use a custom release name:

```
oc create secret generic <release-name>-dynamic-plugins-registry-auth \
  --from-file=auth.json=./auth.json
```

## Results

- Verify that the secret exists in the project:

```
oc get secret <release-name>-dynamic-plugins-registry-auth
```
  Important:
      Create this secret in the same OpenShift project as the Helm release, and create it before you install or upgrade the Helm release.

    The dynamic plug-in init container uses `skopeo` to pull OCI artifacts directly. It does not use Kubernetes `imagePullSecrets`, cluster-level `ImageDigestMirrorSet` or `ImageTagMirrorSet`, or OpenShift Container Platform global pull secrets. You must provide registry credentials in the `auth.json` secret even if your cluster is configured with image mirrors.

**OpenShift web console steps**

You can create the `dynamic-plugins-registry-auth` secret in the OpenShift web console.

1. In the OpenShift web console, select the OpenShift project where you will install the Helm release.
2. In the Administrator view, click Workloads> (and then)Secrets.
3. Click Create> (and then)Key/value secret.
4. Set the secret name to `<release-name>-dynamic-plugins-registry-auth`.
5. Add a key named `auth.json` and paste the contents of your auth.json file as the value.
6. Click Create.


**Helm chart configuration**

When you configure the Helm chart, set `redhat-developer-hub.global.pluginMode` to `oci` for OCI container delivery (recommended). Verify that `pluginMode` is set to the correct value. If you omit this setting, the chart defaults to `tarball`.

Set `imageTagInfo` to the plug-in version that matches your deployment. To determine the correct version tag, see "Determine version tags before you install".

```
redhat-developer-hub:
  global:
    pluginMode: oci
    imageTagInfo: "<plugin-version>"
```
If you need to change `pluginMode` after installing the Helm release, upgrade the Helm release.

**OpenShift web console:**

1. In the Developer view, click Helm.
2. Select the Helm release.
3. Click Actions> (and then)Upgrade.
4. In the YAML view, set `redhat-developer-hub.global.pluginMode` to `oci` (OCI container delivery).
5. Click Upgrade.


**Command line:**

- Run the `helm upgrade` command with your updated values file:

```
helm upgrade <release-name> <chart> -n <project> -f <values.yaml>
```
