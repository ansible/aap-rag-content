# Installation settings to secure your platform
## Secure sensitive variables with ansible vault

By securing sensitive values in the installation inventory file with Ansible Vault, both RPM-based and containerized Ansible Automation Platform installations benefit from improved security, password hygiene, and maintainability.

### Procedure

1.  Navigate to the install directory by using the following command:
`cd /path/to/ansible-automation-platform-setup-bundle-2.5-<version>`

2.  Create a vault file by using the following command:
`ansible-vault create vault.yml`

3.  When prompted, enter a vault password This password is required to access or modify the vault and is required for day-two operations such as backups and reconfigurations. Important:
Passwords with special characters must be in double quotes.

4.  Store the vault password securely, in accordance with your organizations security policy, for example, using a password manager or vault service.
5.  Add your sensitive variables to the vault and ensure they are not also defined in the inventory file. To edit your vault file use:

`ansible-vault edit <file>`

