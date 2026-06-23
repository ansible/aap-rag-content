# Configuration as Code migration guide for Ansible Automation Platform 2.7
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

