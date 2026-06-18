# Connect to external secret management systems with built-in credentials

Event-Driven Ansible controller includes built-in credentials to sync projects, run rulebooks, execute job templates, fetch container images, and process data through event streams.

These built-in credential types are not editable. So if you want credential types that support authentication with other systems, you can create your own credential types that can be used in your source plugins. Each credential type contains an input configuration and an injector configuration that can be passed to an Ansible rulebook to configure your sources. For more information, see Create custom credentials for Event-Driven Ansible.

If you will be executing job templates through automation controller, you can retrieve credential values from external secret management systems listed in External secret management credential types.

## External secret management credential types

In addition to the built-in credential types, Event-Driven Ansible supports a variety of external secret management credential types. These credential types allow rulebooks to securely retrieve sensitive information (API keys, and similar) directly from your organization’s centralized secret vault.

The following external credential types are available for use in Event-Driven Ansible controller:

- AWS Secrets Manager
- Azure Key Vault
- Centrify Vault Credential Provider
- CyberArk Central Credential Provider
- CyberArk Conjur Secrets Manager
- HashiCorp Vault Secret
- HashiCorp Vault Signed SSH
- Thycotic DevOps Secrets Vault
- Thycotic Secret Server
- GitHub App Installation Access Token


The process for using these credentials in a rulebook activation is consistent with how they are used in automation controller.
