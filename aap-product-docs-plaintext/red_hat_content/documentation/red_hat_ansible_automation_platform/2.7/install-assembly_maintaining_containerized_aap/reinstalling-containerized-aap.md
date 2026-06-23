# Maintain containerized Ansible Automation Platform
## Reinstall containerized Ansible Automation Platform

Reinstall a containerized deployment after uninstalling and preserving the database.

### Procedure

Follow the steps in [Install containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_installing_containerized_aap "Run the install playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.") and include the existing secret key value in the playbook command:

```
$ ansible-playbook -i inventory ansible.containerized_installer.install -e controller_secret_key=<secret_key_value>
```
