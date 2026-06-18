+++
title = "Access troubleshooting information in the UI - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/troubleshoot-proc_settings_troubleshooting"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/troubleshoot-proc_settings_troubleshooting/", "Access troubleshooting information in the UI"]]
category = "Troubleshoot"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/troubleshoot-proc_settings_troubleshooting/aem-page/troubleshoot-proc_settings_troubleshooting.html"
last_crumb = "Access troubleshooting information in the UI"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Access troubleshooting information in the UI"
oversized = "false"
page_slug = "troubleshoot-proc_settings_troubleshooting"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/troubleshoot-proc_settings_troubleshooting"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/troubleshoot-proc_settings_troubleshooting/toc/toc.json"
type = "aem-page"
+++

# Access troubleshooting information in the UI

You can use the **Troubleshooting** page to enable or disable certain flags that aid in debugging issues within Ansible Automation Platform.

## Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)Troubleshooting.
2.  The **Troubleshooting** page is displayed.
3.  Click Edit.
4.  You can select the following options:

  - **Enable or Disable tmp dir cleanup**: Select this to enable or disable the cleanup of tmp directories generated during execution of a job after job execution completes.
  - **Debug Web Requests**: Select this to enable or disable web request profiling for debugging slow web requests.
  - **Release Receptor Work**: Select this to turn on or off the deletion of job pods after they complete or fail. This can be helpful in debugging why a job failed.
  - **Keep receptor work on error**: Select this to prevent receptor work from being released when an error is detected.

5.  Click Save to save your changes.
