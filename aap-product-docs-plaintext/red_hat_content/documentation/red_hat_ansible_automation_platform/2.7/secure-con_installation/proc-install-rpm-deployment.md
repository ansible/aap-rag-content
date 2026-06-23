# Installation settings to secure your platform
## Use an external vault file with an RPM-based Ansible Automation Platform deployment

When installing Ansible Automation Platform using RPM packages, you can use an external Ansible vault file to securely provide sensitive variables, such as passwords, during the installation process.

### About this task

For RPM-based installations, you can provide the Ansible vault at runtime when executing the setup script.

Add the following sensitive variables to the vault file:

```
admin_password: <secure_password>
pg_password: <secure_password>
automationgateway_admin_password: <secure_password>
automationgateway_pg_password: <secure_password>
automationhub_admin_password: <secure_password>
automationhub_pg_password: <secure_password>
automationedacontroller_admin_password: <secure_password>
automationedacontroller_pg_password: <secure_password>

*In the case of a connected installation:

registry_password: <secure_cdn_password>
```
To use the vault during installation, use the following procedure:

### Procedure

1.  Ensure the vault file, for example, `vault.yml`, contains all required sensitive variables.
2.  Run the installation using the following command:
`./setup.sh -e @vault.yml -ask-vault-pass`

Using this procedure ensures that the installation program reads encrypted variables from the vault and prompts for the vault password.

