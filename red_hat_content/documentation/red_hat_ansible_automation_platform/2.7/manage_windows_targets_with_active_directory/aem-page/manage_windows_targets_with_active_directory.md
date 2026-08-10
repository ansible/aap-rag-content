+++
title = "Manage Windows targets with Active Directory - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/manage_windows_targets_with_active_directory"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/manage_windows_targets_with_active_directory/aem-page/manage_windows_targets_with_active_directory.html"
last_crumb = "Manage Windows targets with Active Directory"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Manage Windows targets with Active Directory"
oversized = "false"
page_slug = "manage_windows_targets_with_active_directory"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/manage_windows_targets_with_active_directory"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/manage_windows_targets_with_active_directory/toc/toc.json"
type = "aem-page"
+++

# Manage Windows targets with Active Directory

Manage secure Active Directory authentication and identity delegation.

**Dynamic Active Directory LDAP Inventories**

The `microsoft.ad.ldap` inventory plugin queries Active Directory domain hierarchies dynamically. This eliminates static file maintenance across vast Windows server footprints.

- **Capabilities**: Built-in support for Jinja2 group assignment templates, runtime *Local Administrator Password Solution* (LAPS) password decryption, and native *Simple and Protected GSSAPI Negotiation Mechanism* (SPNEGO) authentication compliance.

**Group managed service accounts (gMSA)**

Group Managed Service Accounts (gMSAs) provide automatic password rotation but cannot serve as the initial interactive connection identity for WinRM, PSRP, or OpenSSH endpoints. However, automation playbooks can programmatically deploy, rotate, and map gMSA targets to Windows tasks, schedules, and application pools using the `microsoft.ad.service_account` and `microsoft.ad.kds_root_key` modules.
