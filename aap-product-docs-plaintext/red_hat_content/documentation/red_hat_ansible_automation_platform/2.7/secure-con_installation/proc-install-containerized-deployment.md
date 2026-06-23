# Installation settings to secure your platform
## Use an external vault file with a containerized installation

For containerized installations of Ansible Automation Platform, use the provided automation execution playbook with the external vault file.

### About this task

Add the following sensitive variables to the vault file:

```
postgresql_admin_password:  <secure_password>
gateway_admin_password:  <secure_password>
gateway_pg_password:  <secure_password>
controller_admin_password:  <secure_password>
controller_pg_password:  <secure_password>
hub_admin_password:  <secure_password>c
hub_pg_password:  <secure_password>
eda_admin_password:  <secure_password>
eda_pg_password: <secure_password>

*In the case of a connected installation:

registry_password: <secure_cdn_password>
```
To use the new Ansible vault with the installation program, use the following procedure:

### Procedure

1.  Ensure your vault file, for example, `vault.yml`, contains all required sensitive variables.
2.  Run the container installer using the following command:
`ansible-playbook ansible.containerized_installer.install -e @vault.yml -ask-become-pass`.

Ensure that the vault file is located in the working directory, or provide the full path. Do not duplicate the encrypted variables in the `plaintext` inventory file.
