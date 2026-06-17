+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_self_service_enable_feedback"
template = "docs/aem-title.html"
title = "Enable feedback to Red Hat - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_self_service_about/", "Install Ansible automation portal (OpenShift Container Platform only)"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_self_service_enable_feedback/aem-page/install-proc_self_service_enable_feedback.html"
last_crumb = "Enable feedback to Red Hat"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Enable feedback to Red Hat"
oversized = "false"
page_slug = "install-proc_self_service_enable_feedback"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_self_service_enable_feedback"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_self_service_enable_feedback/toc/toc.json"
type = "aem-page"
+++

# Enable feedback to Red Hat

Enable the optional feedback form to allow users to submit suggestions and general feedback directly through the Ansible automation portal interface.

## Before you begin

- You have administrative access to the OpenShift Container Platform console.
- Ansible automation portal is installed in an OpenShift project.

## Procedure

1.  Log in to the OpenShift Container Platform console.
2.  In the Developer perspective, navigate to Helm.
3.  Click the More actions icon for your Ansible automation portal Helm release and select Upgrade.
4.  Select YAML view.
5.  Locate the `ansible` section and set the `feedback.enabled` value to `true`:
  

```
ansible:
  feedback:
    enabled: true
```

6.  Click Upgrade.

## What to do next

To verify, log in to Ansible automation portal and confirm that the Feedback button is visible in the bottom-left corner of the console.
