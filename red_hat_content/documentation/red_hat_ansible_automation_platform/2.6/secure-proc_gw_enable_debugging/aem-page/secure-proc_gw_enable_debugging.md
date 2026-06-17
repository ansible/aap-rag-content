+++
title = "Enable debugging for enterprise authentication - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_gw_enable_debugging"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_gw_enable_debugging/aem-page/secure-proc_gw_enable_debugging.html"
last_crumb = "Enable debugging for enterprise authentication"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Enable debugging for enterprise authentication"
oversized = "false"
page_slug = "secure-proc_gw_enable_debugging"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-proc_gw_enable_debugging"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_gw_enable_debugging/toc/toc.json"
type = "aem-page"
+++

# Enable debugging for enterprise authentication

To further diagnose authentication issues, enable debug logging in platform gateway.

## Procedure

1.  Change the logging configuration in the platform gateway’s `settings.py` file.
2.  Set the logging level for the `ansible_base` logger to `DEBUG`:
  

```
LOGGING['loggers']['ansible_base']['level'] = 'DEBUG'
```
    After this change, detailed `AuthTokenError` messages are displayed in the logs, providing specific information about the cause of the failure.
