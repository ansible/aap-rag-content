+++
title = "Enable a custom support URL - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_self_service_customize_portal_ui"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_self_service_about/", "Install Ansible automation portal (OpenShift Container Platform only)"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_self_service_customize_portal_ui/aem-page/install-proc_self_service_customize_portal_ui.html"
last_crumb = "Enable a custom support URL"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Enable a custom support URL"
oversized = "false"
page_slug = "install-proc_self_service_customize_portal_ui"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_self_service_customize_portal_ui"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_self_service_customize_portal_ui/toc/toc.json"
type = "aem-page"
+++

# Enable a custom support URL

Update the Helm configuration to redirect the default support link to your organization's specific support resources.

## Before you begin

- You have administrative access to the OpenShift Container Platform console.
- Ansible automation portal is installed in an OpenShift project.

## Procedure

1.  Log in to the OpenShift Container Platform console.
2.  In the Developer perspective, navigate to Helm.
3.  Click the More actions icon for your Ansible automation portal Helm release and select Upgrade.
4.  Select YAML view.
5.  Add the `CUSTOMER_SUPPORT_URL` environment variable to the `extraEnvVars` section:
  

```
redhat-developer-hub:
  upstream:
    backstage:
      extraEnvVars:
        - name: CUSTOMER_SUPPORT_URL
          value: https://your-support-portal.example.com
```

6.  Click Upgrade.

## What to do next

To verify the configuration, log in to Ansible automation portal. Hover over the Support link in the upper right of the UI (next to the Create icon) and verify it points to your custom URL.
