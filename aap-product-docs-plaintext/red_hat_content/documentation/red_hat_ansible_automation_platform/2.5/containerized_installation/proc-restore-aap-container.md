# 2. Ansible Automation Platform containerized installation
## 2.11. Restoring containerized Ansible Automation Platform




Restore your container-based installation of Ansible Automation Platform from a backup.

**Prerequisites**

You have done the following:


- Logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.


**Procedure**

1. Go to the Red Hat Ansible Automation Platform installation directory on your Red Hat Enterprise Linux host.
1. Run the `    restore` playbook:


```
$ ansible-playbook -i &lt;path_to_inventory&gt; ansible.containerized_installer.restore
```




This restores the important data deployed by the containerized installer such as:

- PostgreSQL databases
- Configuration files
- Data files


By default, the backup directory is set to `./backups` . You can change this by using the `backup_dir` variable in your `inventory` file.

