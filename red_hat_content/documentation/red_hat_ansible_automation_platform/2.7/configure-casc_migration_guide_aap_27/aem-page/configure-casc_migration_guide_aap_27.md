+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-casc_migration_guide_aap_27"
title = "Configuration as Code migration guide for Ansible Automation Platform 2.7 - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-casc_migration_guide_aap_27/", "Configuration as Code migration guide for Ansible Automation Platform 2.7"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-casc_migration_guide_aap_27/aem-page/configure-casc_migration_guide_aap_27.html"
last_crumb = "Configuration as Code migration guide for Ansible Automation Platform 2.7"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configuration as Code migration guide for Ansible Automation Platform 2.7"
oversized = "false"
page_slug = "configure-casc_migration_guide_aap_27"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure-casc_migration_guide_aap_27"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-casc_migration_guide_aap_27/toc/toc.json"
type = "aem-page"
+++

# Configuration as Code migration guide for Ansible Automation Platform 2.7

If you are upgrading to Ansible Automation Platform 2.7, upgrade all component collections to their latest versions and update your playbooks to use platform gateway for authentication and API access.

## Collection version requirements

Important:

You must upgrade to the latest version of all component collections shipped for Ansible Automation Platform 2.7 before running automation against the upgraded platform. Older collection versions might construct URLs or authentication flows that target component APIs directly, resulting in HTTP 404 errors or authentication failures after direct access removal.

| Collection           | Purpose                                                                             |
| -------------------- | ----------------------------------------------------------------------------------- |
| `ansible.controller` | Automation controller API modules and resource management through platform gateway. |
| `ansible.hub`        | Automation hub and Galaxy API modules through platform gateway.                     |
| `ansible.eda`        | Event-Driven Ansible API modules through platform gateway.                          |
| `ansible.platform`   | Platform gateway authentication, tokens, and platform-wide resource management.     |


After you upgrade the collections, complete the following tasks:

- Pin or upgrade collections in `requirements.yml` and execution environments to the latest versions available for your release.
- Rebuild execution environments and refresh project and collection dependencies.
- Verify collection versions in use before running production playbooks.

## Gateway-managed connection values

All `host`, `username`, `password`, and `token` values used by existing playbooks and automation content must be created and managed in platform gateway.

Do not continue using the following patterns:

- Component-specific hostnames, such as `controller.example.com` or `hub.example.com`, as API targets in playbooks.
- Legacy Personal Access Tokens (PATs) or API tokens issued directly from automation controller, automation hub, or Event-Driven Ansible controller.
- Username and password pairs scoped only to a single component.


Instead, do the following:

- Create credentials, OAuth2 applications, and API tokens in platform gateway.
- Update existing playbooks, inventory variables, and Configuration as Code content to use the platform gateway URL for `aap_hostname` or equivalent module parameters.
- Use platform gateway-issued tokens for `aap_token` or equivalent authentication parameters.


For detailed setup instructions and before/after examples, see [Set up your automation environment for Configuration as Code](/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-set_up_automation_environment_for_casc "Configuration as Code is a way of working where you define and manage the configuration of Ansible Automation Platform using version-controlled configuration files, such as YAML, instead of clicking through the web UI.").

## Deprecated parameters

The following parameters are deprecated and scheduled for removal in a future release of Ansible Automation Platform. Update your playbooks to use the replacement parameters.

| Module                 | Deprecated parameter  | Replacement                   | Details                                                                                                                            |
| ---------------------- | --------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `user`                 | `organizations`       | `role_user_assignment` module | Use the `role_user_assignment` module to assign organization roles to users instead of the `organizations` parameter.              |
| `user`                 | `is_platform_auditor` | `role_user_assignment` module | Assign the Platform Auditor role by using the `role_user_assignment` module.                                                       |
| `user`                 | `authenticators`      | `associated_authenticators`   | The `associated_authenticators` parameter accepts a dictionary keyed by authenticator ID with values containing `uid` and `email`. |
| `user`                 | `authenticator_uid`   | `associated_authenticators`   | Use the `associated_authenticators` parameter instead.                                                                             |
| `role_user_assignment` | `object_id`           | `object_ids`                  | The `object_ids` parameter accepts a list of resource identifiers, enabling batch role assignments in a single task.               |

## Removed modules from the ansible.hub collection

Ansible Automation Platform 2.7 removes the following modules from the `ansible.hub` collection. Use the `ansible.platform` replacements instead. Other modules in the `ansible.hub` collection remain available.

| Removed module         | Replacement              | Action required                                                                                                                                                                                                                       |
| ---------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ansible.hub.ah_user`  | `ansible.platform.user`  | Update all playbooks that use `ansible.hub.ah_user` to use `ansible.platform.user`. The `ansible.platform.user` module manages users through platform gateway and supports additional parameters such as `associated_authenticators`. |
| `ansible.hub.ah_token` | `ansible.platform.token` | Update all playbooks that use `ansible.hub.ah_token` to use `ansible.platform.token`. Note that the `ansible.platform.token` module is not idempotent; each run creates a new token.                                                  |

## New modules

The following modules are new in `ansible.platform` version 2.7:

`feature_flag`
Query and manage feature flags. Use this module to enable or disable run-time feature flags for your platform.

`ca_certificate`
Manage CA certificates for mutual TLS (mTLS) authentication between services.

`role_team_assignment`
Assign roles to teams for specific resources or organizations. Supports batch operations through the `assignment_objects` parameter.

`role_definition`
Create custom RBAC role definitions with specific permissions scoped to a content type.

`ui_plugin_route`
Configure UI plugin routes for front-end plugin integration with platform gateway.

## New features in existing modules

The following features are available in existing modules:

- **Mutual TLS support**: The `service` and `route` modules support an `enable_mtls` parameter for mutual TLS authentication. When you enable mTLS, set `enable_gateway_auth` to `false`.
- **Route timeouts**: The `service`, `route`, and `ui_plugin_route` modules support `request_timeout_seconds` and `idle_timeout_seconds` parameters for per-route timeout configuration.
- **OIDC User Identity**: The `authenticator` module supports OIDC User Identity configuration for platform gateway.
- **Batch role assignments**: The `role_user_assignment` module supports `object_ids` for assigning a role to a user across multiple resources in a single task.

## Example: Update a playbook for 2.7

The following example shows how to update a playbook that uses deprecated parameters.

**Before (2.6)**

```yaml
- name: Create user with org membership
  ansible.platform.user:
    username: "demo-user"
    organizations:
      - "Demo-Organization"
    is_platform_auditor: true
```
**After (2.7)**

```yaml
- name: Create user
  ansible.platform.user:
    username: "demo-user"
    state: present

- name: Assign organization role to user
  ansible.platform.role_user_assignment:
    user: "demo-user"
    role_definition: "Organization Member"
    object_ids:
      - "Demo-Organization"
    state: present

- name: Assign Platform Auditor role to user
  ansible.platform.role_user_assignment:
    user: "demo-user"
    role_definition: "Platform Auditor"
    # object_ids is not required for platform-wide roles
    state: present
```
