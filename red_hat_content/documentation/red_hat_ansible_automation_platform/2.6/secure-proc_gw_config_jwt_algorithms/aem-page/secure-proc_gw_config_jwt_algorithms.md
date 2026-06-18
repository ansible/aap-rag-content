+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_gw_config_jwt_algorithms"
title = "Configure JWT_Algorithms manually - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_gw_config_jwt_algorithms/aem-page/secure-proc_gw_config_jwt_algorithms.html"
last_crumb = "Configure JWT_Algorithms manually"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure JWT_Algorithms manually"
oversized = "false"
page_slug = "secure-proc_gw_config_jwt_algorithms"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-proc_gw_config_jwt_algorithms"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_gw_config_jwt_algorithms/toc/toc.json"
type = "aem-page"
+++

# Configure JWT_Algorithms manually

To resolve the authentication failure, manually provide the list of supported algorithms in the platform gateway configuration.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Select your OIDC authenticator from the list.
3.  Click Edit authentication and locate the **OIDC JWT Algorithm(s)** field.
4.  Enter the list of supported algorithms as a YAML list or a JSON array. These algorithms are typically available from your IdP’s OpenID Connect (OIDC) discovery endpoint.  **Example**

```
[
    "PS384",
    "ES384",
    "RS384",
    "HS256",
    "HS512",
    "ES256",
    "RS256",
    "HS384",
    "ES512",
    "PS256",
    "PS512",
    "RS512"
]
```

5.  Save your changes. The system uses these specified algorithms for token verification, resolving any authentication failures related to their absence.
