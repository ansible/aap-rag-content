# 2. Hardening Ansible Automation Platform
## 2.3. Initial configuration
### 2.3.4. External credential vault considerations




Secrets management is an essential component of maintaining a secure automation platform. We recommend the following secrets management practices:

- Ensure that there are no unauthorized users with access to the system, and ensure that only users who require access are granted it. Automation controller encrypts sensitive information such as passwords and API tokens, but also stores the key to decryption. Authorized users potentially have access to everything.
- Use an external system to manage secrets. In cases where credentials need to be updated, an external system can retrieve updated credentials with less complexity than an internal system. External systems for managing secrets include CyberArk, HashiCorp Vault, Microsoft Azure Key Management, and others. For more information, see the [Secret management system](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-secret-management) section of Using automation execution.


