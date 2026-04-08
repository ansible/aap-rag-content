# 2. Hardening Ansible Automation Platform
## 2.2. Installation
### 2.2.4. Secure sensitive variables with ansible vault




By securing sensitive values in the installation inventory file with Ansible Vault, both RPM-based and containerized Ansible Automation Platform installations benefit from improved security, password hygiene, and maintainability.

**Procedure**

1. Navigate to the install directory by using the following command:

`    cd /path/to/ansible-automation-platform-setup-bundle-2.6-&lt;version&gt;`


1. Create an Ansible vault file by using the following command:

`    ansible-vault create vault.yml`


1. When prompted, enter a password. This password is required to access or modify the Ansible vault file and is required for day-two operations such as backups and reconfigurations.

Important
Passwords with special characters must be in double quotes.




1. Add your sensitive variables to the Ansible vault file and ensure they are not also defined in the installation program inventory file.
1. Store the vault password securely in accordance with your organization’s security policy, for example, using a password manager or a service like Hashicorp Vault.

To edit your vault file use:

`    ansible-vault edit vault.yml`




#### 2.2.4.1. Use an external Ansiblevault file with an RPM-based Ansible Automation Platform deployment




When installing Ansible Automation Platform using RPM packages, you can use an external Ansible vault file to securely provide sensitive variables, such as passwords, during the installation process.

For RPM-based installations, you can provide the Ansible vault at runtime when executing the setup script.

Add the following sensitive variables to the Ansible vault file:

```
admin_password: &lt;secure_password&gt;
pg_password: &lt;secure_password&gt;
automationgateway_admin_password: &lt;secure_password&gt;
automationgateway_pg_password: &lt;secure_password&gt;
automationhub_admin_password: &lt;secure_password&gt;
automationhub_pg_password: &lt;secure_password&gt;
automationedacontroller_admin_password: &lt;secure_password&gt;
automationedacontroller_pg_password: &lt;secure_password&gt;

*In the case of a connected installation:

registry_password: &lt;secure_cdn_password&gt;
```

To use the Ansible vault file during installation, use the following procedure:

**Procedure**

1. Ensure the Ansible vault file, for example, `    vault.yml` , contains all required sensitive variables.
1. Run the installation using the following command:

`    ./setup.sh -e @vault.yml -ask-vault-pass`

Using this procedure ensures that the installation program reads encrypted variables from the vault and prompts for the vault password.




#### 2.2.4.2. Use an external vault file with a containerized installation




For containerized installations of Ansible Automation Platform, use the provided automation execution playbook with the external Ansible vault file.

Add the following sensitive variables to the vault file:

```
postgresql_admin_password:  &lt;secure_password&gt;
gateway_admin_password:  &lt;secure_password&gt;
gateway_pg_password:  &lt;secure_password&gt;
controller_admin_password:  &lt;secure_password&gt;
controller_pg_password:  &lt;secure_password&gt;
hub_admin_password:  &lt;secure_password&gt;c
hub_pg_password:  &lt;secure_password&gt;
eda_admin_password:  &lt;secure_password&gt;
eda_pg_password: &lt;secure_password&gt;

*In the case of a connected installation:

registry_password: &lt;secure_cdn_password&gt;
```

To use the new Ansible vault with the installation program, use the following procedure:

**Procedure**

1. Ensure your Ansible vault file (for example, `    vault.yml` ) contains all required sensitive variables.
1. Run the container installer using the following command:

`    ansible-playbook ansible.containerized_installer.install -e @vault.yml -ask-become-pass` .

Ensure that the Ansible vault file is located in the working directory, or provide the full path. Do not duplicate the encrypted variables in the plaintext installation inventory file.




