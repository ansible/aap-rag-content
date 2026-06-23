# Configuration as Code with the ansible.platform collection
## Check mode and idempotency

All resource modules in the `ansible.platform` collection support Ansible check mode (`--check`). In check mode, modules report what changes they would make without applying them. Use check mode to verify your playbooks before applying changes to a production environment.

Most modules are idempotent: running the same playbook multiple times produces the same result. The `token` module is an exception — each run creates a new token.

