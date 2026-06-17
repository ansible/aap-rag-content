# 3. Pre-installation configuration
## 3.6. Setting up a project for self-service automation portal in OpenShift Container Platform
### 3.6.1. Setting up a project in the OpenShift Container Platform web console

You can use the OpenShift Container Platform web console to create a project in your cluster.

**Procedure**

1. In a browser, log in to the OpenShift Container Platform web console.

2. Creating a project varies slightly depending on which perspective you have on:


1. From the **Developer** perspective: select **Project** then **Create Project**.
2. From the **Administrator** perspective: select **Home** then **Project** then **Create Project**.

3. In the **Create Project** dialog box, enter a unique name **Name** field.


- Lowercase alphanumeric characters (`a-z`, `0-9`) and the hyphen character (`-`) are permitted for project names.

- The underscore (`_`) character is not permitted.

- The maximum length for project names is 63 characters.


1. Optional: display name and description for your project.

4. Click Click to create the project.

### 3.6.2. Setting up an OpenShift Container Platform project using `oc`

You can run commands from your terminal to add a project to your cluster.

**Prerequisites**

- You have the login details for your Openshift cluster.
- You have installed the `oc` CLI tool.

**Procedure**

1. In a terminal, log in to OpenShift Container Platform using your credentials:

oc login <OpenShift_API_URL> -u <username>

The following example shows the output for a successful login:

$ oc login https://api.<my_cluster>.com:6443 -u kubeadmin
WARNING: Using insecure TLS client config. Setting this option is not supported!

Console URL: https://api.<my_cluster>.com:6443/console
Authentication required for https://api.<my_cluster>.com:6443 (openshift)
Username: kubeadmin
Password:
Login successful.

You have access to 22 projects, the list has been suppressed. You can list all projects with 'oc projects'

Using project "default".

2. Create a new project. Use a unique project name.

$ oc new-project <self-service-project-name>


- Lowercase alphanumeric characters (`a-z`, `0-9`) and the hyphen character (`-`) are permitted for project names.

- The underscore (`_`) character is not permitted.

- The maximum length for project names is 63 characters.

Example:

$ oc new-project <my-project>

Now using project "my-project" on server "https://openshift.example.com:6443".

3. Open your new project:

$ oc project <self-service-project-name>

## 3.7. Choose a plug-in delivery method

Self-service automation portal supports two plug-in installation methods. Choose the method that fits your environment:

- **OCI container (recommended)**: self-service automation portal automatically pulls an Open Container Initiative (OCI) container from `registry.redhat.io`.
- **HTTP plug-in registry**: Manually create an HTTP plug-in registry that contains the necessary self-service automation portal plug-ins.

### 3.7.1. OCI container delivery

Use OCI container delivery to automatically pull an OCI container from `registry.redhat.io` that includes the self-service automation portal plug-ins. This is the recommended method for production deployments.

This method is the default for the Helm chart and is the recommended method for production deployments.

**Prerequisites**

- You have a Red Hat account with access to `registry.redhat.io`.
- You have credentials for `registry.redhat.io`.
- You have access to the OpenShift project where you will install the Helm chart.
- You have installed the OpenShift CLI (`oc`) and logged in to your cluster.
- You have a registry service account token from the Red Hat Customer Portal.

**Procedure**

1. Create an `auth.json` file on your local machine.

2. Add the following structure to the `auth.json` file:

{
"auths": {
"registry.redhat.io": {
"auth": "<base64-encoded-username-password>"
}
}
}

3. Generate the base64-encoded authentication value:

printf '%s' '<username>:<password>' | base64 -w0

4. Replace `<base64-encoded-username-password>` in the `auth.json` file with the output from the previous step.

5. Create the authentication secret in the target OpenShift project. The secret name must match your Helm release name.

If you install from the OpenShift catalog and you use the default release name `redhat-rhaap-portal`:

oc create secret generic redhat-rhaap-portal-dynamic-plugins-registry-auth \
--from-file=auth.json=./auth.json

If you use a custom release name:

oc create secret generic <release-name>-dynamic-plugins-registry-auth \
--from-file=auth.json=./auth.json

**Verification**

- Verify that the secret exists in the project:

oc get secret <release-name>-dynamic-plugins-registry-auth


Important
Create this secret in the same OpenShift project as the Helm release, and create it before you install or upgrade the Helm release.

**OpenShift web console steps**

You can create the `dynamic-plugins-registry-auth` secret in the OpenShift web console.

1. In the OpenShift web console, select the OpenShift project where you will install the Helm release.
2. In the **Administrator** view, click **Workloads** → **Secrets**.
3. Click **Create** → **Key/value secret**.
4. Set the secret name to `<release-name>-dynamic-plugins-registry-auth`.
5. Add a key named `auth.json` and paste the contents of your `auth.json` file as the value.
6. Click **Create**.

**Helm chart configuration**

When you configure the Helm chart, set `redhat-developer-hub.global.pluginMode` to match your chosen delivery method:

- `oci` — OCI container delivery (recommended).
- `tarball` — HTTP plug-in registry.

Verify that `pluginMode` is set to the correct value. If you omit this setting, the chart uses its built-in default.

redhat-developer-hub:
global:
pluginMode: oci

If you need to change `pluginMode` after installing the Helm release, upgrade the Helm release.

**OpenShift web console:**

1. In the **Developer** view, click **Helm**.
2. Select the Helm release.
3. Click **Actions** → **Upgrade**.
4. In the **YAML view**, set `redhat-developer-hub.global.pluginMode` to `oci` (OCI container delivery) or `tarball` (HTTP plug-in registry).
5. Click **Upgrade**.

**Command line:**

- Run the `helm upgrade` command with your updated values file:

helm upgrade <release-name> <chart> -n <project> -f <values.yaml>

**Additional resources**

- [Registry Service Accounts](https://access.redhat.com/RegistryAuthentication)

### 3.7.2. HTTP plug-in registry

The HTTP plug-in registry method hosts plug-in tarball files in a local OpenShift registry that the dynamic plug-in installer pulls during startup.

#### 3.7.2.1. Log into OpenShift CLI

To deploy a plug-in registry, you must install the OpenShift CLI (`oc`) locally and log in to your cluster.

See [Installing OpenShift CLI in the OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.8/html/cli_tools/openshift-cli-oc#installing-openshift-cli) documentation.

**Procedure**

1. Log in to OpenShift Container Platform using your credentials:

oc login <OpenShift_API_URL> -u <username>

2. Create a new project or switch to an existing project:

oc new-project <project-name>

Or:

oc project <project-name>

#### 3.7.2.2. Download plug-ins and push to the registry

To provide Ansible plug-ins to Red Hat Developer Hub, download the setup bundle and push the extracted files to a local Red Hat OpenShift registry.

By setting up a centralized httpd service, you can access these plug-in files through Helm chart configuration.

**Procedure**

1. Create a directory on your local machine to store the plug-in files.

mkdir /path/to/<ansible-backstage-plugins-local-dir>

2. Set an environment variable `$DYNAMIC_PLUGIN_ROOT_DIR` to represent the directory path.

export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/<ansible-backstage-plugins-local-dir>

3. Download the setup bundle. In a browser, navigate to the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software). and select the **Product Software** tab.

4. Click **Download now** next to **Ansible self-service automation portal Setup Bundle** to download the latest version of the plug-ins.

The format of the filename is `self-service-automation-portal-plugins-x.y.z.tar.gz`.

Substitute the Ansible plug-ins release version, for example `2.0.0`, for `x.y.z`.

5. Extract the contents to `$DYNAMIC_PLUGIN_ROOT_DIR`:

$ tar --exclude='*code*' -xzf self-service-automation-portal-plugins-x.y.z.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR

6. Verify that the extracted files are in the `$DYNAMIC_PLUGIN_ROOT_DIR` directory:

ls $DYNAMIC_PLUGIN_ROOT_DIR

You should see the following files:

ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity

The files with the .integrity file type contain the plug-in SHA value.

7. Create an httpd service as part of your OpenShift project:

oc new-build httpd --name=plugin-registry --binary
oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
oc new-app --image-stream=plugin-registry

**Verification**

1. Run the following command to verify that the plug-in registry deployed correctly:

oc exec $(oc get pods -l deployment=plugin-registry -o jsonpath='{.items[0].metadata.name}') -- ls -l /opt/app-root/src

2. Confirm that the required tarball files are in the plug-in registry.

**Helm chart configuration** When you configure the Helm chart, set `redhat-developer-hub.global.pluginMode` to `tarball`:

redhat-developer-hub:
global:
pluginMode: tarball

## 3.8. Creating secrets in OpenShift for your environment variables

Before installing the Helm chart, you must create a set of secrets in your OpenShift project. The self-service automation portal Helm chart fetches environment variables from OpenShift secrets.

### 3.8.1. Creating Ansible Automation Platform authentication secrets

You must create a secret in OpenShift Container Platform for Ansible Automation Platform authentication.

**Procedure**

1. Log in to your OpenShift Container Platform instance.

2. Open your OpenShift project for self-service automation portal in the **Administrator** view.

3. Click **Secrets** in the side pane.

4. Click **Create** to open the form for creating a new secret.

5. Select the **Key/Value** option.

6. Create a secret named `secrets-rhaap-portal`.


Note
The secret must use this exact name.

7. Add the following key-value pairs to the secret.


Note
The secrets must use the exact key names specified below.


- Key: `aap-host-url`

Value needed: Ansible Automation Platform instance URL

- Key: `oauth-client-id`

Value needed: Ansible Automation Platform OAuth client ID

- Key: `oauth-client-secret`

Value needed: Ansible Automation Platform OAuth client secret value

- Key: `aap-token`

Value needed: Token for Ansible Automation Platform user authentication (must have `read` access).

8. Click Create to create the secret.

### 3.8.2. Creating GitHub and Gitlab secrets

Create an OpenShift secret to hold Personal Access Tokens for your external Source Control Management systems, such as GitHub or GitLab. This helps securely manage access credentials.

This procedure establishes the required `secrets-scm` Key/Value secret within your OpenShift Container Platform project to securely store the GitHub and/or GitLab Personal Access Tokens (PATs).

**Procedure**

1. Log in to your OpenShift Container Platform instance.

2. Open your OpenShift project for self-service automation portal.

3. Click **Secrets** in the side pane.

4. Click **Create** to open the form for creating a new secret.

5. Select the **Key/Value** option.

6. Create a secret named `secrets-scm`.


Note
The secret must use this exact name.

7. Add the following key-value pairs to the secret. If you are only using one SCM, just add the key-value pair for that SCM.


Note
The secrets must use the exact key names specified below.


- Key: `github-token`

Value needed: Github Personal Access Token (PAT)

- Key: `gitlab-token`

Value needed: Gitlab Personal Access Token (PAT)

8. Click **Create** to create the secret.

# Chapter 4. Install the self-service automation portal Helm chart

You can use the configured secrets and plugin registry to install the self-service automation portal. Deploy the application onto your OpenShift cluster using the provided Helm chart.

## 4.1. Configure the self-service automation portal Helm chart from the OpenShift catalog

Deploy the Helm chart from the OpenShift catalog by configuring the base URL and organization name in the YAML view. This launches the self-service automation portal installation.

**Prerequisites**

- You have created a project for self-service automation portal in OpenShift Container Platform.

- You have created secrets in OpenShift Container Platform for Ansible Automation Platform authentication.

- If you configure SCM integration (for example, importing from private repositories or using templates that access SCM), you have created secrets in OpenShift for SCM authentication.

- You have completed one of the plug-in delivery methods:


- For OCI delivery: You have created the `<release-name>-dynamic-plugins-registry-auth` secret.

**Procedure**

1. In the OpenShift Container Platform web console, select the **Developer** view.

2. Select your project and click the Helm option in the OpenShift sidebar.

3. Click Create and select **Helm Release**.

4. Search for `Portal` in the Helm Charts filter, and select the `Automation Portal` chart.

5. Click Create and select the **YAML view**.

6. Update the `clusterRouterBase` value with the base URL of your OpenShift instance.


Important
You must replace the default `apps.example.com` placeholder value. If the default value remains, Helm chart validation fails.

redhat-developer-hub:
global:
clusterRouterBase: apps.example.com

7. Configure the plug-in delivery mode by setting the `pluginMode` key:


- For OCI delivery, set the value to `oci`.

redhat-developer-hub:
global:
pluginMode: oci

8. **Optional:** To use a specific plug-in version, update the `imageTagInfo` value:

redhat-developer-hub:
global:
imageTagInfo: "2.1"

9. Set the Ansible Automation Platform organization to synchronize. The default value is `Default`. Update the `orgs` key to match your organization name:

redhat-developer-hub:
upstream:
backstage:
appConfig:
catalog:
providers:
rhaap:
'{{- include "catalog.providers.env" . }}':
orgs: "<your-aap-organization-name>"

10. **Optional:** Update the `CUSTOMER_SUPPORT_URL` to point to your support portal:

redhat-developer-hub:
upstream:
backstage:
extraEnvVars:
- name: CUSTOMER_SUPPORT_URL
value: https://access.redhat.com/support

11. Click Create.

**Additional resources**

- [Choose a plug-in delivery method](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#self-service-create-ocp-registry_self-service-preinstall-config)

## 4.2. Verify the installation

Verify the Helm chart installation from the OpenShift Container Platform web console.

**Procedure**

1. In a browser, log in to your OpenShift instance.

2. In the **Developer** view, navigate to the **Topology** view for the namespace where you deployed the Helm chart.

The deployment appears: the label on the icon is `D`. The name of the deployment is `<installation-name>-backstage`, for example `<my-self-service-automation-portal-backstage>`.

While it is deploying, the icon is light blue. The color changes to dark blue when deployment is complete.


![Deployment on OpenShift console](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/06c45647f2a2be815da7e2006fd83257/self-service-verify-helm-install.png)

# Chapter 5. Install self-service automation portal in air-gapped OpenShift Container Platform environments

You can install self-service automation portal in a disconnected OpenShift Container Platform environment.

## 5.1. Prerequisites

Review the mandatory subscriptions, permissions, and platform access required before starting the installation. Fulfilling these needs helps ensure a successful deployment.

- You have a valid subscription to Red Hat Ansible Automation Platform.

- You have access to an instance of Red Hat Ansible Automation Platform 2.6 with the appropriate permissions to create an OAuth application.

- You have access to an OpenShift Container Platform instance with the appropriate permissions within your project to create an application.

- You have installed `oc`, the OpenShift command-line interface (CLI) tool, on your local machine.

- You have installed Helm 3.10 or newer.

- You have installed and configured Podman for pulling and pushing container images.

- You have internet access to pull images and charts from public repositories, including `registry.redhat.io`.

- A Red Hat pull secret that allows you to pull images from registry.redhat.io.

- You have a method to provide the Ansible plug-ins in the disconnected environment:


- For OCI delivery: A method to mirror the OCI artifacts image referenced by `imageTagInfo`.
- For HTTP plug-in registry: The ability to host the plug-in tarball files.

- You have registry credentials for the registry endpoint used by the dynamic plug-in installer.

## 5.2. Prepare for air-gapped installation

Before you can install self-service automation portal in a disconnected OpenShift Container Platform environment, you must complete some processes on a connected bastion host.

### 5.2.1. Mirror container images

Mirror the required container images from the Red Hat registry to your local disconnected registry. This step prepares the images for installing self-service automation portal in an isolated environment.

If you mirror `registry.redhat.io` content to a different registry host (or to a registry prefix such as `quay.io/<org>`), you can set `redhat-developer-hub.global.imageRegistry` so the Helm chart pulls all of its images from that mirrored location. `imageRegistry` is a single override that controls the registry for the base application image, PostgreSQL image, OCI plug-in artifacts, and Ansible Dev Tools sidecar.

The dynamic plug-in init container does not use cluster-level image mirror configuration (for example, `ImageDigestMirrorSet` or `ImageTagMirrorSet`). You must set `imageRegistry` even if your cluster redirects `registry.redhat.io` pulls.

**Procedure**

1. Log in to `registry.redhat.io`:

$ podman login registry.redhat.io

2. Enter your Red Hat username and password when prompted.

3. Log in to your disconnected registry:

$ podman login <disconnected_registry_url>

4. Pull the Red Hat Developer Hub image from `registry.redhat.io`:

$ podman pull registry.redhat.io/rhdh/rhdh-hub-rhel9:x.y.z

5. Tag the image for your disconnected registry:

$ podman tag registry.redhat.io/rhdh/rhdh-hub-rhel9:x.y.z <disconnected_registry_url>/<your_namespace>/rhdh/rhdh-hub-rhel9:x.y.z

6. Push the tagged image to your disconnected registry:

$ podman push <disconnected_registry_url>/<your_namespace>/rhdh/rhdh-hub-rhel9:x.y.z

7. If you use the built-in PostgreSQL database, mirror the PostgreSQL 15 image. An external database is the supported production architecture and does not require this step:

$ podman pull registry.redhat.io/rhel9/postgresql-15:<tag>
$ podman tag registry.redhat.io/rhel9/postgresql-15:<tag> <disconnected_registry_url>/<your_namespace>/rhel9/postgresql-15:<tag>
$ podman push <disconnected_registry_url>/<your_namespace>/rhel9/postgresql-15:<tag>

8. If you use OCI container delivery, mirror the Ansible plug-ins OCI artifacts image:

$ podman pull registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>
$ podman tag registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version> <disconnected_registry_url>/<your_namespace>/ansible-automation-platform/automation-portal:<plugin-version>
$ podman push <disconnected_registry_url>/<your_namespace>/ansible-automation-platform/automation-portal:<plugin-version>

9. Mirror the Ansible Dev Tools sidecar image. Use the path that matches your Ansible Automation Platform version:

**Ansible Automation Platform 2.5:**

$ podman pull registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel9:latest
$ podman tag registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel9:latest <disconnected_registry_url>/<your_namespace>/ansible-automation-platform-25/ansible-dev-tools-rhel9:latest
$ podman push <disconnected_registry_url>/<your_namespace>/ansible-automation-platform-25/ansible-dev-tools-rhel9:latest

**Ansible Automation Platform 2.6:**

$ podman pull registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest
$ podman tag registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest <disconnected_registry_url>/<your_namespace>/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest
$ podman push <disconnected_registry_url>/<your_namespace>/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest

### 5.2.2. Download the helm chart package

Download the Helm chart package and modify the internal image references to point to your disconnected registry. This prepares the installation package for the air-gapped environment.

**Procedure**

1. Add the OpenShift Helm charts repository and update your local cache:

helm repo add openshift-helm-charts https://charts.openshift.io/
helm repo update

2. Pull the required version of the chart:

helm pull openshift-helm-charts/redhat-rhaap-portal --version x.y.z

The chart is saved as a `.tgz` file (for example, `redhat-rhaap-portal-1.0.1.tgz`).

3. Extract the chart files:

tar -xvf redhat-rhaap-portal-x.y.z.tgz

This creates a directory with a name similar to `redhat-rhaap-portal-1.0.1/`.

4. In the `redhat-rhaap-portal/values.yaml` file, replace all `image:` references with the full path to the images in your disconnected registry.

5. Repack the chart with your modifications:

helm package redhat-rhaap-portal-x.y.z

6. A new .tgz file is created containing your changes.

### 5.2.3. Transfer assets to the disconnected environment

Transfer the modified Helm chart package from the connected bastion host to a machine inside your disconnected network. This action stages the installation assets for deployment within the isolated OpenShift environment.

**Procedure**

1. Copy the modified Helm chart `.tgz` file or files (for example, `redhat-rhaap-portal-1.0.1.tgz`) from your connected bastion host to a machine or jump box within your disconnected OpenShift network.
2. If you use the HTTP plug-in registry method, transfer the plug-in tarball files to the disconnected environment.

## 5.3. Installing the Helm chart in the disconnected OpenShift environment

You can install the modified Helm chart using the `helm install` command in your disconnected OpenShift environment. This deploys the self-service automation portal using the locally available assets.

Continued steps for installing the Helm chart in a disconnected OpenShift environment are detailed in this section.

### 5.3.1. Accessing the disconnected OpenShift environment

Ensure your disconnected OpenShift cluster is configured to trust the private registry containing the mirrored container images. This step is crucial for successful image pulling during installation.

**Prerequisites**

- You have the necessary kubeconfig and permissions for setting up image pull secrets or insecure registries.

**Procedure**

1. In a terminal, log in to your disconnected OpenShift cluster using the `oc` CLI.

oc login --token=<your_token> --server=<your_openshift_api_url>

Use the following command if you have a kubeconfig:

export KUBECONFIG=/path/to/your/kubeconfig
oc login

2. Ensure that your OpenShift cluster is configured to trust your disconnected registry.

### 5.3.2. Configure plug-in delivery for disconnected environments

Complete one of the plug-in delivery methods for disconnected environments.

**Procedure**

- For OCI delivery: Create the `<release-name>-dynamic-plugins-registry-auth` secret with credentials for your disconnected registry that hosts the mirrored Ansible plug-ins OCI artifacts.

**Additional resources**

- [Choose a plug-in delivery method](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#self-service-create-ocp-registry_self-service-preinstall-config)

### 5.3.3. Install the Helm chart

Install self-service automation portal by using the `helm install` command. You must reference the local Helm chart file and include the required configuration using a values file (`-f`) or `--set` flags.

**Procedure**

1. On the machine within your disconnected environment, navigate to the directory where you placed the transferred Helm chart `.tgz` file:

$ cd /path/to/your/transferred/charts/

2. Define your namespace and cluster router base as environment variables:

$ export MY_NAMESPACE="<your_namespace_name>"
$ export MY_CLUSTER_ROUTER_BASE="<your_cluster_router_base>"

3. If the namespace does not exist, create it:

$ oc new-project "${MY_NAMESPACE}"

4. Create a custom values file and reuse it for install and upgrade. Choose the example that matches your plug-in delivery method.

**OCI delivery** (`values-oci.yaml`):

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
upstream:
backstage:
# The Helm chart pins images by SHA256 digest by default.
# When mirroring with podman tag/push, the digest is not preserved.
# Override with tag-based references.
image:
repository: rhdh/rhdh-hub-rhel9
tag: "1.8"
appConfig:
ansible:
rhaap:
checkSSL: true  # Set to false if using self-signed certificates.
catalog:
providers:
rhaap:
'{{- include "catalog.providers.env" . }}':
orgs: "<your-aap-organization-name>"
# If you use the built-in PostgreSQL database, uncomment the following lines.
# An external database is the supported production architecture.
# postgresql:
#   image:
#     repository: rhel9/postgresql-15
#     tag: "latest"

**HTTP plug-in registry delivery** (`values-tarball.yaml`):

redhat-developer-hub:
global:
clusterRouterBase: <your_cluster_router_base>
pluginMode: tarball
# Registry host only. Replaces registry.redhat.io for the images.
imageRegistry: "<disconnected_registry_url>"
upstream:
backstage:
image:
repository: rhdh/rhdh-hub-rhel9
tag: "1.8"
appConfig:
ansible:
rhaap:
checkSSL: true  # Set to false if using self-signed certificates.
catalog:
providers:
rhaap:
'{{- include "catalog.providers.env" . }}':
orgs: "<your-aap-organization-name>"
# If you use the built-in PostgreSQL database, uncomment the following lines.
# An external database is the supported production architecture.
# postgresql:
#   image:
#     repository: rhel9/postgresql-15
#     tag: "latest"


Important
Set `imageRegistry` to the registry host only (for example, `mirror.example.com`). Do not include repository paths. The chart appends the default repository path `ansible-automation-platform/automation-portal` automatically. If your mirror uses a different repository structure, set `ociPluginImage` to the full image path instead.

5. Install the chart using the `helm install` command:

$ helm install redhat-rhaap-portal \
redhat-rhaap-portal-x.y.z.tgz \
--namespace "${MY_NAMESPACE}" \
-f /path/to/values-oci.yaml

To apply changes after deployment, upgrade the Helm release. If you install from the OpenShift web console, use Developer → Helm → select the release → Actions → Upgrade → YAML view.

To upgrade from the command line:

$ helm upgrade redhat-rhaap-portal \
redhat-rhaap-portal-x.y.z.tgz \
--namespace "${MY_NAMESPACE}" \
-f /path/to/values-oci.yaml

Alternatively, you can pass values using `--set` flags.

**OCI delivery:**

$ helm install redhat-rhaap-portal \
redhat-rhaap-portal-x.y.z.tgz \
--namespace "${MY_NAMESPACE}" \
--set redhat-developer-hub.global.clusterRouterBase="${MY_CLUSTER_ROUTER_BASE}" \
--set redhat-developer-hub.global.imageRegistry="<disconnected_registry_url>" \
--set redhat-developer-hub.global.pluginMode=oci

To also set `ociPluginImage` via `--set`:

--set redhat-developer-hub.global.ociPluginImage="<disconnected_registry_url>/custom-path/automation-portal"

**HTTP plug-in registry delivery:**

$ helm install redhat-rhaap-portal \
redhat-rhaap-portal-x.y.z.tgz \
--namespace "${MY_NAMESPACE}" \
--set redhat-developer-hub.global.clusterRouterBase="${MY_CLUSTER_ROUTER_BASE}" \
--set redhat-developer-hub.global.imageRegistry="<disconnected_registry_url>" \
--set redhat-developer-hub.global.pluginMode=tarball

### 5.3.4. Configure CA certificates for private registries

If your private registry uses a certificate signed by an internal or self-signed CA, the `install-dynamic-plugins` init container fails with `x509: certificate signed by unknown authority`. Mount the CA certificate into the init container so that `skopeo` trusts the registry.

**Procedure**

1. Obtain the CA certificate chain that signed your mirror registry’s TLS certificate. If the registry uses a certificate chain, include the full chain:

$ cat registry.crt intermediate.crt root.crt > ca-bundle.crt

2. Create a ConfigMap from the CA certificate:

$ oc create configmap registry-ca-crt \
--from-file=ca.crt=ca-bundle.crt -n <namespace>

3. Add the volume and mount to your values file:

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
mountPath: /etc/containers/certs.d/<registry-host>
readOnly: true

Important

The `mountPath` must be the registry hostname only (for example, `/etc/containers/certs.d/mirror.example.com`). Do not include repository paths. If the registry uses a non-standard port, include it in the path (for example, `/etc/containers/certs.d/mirror.example.com:5000`).

## 5.4. Verify the disconnected installation

Verify the successful installation of the Helm chart in the disconnected environment. Check the Helm release status, monitor the pods, and verify that the application routes are accessible.

**Procedure**

1. Check the Helm release status:

$ helm list -n ${MY_NAMESPACE}

2. Monitor the pods in your namespace to ensure they are running:

$ oc get pods -n ${MY_NAMESPACE}

3. Check for `ImagePullBackOff` or other errors in pod events:

$ oc describe pod <pod_name> -n ${MY_NAMESPACE}

4. If the chart uses routes to expose services, verify that the routes are created and accessible:

$ oc get route -n ${MY_NAMESPACE}

## 5.5. Troubleshooting disconnected installations

Use this reference to troubleshoot common issues that occur during disconnected self-service automation portal installations.

| Symptom | Cause | Solution |
| --- | --- | --- |
| <br> `authentication required` or `unauthorized` in `install-dynamic-plugins` init container logs | <br>  Auth secret missing or malformed. The init container uses `skopeo` and does not use cluster pull secrets. | <br>  Create `<release-name>-dynamic-plugins-registry-auth` secret. Use `base64 -w0` to avoid multiline values that corrupt `auth.json`. |
| <br>  Duplicate path in OCI URL (for example, `…​/ansible-automation-platform/ansible-automation-platform/…​`) | <br> `imageRegistry` includes a repository path instead of the registry host only. | <br>  Set `imageRegistry` to the registry host only. If your mirror uses a different repository structure, use `ociPluginImage` to set the full image path. |
| <br> `x509: certificate signed by unknown authority` in init container logs | <br>  Private registry uses a self-signed or internal CA certificate. | <br>  Mount the CA certificate into the init container. See [Configure CA certificates for private registries](#self-service-install-disconnected-configure-ca-certs_self-service-disconnected-install-helm-chart "5.3.4.&nbsp;Configure CA certificates for private registries"). |

# Chapter 6. Inspecting the deployment on OpenShift

You can inspect the deployment logs and ConfigMap on the OpenShift console to verify that the deployment conforms with the settings in your Helm chart.

## 6.1. Viewing the deployment logs

You can view the deployment logs in the OpenShift console. Pay close attention to the install-dynamic-plugins container logs. This helps confirm that the required plug-ins installed successfully.

**Procedure**

1. In a browser, log in to your OpenShift instance.

2. In the **Developer** view, navigate to the **Topology** view for the namespace where you deployed the Helm chart.

3. The deployment appears: the label on the icon is `D`.

The name of the deployment is `<installation-name>-backstage`, for example `<my-self-service-automation-portal-backstage>`.

4. Click the icon representing the deployment.

5. The **Details** pane for the deployment opens.

6. Select the **Resources** tab.

7. Click **View logs** for the deployment pod in the **Pods** section:


![Deployment on OpenShift console](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/7db4d1cfa7a66893597c9306c073b561/self-service-view-deployment-logs.png)
The **Pod details** page opens for the deployment pod.

8. Select the **Logs** tab in the **Pod details** page.

9. To view the install messages, select the `install-dynamic-plugins` container from the **INIT CONTAINERS** section of the dropdown list of containers:


![View install messages](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/e9518a231caeb6d563f762c47f17d7e5/self-service-view-install-messages.png)
The log stream displays the progress of the installation of the plug-ins from the plug-in registry.

The log stream for successful installation of the plug-ins resembles the following output:

======= Installing dynamic plugin http://plugin-registry:8080/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-0.1.0.tgz
*=> Grabbing package archive through pm pack'
•=› Vertfying package Integrity
•*> Extracting package archtve /dynamtc-plugtns-root/anstble-backstage-plugtn-catalog-backend-nodule-rhaap-dynamic-0.1.0.tgz
•*› Removing package archive /dynamic-plugins-root/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-0.1.0. tgz
-> Successfully installed dynamic plugin http://plugin-registry:8080/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-0.1.0.tgz

10. Select the **Environment** tab in the **Pod details** page to view the environment variables for the containers. If you set additional environment variables in your Helm chart, check that they are listed here.


![Pod environment variables](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/0a87b7e4f33737aecc0c1af2f37dc039/self-service-pod-env-variables.png)

# Chapter 7. Accessing the self-service automation portal deployment

Complete the necessary post-installation configuration, including updating the OAuth application and setting up initial Role-Based Access Control (RBAC). You can then access and sign in to the portal.

## 7.1. Adding the deployment URL to the OAuth Application

When you set up your OAuth application in Ansible Automation Platform before deploying self-service automation portal, you added placeholder text for the `Redirect URIs` value.

You must update this value using the URL from the deployed application so that you can run automation on self-service automation portal from self-service automation portal.

**Procedure**

1. Determine the `Redirect URI` from your OpenShift deployment:


1. Open the URL for the deployment from the OpenShift console to display the sign-in page for self-service automation portal.


![Open URL from OpenShift web console](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/5a9b8eff9be9b2bc899e6d7f8eb1a69c/self-service-topology-get-url.png)

2. Copy the URL for the sign-in page for self-service automation portal.

3. To determine the `Redirect URI` value, append `/api/auth/rhaap/handler/frame` to the end of the deployment URL.

For example, if the URL for the deployment is `https://my-automation-portal-project.mycluster.com`, then the `Redirect URI` value is `https://my-automation-portal-project.mycluster.com/api/auth/rhaap/handler/frame`.

2. Update the `Redirect URIs` field in the OAuth application in Ansible Automation Platform:


1. In a browser, open your instance of Ansible Automation Platform.
2. Navigate to Access Management → OAuth Applications.
3. In the list view, click the OAuth application you created.
4. Replace the placeholder text in the `Redirect URIs` field with the value you determined from your OpenShift deployment.
5. Click `Save` to apply the changes.

## 7.2. Configuring custom SSL certificates for self-service automation portal

If your Ansible Automation Platform instance uses custom or self-signed SSL certificates, you must configure self-service automation portal to trust those certificates. Without this configuration, authentication between self-service automation portal and Ansible Automation Platform fails with SSL verification errors.

**Prerequisites**

- You have administrator access to your OpenShift Container Platform cluster.
- You have the custom Certificate Authority (CA) certificate file used by your Ansible Automation Platform instance.
- self-service automation portal is installed in your OpenShift Container Platform cluster.

**Procedure**

1. Obtain the CA certificate file from your Ansible Automation Platform instance.

If you do not have the CA certificate file, you can extract it from your Ansible Automation Platform server:

openssl s_client -showcerts -connect <aap-hostname>:443 </dev/null 2>/dev/null | openssl x509 -outform PEM > aap-ca-cert.pem

Replace `<aap-hostname>` with your Ansible Automation Platform hostname.

2. Log in to your OpenShift Container Platform cluster with administrator privileges.

3. Create a ConfigMap containing your custom CA certificate:

oc create configmap custom-ca-bundle \
--from-file=ca-bundle.crt=aap-ca-cert.pem \
-n <namespace>

Replace `<namespace>` with the namespace where self-service automation portal is installed.

4. Update your self-service automation portal Helm chart values to mount the custom CA certificate:

upstream:
backstage:
extraEnvVarsSecrets:
- custom-ca-bundle
extraVolumes:
- name: custom-ca
configMap:
name: custom-ca-bundle
extraVolumeMounts:
- name: custom-ca
mountPath: /etc/pki/ca-trust/source/anchors/
readOnly: true

5. Apply the updated configuration by upgrading the self-service automation portal Helm chart:

helm upgrade <release-name> <chart-name> \
-f values.yaml \
-n <namespace>

Replace `<release-name>` with your Helm release name and `<chart-name>` with the self-service automation portal chart name.

6. Wait for the self-service automation portal pods to restart with the new configuration.

**Verification**

1. Verify that the self-service automation portal pods are running:

oc get pods -n <namespace>

All self-service automation portal pods should show a status of `Running`.

2. Attempt to sign in to self-service automation portal using your Ansible Automation Platform credentials.

If the SSL certificate configuration is correct, you can authenticate successfully without SSL verification errors.

3. Check the self-service automation portal logs for SSL-related errors:

oc logs -n <namespace> <pod-name> | grep -i ssl

If you see no SSL verification errors, the custom CA certificate is trusted correctly.

**Troubleshooting**

If you continue to experience SSL verification errors after following this procedure:

- Verify that the CA certificate file contains the complete certificate chain.
- Ensure that the certificate file is in PEM format.
- Confirm that the Ansible Automation Platform hostname in your configuration matches the hostname in the SSL certificate.
- Check that the `checkSSL` parameter in your Helm values is set to `true` (the default). Setting it to `false` disables SSL verification entirely, which is not recommended for production environments.

## 7.3. Signing in to self-service automation portal

Log in to the deployed self-service automation portal using your existing Ansible Automation Platform credentials. The portal uses these credentials for authentication.

**Prerequisites**

- You have configured an OAuth application in Ansible Automation Platform for self-service automation portal.
- You have configured a user account in Ansible Automation Platform.

**Procedure**

1. In a browser, navigate to the URL for self-service automation portal to open the sign-in page.


![Self-service sign-in page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/7301d2b380047719b3fda17728454b83/self-service-sign-in-page.png)

2. Click Sign In.

3. The sign-in page for Ansible Automation Platform appears:


![Ansible Automation Platform sign-in page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/cd442c9292d68a910b63db55552d026f/rhaap-sign-in-page.png)

4. Enter your Ansible Automation Platform credentials and click **Log in**.

5. The self-service automation portal web console opens.

**Troubleshooting**

If you are using custom or self-signed SSL certificates and when attempting to log in to self-service automation portal, it displays the error:

`Login failed; caused by Error: Failed to send POST request: fetch failed`

This error indicates that self-service automation portal cannot verify the SSL certificate from your Ansible Automation Platform instance.

To resolve this issue, configure self-service automation portal to trust your custom CA certificate. For more information, see [Section 7.2, “Configuring custom SSL certificates for self-service automation portal”](#self-service-configure-custom-ssl_self-service-accessing-deployment "7.2.&nbsp;Configuring custom SSL certificates for self-service automation portal").

Note

While you can disable SSL validation by setting `checkSSL: false` in the Helm chart configuration, this approach is not recommended for production environments as it reduces security. Instead, configure self-service automation portal to trust your custom CA certificate.

## 7.4. Setting up initial RBAC rules in self-service automation portal

After you install self-service automation portal and synchronize it with Ansible Automation Platform, only users with Ansible Automation Platform administrator privileges can view the auto-generated templates.

You must configure initial Role-Based Access Control (RBAC) permissions to allow non-admin users to view and execute synchronized Ansible Automation Platform job templates.

### 7.4.1. Understanding the permission model

Self-service automation portal and Ansible Automation Platform use separate but related permission systems. Ansible Automation Platform RBAC is the source of truth for synchronization scope and execution permissions.

**Self-service automation portal RBAC:**

- Controls which users can view templates in the self-service automation portal catalog.
- Controls which users can access portal templates and submit jobs.

**Ansible Automation Platform RBAC:**

- **Controls synchronization scope:** Only Ansible Automation Platform job templates accessible by the configured Ansible Automation Platform token (ansible.rhaap.token) are synchronized to self-service automation portal.
- **Controls Ansible Automation Platform job template visibility and execution:** Ansible Automation Platform permissions determine whether authenticated users can view and execute Ansible Automation Platform job templates in self-service automation portal.
- **Validates execution permissions:** When a self-service automation portal user executes a template, Ansible Automation Platform checks that user’s execute permissions before launching the job.

Note

If a user can see a self-service automation portal template in the catalog but lacks Ansible Automation Platform execution permissions for the associated Ansible Automation Platform job template in Ansible Automation Platform, the user cannot run the Ansible Automation Platform Job.

### 7.4.2. Configuring RBAC for synchronization

Synchronization uses an Ansible Automation Platform token configured in the self-service automation portal to determine which data to synchronize from Ansible Automation Platform.

By default, self-service automation portal synchronizes Ansible Automation Platform Organization, Team, and User identity information. Self-service automation portal also synchronizes Ansible Automation Platform job template information accessible by the configured Ansible Automation Platform token.

**Prerequisites**

- You have credentials for an Ansible Automation Platform administrator.
- Synchronization of Ansible Automation Platform Organization information from Ansible Automation Platform is complete.
- Users who execute Ansible Automation Platform job templates through self-service automation portal must have job template **Execute** permissions assigned in Ansible Automation Platform for the respective Ansible Automation Platform job templates.
- The **Allow external users to create OAuth2 tokens** setting is enabled in the Settings → Platform gateway settings in Ansible Automation Platform.

**Procedure**

1. Log in to self-service automation portal with an account that has Ansible Automation Platform administrator privileges.

2. In the navigation pane of self-service automation portal, select Administration → RBAC.

3. Click Create to create a new role and enter a name, for example `portal-users`.

4. Click Next.


![Create new role](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/8e8d2b1e5b8d880bb39cb45ab87a43b6/self-service-create-new-rbac-role.png)

5. In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role, then click Next.


![Select users and groups table showing Members column](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/8ca5cfa49f4e0518a89cd408c80fc1ef/self-service-rbac-select-users-groups.png)

Note
The **Members** column displays the total count of users in each team, including both regular team members and administrators.

You can only select Ansible Automation Platform teams and users from the Ansible Automation Platform Organization that you have configured for synchronization with self-service automation portal.

6. Click Next to configure permissions in the **Add permission policies** section:


1. Select the **Catalog** plugin from the **Select plugins** dropdown menu.

2. Select the checkbox for `catalog.entity.read`.


![Add permission policies](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/7002db599883040e018acfd6d7f1e55c/self-service-add-permission-policies.png)

7. Select the **Scaffolder** plugin and enable all scaffolder permissions:


- `scaffolder.template.parameter.read`

- `scaffolder.template.step.read`

- `scaffolder.action.execute`

- `scaffolder.task.cancel`

- `scaffolder.task.create`

- `scaffolder.task.read`


Note
The `scaffolder.task.read` permission must be enabled so that users can view previous task runs in the **History** page in the self-service automation portal console.

8. Click Next to review your settings, then Create to create the new role.

On successful completion, your new role is included in the **All roles** list when you select Administration → RBAC in the navigation pane in self-service automation portal.

**Verification**

On successful completion, your new role is included in the **All roles** list when you select Administration → RBAC in the navigation pane in self-service automation portal.

**Additional resources**

- [Ansible Automation Platform token best practices](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-token-based-authentication#gw-oauth2-security-controls)

### 7.4.3. Configuring conditional access

Optionally, you can configure conditional self-service automation portal RBAC policies to filter role access to specific Ansible Automation Platform job templates by tag for specific Ansible Automation Platform teams or users.

Ansible Automation Platform labels applied to Ansible Automation Platform job templates are synchronized to self-service automation portal as tags and can be used for conditional access control.

Note

Ansible Automation Platform labels are converted to lowercase tags with special characters replaced by hyphens (for example, the Ansible Automation Platform label `Network-Automation` becomes the tag `network-automation`).

**Prerequisites**

- Ansible Automation Platform job templates must have Ansible Automation Platform labels applied and synchronized with self-service automation portal.
- Users who execute Ansible Automation Platform job templates through self-service automation portal must have Ansible Automation Platform job template **Execute** permissions assigned in Ansible Automation Platform for the respective Ansible Automation Platform job templates.

**Procedure**

1. Log in to self-service automation portal with an account that has Ansible Automation Platform administrator privileges.

2. In the navigation pane of self-service automation portal, select Administration → RBAC.

3. Click Create to create a new role and enter a name, for example `network-templates`.

4. Click Next.

5. In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role (for example, the Ansible Automation Platform network-team), then click Next.


![Select users and groups table showing Members column](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/8ca5cfa49f4e0518a89cd408c80fc1ef/self-service-rbac-select-users-groups.png)

Note
The **Members** column displays the total count of users in each team, including both regular team members and administrators.

You can only select Ansible Automation Platform teams and users from the Ansible Automation Platform Organization that you are using in self-service automation portal.

6. Click Next to configure permissions in the **Add permission policies** section:


- Select the **Catalog** plugin from the **Select plugins** dropdown menu.
- Select the checkbox for `catalog.entity.read`.
- Click Conditional to configure a condition-based policy.

7. In the condition builder, configure a rule to filter by tag:


- **Rule:** Select `HAS_METADATA` from the dropdown menu
- **Key:** Enter `tags`
- **Value:** Enter the tag value to filter by (for example, `network-automation`)

8. Select the **Scaffolder** plugin and enable all scaffolder permissions:


- `scaffolder.template.parameter.read`
- `scaffolder.template.step.read`
- `scaffolder.action.execute`
- `scaffolder.task.cancel`
- `scaffolder.task.create`
- `scaffolder.task.read`

9. Click Next to review your settings, then click Create to create the new role.

**Verification**

On successful completion, your new role is included in the **All roles** list when you select Administration → RBAC in the navigation pane in self-service automation portal.

1. Log in to self-service automation portal as a non-Ansible Automation Platform administrator user who is a member of a team you granted permissions to.

2. Verify that the user can see auto-generated templates in self-service automation portal.


- If you configured conditional access by tag, the user should see only templates with the specified tags.
- If you did not configure conditional access, the user should see all Ansible Automation Platform job templates for which they have job template **Execute** permissions in Ansible Automation Platform.

3. To verify execution permissions work correctly, attempt to execute a template:


1. If the user has job template **Execute** permissions in Ansible Automation Platform for the template, the user can view the template, and the job launches successfully.

### 7.4.4. Permissions reference for Ansible Automation Platform job template access

Permissions for Ansible Automation Platform job templates

| Permission | Resource type | Policy | Description |
| --- | --- | --- | --- |
| <br> `catalog.entity.read` | <br>  catalog-entity | <br>  read | <br>  Users can view synchronized Ansible Automation Platform job templates in the self-service automation portal. |
| <br> `scaffolder.template.parameter.read` | <br>  scaffolder-template | <br>  read | <br>  Users can read template parameters. |
| <br> `scaffolder.action.execute` | <br>  scaffolder-action | <br>  use | <br>  Users can execute actions through templates. |
| <br> `scaffolder.task.create` |  | <br>  create | <br>  Users can trigger the execution of Ansible Automation Platform job templates. |
| <br> `scaffolder.task.read` |  | <br>  read | <br>  Users can view task execution history and logs on the **History** page. |
| <br> `scaffolder.task.cancel` |  | <br>  use | <br>  Users can cancel currently running templates. |

## 7.5. Adjusting synchronization frequency between Ansible Automation Platform and self-service automation portal

The Helm chart defines how frequently users, teams and organization configuration information is synchronized from Ansible Automation Platform to self-service automation portal.

The frequency is set by the `catalog.providers.rhaap.schedule.frequency` key. By default, the synchronization occurs hourly.

**Procedure**

- To adjust the synchronization frequency, edit the value for the `catalog.providers.rhaap.schedule.frequency` key in the Helm chart.

catalog:
...
providers:
rhaap:
'{{- include "catalog.providers.env" . }}':
schedule:
frequency: {minutes: 60}
timeout: {seconds: 30}


Note
Increasing the synchronization frequency generates extra traffic.

Bear this in mind when deciding the frequency, particularly if you have a large number of users.

# Chapter 8. Upgrading self-service automation portal

To ensure that your self-service automation portal deployment has the latest features and fixes, you must upgrade the plug-in registry and Helm chart to the latest versions.

## 8.1. self-service automation portal version compatibility

When upgrading self-service automation portal, ensure version compatibility between the Helm chart, plug-in bundle, and Ansible Automation Platform version to avoid installation or upgrade failures.

### 8.1.1. Version components

A self-service automation portal deployment consists of three version-dependent components:

Helm chart version
The version of the self-service automation portal Helm chart deployed in OpenShift Container Platform. Example: `2.1.0`

Plug-in bundle version
The version of the Ansible plug-ins setup bundle downloaded from the Red Hat Customer Portal. Example: `self-service-automation-portal-plugins-2.1.0.tar.gz`

Ansible Automation Platform version
The version of Ansible Automation Platform that self-service automation portal connects to. Example: `2.6`

### 8.1.2. Version alignment requirements

For a successful self-service automation portal upgrade:

- The Helm chart version and plug-in bundle version must have matching major and minor versions. The patch version can differ, but the plug-in bundle patch version must be equal to or greater than the Helm chart patch version.

Example: Plug-in bundle version `2.1.1` is compatible with Helm chart version `2.1.0`, but plug-in bundle version `2.0.0` is not compatible with Helm chart version `2.1.0`.

- The self-service automation portal version must be compatible with your Ansible Automation Platform version.

See the [Ansible Automation Platform Life Cycle](https://access.redhat.com/support/policy/updates/ansible-automation-platform) for version compatibility information.

### 8.1.3. Common version mismatch scenarios

The following scenarios can cause upgrade failures:

Plug-in bundle and Helm chart mismatch
If you download plug-in bundle version `2.0.0` but upgrade to Helm chart version `2.1.0`, the installation fails because the major.minor versions do not match. Similarly, if the plug-in bundle patch version is lower than the Helm chart patch version, you might encounter compatibility issues.

Stale plug-in bundle
If you download a plug-in bundle, and a new version is released before you complete the installation, you might install an outdated bundle with a newer Helm chart. This causes version mismatch errors during deployment.

### 8.1.4. Best practices for version management

To avoid version mismatch issues during upgrades:

- Identify your target version before starting the upgrade process. Check the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) for the latest available versions.
- Download the plug-in bundle and upgrade the Helm chart in the same maintenance window to minimize the risk of version drift between download and installation.
- Verify the plug-in bundle version before extracting it. Check that the filename major.minor version (for example, `2.1` in `self-service-automation-portal-plugins-2.1.1.tar.gz`) matches your target Helm chart major.minor version. Ensure that the plug-in bundle patch version is equal to or greater than the Helm chart patch version.
- Keep a record of your current self-service automation portal version. Document the versions of all three components (Helm chart, plug-ins, Ansible Automation Platform) to simplify future upgrades and troubleshooting.

**Additional resources**

- [Ansible Automation Platform Life Cycle](https://access.redhat.com/support/policy/updates/ansible-automation-platform)
- [Installing the self-service automation portal in an air-gapped environment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_self-service_automation_portal/self-service-disconnected-install_aap-self-service-install)

## 8.2. Download plug-ins and push to the registry

To provide Ansible plug-ins to Red Hat Developer Hub, download the setup bundle and push the extracted files to a local Red Hat OpenShift registry.

By setting up a centralized httpd service, you can access these plug-in files through Helm chart configuration.

**Procedure**

1. Create a directory on your local machine to store the plug-in files.

mkdir /path/to/<ansible-backstage-plugins-local-dir>

2. Set an environment variable `$DYNAMIC_PLUGIN_ROOT_DIR` to represent the directory path.

export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/<ansible-backstage-plugins-local-dir>

3. Download the setup bundle. In a browser, navigate to the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software). and select the **Product Software** tab.

4. Click **Download now** next to **Ansible self-service automation portal Setup Bundle** to download the latest version of the plug-ins.

The format of the filename is `self-service-automation-portal-plugins-x.y.z.tar.gz`.

Substitute the Ansible plug-ins release version, for example `2.0.0`, for `x.y.z`.

5. Extract the contents to `$DYNAMIC_PLUGIN_ROOT_DIR`:

$ tar --exclude='*code*' -xzf self-service-automation-portal-plugins-x.y.z.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR

6. Verify that the extracted files are in the `$DYNAMIC_PLUGIN_ROOT_DIR` directory:

ls $DYNAMIC_PLUGIN_ROOT_DIR

You should see the following files:

ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity

The files with the .integrity file type contain the plug-in SHA value.

7. Create an httpd service as part of your OpenShift project:

oc new-build httpd --name=plugin-registry --binary
oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
oc new-app --image-stream=plugin-registry

**Verification**

1. Run the following command to verify that the plug-in registry deployed correctly:

oc exec $(oc get pods -l deployment=plugin-registry -o jsonpath='{.items[0].metadata.name}') -- ls -l /opt/app-root/src

2. Confirm that the required tarball files are in the plug-in registry.

**Helm chart configuration** When you configure the Helm chart, set `redhat-developer-hub.global.pluginMode` to `tarball`:

redhat-developer-hub:
global:
pluginMode: tarball

## 8.3. Updating the plug-in registry

To update the plug-in registry, you must upload your plug-in files to OpenShift, and start a new build of the registry.

**Prerequisites**

- You have downloaded the plug-in TAR files for self-service automation portal.
- You have set an environment variable, for example `$DYNAMIC_PLUGIN_ROOT_DIR`, to represent the path to the local directory where you have stored the TAR files.

**Procedure**

1. In a terminal, log in to your OpenShift Container Platform instance.

2. Open your OpenShift project for self-service automation portal.

$ oc project <YOUR_SELF_SERVICE_AUTOMATION_PORTAL_PROJECT>

3. Find the name of your current plug-in registry build configuration:

$ oc get buildconfig

4. From the output, identify the correct build configuration name, for example `aap-self-service-plugins`.

5. Run the following command to start a new build in in your OpenShift project.

$ oc start-build <build_config_name> --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait



- The command assumes that `$DYNAMIC_PLUGIN_ROOT_DIR` represents the directory for your TAR files. Replace this in the command if you have chosen a different environment variable name.
- Replace `<build_config_name>` with the build configuration name you identified.

When the build starts, the following message is displayed:

Uploading directory "/path/to/dynamic_plugin_root" as binary input for the build ...
Uploading finished

**Verification**

1. Open the **Topology** view in the **Developer** perspective for your project in the OpenShift web console.
2. Select the plugin registry icon to open the **plugin-registry** details pane.
3. In the **Pods** section of the **plugin-registry** details pane, select **View logs** for the new build pod. The format for the pod name is `<build_config_name>-<build_number>-build`.
4. Click the **terminal** tab and log in to the container.
5. In the terminal, run `ls` to view the TAR files in the plugin registry.
6. Verify that the new TAR files have been uploaded.

## 8.4. Updating the self-service automation portal version numbers for a Helm installation

After you have updated your plug-in registry for your self-service automation portal project on your OpenShift Container Platform instance, you must update the Helm chart with the new versions of your plug-ins files.

You can update the Helm chart from the command line using `helm` commands, or from the OpenShift web console.

Note

For upgrades in air-gapped or disconnected environments, the standard procedure cannot be used directly. You must first mirror the necessary container images to your local registry and prepare the Helm chart for offline use.

For detailed instructions on this process, see the [Installing the self-service automation portal in an air-gapped environment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_self-service_automation_portal/self-service-disconnected-install_aap-self-service-install) section of *[Installing self-service automation portal](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_self-service_automation_portal)*.

**Procedure**

- **Update the Helm chart from the command line:**


1. In a terminal, log in to your OpenShift instance.

2. Open your OpenShift Project that has your self-service automation portal installation.

3. Run the following command to ensure your Helm repository is up to date:

$ helm repo update

4. Find the latest version of the Helm chart:

$ helm search repo openshift-helm-charts/redhat-rhaap-portal

5. Upgrade the Helm release:

$ helm upgrade <release_name> openshift-helm-charts/redhat-rhaap-portal --version <chart_version>

Replace `<release_name>` with the name of your Helm release and `<chart_version>` with the new Helm chart version number you identified in the previous step.

- **Update the Helm chart using the OpenShift web console:**


1. In a browser, log in to your OpenShift Container Platform web console.
2. Switch to the **Developer** perspective.
3. Ensure you are in the OpenShift Project that has your self-service automation portal Helm deployment.
4. From the navigation menu, Select **Helm**.
5. Find your existing self-service automation portal deployment in the list of **Helm releases** and click its name.
6. Select Actions → Upgrade.
7. In the **Upgrade** pane, select the version that you want to upgrade to from the **Chart Version** dropdown list.
8. Review the YAML configuration to ensure your custom values are preserved.
9. Click Upgrade to begin the upgrade.

**Verification**

After the upgrade completes, verify that the updated self-service automation portal instance is running: . In the OpenShift Container Platform web console, navigate to the **Topology** view for your project. . Check that the self-service automation portal instance is available and that all associated pods are in a **Running** state.

## 8.5. Troubleshooting self-service automation portal upgrades

You might encounter issues during self-service automation portal upgrades. The following sections describe common problems and their solutions.

### 8.5.1. Plug-in version mismatch errors

**Symptom**: After you upgrade the Helm chart, self-service automation portal pods fail to start with errors indicating that plug-in files cannot be loaded or have incorrect versions.

**Cause**: The plug-in bundle major.minor version does not match the Helm chart major.minor version, or the plug-in bundle patch version is lower than the Helm chart patch version.

**Solution**:

1. Check your current plug-in bundle version:

oc exec $(oc get pods -l deployment=plugin-registry -o jsonpath='{.items[0].metadata.name}') -- \
ls -l /opt/app-root/src | grep ansible-plugin

The version number appears in the plug-in file names.

2. Identify your Helm chart version:

helm list -n <namespace>

Look for your self-service automation portal release and note the chart version.

3. If the versions do not match:


1. Download the correct plug-in bundle version from the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software).
2. Update your plug-in registry following the procedure in [Section 8.2, “Download plug-ins and push to the registry”](#rhdh-download-tar_self-service-upgrading "8.2.&nbsp;Download plug-ins and push to the registry").
3. Wait for the self-service automation portal pods to restart automatically.

### 8.5.2. Pods stuck in CrashLoopBackOff after upgrade

**Symptom**: After you upgrade, self-service automation portal pods repeatedly restart and show a status of `CrashLoopBackOff`.

**Cause**: Database schema migration failed, or the upgrade introduced configuration errors.

**Solution**:

1. Check the pod logs for specific error messages:

oc logs -n <namespace> <pod_name> --previous

2. If you see database migration errors:


1. Verify that your database is accessible:

oc exec -it -n <namespace> <pod_name> -- pg_isready -h <database_host>

2. Check database connection secrets:

oc get secret -n <namespace> | grep -i database

3. If you use an external database, verify that the database user has the required permissions.

3. If you see configuration errors:


1. Review your Helm values for syntax errors:

helm get values <release_name> -n <namespace>

2. Compare with your previous working configuration to identify changes.

3. Revert problematic configuration changes and upgrade again.

### 8.5.3. self-service automation portal upgrade considerations for Ansible Automation Platform 2.4 to 2.6

Consider the following when you upgrade self-service automation portal from Ansible Automation Platform 2.4 to Ansible Automation Platform 2.6:

1. Upgrade your Ansible Automation Platform instance to version 2.6 before you upgrade self-service automation portal.

The self-service automation portal version that is compatible with Ansible Automation Platform 2.6 requires Ansible Automation Platform 2.6 features for full functionality.

2. Review the Ansible Automation Platform 2.6 release notes for breaking changes that affect self-service automation portal.

3. Back up your existing self-service automation portal configuration before you upgrade:

helm get values <release_name> -n <namespace> > backup-values.yaml

4. After you upgrade, verify that OAuth authentication still functions:


1. Check that your OAuth application in Ansible Automation Platform is configured correctly.
2. Test the sign-in functionality.
3. If authentication fails, verify that the OAuth redirect URL matches your upgraded deployment URL.

5. Update any custom templates or configurations to use syntax that is compatible with the new self-service automation portal version.

### 8.5.4. Helm upgrade fails with a `release not found` error

**Symptom**: Running `helm upgrade` returns an error stating that the release cannot be found.

**Cause**: The Helm release name or namespace is incorrect.

**Solution**:

1. List all Helm releases in your cluster:

helm list --all-namespaces

2. Identify the correct release name and namespace for your self-service automation portal deployment.

3. Run the upgrade command with the correct parameters:

helm upgrade <correct_release_name> openshift-helm-charts/redhat-rhaap-portal \
--version <target_version> \
-n <correct_namespace>

### 8.5.5. Custom values lost after upgrade

**Symptom**: After you upgrade, your custom configurations (such as custom CA certificates, OAuth settings, or RBAC configurations) are no longer applied.

**Cause**: The upgrade command did not include your custom values file, or the values were overwritten.

**Solution**:

1. Before you upgrade, export your current values:

helm get values <release_name> -n <namespace> > current-values.yaml

2. When you upgrade, specify your values file:

helm upgrade <release_name> openshift-helm-charts/redhat-rhaap-portal \
--version <target_version> \
-f current-values.yaml \
-n <namespace>

3. After you upgrade, verify that your custom values are still applied:

helm get values <release_name> -n <namespace>

**Additional resources**

- [Section 8.1, “self-service automation portal version compatibility”](#self-service-version-compatibility_self-service-upgrading "8.1.&nbsp;self-service automation portal version compatibility")

# Chapter 9. Telemetry capturing

The telemetry data collection feature helps in collecting and analyzing the telemetry data to improve your experience with self-service automation portal. This feature is enabled by default.

## 9.1. Telemetry data collected by Red Hat

Red Hat collects and analyses the following data:

- Events of page visits and clicks on links or buttons.
- System-related information, for example, locale, timezone, user agent including browser and OS details.
- Page-related information, for example, title, category, extension name, URL, path, referrer, and search parameters.
- Anonymized IP addresses, recorded as `0.0.0.0`.
- Anonymized username hashes, which are unique identifiers used solely to identify the number of unique users of the RHDH application.
- Feedback and sentiment submitted through the self-service automation portal feedback form, including a 1-5 star rating and feedback text. Users must acknowledge that they share the feedback with Red Hat before submitting.

Note

The feedback form is disabled by default and optional. For information about enabling the feedback form, see [Enabling feedback to Red Hat](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_self-service_automation_portal/index#proc-self-service-enable-feedback_self-service-telemetry) in *Configuring self-service automation portal*.

## 9.2. Disabling telemetry data collection

You can disable and enable the telemetry data collection feature for self-service automation portal by updating the Helm chart for your OpenShift Container Platform project.

**Procedure**

1. Log in to the OpenShift Container Platform console and open the project for self-service automation portal in the **Developer** perspective.

2. Navigate to **Helm**.

3. Click the **More actions ⋮** icon for your self-service automation portal Helm chart and select **Upgrade**.

4. Select **YAML view**.

5. Locate the `redhat-developer-hub.global.dynamic.plugins` section of the Helm chart.

6. To disable telemetry data collection, add the following lines to the `redhat-developer-hub.global.dynamic.plugins` section.

redhat-developer-hub:
global:
....
dynamic:
plugins:
- disabled: true
package: >-
./dynamic-plugins/dist/backstage-community-plugin-analytics-provider-segment

To re-enable telemetry data collection, delete these lines.

7. Click Upgrade to apply the changes to the Helm chart and restart the pod.

# Legal Notice

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
