+++
title = "Configure automation hub tokens - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-token_management_hub"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-token_management_hub/", "Configure automation hub tokens"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-token_management_hub/aem-page/secure-token_management_hub.html"
last_crumb = "Configure automation hub tokens"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure automation hub tokens"
oversized = "false"
page_slug = "secure-token_management_hub"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-token_management_hub"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-token_management_hub/toc/toc.json"
type = "aem-page"
+++

# Configure automation hub tokens

You must authenticate your hub instance before you can upload or download collections.

Note:

Automation hub does not support basic authentication or authenticating through service accounts.

Your method for creating the API token differs according to the type of automation hub that you are using:

- Automation hub uses offline token management. See Creating the offline token in automation hub.
- Private automation hub uses API token management. See Creating the API token in private automation hub.
- If you are using Keycloak to authenticate your private automation hub, follow the procedure for Creating the offline token in automation hub.

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

## Create the API token in private automation hub

In private automation hub, you can create an API token using API token management. The API token is a secret token used to protect your content, so be sure to store it in a secure location.

### Before you begin

- Valid subscription credentials for Red Hat Ansible Automation Platform.

### About this task

Note:

The API token does not expire.

### Procedure

1.  Log in to your private automation hub.
2.  From the navigation panel, select Automation Content> (and then)API token.
3.  Click Load Token.
4.  To copy the API token, click the Copy to clipboard icon.
5.  Paste the API token into a file and store in a secure location.

### What to do next

The API token is now available for configuring automation hub as your default collections server or uploading collections using the `ansible-galaxy` command line tool.
