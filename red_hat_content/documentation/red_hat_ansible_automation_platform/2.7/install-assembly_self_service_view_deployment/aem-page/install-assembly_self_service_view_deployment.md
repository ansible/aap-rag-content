+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_view_deployment"
title = "Verify the configuration - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_about/", "Install Ansible automation portal (OpenShift Container Platform only)"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_view_deployment/aem-page/install-assembly_self_service_view_deployment.html"
last_crumb = "Verify the configuration"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Verify the configuration"
oversized = "false"
page_slug = "install-assembly_self_service_view_deployment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_view_deployment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_view_deployment/toc/toc.json"
type = "aem-page"
+++

# Verify the configuration

You can inspect the deployment logs and ConfigMap on the OpenShift console to verify that the deployment conforms with the settings in your Helm chart.

## View the deployment logs

Inspect the `install-dynamic-plugins` init container logs to confirm that plug-ins installed from your configured delivery method.

### Procedure

1.  In a browser, log in to your OpenShift instance.
2.  In the **Developer** perspective, open the **Topology** view for the namespace where you deployed the chart.
3.  Select the deployment named `<release-name>-rhaap-portal`.
4.  Open the deployment pod logs.
5.  In the pod details page, select the **Logs** tab.
6.  From **Init containers**, select `install-dynamic-plugins`.
      **Expected log output for OCI delivery (recommended)**

    When `pluginMode` is `oci`, successful installation resembles the following output:

```
======= Installing dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>!ansible-backstage-plugin-catalog-backend-module-rhaap
...
-> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>!ansible-backstage-plugin-catalog-backend-module-rhaap
```
    Replace `<plugin-version>` with the value from your `imageTagInfo` setting. If you use a mirror registry, the registry host in the log reflects your `imageRegistry` or `ociPluginImage` configuration.

    **Expected log output for HTTP plug-in registry (deprecated)**

    When `pluginMode` is `tarball`, successful installation resembles the following output:

```
======= Installing dynamic plugin http://plugin-registry:8080/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-x.y.z.tgz
...
-> Successfully installed dynamic plugin http://plugin-registry:8080/ansible-backstage-plugin-catalog-backend-module-rhaap-dynamic-x.y.z.tgz
```
    The tarball file name includes the plug-in version from your bundle.

7.  On the **Environment** tab, verify that environment variables from your Helm chart appear as expected.
