+++
title = "Install with a Helm chart - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_install_ocp_helm"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_intro/", "Install Ansible plug-ins for Red Hat Developer Hub"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_install_ocp_helm/aem-page/install-assembly_rhdh_install_ocp_helm.html"
last_crumb = "Install with a Helm chart"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Install with a Helm chart"
oversized = "false"
page_slug = "install-assembly_rhdh_install_ocp_helm"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_install_ocp_helm"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_install_ocp_helm/toc/toc.json"
type = "aem-page"
+++

# Install with a Helm chart

The following procedures describe how to install Ansible plug-ins in Red Hat Developer Hub instances on Red Hat OpenShift Container Platform using a Helm chart.

The workflow is as follows:

1. Download the Ansible plug-ins files.
2. Create a plug-in registry in your OpenShift cluster to host the Ansible plug-ins.
3. Add the plug-ins to the Helm chart.
4. Create a custom ConfigMap.
5. Add your custom ConfigMap to your Helm chart.
6. Edit your custom ConfigMap and Helm chart according to the required and optional configuration procedures.  Note:
      You can save changes to your Helm and ConfigMap after each update to your configuration. You do not have to make all the changes to these files in a single session.

## Prerequisites

To proceed, you must have Red Hat Developer Hub installed on Red Hat OpenShift Container Platform (RHOCP) and a valid subscription to Red Hat Ansible Automation Platform.

- Red Hat Developer Hub installed on Red Hat OpenShift Container Platform.   * For Helm installation, follow the steps in the Installing Red Hat Developer Hub on OpenShift Container Platform with the Helm chart section of *Installing Red Hat Developer Hub on OpenShift Container Platform*.
  * For Operator installation, follow the steps in the Installing Red Hat Developer Hub on OpenShift Container Platform with the Operator section of *Installing Red Hat Developer Hub on OpenShift Container Platform*.
- A valid subscription to Red Hat Ansible Automation Platform.
- An OpenShift Container Platform instance with the appropriate permissions within your project to create an application.
- The Red Hat Developer Hub instance can query the automation controller API.
- Optional: To use the integrated learning paths, you must have outbound access to developers.redhat.com.

## Recommended RHDH preconfiguration

Red Hat recommends performing the following initial configuration tasks in Red Hat Developer Hub (RHDH). However, you can install the Ansible plug-ins for Red Hat Developer Hub before completing these tasks.

- Authentication in Red Hat Developer Hub
- Authorization in Red Hat Developer Hub


 Note:

Red Hat provides a repository of software templates for RHDH that uses the `publish:github` action. To use these software templates, you must install the required GitHub dynamic plugins.

## Plug-in delivery method

Ansible plug-ins for Red Hat Developer Hub support two delivery methods. Select the method that fits your environment.

Ansible automation portal supports two plug-in delivery methods:

- **OCI container delivery (recommended)**: Ansible automation portal automatically pulls an Open Container Initiative (OCI) container from `registry.redhat.io` that contains the plug-ins. Use this method for new installations.
- **HTTP plug-in registry (deprecated)**: Manually create an HTTP plug-in registry that hosts plug-in tarball files. This method is deprecated and will be removed in a future release of Ansible Automation Platform. Existing installations that use this method should migrate to OCI container delivery.


 Note:

If you are installing Ansible automation portal in a disconnected or air-gapped OpenShift Container Platform environment, complete the pre-installation configuration in this chapter and then follow the procedures in the disconnected installation chapter. The disconnected installation chapter includes additional steps for mirroring container images, configuring registry authentication, and installing the Helm chart in isolated environments.

### Use OCI container delivery method

Red Hat Developer Hub pulls the Ansible plug-ins directly from `registry.redhat.io` as OCI artifacts. This is the recommended method that requires a registry authentication secret in the same OpenShift project as your Red Hat Developer Hub deployment.

#### Before you begin

- You have a Red Hat account with access to `registry.redhat.io`.
- You have a registry service account token from the Red Hat Customer Portal.
- You have access to the OpenShift project. In the same project you had installed Red Hat Developer Hub.
- You have installed the OpenShift CLI (`oc`) and logged in to your cluster.

#### About this task

This method is the default for the Helm chart and is the recommended method for production deployments.

#### Procedure

1.  Create an auth.json file on your local machine with your `registry.redhat.io` credentials:
  

```json
{
  "auths": {
    "registry.redhat.io": {
      "auth": "<base64-encoded-username:password>"
    }
  }
}
```
    To generate the base64-encoded value use the `printf '%s' '<username>:<password>' | base64` command.

2.  Create the authentication secret in the OpenShift project where you installed Red Hat Developer Hub.
      The secret name must follow the pattern `<deployment-name>-dynamic-plugins-registry-auth`, where `<deployment-name>` matches your Red Hat Developer Hub deployment name.

  -          For a default Red Hat Developer Hub Helm installation with release name `developer-hub`:



```
oc create secret generic developer-hub-dynamic-plugins-registry-auth \
  --from-file=auth.json=./auth.json
```

  -          If you use a different Helm release name:



```
oc create secret generic <deployment-name>-dynamic-plugins-registry-auth \
  --from-file=auth.json=./auth.json
```

  -          If you already have Podman credentials configured locally:



```
oc create secret generic <deployment-name>-dynamic-plugins-registry-auth \
  --from-file=auth.json=${XDG_RUNTIME_DIR}/containers/auth.json
```

  
   Important:
      Create this secret in the same OpenShift project as your Red Hat Developer Hub deployment, and create it before you configure the plug-ins. Use a Red Hat Registry service account token, not your personal Red Hat account credentials.

#### Results

Verify that the secret exists in the project:

```
oc get secret <deployment-name>-dynamic-plugins-registry-auth
```

### HTTP plug-in registry

The HTTP plug-in registry method hosts plug-in tarball files in a local OpenShift registry that the dynamic plug-in installer pulls during startup.

 Important:

The HTTP plug-in registry method is deprecated and will be removed in a future release of Red Hat Ansible Automation Platform. Use [OCI container delivery](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_self_service_oci_container_delivery "Use OCI container delivery to pull plug-in artifacts from registry.redhat.io/ansible-automation-platform/automation-portal. The plug-in version must match the imageTagInfo value in your Helm chart configuration. This is the recommended method for new installations.") for new installations. The Ansible automation portal setup bundle on the [Product Software downloads page](https://access.redhat.com/downloads/content/480/) is provided for existing installations that have not yet migrated to OCI delivery.

#### Download the Ansible plug-ins files

Download the Ansible plug-ins for Red Hat Developer Hub **Setup Bundle** from the Red Hat Ansible Automation Platform Product Software downloads page.

##### Procedure

1.  In a browser, navigate to the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) and select the **Product Software** tab.
2.  Click **Download now** next to **Ansible plug-ins for Red Hat Developer Hub Setup Bundle** to download the latest version of the plug-ins. The format of the filename is `ansible-rhdh-plugins-x.y.z.tar.gz`. Substitute the Ansible plug-ins release version, for example `2.0.0`, for `x.y.z`.

3.  Create a directory on your local machine to store the `.tar` files.

```
$ mkdir /path/to/<ansible-backstage-plugins-local-dir-changeme>
```

4.  Set an environment variable (`$DYNAMIC_PLUGIN_ROOT_DIR`) to represent the directory path.

```
$ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/<ansible-backstage-plugins-local-dir-changeme>
```

5.  Extract the `ansible-rhdh-plugins-<version-number>.tar.gz` contents to `$DYNAMIC_PLUGIN_ROOT_DIR`.

```
$ tar --exclude='*code*' -xzf ansible-rhdh-plugins-x.y.z.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR
```
    Substitute the Ansible plug-ins release version, for example `2.0.0`, for `x.y.z`.

##### Results

Run `ls` to verify that the extracted files are in the `$DYNAMIC_PLUGIN_ROOT_DIR` directory:

```
$ ls $DYNAMIC_PLUGIN_ROOT_DIR
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity
```
The files with the `.integrity` file type contain the plugin SHA value. The SHA value is used during the plug-in configuration.

#### Create a registry for the Ansible plug-ins

Set up a registry in your OpenShift cluster to host the Ansible plug-ins and make them available for installation in Red Hat Developer Hub (RHDH).

##### Procedure

1.  Log in to your OpenShift Container Platform instance with credentials to create a new application.
2.  Open your Red Hat Developer Hub OpenShift project.

```
$ oc project <YOUR_DEVELOPER_HUB_PROJECT>
```

3.  Run the following commands to create a plug-in registry build in the OpenShift cluster.

```
$ oc new-build httpd --name=plugin-registry --binary
$ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
$ oc new-app --image-stream=plugin-registry
```

##### Results

To verify that the plugin-registry was deployed successfully, open the **Topology** view in the **Developer** perspective on the Red Hat Developer Hub application in the OpenShift Web console.

1. Click the plug-in registry to view the log.  
![Developer perspective](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/rhdh-plugin-registry.png)  
     (1) Developer hub instance

     (2) Plug-in registry

2. Click the terminal tab and login to the container.

3. In the terminal, run `ls` to confirm that the `.tar` files are in the plugin registry.

```
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
```
     The version numbers and file names can differ.
