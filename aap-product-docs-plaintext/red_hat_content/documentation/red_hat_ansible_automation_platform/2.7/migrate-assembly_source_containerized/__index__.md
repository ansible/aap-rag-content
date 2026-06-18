# Prepare and export data from a container-based environment

Prepare and export data from your container-based Ansible Automation Platform deployment.

## Prepare and assess the source environment

Document your current containerized deployment configuration, topology, and components to create a comprehensive reference for migration.

### Procedure

1.  Document the full topology of your current containerized deployment:
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
5.  Identify all custom configurations and settings
6.  Document container resource allocations and volumes

## Export the source environment

Export databases, secrets, and custom configurations from your source containerized Ansible Automation Platform deployment to create the migration artifact.

### Procedure

1.  Create a complete backup of the source environment:


```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.backup
```

2.  Get the connection settings from one node in each of the component groups.   - Access the automation controller node and run:

```
$ podman exec -it automation-controller-task bash -c 'awx-manage print_settings | grep '^DATABASES'
```

- Access the automation hub node and run:

```
$ podman exec -it automation-hub-api bash -c "pulpcore-manager diffsettings | grep '^DATABASES'"
```

- Access the platform gateway node and run:

```
$ podman exec -it automation-gateway bash -c "aap-gateway-manage print_settings | grep '^DATABASES'"
```

3.  Validate the database size and make sure you have enough space on the filesystem for the `pg_dump`. You can verify the database sizes by connecting to your database server and running the following command as the `postgres` user:

```
$ podman exec -it postgresql bash -c 'psql -c "\l+"'
```
Adjust the filesystem size or mount an external filesystem as needed before performing the next step.

Note:
These commands send all target files to the `/tmp` filesystem. Adjust the commands to match your environment’s needs.

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

5.  Perform database dumps of all components on the platform gateway node within the artifact created previously. To run the `psql` and `pg_restore` commands, you must create a temporary container and run the commands inside of it. This command must be run from the database node.

```
$ podman run -it --rm --name postgresql_restore_temp --network host --volume ~/aap/tls/extracted:/etc/pki/ca-trust/extracted:z --volume ~/aap/postgresql/server.crt:/var/lib/pgsql/server.crt:ro,z --volume ~/aap/postgresql/server.key:/var/lib/pgsql/server.key:ro,z --volume /tmp/backups/artifact:/var/lib/pgsql/backups:ro,z registry.redhat.io/rhel9/postgresql-15:latest bash
```
Note:
This command assumes the image `registry.redhat.io/rhel9/postgresql-15:latest`. If you are missing the image, check the available images for the user with `podman images ls`.

The command above opens a shell inside the container named `postgresql_restore_temp` and has the artifact mounted into `/var/lib/pgsql/backups`. Also, this command is mounting the PostgreSQL certificates to ensure that you can resolve the correct certificates.

```
bash-4.4$ cd /var/lib/pgsql/backups
bash-4.4$ psql -h <pg_hostname> -U <component_pg_user> -d <database_name> -t -c 'SHOW server_version;' # ensure connectivity to db
bash-4.4$ pg_dump -h <pg_hostname> -U <component_pg_user> -d <component_pg_name> --clean --create -Fc -f <component>/<component>.pgc
bash-4.4$ ls -ld <component>/<component>.pgc
bash-4.4$ echo "<component>_pg_database: <database_name>" >> secrets.yml ## Add the DB name for the component to the secrets file
```
After collecting this data, exit from this temporary container.

6.  Export the secrets from the containerized environment from one node of each component group. For each step below, use the `root` user to run the commands.

1.  Access the automation controller node and gather the secret key and add to the `controller_secret_key` value in `secrets.yaml` file.

```
$ podman secret inspect --showsecret --format "{{.SecretData}}" controller_secret_key
```

2.  Access the automation hub node and gather the secret key and add to the `hub_secret_key` value in `secrets.yaml` file.

```
$ podman secret inspect --showsecret --format "{{.SecretData}}" hub_secret_key
```

3.  Access the automation hub node and gather the `database_fields.symmetric.key` value and add to the `hub_db_fields_encryption_key` value in `secrets.yaml` file.

```
$ podman secret inspect --showsecret --format "{{.SecretData}}" hub_database_fields
```

4.  Access the platform gateway node and gather the secret key and add to the `gateway_secret_key` value in `secrets.yaml` file.

```
$ podman secret inspect --showsecret --format "{{.SecretData}}" gateway_secret_key
```

7.  Export automation controller custom configurations. If any `extra_settings` exist in your containerized installation inventory, copy them into a new file and saving them under `/tmp/backups/artifact/controller/custom_configs`.

8.  Package the artifact.

```
# cd /tmp/backups/artifact/
# [ -f sha256sum.txt ] && rm -f sha256sum.txt; find . -type f -name "*.pgc" -exec sha256sum {} \; >> sha256sum.txt
# cat sha256sum.txt
# cd ..
# tar cf artifact.tar artifact
# sha256sum artifact.tar > artifact.tar.sha256
# sha256sum --check artifact.tar.sha256
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

9.  Download the `artifact.tar` and `artifact.tar.sha256` to your local machine or transfer to the target node with the `scp` command.
