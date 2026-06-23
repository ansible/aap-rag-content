# Configuration as Code migration guide for Ansible Automation Platform 2.7
## Removed modules from the ansible.hub collection

Ansible Automation Platform 2.7 removes the following modules from the `ansible.hub` collection. Use the `ansible.platform` replacements instead. Other modules in the `ansible.hub` collection remain available.

| Removed module         | Replacement              | Action required                                                                                                                                                                                                                       |
| ---------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ansible.hub.ah_user`  | `ansible.platform.user`  | Update all playbooks that use `ansible.hub.ah_user` to use `ansible.platform.user`. The `ansible.platform.user` module manages users through platform gateway and supports additional parameters such as `associated_authenticators`. |
| `ansible.hub.ah_token` | `ansible.platform.token` | Update all playbooks that use `ansible.hub.ah_token` to use `ansible.platform.token`. Note that the `ansible.platform.token` module is not idempotent; each run creates a new token.                                                  |

