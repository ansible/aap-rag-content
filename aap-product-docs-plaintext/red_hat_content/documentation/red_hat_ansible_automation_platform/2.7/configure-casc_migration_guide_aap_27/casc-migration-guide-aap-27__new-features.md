# Configuration as Code migration guide for Ansible Automation Platform 2.7
## New features in existing modules

The following features are available in existing modules:

- **Mutual TLS support**: The `service` and `route` modules support an `enable_mtls` parameter for mutual TLS authentication. When you enable mTLS, set `enable_gateway_auth` to `false`.
- **Route timeouts**: The `service`, `route`, and `ui_plugin_route` modules support `request_timeout_seconds` and `idle_timeout_seconds` parameters for per-route timeout configuration.
- **OIDC User Identity**: The `authenticator` module supports OIDC User Identity configuration for platform gateway.
- **Batch role assignments**: The `role_user_assignment` module supports `object_ids` for assigning a role to a user across multiple resources in a single task.

