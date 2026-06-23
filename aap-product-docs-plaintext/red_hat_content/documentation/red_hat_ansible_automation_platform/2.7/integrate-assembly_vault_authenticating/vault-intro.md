# Authenticate to hashicorp.vault
## About the Vault integration

Vault lets you centrally store and manage secrets securely. The Ansible Automation Platform certified `hashicorp.vault` collection provides fully automated lifecycle and operation management for Vault. You can create, update, and delete secrets through playbooks.

- **Existing `community.hashi_vault` users:** The `hashicorp.vault` solution is intended to replace unsupported `community.hashi_vault` collection. Use the migration path to keep your existing playbooks.
- **New Vault users:** The `hashicorp.vault` collection is included in the supported execution environment from automation hub.


Note:

Although the `hashicorp.vault` and `hashi.terraform` collections work independently of each other and are designed for different tasks, you can use them together in advanced workflows.

