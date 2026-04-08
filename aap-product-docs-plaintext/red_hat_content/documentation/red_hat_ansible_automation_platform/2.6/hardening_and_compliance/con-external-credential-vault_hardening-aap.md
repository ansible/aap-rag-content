# 2. Hardening Ansible Automation Platform
## 2.3. Initial configuration
### 2.3.4. External credential management considerations




Secrets management is an essential component of maintaining a secure automation platform.

Use an external system to manage secrets. In cases where credentials need to be updated, an external system can retrieve updated credentials with less complexity than an internal system. External systems for managing secrets include CyberArk, HashiCorp Vault, Microsoft Azure Key Management, and others. For more information, see [Secret management system](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-secret-management) .

