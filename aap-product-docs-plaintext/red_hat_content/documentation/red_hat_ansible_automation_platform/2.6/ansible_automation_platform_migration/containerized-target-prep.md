# 7. Target environment
## 7.1. Container-based Ansible Automation Platform
### 7.1.1. Preparing and assessing the target environment

Transfer the migration artifact, install containerized Ansible Automation Platform, and configure the inventory file to match your source environment topology and database settings.

**Procedure**

1. Validate the file system home folder size and make sure it has enough space to transfer the artifact.

2. Transfer the artifact to the nodes where you will be working by using `scp` or any preferred file transfer method. It is recommended that you work from the platform gateway node as it has access to most systems. However, if you have access or file system space limitations due to the PostgreSQL dumps, work from the database node instead.

3. Download the latest version of containerized Ansible Automation Platform from the [Ansible Automation Platform download page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software).

4. Validate the artifact checksum.

5. Extract the artifact on the home folder for the user running the containers.

$ cd ~

$ sha256sum --check artifact.tar.sha256

$ tar xf artifact.tar

$ cd artifact

$ sha256sum --check sha256sum.txt

6. Generate an inventory file for your containerized deployment.

Configure the inventory file to match the same topology as the source environment. Configure the component database names and the `secret_key` values from the artifact’s `secrets.yml` file.

You can do this in two ways:


- Set the extra variables in the inventory file.

- Use the `secrets.yml` file as an additional variables file when running the installation program.


1. Option 1: Extra variables in the inventory file

$ egrep 'pg_database|_key' inventory
controller_pg_database=<redacted>
controller_secret_key=<redacted>
gateway_pg_database=<redacted>
gateway_secret_key=<redacted>
hub_pg_database=<redacted>
hub_secret_key=<redacted>
__hub_database_fields=<redacted>


Note
The `__hub_database_fields` value comes from the `hub_db_fields_encryption_key` value in your secret.

2. Option 2: Additional variables file

$ ansible-playbook -i inventory ansible.containerized_installer.install -e @~/artifact/secrets.yml -e "__hub_database_fields='{{ hub_db_fields_encryption_key }}'"

7. Install and configure the containerized target environment.

8. Verify PostgreSQL database version is on version 15.

9. Create a backup of the initial containerized environment.

$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.backup

10. Verify the fresh installation functions correctly.

**Additional resources**

- [Backing up containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/maintaining-containerized-aap#backing-up-containerized-ansible-automation-platform)

