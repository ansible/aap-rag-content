# Configuration as Code migration guide for Ansible Automation Platform 2.7
## Deprecated parameters

The following parameters are deprecated and scheduled for removal in a future release of Ansible Automation Platform. Update your playbooks to use the replacement parameters.

| Module                 | Deprecated parameter  | Replacement                   | Details                                                                                                                            |
| ---------------------- | --------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `user`                 | `organizations`       | `role_user_assignment` module | Use the `role_user_assignment` module to assign organization roles to users instead of the `organizations` parameter.              |
| `user`                 | `is_platform_auditor` | `role_user_assignment` module | Assign the Platform Auditor role by using the `role_user_assignment` module.                                                       |
| `user`                 | `authenticators`      | `associated_authenticators`   | The `associated_authenticators` parameter accepts a dictionary keyed by authenticator ID with values containing `uid` and `email`. |
| `user`                 | `authenticator_uid`   | `associated_authenticators`   | Use the `associated_authenticators` parameter instead.                                                                             |
| `role_user_assignment` | `object_id`           | `object_ids`                  | The `object_ids` parameter accepts a list of resource identifiers, enabling batch role assignments in a single task.               |

