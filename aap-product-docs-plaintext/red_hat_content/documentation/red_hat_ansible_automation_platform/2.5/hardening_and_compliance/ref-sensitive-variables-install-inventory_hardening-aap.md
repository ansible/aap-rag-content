# 2. Hardening Ansible Automation Platform
## 2.2. Installation
### 2.2.4. Sensitive variables in the installation inventory




The installation inventory file contains a number of sensitive variables, mainly those used to set the initial passwords used by Ansible Automation Platform, which are normally kept in plain text in the inventory file. To prevent unauthorized viewing of these variables, you can keep these variables in an encrypted [Ansible vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html) .

To do this, go to the installer directory

`cd /path/to/ansible-automation-platform-setup-bundle-2.5-1-x86_64`

and create a vault file

`ansible-vault create vault.yml`

You are prompted for a password to the new Ansible vault. Do not lose the vault password because it is required every time you need to access the vault file, including during day-two operations and performing backup procedures. You can secure the vault password by storing it in an encrypted password manager or in accordance with your organizational policy for storing passwords securely.

Add the sensitive variables to the vault, for example:

```
admin_password/controller_admin_password: &lt;secure_controller_password&gt;
pg_password/controller_pg_password: &lt;secure_db_password&gt;
automationhub_admin_password/hub_admin_password: &lt;secure_hub_password&gt;
automationhub_pg_password/hub_pg_password: &lt;secure_hub_db_password&gt;
automationedacontroller_admin_password/eda_admin_password: &lt;secure_eda_password&gt;
automationedacontroller_pg_password/eda_pg_password: &lt;secure_eda_db_password&gt;
-/gateway_admin_password: &lt;secure_gateway_password&gt;
-/gateway_pg_password:&lt;secure_gateway_db_password&gt;
```

Make sure these variables are not also present in the installation inventory file. To use the new Ansible vault with the installation program, run it with the command `./setup.sh -e @vault.yml — --ask-vault-pass` .

