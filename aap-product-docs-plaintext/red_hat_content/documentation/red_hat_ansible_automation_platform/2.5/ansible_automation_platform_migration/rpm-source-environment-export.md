# 6. Source environment
## 6.1. RPM-based Ansible Automation Platform
### 6.1.2. Exporting the source environment




From your source environment, export the data and configurations needed for migration.

**Procedure**

1. Verify the PostgreSQL database version is PostgreSQL version 15.

You can verify your current PostgreSQL version by connecting to your database server and running the following command as the `    postgres` user:


```
$ psql -c 'SELECT version();'
```

Important
PostgreSQL version 15 is a strict requirement for the migration process to succeed. If running PostgreSQL 13 or earlier, upgrade to version 15 before proceeding with the migration.

If using an Ansible Automation Platform managed database, re-run the installation program to upgrade the PostgreSQL version. If using a customer provided (external) database, contact your database administrator or service provider to confirm the version and arrange for an upgrade if required.




1. Create a complete backup of the source environment:


```
$ ./setup.sh -e 'backup_dest=/path/to/backup_dir/' -b
```


1. Get the connection settings from one node from each of the component groups.

For each command, access the host and become the `    root` user.


- Access the automation controller node and run:


```
# awx-manage print_settings | grep '^DATABASES'
```


- Access the automation hub node and run:


```
# grep '^DATABASES' /etc/pulp/settings.py
```


- Access the platform gateway node and run:


```
# aap-gateway-manage print_settings | grep '^DATABASES'
```



1. Stage the manually created artifact on the platform gateway node.


```
# mkdir -p /tmp/backups/artifact/{controller,gateway,hub}
```


```
# mkdir -p /tmp/backups/artifact/controller/custom_configs
```


```
# touch /tmp/backups/artifact/secrets.yml
```


```
# cd /tmp/backups/artifact/
```


1. Validate the database size and make sure you have enough space on the filesystem for the `    pg_dump` .

You can verify the database sizes by connecting to your database server and running the following command as the `    postgres` user:


```
$ psql -c '\l+'
```

Adjust the filesystem size or mount an external filesystem as needed before performing the next step.

Note
These commands send all target files to the `    /tmp` filesystem. Adjust the commands to match your environment’s needs.




1. Perform database dumps of all components on the platform gateway node within the artifact you created.


```
# psql -h &lt;pg_hostname&gt; -U &lt;component_pg_user&gt; -d &lt;database_name&gt; -t -c 'SHOW server_version;' # ensure connectivity to the database
```


```
# pg_dump -h &lt;pg_hostname&gt; -U &lt;component_pg_user&gt; -d &lt;component_pg_name&gt; --clean --create -Fc -f &lt;component&gt;/&lt;component&gt;.pgc
```


```
# ls -ld &lt;component&gt;/&lt;component&gt;.pgc
```


```
# echo "&lt;component&gt;_pg_database: &lt;database_name&gt;" &gt;&gt; secrets.yml ## Add the database name for the component to the secrets file
```


1. Export secrets from the RPM environment from one node of each component group.

For each of the following steps, use the `    root` user to run the commands.


- Access the automation controller node, gather the secret key, and add it to the `        controller_secret_key` value in the `        secrets.yml` file.


```
# cat /etc/tower/SECRET_KEY
```


- Access the automation hub node, gather the secret key, and add it to the `        hub_secret_key` value in the `        secrets.yml` file.


```
# grep '^SECRET_KEY' /etc/pulp/settings.py | awk -F'=' '{ print $2 }'
```


- Access the automation hub node, gather the `        database_fields.symmetric.key` value, and add it to the `        hub_db_fields_encryption_key` value in the `        secrets.yml` file.


```
# cat /etc/pulp/certs/database_fields.symmetric.key
```


- Access the platform gateway node, gather the secret key, and add it to the `        gateway_secret_key` value in the `        secrets.yml` file.


```
# cat /etc/ansible-automation-platform/gateway/SECRET_KEY
```



1. Export automation controller custom configurations.

If any custom settings exist on the `    /etc/tower/conf.d` , copy them to `    /tmp/backups/artifact/controller/custom_configs` .

Configuration files on automation controller that are managed by the installation program and not considered custom:


-  `        /etc/tower/conf.d/postgres.py`
-  `        /etc/tower/conf.d/channels.py`
-  `        /etc/tower/conf.d/caching.py`
-  `        /etc/tower/conf.d/cluster_host_id.py`

1. Package the artifact.


```
# cd /tmp/backups/artifact/
```


```
# [ -f sha256sum.txt ] &amp;&amp; rm -f sha256sum.txt; find . -type f -name "*.pgc" -exec sha256sum {} \; &gt;&gt; sha256sum.txt
```


```
# cat sha256sum.txt
```


```
# cd ..
```


```
# tar cf artifact.tar artifact
```


```
# sha256sum artifact.tar &gt; artifact.tar.sha256
```


```
# sha256sum --check artifact.tar.sha256
```


```
# tar tvf artifact.tar
```

Example output of `    tar tvf artifact.tar` :


```
drwxr-xr-x ansible/ansible     0 2025-05-08 16:48 artifact/    drwxr-xr-x ansible/ansible     0 2025-05-08 16:33 artifact/controller/    -rw-r--r-- ansible/ansible 732615 2025-05-08 16:26 artifact/controller/controller.pgc    drwxr-xr-x ansible/ansible      0 2025-05-08 16:33 artifact/controller/custom_configs/    drwxr-xr-x ansible/ansible      0 2025-05-08 16:11 artifact/gateway/    -rw-r--r-- ansible/ansible 231155 2025-05-08 16:28 artifact/gateway/gateway.pgc    drwxr-xr-x ansible/ansible      0 2025-05-08 16:26 artifact/hub/    -rw-r--r-- ansible/ansible 29252002 2025-05-08 16:26 artifact/hub/hub.pgc    -rw-r--r-- ansible/ansible      614 2025-05-08 16:24 artifact/secrets.yml    -rw-r--r-- ansible/ansible      338 2025-05-08 16:48 artifact/sha256sum.txt
```


1. Download the `    artifact.tar` and `    artifact.tar.sha256` to your local machine or transfer to the target node with the `    scp` command.


**Additional resources**

-  [Backing up your Ansible Automation Platform instance](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/assembly-platform-install-scenario#proc-backup-aap_platform-install-scenario)


