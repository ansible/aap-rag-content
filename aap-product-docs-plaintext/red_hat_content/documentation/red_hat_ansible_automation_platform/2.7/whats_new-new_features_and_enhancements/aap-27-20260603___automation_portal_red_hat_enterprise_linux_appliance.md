# New features and enhancements
## The Configuration as Code with the ansible.platform collection

The ansible.platform collection is the unified Configuration as Code (CaC) interface for Ansible Automation Platform 2.7. It provides 22 modules and 1 lookup plugin for managing platform resources through the platform gateway API, replacing direct access to individual component APIs.

For more information, see Configure your platform with Configuration as Code in the Ansible Automation Platform documentation.

All ansible.platform modules now run as action plugins on the Ansible controller node instead of on managed nodes. This is a behavioral change that affects all playbooks using this collection.

What changed

- All ansible.platform tasks now run on the controller, not on managed nodes. Playbooks must target localhost with connection: local or connection: ansible.platform.http.
- `delegate_to` to a remote host no longer works for ansible.platform tasks.
- A new connection mode, connection: ansible.platform.http, reuses authenticated sessions across tasks in a play. Authentication happens once instead of per task, significantly reducing overhead for large CaC deployments.

New modules
The following modules are new in ansible.platform for Ansible Automation Platform 2.7:

| Module                 | Description                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| `feature_flag`         | Query and manage run-time feature flags for the platform.                                 |
| `ca_certificate`       | Manage CA certificates for mutual TLS (mTLS) authentication between services.             |
| `role_team_assignment` | Assign roles to teams for specific resources or organizations. Supports batch operations. |
| `role_definition`      | Create custom RBAC role definitions with specific permissions scoped to a content type.   |
| `ui_plugin_route`      | Configure UI plugin routes for front-end plugin integration with platform gateway.        |

New features in existing modules

- **Mutual TLS support**: The service and route modules support an `enable_mtls` parameter for mutual TLS authentication between services.
- **Route timeouts**: The service, route, and `ui_plugin_route` modules support `request_timeout_seconds` and `idle_timeout_seconds` parameters for per-route timeout configuration.
- **OIDC User Identity**: The authenticator module supports OpenID Connect User Identity configuration for platform gateway, enabling OIDC integration for user authentication and authorization.
- **Batch role assignments**: The `role_user_assignment` module supports object_ids for assigning a role to a user across multiple resources in a single task.

Ansible automation portal is now available as a pre-built RHEL 9 virtual machine appliance. The appliance packages automation portal as a QCOW2 or VMDK disk image that you deploy on your existing virtualization infrastructure.

- Key capabilities include:
* Multi-platform deployment: Deploy on RHEL with KVM, Red Hat OpenShift Virtualization, or VMware vSphere.
* Automated first-boot configuration: Provide SSH keys and AAP OAuth credentials in a cloud-init user-data file. The appliance configures itself on first boot with no manual steps.
* Atomic upgrades and rollback: Built on RHEL 9 image mode (bootc). Upgrade the appliance atomically while preserving configuration and data, and roll back to the previous version if needed.

For more information, see the Ansible automation portal documentation.

