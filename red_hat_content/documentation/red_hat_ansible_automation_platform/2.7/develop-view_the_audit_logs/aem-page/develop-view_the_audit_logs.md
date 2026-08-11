+++
template = "docs/aem-title.html"
title = "View the audit logs - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-view_the_audit_logs"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-view_the_audit_logs/aem-page/develop-view_the_audit_logs.html"
last_crumb = "View the audit logs"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "View the audit logs"
oversized = "false"
page_slug = "develop-view_the_audit_logs"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-view_the_audit_logs"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-view_the_audit_logs/toc/toc.json"
type = "aem-page"
+++

# View the audit logs

The Ansible Visual Studio (VS Code) extension now records all Red Hat Ansible Lightspeed operations in an audit log for future use. Each interaction is recorded with a timestamp, the type of action performed, details of the requested task, and other relevant information.

## About this task

The logs are displayed in the Ansible Lightspeed Output Channel of the VS Code editor and are available until you close VS Code.

## Procedure

1.  Open VS Code.
2.  Open the Command Palette of the VS Code editor.
3.  Click Output> (and then)Show Output Channels, and then select **Ansible Lightspeed**.
  An **Output** panel displays at the bottom of the VS Code editor with a log of all user actions.
