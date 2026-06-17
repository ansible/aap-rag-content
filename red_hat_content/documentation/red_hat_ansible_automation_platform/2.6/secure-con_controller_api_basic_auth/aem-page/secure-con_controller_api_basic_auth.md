+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_controller_api_basic_auth"
title = "Basic authentication - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_api_auth_methods/", "Authenticate through the API"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_controller_api_basic_auth/aem-page/secure-con_controller_api_basic_auth.html"
last_crumb = "Basic authentication"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Basic authentication"
oversized = "false"
page_slug = "secure-con_controller_api_basic_auth"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-con_controller_api_basic_auth"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_controller_api_basic_auth/toc/toc.json"
type = "aem-page"
+++

# Basic authentication

Basic authentication is stateless. You must send the base64-encoded username and password along with each request through the Authorization header. You can use this method for API calls from curl requests, Python scripts, or individual requests to the API.

OAuth 2 token authentication through platform gateway is the recommended method for accessing the API.

The following is an example of basic authentication with curl:

```
# the --user flag adds this Authorization header for us
curl -X GET --user 'user:password' https://<gateway server name>/api/gateway/v1/tokens/ -k -L
```

## Disable basic authentication

In Ansible Automation Platform 2.6 and earlier, you could disable basic authentication for security purposes.

Basic authentication is automatically disabled in Ansible Automation Platform 2.7 and cannot be re-enabled. All authentication must use OAuth 2 tokens created through platform gateway.

For authentication in Ansible Automation Platform 2.7, see:
