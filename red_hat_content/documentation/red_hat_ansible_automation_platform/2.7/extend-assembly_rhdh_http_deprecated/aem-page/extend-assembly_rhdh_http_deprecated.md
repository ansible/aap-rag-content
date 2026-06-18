+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_http_deprecated"
template = "docs/aem-title.html"
title = "Install Ansible plug-ins using an HTTP plug-in registry (deprecated) - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_intro/", "Ansible plug-ins for Red Hat Developer Hub"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_http_deprecated/aem-page/extend-assembly_rhdh_http_deprecated.html"
last_crumb = "Install Ansible plug-ins using an HTTP plug-in registry (deprecated)"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Install Ansible plug-ins using an HTTP plug-in registry (deprecated)"
oversized = "false"
page_slug = "extend-assembly_rhdh_http_deprecated"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_http_deprecated"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_http_deprecated/toc/toc.json"
type = "aem-page"
+++

# Install Ansible plug-ins using an HTTP plug-in registry (deprecated)

The HTTP plug-in registry installation method is deprecated and will be removed in a future release. Use OCI-based plug-in delivery instead.

## Install Ansible plug-ins using an HTTP plug-in registry (deprecated)

The HTTP plug-in registry method is deprecated and will be removed in a future release. Red Hat recommends using OCI-based plug-in delivery instead.

 Important:

The HTTP plug-in registry method is deprecated and will be removed in a future release. Red Hat recommends using OCI-based plug-in delivery as described in the main installation procedure. For disconnected environments, use OCI image mirroring instead of an HTTP registry.

The following procedures describe how to install the Ansible plug-ins using an HTTP plug-in registry hosted in your OpenShift Container Platform cluster. This method requires downloading plug-in tarballs, creating an HTTP registry in the cluster, and referencing the plug-ins by HTTP URL with SHA integrity hashes.

## Download the Ansible plug-ins files

Download the Ansible plug-ins for Red Hat Developer Hub **Setup Bundle** from the Red Hat Ansible Automation Platform Product Software downloads page.

### Procedure

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

### Results

Run `ls` to verify that the extracted files are in the `$DYNAMIC_PLUGIN_ROOT_DIR` directory:

```
$ ls $DYNAMIC_PLUGIN_ROOT_DIR
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity
```
The files with the `.integrity` file type contain the plugin SHA value. The SHA value is used during the plug-in configuration.

## Create a registry for the Ansible plug-ins

Set up a registry in your OpenShift cluster to host the Ansible plug-ins and make them available for installation in Red Hat Developer Hub (RHDH).

### Procedure

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

### Results

To verify that the plugin-registry was deployed successfully, open the **Topology** view in the **Developer** perspective on the Red Hat Developer Hub application in the OpenShift Web console.

1. Click the plug-in registry to view the log.  
![Developer perspective](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rhdh-plugin-registry.png)  
     (1) Developer hub instance

     (2) Plug-in registry

2. Click the terminal tab and login to the container.

3. In the terminal, run `ls` to confirm that the `.tar` files are in the plugin registry.

```
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
```
     The version numbers and file names can differ.

## Install the plug-ins from the HTTP registry

Add the Ansible plug-ins from the HTTP registry to your Red Hat Developer Hub dynamic plug-in configuration.

### About this task

For each plug-in, you need the HTTP URL to the `.tgz` file in the registry and the SHA-512 integrity hash from the corresponding `.integrity` file.

### Procedure

1.  Add the plug-ins to your dynamic plug-ins configuration. Replace `<x.y.z>` with the correct plug-in version. Use the SHA-512 hash from the corresponding `.integrity` file for each `integrity` value.
      **Operator installation**

    Add the plug-ins to your dynamic plug-ins ConfigMap (for example, `rhaap-dynamic-plugins-config`).

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: rhaap-dynamic-plugins-config
data:
  dynamic-plugins.yaml: |
    # ...
    plugins:
      - disabled: false
        package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-<x.y.z>.tgz'
        integrity: <SHA512_value>
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
          http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-<x.y.z>.tgz
        integrity: <SHA512_value>
        pluginConfig:
          dynamicPlugins:
            backend:
              ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```
    Reference this ConfigMap in your `Backstage` CR under `spec.application.dynamicPluginsConfigMapName`.

    **Helm chart installation**

    In the OpenShift Container Platform Developer UI, navigate to **Helm** > **developer-hub** > **Actions** > **Upgrade** > **Yaml view**. Add the plug-ins under the `global.dynamic.plugins` section.

```yaml
global:
  # ...
    plugins:
      - disabled: false
        integrity: <SHA512_value>
        package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-<x.y.z>.tgz'
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
        integrity: <SHA512_value>
        package: >-
          http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-<x.y.z>.tgz
        pluginConfig:
          dynamicPlugins:
            backend:
              ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```

2.  Apply the changes. For Helm deployments, click **Upgrade**. The Developer Hub pods restart and the plug-ins are installed.

### Results

1. In the OpenShift Container Platform web console, open the pod details for the Red Hat Developer Hub deployment.
2. Select the **Logs** tab and choose the `install-dynamic-plugins` container from the drop-down list.
3. Search the log for the Ansible plug-ins. A successful installation produces log entries similar to:

```terminal
=> Successfully installed dynamic plugin http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-<x.y.z>.tgz
```

After installing the plug-ins from the HTTP registry, continue with the configuration steps.
