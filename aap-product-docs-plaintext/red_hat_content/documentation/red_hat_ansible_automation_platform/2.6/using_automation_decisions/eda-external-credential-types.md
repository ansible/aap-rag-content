# 3. Credential types
## 3.1. External secret management credential types




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


The process for using these credentials in a rulebook activation is consistent with how they are used in automation controller. For more information, see [Secret management system](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-secret-management) .

**Additional references**

-  [Configuring automation execution](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/index)


