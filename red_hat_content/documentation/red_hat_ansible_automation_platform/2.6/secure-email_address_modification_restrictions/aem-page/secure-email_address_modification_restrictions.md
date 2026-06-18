+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-email_address_modification_restrictions"
template = "docs/aem-title.html"
title = "Email address modification restrictions - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-email_address_modification_restrictions/aem-page/secure-email_address_modification_restrictions.html"
last_crumb = "Email address modification restrictions"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Email address modification restrictions"
oversized = "false"
page_slug = "secure-email_address_modification_restrictions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-email_address_modification_restrictions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-email_address_modification_restrictions/toc/toc.json"
type = "aem-page"
+++

# Email address modification restrictions

The platform restricts email address modifications because it uses email addresses as the primary criterion for linking external identities to existing accounts.

Non-admin users cannot modify their Ansible Automation Platform email address. Only administrators manage email address changes to prevent unauthorized account linking.

The following users can modify email addresses:

- Platform administrators (superusers)
- Organization administrators, on deployments where Organization admins can manage users and teams is enabled


If a user's email address requires updating, contact a platform administrator to make the change.
