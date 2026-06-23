# Modules in the ansible.platform collection
## Authentication

| Module               | Description                                                                                                                        | Supported states                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| `authenticator`      | Configure authentication providers such as LDAP, OIDC, SAML, and GitHub.                                                           | present, absent, exists, enforced |
| `authenticator_map`  | Define authentication mapping rules to map external groups to Ansible Automation Platform roles, teams, and organizations.         | present, absent, exists, enforced |
| `authenticator_user` | Associate users with authentication providers for migration between providers. This module does not support deleting associations. | present, exists                   |

