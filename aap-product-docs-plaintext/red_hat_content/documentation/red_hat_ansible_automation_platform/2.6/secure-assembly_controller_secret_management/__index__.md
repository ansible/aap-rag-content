# Configure an external secret management system for automation

Configure machine and cloud credentials to allow your automation to securely access external services and machines. Encrypting and storing sensitive values like SSH keys and API tokens in the database helps ensure your authentication details remain protected.

With external credentials backed by credential plugins, you can map credential fields (such as a password or an SSH Private key) to values stored in a `secret management system` instead of providing them to automation controller directly.

Automation controller provides a secret management system that include integrations for:

- AWS Secrets Manager Lookup
- Centrify Vault Credential Provider Lookup
- *CyberArk Central Credential Provider* Lookup (CCP)
- CyberArk Conjur Secrets Manager Lookup
- HashiCorp Vault *Key-Value* Store (KV)
- HashiCorp Vault SSH Secrets Engine
- Microsoft Azure *Key Management System* (KMS)
- Thycotic DevOps Secrets Vault
- Thycotic Secret Server
- GitHub app token lookup


These external secret values are fetched before running a playbook that needs them.
