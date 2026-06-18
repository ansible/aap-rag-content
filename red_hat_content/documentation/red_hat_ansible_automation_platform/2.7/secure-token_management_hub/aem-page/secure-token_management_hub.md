+++
title = "Configure automation hub tokens - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-token_management_hub"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-token_management_hub/", "Configure automation hub tokens"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-token_management_hub/aem-page/secure-token_management_hub.html"
last_crumb = "Configure automation hub tokens"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure automation hub tokens"
oversized = "false"
page_slug = "secure-token_management_hub"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-token_management_hub"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-token_management_hub/toc/toc.json"
type = "aem-page"
+++

# Configure automation hub tokens

You must authenticate your hub instance before you can upload or download collections.

As of Ansible Automation Platform's 2.7 release, you can no longer access the API through automation hub. To authenticate automation hub, follow the platform gateway authentication process.

Note:

Automation hub does not support basic authentication or authenticating through service accounts.

To sync collections from console.redhat.com to your automation hub instance, or if you are using Keycloak to authenticate your private automation hub, follow the procedure to create the offline token in automation hub.

## Create the offline token in automation hub

In automation hub, you can create an offline token using **Token management**. The offline token is a secret token used to protect your content, so be sure to store it in a secure location.

### About this task

Note:

Your offline token expires after 30 days of inactivity.

### Procedure

1.  Navigate to [Ansible Automation Platform on the Red Hat Hybrid Cloud Console](https://console.redhat.com/ansible/automation-hub/token/).
2.  From the navigation panel, select Automation Hub> (and then)Connect to Hub.
3.  Under **Offline token**, click Load Token.
4.  Click the Copy to clipboard icon to copy the offline token.
5.  Paste the token into a file and store in a secure location.

### What to do next

The offline token is now available for configuring automation hub as your default collections server or for uploading collections by using the `ansible-galaxy` command line tool.
