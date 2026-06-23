# Install automation dashboard to calculate savings (RHEL only)
## Install automation dashboard
### Uninstall automation dashboard

Uninstall automation dashboard and its dependencies by using a single command, ensuring a clean removal from your host.

#### Procedure

Run the following command to uninstall automation dashboard and its dependencies, including the PostgreSQL database container:

```bash
ansible-playbook -i inventory
ansible.containerized_installer.dashboard_uninstall
```


Note:

Uninstalling automation dashboard permanently deletes all collected metrics data, saved reports, and the PostgreSQL database.
