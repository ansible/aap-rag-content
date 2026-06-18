+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_helm_install"
template = "docs/aem-title.html"
title = "Install the Ansible automation portal Helm chart - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_about/", "Install Ansible automation portal (OpenShift Container Platform only)"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_helm_install/aem-page/install-assembly_self_service_helm_install.html"
last_crumb = "Install the Ansible automation portal Helm chart"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Install the Ansible automation portal Helm chart"
oversized = "false"
page_slug = "install-assembly_self_service_helm_install"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_helm_install"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_helm_install/toc/toc.json"
type = "aem-page"
+++

# Install the Ansible automation portal Helm chart

You can use the configured secrets and plugin registry to install the Ansible automation portal. Deploy the application onto your OpenShift cluster using the provided Helm chart.

## Configure the Helm chart from the OpenShift catalog

Deploy the Helm chart from the OpenShift catalog by configuring the base URL and organization name in the YAML view. This launches the Ansible automation portal installation.

### Before you begin

- You have created a project for Ansible automation portal in OpenShift Container Platform.
- You have created secrets in OpenShift Container Platform for Red Hat Ansible Automation Platform authentication.
- If you configure SCM integration (for example, importing from private repositories or using templates that access SCM), you have created secrets in OpenShift for SCM authentication.
- You have completed one of the plug-in delivery methods:
  * For OCI delivery: You have created the `<release-name>-dynamic-plugins-registry-auth` secret.
  * For HTTP plug-in registry (deprecated): You have deployed the plug-in registry and plan to set `pluginMode` to `tarball`.

### Procedure

1.  In the OpenShift Container Platform web console, select the Developer view.
2.  Select your project and click the Helm option in the OpenShift sidebar.
3.  Click Create and select Helm Release.
4.  Search for `Portal` in the Helm Charts filter, and select the Automation Portal chart.
5.  Click Create and select the YAML view.
6.  Update the `clusterRouterBase` value with the base URL of your OpenShift instance.
  
   Important:
      You must replace the default `apps.example.com` placeholder value. If the default value remains, Helm chart validation fails.

```
redhat-developer-hub:
  global:
    clusterRouterBase: apps.example.com
```

7.  Configure the plug-in delivery mode and version by setting the `pluginMode` and `imageTagInfo` keys:
  - For OCI delivery, set `pluginMode` to `oci`.
      Set `imageTagInfo` to the plug-in version from the Helm chart or the lifecycle page. To determine the correct version tag, see "Determine version tags before you install".

  

```
redhat-developer-hub:
  global:
    pluginMode: oci
    imageTagInfo: "<plugin-version>"
```

8.  Set the Red Hat Ansible Automation Platform organization to synchronize. The default value is `Default`. Update the `orgs` key to match your organization name:
  

```
redhat-developer-hub:
  upstream:
    backstage:
      appConfig:
        catalog:
          providers:
            rhaap:
              '{{- include "catalog.providers.env" . }}':
                orgs: "<your-aap-organization-name>"
```

9.  **Optional:** Update the `CUSTOMER_SUPPORT_URL` to point to your support portal:
  

```
redhat-developer-hub:
  upstream:
    backstage:
      extraEnvVars:
        - name: CUSTOMER_SUPPORT_URL
          value: https://access.redhat.com/support
```

10.  Click Create.

## Verify the installation

Verify the Helm chart installation from the OpenShift Container Platform web console.

### Procedure

1.  In a browser, log in to your OpenShift instance.
2.  In the Developer view, navigate to the Topology view for the namespace where you deployed the Helm chart.
      The deployment appears with the label `D` on the icon. The name of the deployment is `<installation-name>-backstage`, for example `<my-self-service-automation-portal-backstage>`.

    While it is deploying, the icon is light blue. The color changes to dark blue when deployment is complete.

*Figure 1. OpenShift deployment topology view*
![Deployment on OpenShift console](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-verify-helm-install.png)
