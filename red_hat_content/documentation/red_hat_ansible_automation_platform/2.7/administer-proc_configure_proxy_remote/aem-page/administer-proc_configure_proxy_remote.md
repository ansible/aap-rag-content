+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_configure_proxy_remote"
title = "Configure proxy settings - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-manage_your_organization_s_automation_content/", "Manage your organization's automation content"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-proc_configure_proxy_remote/aem-page/administer-proc_configure_proxy_remote.html"
last_crumb = "Configure proxy settings"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure proxy settings"
oversized = "false"
page_slug = "administer-proc_configure_proxy_remote"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-proc_configure_proxy_remote"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-proc_configure_proxy_remote/toc/toc.json"
type = "aem-page"
+++

# Configure proxy settings

If your private automation hub is behind a network proxy, you can configure proxy settings on the remote to sync content located outside of your local network.

## Before you begin

- You have valid **Modify Ansible repo content** permissions.
- You have a proxy URL and credentials from your local network administrator.

## Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Remotes.
3.  In either the **rh-certified** or **Community** remote, click the More Actions icon **⋮** and select **Edit remote**.
4.  Expand the **Show advanced options** drop-down menu.
5.  Enter your proxy URL, proxy username, and proxy password in the appropriate fields.
6.  Click Save remote.
