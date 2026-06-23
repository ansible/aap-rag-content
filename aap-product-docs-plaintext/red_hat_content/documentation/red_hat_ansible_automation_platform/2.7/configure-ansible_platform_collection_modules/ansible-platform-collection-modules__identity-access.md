# Modules in the ansible.platform collection
## Identity and access management

| Module                 | Description                                                                                                        | Supported states                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| `organization`         | Create, update, or delete organizations.                                                                           | present, absent, exists, enforced |
| `user`                 | Create, update, or delete users. Configure superuser status and authenticator associations.                        | present, absent, exists, enforced |
| `team`                 | Create, update, or delete teams within an organization.                                                            | present, absent, exists, enforced |
| `role_definition`      | Create, update, or delete custom RBAC role definitions with specific permissions.                                  | present, absent, exists, enforced |
| `role_user_assignment` | Assign roles to users for specific resources or organizations.                                                     | present, absent, exists           |
| `role_team_assignment` | Assign roles to teams for specific resources or organizations. Supports batch operations with`assignment_objects`. | present, absent, exists           |

