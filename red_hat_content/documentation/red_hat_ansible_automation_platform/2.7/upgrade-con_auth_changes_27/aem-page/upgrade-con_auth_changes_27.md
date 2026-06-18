+++
template = "docs/aem-title.html"
title = "Authentication changes in Ansible Automation Platform 2.7 - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_auth_changes_27"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_auth_changes_27/", "Authentication changes in Ansible Automation Platform 2.7"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_auth_changes_27/aem-page/upgrade-con_auth_changes_27.html"
last_crumb = "Authentication changes in Ansible Automation Platform 2.7"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Authentication changes in Ansible Automation Platform 2.7"
oversized = "false"
page_slug = "upgrade-con_auth_changes_27"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-con_auth_changes_27"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_auth_changes_27/toc/toc.json"
type = "aem-page"
+++

# Authentication changes in Ansible Automation Platform 2.7

In Ansible Automation Platform 2.7, all authentication has been consolidated through platform gateway. Direct API access to individual platform components has been removed.

Important:

Only upgrades from Ansible Automation Platform 2.6 to 2.7 are supported. If you are running version 2.4 or 2.5, you must first upgrade to version 2.6 before upgrading to 2.7.

## Architectural changes in Ansible Automation Platform 2.7

Ansible Automation Platform 2.7 removes direct API access and component-level authentication. All external access to platform components must go through platform gateway.

The following features and access methods are removed in this release:

- Direct API access to automation controller, automation hub, and Event-Driven Ansible controller.
- Basic authentication at the component level.
- Component-level Personal Access Tokens (PATs) and legacy OAuth applications.
- Third-party authentication provider configuration (LDAP, SAML, RADIUS, TACACS+) within automation controller.
- Direct external routes or ingress to automation controller and automation hub.


Important:

If you use Red Hat Ansible Lightspeed and have automation or scripts that change the `max_stream_duration` or `stream_idle_timeout` global proxy settings, you must update your scripts. These global settings have been removed, and you should now use the per-route service timeouts that are configurable on any route.

## How direct access is prevented in Ansible Automation Platform 2.7

In Ansible Automation Platform 2.7, platform components are configured to accept only platform gateway JWT authentication, ensuring that all external access goes through platform gateway.

When deployed as part of Ansible Automation Platform, this enforcement is immutable and cannot be changed through configuration files or environment variables, ensuring no bypass is possible.
