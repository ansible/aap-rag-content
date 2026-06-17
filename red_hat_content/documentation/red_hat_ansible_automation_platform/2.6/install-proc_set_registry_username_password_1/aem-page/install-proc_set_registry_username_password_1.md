+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_set_registry_username_password_1"
title = "Create a registry service account - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_set_registry_username_password_1/aem-page/install-proc_set_registry_username_password_1.html"
last_crumb = "Create a registry service account"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Create a registry service account"
oversized = "false"
page_slug = "install-proc_set_registry_username_password_1"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_set_registry_username_password_1"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_set_registry_username_password_1/toc/toc.json"
type = "aem-page"
+++

# Create a registry service account

Create a registry service account on the Red Hat Customer Portal to generate a token and username. Use these to set the `registry_username` and `registry_password` variables required for online non-bundled installations.

## Procedure

1.  Go to <https://access.redhat.com/terms-based-registry/accounts>.
2.  On the **Registry Service Accounts** page click New Service Account.
3.  Enter a name for the account using only the allowed characters.
4.  Optionally enter a description for the account.
5.  Click Create.
6.  Find the created account in the list by searching for your name in the search field.
7.  Click the name of the account that you created.
8.  Alternatively, if you know the name of your token, you can go directly to the page by entering the URL:
  

```
https://access.redhat.com/terms-based-registry/token/<name-of-your-token>
```

9.  A **token** page opens, displaying a generated username (different from the account name) and a token.   1.  If no token is displayed, click Regenerate Token. You can also click this to generate a new username and token.
10.  Copy the username (for example "1234567|testuser") and use it to set the variable `registry_username`.
11.  Copy the token and use it to set the variable `registry_password`.
