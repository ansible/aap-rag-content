# 7. Target environment
## 7.1. Container-based Ansible Automation Platform
### 7.1.1. Preparing and assessing the target environment




Transfer the migration artifact, install containerized Ansible Automation Platform, and configure the inventory file to match your source environment topology and database settings.

**Procedure**

1. Validate the file system home folder size and make sure it has enough space to transfer the artifact.
1. Transfer the artifact to the nodes where you will be working by using `    scp` or any preferred file transfer method. It is recommended that you work from the platform gateway node as it has access to most systems. However, if you have access or file system space limitations due to the PostgreSQL dumps, work from the database node instead.
1. Download the latest version of containerized Ansible Automation Platform from the [Ansible Automation Platform download page](https://access.redhat.com/downloads/content/480/ver=2.5/rhel---9/2.5/x86_64/product-software) .
1. Validate the artifact checksum.
1. Extract the artifact on the home folder for the user running the containers.


```
$ cd ~
```


```
$ sha256sum-check artifact.tar.sha256
```


```
$ tar xf artifact.tar
```


```
$ cd artifact
```


```
$ sha256sum-check sha256sum.txt
```


1. Generate an inventory file for your containerized deployment.

Configure the inventory file to match the same topology as the source environment. Configure the component database names and the `    secret_key` values from the artifact’s `    secrets.yml` file.

You can do this in two ways:


- Set the extra variables in the inventory file.
- Use the `        secrets.yml` file as an additional variables file when running the installation program.


1. Option 1: Extra variables in the inventory file


```
$ egrep 'pg_database|_key' inventory            controller_pg_database=&lt;redacted&gt;            controller_secret_key=&lt;redacted&gt;            gateway_pg_database=&lt;redacted&gt;            gateway_secret_key=&lt;redacted&gt;            hub_pg_database=&lt;redacted&gt;            hub_secret_key=&lt;redacted&gt;            __hub_database_fields=&lt;redacted&gt;
```

Note
The `            __hub_database_fields` value comes from the `            hub_db_fields_encryption_key` value in your secret.




1. Option 2: Additional variables file


```
$ ansible-playbook -i inventory ansible.containerized_installer.install -e @~/artifact/secrets.yml -e "__hub_database_fields='{{ hub_db_fields_encryption_key }}'"
```




1. Install and configure the containerized target environment.
1. Verify PostgreSQL database version is on version 15.
1. Create a backup of the initial containerized environment.


```
$ ansible-playbook -i &lt;path_to_inventory&gt; ansible.containerized_installer.backup
```


1. Verify the fresh installation functions correctly.


**Additional resources**

-  [Backing up containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/maintaining-containerized-aap#backing-up-containerized-ansible-automation-platform)


