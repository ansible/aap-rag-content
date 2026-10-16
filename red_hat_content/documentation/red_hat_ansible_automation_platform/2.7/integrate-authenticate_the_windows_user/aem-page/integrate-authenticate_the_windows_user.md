+++
template = "docs/aem-title.html"
title = "Authenticate the Windows user - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-authenticate_the_windows_user"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-automate_microsoft_windows_with_ansible_automation_platform/", "Integrate with Microsoft Windows"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-authenticate_the_windows_user/aem-page/integrate-authenticate_the_windows_user.html"
last_crumb = "Authenticate the Windows user"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Authenticate the Windows user"
oversized = "false"
page_slug = "integrate-authenticate_the_windows_user"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-authenticate_the_windows_user"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-authenticate_the_windows_user/toc/toc.json"
type = "aem-page"
+++

# Authenticate the Windows user

You must decide whether the connecting automation user is a domain or a local user and an administrator user account or not.

There are four main questions:

1. Which user to use to connect.
2. If, or where, credential delegation is required.
3. Is using SSH acceptable given the support-related limitations?
4. When using WinRM, is a central certificate management already established and used in the organization?

**Domain or Local User**

Ensure reliable automation access by configuring appropriate local or domain users. Prevent connection failures by verifying domain user accessibility, and streamline cross-domain management by using a consistent user account.

**Administrator or Less Privileged User**

To establish initial connectivity and validate critical playbooks, configure your setup using an administrator account if permitted by your security policies. Since features like default NTLM access are strictly restricted to the true Administrator user, first verifying your automation with full privileges ensures reliable baseline functionality before you transition to a less privileged account.
