# Modules in the ansible.platform collection

The `ansible.platform` collection provides modules for managing Ansible Automation Platform resources. The following tables list the available modules grouped by category.

## Identity and access management

| Module                 | Description                                                                                                        | Supported states                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| `organization`         | Create, update, or delete organizations.                                                                           | present, absent, exists, enforced |
| `user`                 | Create, update, or delete users. Configure superuser status and authenticator associations.                        | present, absent, exists, enforced |
| `team`                 | Create, update, or delete teams within an organization.                                                            | present, absent, exists, enforced |
| `role_definition`      | Create, update, or delete custom RBAC role definitions with specific permissions.                                  | present, absent, exists, enforced |
| `role_user_assignment` | Assign roles to users for specific resources or organizations.                                                     | present, absent, exists           |
| `role_team_assignment` | Assign roles to teams for specific resources or organizations. Supports batch operations with`assignment_objects`. | present, absent, exists           |

## Authentication

| Module               | Description                                                                                                                        | Supported states                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| `authenticator`      | Configure authentication providers such as LDAP, OIDC, SAML, and GitHub.                                                           | present, absent, exists, enforced |
| `authenticator_map`  | Define authentication mapping rules to map external groups to Ansible Automation Platform roles, teams, and organizations.         | present, absent, exists, enforced |
| `authenticator_user` | Associate users with authentication providers for migration between providers. This module does not support deleting associations. | present, exists                   |

## Gateway infrastructure

| Module            | Description                                                                                                  | Supported states                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| `service`         | Configure API service routes for automation controller, automation hub, and Event-Driven Ansible controller. | present, absent, exists, enforced |
| `route`           | Configure non-API gateway routes.                                                                            | present, absent, exists, enforced |
| `service_cluster` | Manage service clusters with health check and outlier detection settings.                                    | present, absent, exists, enforced |
| `service_node`    | Add or remove individual service nodes within clusters.                                                      | present, absent, exists, enforced |
| `service_type`    | Define service type definitions with login and logout paths.                                                 | present, absent, exists, enforced |
| `service_key`     | Manage service authentication keys for inter-service communication.                                          | present, absent, exists, enforced |
| `http_port`       | Configure HTTP listener ports for the Envoy proxy.                                                           | present, absent, exists, enforced |
| `ui_plugin_route` | Configure UI plugin routes for front-end plugin integration.                                                 | present, absent, exists, enforced |

## Platform configuration

| Module         | Description                                                                                                                                                                                                                                                                                       | Supported states                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| `settings`     | Modify platform-wide settings including token authentication, JWT configuration, password policies, and session settings. This module has no`state` parameter and always applies changes. To get a full list of available setting keys for your environment, query the platform gateway REST API. | N/A (always applies)              |
| `feature_flag` | Query and manage feature flags. Only run-time flags can be modified; install-time flags are read-only. This module defaults to`exists` instead of`present`, so you must explicitly set`state: present` to modify a flag.                                                                          | present, absent, exists, enforced |


The `settings` module requires a dictionary of setting keys and values, but the full list of available keys depends on your Ansible Automation Platform deployment. To discover all available setting keys and their current values, query the following REST API endpoint on your platform gateway:

`https://*aap-host*/api/gateway/v1/settings/all/`

## Application and token management

| Module           | Description                                                                                                                                      | Supported states                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| `application`    | Create, update, or delete OAuth2 applications for platform gateway. Configure grant types, client types, and redirect URIs.                      | present, absent, exists, enforced |
| `token`          | Create or delete OAuth2 tokens. Each run creates a new token; this module is not idempotent. The token value is only available at creation time. | present, absent                   |
| `ca_certificate` | Manage CA certificates for mutual TLS (mTLS) authentication.                                                                                     | present, absent, exists           |

## Lookup plugin

| Plugin        | Description                                                                                                                                                                                                                                                                                                                                                                |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gateway_api` | Query Ansible Automation Platform component API endpoints through the platform gateway. Supports pagination, filtering, and returning objects or IDs. Use for read-only lookups of users, teams, organizations, settings, and other resources. The automation controller, platform gateway, Event-Driven Ansible, and automation hub APIs can be queried with this plugin. |
