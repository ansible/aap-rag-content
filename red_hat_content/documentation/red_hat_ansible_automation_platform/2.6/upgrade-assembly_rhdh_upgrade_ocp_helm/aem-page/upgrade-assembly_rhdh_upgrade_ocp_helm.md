+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_rhdh_upgrade_ocp_helm"
title = "Upgrade the Ansible plug-ins with Helm - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-upgrade_additional_services_for_ansible_automation_platform/", "Upgrade additional services for Ansible Automation Platform"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-assembly_rhdh_upgrade_ocp_helm/aem-page/upgrade-assembly_rhdh_upgrade_ocp_helm.html"
last_crumb = "Upgrade the Ansible plug-ins with Helm"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Upgrade the Ansible plug-ins with Helm"
oversized = "false"
page_slug = "upgrade-assembly_rhdh_upgrade_ocp_helm"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-assembly_rhdh_upgrade_ocp_helm"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-assembly_rhdh_upgrade_ocp_helm/toc/toc.json"
type = "aem-page"
+++

# Upgrade the Ansible plug-ins with Helm

To upgrade the Ansible plug-ins, you must update the `plugin-registry` application with the latest Ansible plug-ins files.

## Download the Ansible plug-ins files

Download the Ansible plug-ins for Red Hat Developer Hub **Setup Bundle** from the Red Hat Ansible Automation Platform Product Software downloads page.

### About this task

Important:

The HTTP plug-in registry method is deprecated and will be removed in a future release of Red Hat Ansible Automation Platform. For new installations, use OCI container delivery instead.

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

## Update the plug-in registry

Rebuild your plug-in registry application in your OpenShift cluster with the latest Ansible plug-ins files.

### Before you begin

- You have downloaded the Ansible plug-ins files.
- You have set an environment variable, for example `$DYNAMIC_PLUGIN_ROOT_DIR`, to represent the path to the local directory where you have stored the `.tar` files.

### Procedure

1.  Log in to your OpenShift Container Platform instance with credentials to create a new application.
2.  Open your Red Hat Developer Hub OpenShift project.

```
$ oc project <YOUR_DEVELOPER_HUB_PROJECT>
```

3.  Run the following commands to update your plug-in registry build in the OpenShift cluster. The commands assume that `$DYNAMIC_PLUGIN_ROOT_DIR` represents the directory for your `.tar` files. Replace this in the command if you have chosen a different environment variable name.

```
$ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
```

4.  When the registry has started, the output displays the following message:
  

```
Uploading directory "/path/to/dynamic_plugin_root" as binary input for the build …
Uploading finished
build.build.openshift.io/plugin-registry-1 started
```

### Results

Verify that the `plugin-registry` has been updated.

1. In the OpenShift UI, click **Topology**.
2. Click the **redhat-developer-hub** icon to view the pods for the plug-in registry.
3. Click **View logs** for the plug-in registry pod.
4. Open the **Terminal** tab and run `ls` to view the `.tar` files in the `plug-in registry`.
5. Verify that the new `.tar` file has been uploaded.

## Update the Ansible plug-ins version numbers for a Helm installation

To upgrade the Ansible plug-ins, you must update the `imageTagInfo` parameter in the Helm chart configuration to the desired version. This triggers the Red Hat Developer Hub to pull the new container images directly from the Red Hat registry.

### Procedure

1.  Log in to your Red Hat OpenShift Container Platform instance.
2.  In the OpenShift Developer UI, navigate to Helm> (and then)developer-hub> (and then)Actions> (and then)Upgrade> (and then)Yaml view.
3.  Locate the `global` section.
  

```yaml
...
global:
  # Ensure OCI mode is enabled
  pluginMode: oci

    # UPDATE this value to the new desired version
  imageTagInfo: "2.1"

    # Note: Do not manually update 'plugins' packages;
  # OCI mode handles the download automatically based on the tag above.
  dynamic:
    plugins: []
```

4.  Click Upgrade.
      The Red Hat Developer Hub pods restart and pull the new plug-in versions.

### Results

1. In the OpenShift UI, click Topology.
2. Make sure that the Red Hat Developer Hub instance is available.
