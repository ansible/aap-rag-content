+++
title = "Audit email address modifications - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-audit_email_address_modifications"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-audit_email_address_modifications/aem-page/secure-audit_email_address_modifications.html"
last_crumb = "Audit email address modifications"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Audit email address modifications"
oversized = "false"
page_slug = "secure-audit_email_address_modifications"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-audit_email_address_modifications"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-audit_email_address_modifications/toc/toc.json"
type = "aem-page"
+++

# Audit email address modifications

Use the detect_changed_emails management command to identify users whose email addresses have been modified. The command analyzes audit data from the activity stream and compares it against current user records.

## About this task

The command does not attribute changes to specific causes. It provides data for you to investigate changes that might require further action.

## Procedure

1.  Run the following command to list email changes recorded in the activity stream:
  

```
$ aap-gateway-manage detect_changed_emails
```

2.  Optional: To run a full security audit that includes authenticator linkage checks, duplicate email detection, and high-risk scoring, add the `--audit` flag:
  

```
$ aap-gateway-manage detect_changed_emails --audit
```

3.  Review the output and investigate any accounts where the email address does not match the expected owner based on your organization's directory, the account has elevated RBAC permissions, the email change occurred shortly before a new identity provider login, or the account has both local and external authenticators linked.
