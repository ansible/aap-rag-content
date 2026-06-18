+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_install_ocp_operator"
title = "Install with the Ansible Automation Platform Operator on OpenShift Container Platform - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_intro/", "Install Ansible plug-ins for Red Hat Developer Hub"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_install_ocp_operator/aem-page/install-assembly_rhdh_install_ocp_operator.html"
last_crumb = "Install with the Ansible Automation Platform Operator on OpenShift Container Platform"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Install with the Ansible Automation Platform Operator on OpenShift Container Platform"
oversized = "false"
page_slug = "install-assembly_rhdh_install_ocp_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_install_ocp_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_rhdh_install_ocp_operator/toc/toc.json"
type = "aem-page"
+++

# Install with the Ansible Automation Platform Operator on OpenShift Container Platform

The following procedures describe how to install Ansible plug-ins in Red Hat Developer Hub instances on Red Hat OpenShift Container Platform using the Operator.

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

## Add a sidecar container for Ansible development tools

Add a sidecar container for Ansible development tools in the Developer Hub pod. To do this, you must modify the base ConfigMap for the Red Hat Developer Hub deployment.

### Procedure

1.  In the OpenShift console, select the **Topology** view.
2.  Click **More actions ⋮** on the developer-hub instance and select **Edit backstage** to open the **Backstage details** page.
3.  Select the **YAML** tab.
4.  In the editing pane, add a `containers` block in the `spec.deployment.patch.spec.template.spec` block:
  

```
apiVersion: rhdh.redhat.com/v1alpha4
kind: Backstage
metadata:
  name: developer-hub
spec:
  deployment:
    patch:
      spec:
        template:
          spec:
            containers:
              - command:
                  - adt
                  - server
                image: registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel8:latest
                imagePullPolicy: always
                ports:
                  - containerPort: 8000
                    protocol: TCP
                terminationMessagePolicy: file
```

5.  Click Save.  Note:
      If you want to add extra environment variables to your deployment, you can add them in the `spec.application.extraEnvs` block:

```
spec:
  application:
    ...
    extraEnvs:
      envs:
        - name: <env_variable_name>
          value: <env_variable_value>
```

## Plug-in delivery method when using the Operator

Ansible plug-ins for Red Hat Developer Hub support two delivery methods. Select the method that fits your environment.

- **OCI container delivery (recommended)**: Red Hat Developer Hub pulls the Ansible plug-ins directly from `registry.redhat.io` as OCI artifacts during startup. Use this method for new installations.
- **HTTP plug-in registry (deprecated)**: Manually download the Ansible plug-ins tarball files and deploy an HTTP plug-in registry in your OpenShift cluster. This method is deprecated and will be removed in a future release of Ansible Automation Platform. Existing installations that use this method should migrate to OCI container delivery.


Complete one of the following procedures before configuring the dynamic plug-ins.

### Use the OCI container delivery with the Operator

Red Hat Developer Hub pulls the Ansible plug-ins directly from `registry.redhat.io` as OCI artifacts. This method requires a registry authentication secret in the same OpenShift project as your Red Hat Developer Hub deployment.

#### Before you begin

- You have a Red Hat account with access to `registry.redhat.io`.
- You have a registry service account token from the Red Hat Customer Portal. For more information, see [Registry Service Accounts](https://access.redhat.com/terms-based-registry/).
- You have access to the OpenShift project where you had installed Red Hat Developer Hub.
- You have installed the OpenShift CLI (`oc`) and logged in to your cluster.

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
    To generate the base64-encoded value, use the `printf '%s' '<username>:<password>' | base64` command.

2.  Create the authentication secret in the OpenShift project where you had installed Red Hat Developer Hub.
      The secret name must follow the pattern `<deployment-name>-dynamic-plugins-registry-auth`, where `<deployment-name>` matches the `metadata.name` of your Backstage custom resource.

  -          For a default Operator installation with name `developer-hub`:



```
oc create secret generic developer-hub-dynamic-plugins-registry-auth \
  --from-file=auth.json=./auth.json
```

  -          If you already have Podman credentials configured locally:



```
oc create secret generic <deployment-name>-dynamic-plugins-registry-auth \
  --from-file=auth.json=${XDG_RUNTIME_DIR}/containers/auth.json
```

  
   Important:
      Create this secret in the same OpenShift project as your Red Hat Developer Hub deployment, and create it before you configure the plug-ins.

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

## Install the dynamic plug-ins

To install the dynamic plugins, add them to your ConfigMap for your Red Hat Developer Hub plugin settings (for example, `rhaap-dynamic-plugins-config`).

### About this task

If you have not already created a ConfigMap file for your Red Hat Developer Hub plugin settings, create one by following the procedure in the Creating and using config maps section of the Red Hat OpenShift Container Platform Nodes guide.

### Procedure

1.  Select ConfigMaps in the navigation pane of the OpenShift console.
2.  Select the `rhaap-dynamic-plugins-config` ConfigMap from the list.
3.  Select the YAML tab to edit the `rhaap-dynamic-plugins-config` ConfigMap.
4.  Add the Ansible plug-ins. Choose the configuration that matches your delivery method.
  -          **OCI container delivery method (recommended)**:



```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: rhaap-dynamic-plugins-config
data:
  dynamic-plugins.yaml: |
    includes:
      - dynamic-plugins.default.yaml
    plugins:
      - disabled: false
        package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-backstage-rhaap'
        pluginConfig:
          dynamicPlugins:
            frontend:
              ansible.plugin-backstage-rhaap:
                appIcons:
                  - importName: AnsibleLogo
                    name: AnsibleLogo
                dynamicRoutes:
                  - importName: AnsiblePage
                    menuItem:
                      icon: AnsibleLogo
                      text: Ansible
                    path: /ansible
      - disabled: false
        package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-scaffolder-backend-module-backstage-rhaap'
        pluginConfig:
          dynamicPlugins:
            backend:
              ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```
         Replace `x.y.z` with the Ansible plug-ins version.

  -          **HTTP plug-in registry method (deprecated)**:



```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: rhaap-dynamic-plugins-config
data:
  dynamic-plugins.yaml: |
    includes:
      - dynamic-plugins.default.yaml
    plugins:
      - disabled: false
        package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'
        integrity: <SHA512 value>
        pluginConfig:
          dynamicPlugins:
            frontend:
              ansible.plugin-backstage-rhaap:
                appIcons:
                  - importName: AnsibleLogo
                    name: AnsibleLogo
                dynamicRoutes:
                  - importName: AnsiblePage
                    menuItem:
                      icon: AnsibleLogo
                      text: Ansible
                    path: /ansible
      - disabled: false
        package: >-
          http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
        integrity: <SHA512 value>
        pluginConfig:
          dynamicPlugins:
            backend:
              ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```

5.  Click Save.

### Results

1. In the OpenShift console, select the Topology view.
2. Click the Open URL icon on the deployment pod to open your Red Hat Developer Hub instance in a browser window.


The Ansible plug-in is present in the navigation pane. If you select Administration, you can see the installed plug-ins in the Plugins tab.
