+++
title = "Troubleshoot Generic OIDC scope mismatches - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_gw_troubleshoot_oidc_scope_mismatch"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_gw_troubleshoot_oidc_scope_mismatch/aem-page/secure-proc_gw_troubleshoot_oidc_scope_mismatch.html"
last_crumb = "Troubleshoot Generic OIDC scope mismatches"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Troubleshoot Generic OIDC scope mismatches"
oversized = "false"
page_slug = "secure-proc_gw_troubleshoot_oidc_scope_mismatch"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-proc_gw_troubleshoot_oidc_scope_mismatch"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_gw_troubleshoot_oidc_scope_mismatch/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot Generic OIDC scope mismatches

Authentication fails when the Identity Provider (IdP) does not support the default scopes automatically appended by the system.

## About this task

To prevent the system from appending this default scope, you must add a setting to your authenticator configuration.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Select your OIDC authenticator from the list.
3.  Click Edit authentication.
4.  In the **Additional Authenticator Fields** section, add the following attribute and value. This input box supports either YAML or JSON. Ensure you add this key-value pair on a new line if there are other fields present:
  

```yaml
IGNORE_DEFAULT_SCOPE: True
```

5.  Save your changes. The authenticator now only uses the scopes you explicitly defined, resolving any authentication failures related to unsupported scopes.
