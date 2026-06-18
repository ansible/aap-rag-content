+++
template = "docs/aem-title.html"
title = "Prepare and export data from an RPM-based environment - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/migrate-assembly_source_rpm"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/migrate-assembly_source_environment/", "Prepare and export data from the source environment"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/migrate-assembly_source_rpm/aem-page/migrate-assembly_source_rpm.html"
last_crumb = "Prepare and export data from an RPM-based environment"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Prepare and export data from an RPM-based environment"
oversized = "false"
page_slug = "migrate-assembly_source_rpm"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/migrate-assembly_source_rpm"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/migrate-assembly_source_rpm/toc/toc.json"
type = "aem-page"
+++

# Prepare and export data from an RPM-based environment

Prepare and export data from your RPM-based Ansible Automation Platform deployment.

## Prepare and assess the source environment

Before beginning your migration, document your current RPM deployment to use as a reference throughout the migration process and when configuring your target environment.

### Procedure

1.  Document the full topology of your current RPM deployment:
  1.  Map out all servers, nodes, and their roles (for example control nodes, execution nodes, database servers).
  2.  Note the hostname, IP address, and function of each server in your deployment.
  3.  Document the network configuration between components.
2.  Ansible Automation Platform version information:
  1.  Record the exact Ansible Automation Platform version (X.Y) currently deployed.
3.  Document the specific version of each component:
  1.  Automation controller version
  2.  Automation hub version
  3.  Platform gateway version
4.  Database configuration:
  1.  Database names for each component
  2.  Database users and roles
  3.  Connection parameters and authentication methods
  4.  Any custom PostgreSQL configurations or optimizations

### Export the source environment

From your source environment, export the data and configurations needed for migration.

#### Procedure

1.  Verify the PostgreSQL database version is PostgreSQL version 15. You can verify your current PostgreSQL version by connecting to your database server and running the following command as the `postgres` user:

```
$ psql -c 'SELECT version();'
```
  Important:
      PostgreSQL version 15 is a strict requirement for the migration process to succeed. If running PostgreSQL 13 or earlier, upgrade to version 15 before proceeding with the migration.

    If using an Ansible Automation Platform managed database, re-run the installation program to upgrade the PostgreSQL version. If using a customer provided (external) database, contact your database administrator or service provider to confirm the version and arrange for an upgrade if required.

2.  Create a complete backup of the source environment:
  

```
$ ./setup.sh -e 'backup_dest=/path/to/backup_dir/' -b
```

3.  Get the connection settings from one node from each of the component groups. For each command, access the host and become the `root` user.

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

4.  Stage the manually created artifact on the platform gateway node.

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

5.  Validate the database size and make sure you have enough space on the filesystem for the `pg_dump`. You can verify the database sizes by connecting to your database server and running the following command as the `postgres` user:

```
$ psql -c '\l+'
```
    Adjust the filesystem size or mount an external filesystem as needed before performing the next step.

  Note:
      These commands send all target files to the `/tmp` filesystem. Adjust the commands to match your environment’s needs.

6.  Perform database dumps of all components on the platform gateway node within the artifact you created.

```
# psql -h <pg_hostname> -U <component_pg_user> -d <database_name> -t -c 'SHOW server_version;' # ensure connectivity to the database
```

```
# pg_dump -h <pg_hostname> -U <component_pg_user> -d <component_pg_name> --clean --create -Fc -f <component>/<component>.pgc
```

```
# ls -ld <component>/<component>.pgc
```

```
# echo "<component>_pg_database: <database_name>" >> secrets.yml ## Add the database name for the component to the secrets file
```

7.  Export secrets from the RPM environment from one node of each component group. For each of the following steps, use the `root` user to run the commands.

  - Access the automation controller node, gather the secret key, and add it to the `controller_secret_key` value in the `secrets.yml` file.

```
# cat /etc/tower/SECRET_KEY
```

  - Access the automation hub node, gather the secret key, and add it to the `hub_secret_key` value in the `secrets.yml` file.

```
# grep '^SECRET_KEY' /etc/pulp/settings.py | awk -F'=' '{ print $2 }'
```

  - Access the automation hub node, gather the `database_fields.symmetric.key` value, and add it to the `hub_db_fields_encryption_key` value in the `secrets.yml` file.

```
# cat /etc/pulp/certs/database_fields.symmetric.key
```

  - Access the platform gateway node, gather the secret key, and add it to the `gateway_secret_key` value in the `secrets.yml` file.

```
# cat /etc/ansible-automation-platform/gateway/SECRET_KEY
```

8.  Export automation controller custom configurations. If any custom settings exist on the `/etc/tower/conf.d`, copy them to `/tmp/backups/artifact/controller/custom_configs`.

    Configuration files on automation controller that are managed by the installation program and not considered custom:

  -  `/etc/tower/conf.d/postgres.py`
  -  `/etc/tower/conf.d/channels.py`
  -  `/etc/tower/conf.d/caching.py`
  -  `/etc/tower/conf.d/cluster_host_id.py`

9.  Package the artifact.

```
# cd /tmp/backups/artifact/
```

```
# [ -f sha256sum.txt ] && rm -f sha256sum.txt; find . -type f -name "*.pgc" -exec sha256sum {} \; >> sha256sum.txt
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
# sha256sum artifact.tar > artifact.tar.sha256
```

```
# sha256sum --check artifact.tar.sha256
```

```
# tar tvf artifact.tar
```
    Example output of `tar tvf artifact.tar`:

```
drwxr-xr-x ansible/ansible     0 2025-05-08 16:48 artifact/
drwxr-xr-x ansible/ansible     0 2025-05-08 16:33 artifact/controller/
-rw-r--r-- ansible/ansible 732615 2025-05-08 16:26 artifact/controller/controller.pgc
drwxr-xr-x ansible/ansible      0 2025-05-08 16:33 artifact/controller/custom_configs/
drwxr-xr-x ansible/ansible      0 2025-05-08 16:11 artifact/gateway/
-rw-r--r-- ansible/ansible 231155 2025-05-08 16:28 artifact/gateway/gateway.pgc
drwxr-xr-x ansible/ansible      0 2025-05-08 16:26 artifact/hub/
-rw-r--r-- ansible/ansible 29252002 2025-05-08 16:26 artifact/hub/hub.pgc
-rw-r--r-- ansible/ansible      614 2025-05-08 16:24 artifact/secrets.yml
-rw-r--r-- ansible/ansible      338 2025-05-08 16:48 artifact/sha256sum.txt
```

10.  Download the `artifact.tar` and `artifact.tar.sha256` to your local machine or transfer to the target node with the `scp` command.
