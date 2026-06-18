+++
template = "docs/aem-title.html"
title = "Basic authentication removal - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_api_basic_auth_removal_27"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_api_auth_methods/", "Authenticate through the API"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_api_basic_auth_removal_27/aem-page/secure-con_api_basic_auth_removal_27.html"
last_crumb = "Basic authentication removal"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Basic authentication removal"
oversized = "false"
page_slug = "secure-con_api_basic_auth_removal_27"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_api_basic_auth_removal_27"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_api_basic_auth_removal_27/toc/toc.json"
type = "aem-page"
+++

# Basic authentication removal

Basic authentication has been removed in Ansible Automation Platform 2.7. Direct authentication to automation controller, automation hub, and Event-Driven Ansible controller is no longer available. Use OAuth 2 token authentication through platform gateway instead.

If you have existing scripts or integrations that use basic authentication with direct component URLs, for example, `curl -u user:password https://<controller-host>/api/v2/...`, you must update them to use OAuth 2 token authentication through platform gateway. Replace basic authentication headers with a Bearer token and update the base URL to the platform gateway host. For example:

```
$ curl -H "Authorization: Bearer <oauth2-token-value>" https://<platform-host>/api/controller/v2/...
```
