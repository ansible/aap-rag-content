+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_pat_removal_27"
title = "Personal Access Token removal in Ansible Automation Platform 2.7 - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_pat_removal_27/aem-page/secure-con_pat_removal_27.html"
last_crumb = "Personal Access Token removal in Ansible Automation Platform 2.7"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Personal Access Token removal in Ansible Automation Platform 2.7"
oversized = "false"
page_slug = "secure-con_pat_removal_27"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_pat_removal_27"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_pat_removal_27/toc/toc.json"
type = "aem-page"
+++

# Personal Access Token removal in Ansible Automation Platform 2.7

In Ansible Automation Platform 2.7, component-level Personal Access Tokens (PATs) have been removed. Tokens created directly in automation controller, automation hub, or Event-Driven Ansible controller in Ansible Automation Platform 2.6 or earlier no longer work in Ansible Automation Platform 2.7.

All tokens must now be created and managed through platform gateway.

## Token migration timeline

- **Ansible Automation Platform 2.5:** Platform gateway introduced; component-level PATs deprecated.
- **Ansible Automation Platform 2.6:** PAT migration from components to platform gateway supported; component-level PATs still functional.
- **Ansible Automation Platform 2.7:** Component-level PATs removed; only platform gateway tokens supported.

## Create new tokens after upgrade

Component-level tokens from automation controller, automation hub, or Event-Driven Ansible are not migrated to platform gateway during upgrade. After upgrading to Ansible Automation Platform 2.7, you must create new tokens through platform gateway.

### Procedure

1.  Log in to the platform gateway UI.
2.  Navigate to Access Management> (and then)Users> (and then)[your user]> (and then)Tokens.
3.  Create new tokens as needed.
4.  Update any scripts or integrations to use the new platform gateway tokens.
