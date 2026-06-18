+++
title = "Mandatory platform gateway authentication in Ansible Automation Platform 2.7 - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-mandatory_platform_gateway_authentication_in_ansible_automation_platform_2_7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-mandatory_platform_gateway_authentication_in_ansible_automation_platform_2_7/aem-page/secure-mandatory_platform_gateway_authentication_in_ansible_automation_platform_2_7.html"
last_crumb = "Mandatory platform gateway authentication in Ansible Automation Platform 2.7"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Mandatory platform gateway authentication in Ansible Automation Platform 2.7"
oversized = "false"
page_slug = "secure-mandatory_platform_gateway_authentication_in_ansible_automation_platform_2_7"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-mandatory_platform_gateway_authentication_in_ansible_automation_platform_2_7"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-mandatory_platform_gateway_authentication_in_ansible_automation_platform_2_7/toc/toc.json"
type = "aem-page"
+++

# Mandatory platform gateway authentication in Ansible Automation Platform 2.7

In Red Hat Ansible Automation Platform 2.7, platform gateway is the only supported method for external authentication to platform components. Direct API access to automation controller, automation hub, and Event-Driven Ansible has been removed.

Platform components enforce gateway-only authentication through an immutable configuration. This enforcement activates automatically when components are deployed and cannot be bypassed or disabled.

Attempts to authenticate directly to a platform component using legacy methods result in an HTTP 401 Unauthorized error. Legacy methods include:

- Basic authentication
- Session authentication
- Component-level tokens

## Authentication changes in platform gateway

In Ansible Automation Platform 2.7, all user authentication and API access is centralized through platform gateway. Third-party provider configuration must also be performed in platform gateway.

- **Centralized flow:** All user authentication flows through platform gateway.
- **API requests:** All API requests must use platform gateway URLs and gateway-issued tokens.
- **Third-party providers:** Configuration for LDAP, SAML, and OAuth, must be performed in platform gateway.
- **Disabled methods:** Basic and session authentication are no longer available at the component level.

## Unaffected internal operations

Internal platform operations continue to function normally using internal JWT-based authentication. The following communications do not go through platform gateway.

- **Service-to-service communication:** Interactions between components, such as automation controller retrieving images from automation hub.

- **Rulebook workers:** Event-Driven Ansible worker processes communicating with automation controller through WebSockets.

- **Container registry:** The automation hub container registry supports authentication using gateway tokens by using `podman login` or `docker login`. To authenticate, use your platform gateway credentials:

```
$ podman login <platform-host> --username <gateway-username> --password
```
     For large container image uploads, you might need to adjust platform gateway route timeout settings.
