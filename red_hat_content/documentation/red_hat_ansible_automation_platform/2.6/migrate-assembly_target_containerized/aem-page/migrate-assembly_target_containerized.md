+++
title = "Prepare the container-based target environment and import migration content - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/migrate-assembly_target_containerized"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/migrate-assembly_target_environment/", "Prepare, configure, and validate the target environment"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/migrate-assembly_target_containerized/aem-page/migrate-assembly_target_containerized.html"
last_crumb = "Prepare the container-based target environment and import migration content"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Prepare the container-based target environment and import migration content"
oversized = "false"
page_slug = "migrate-assembly_target_containerized"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/migrate-assembly_target_containerized"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/migrate-assembly_target_containerized/toc/toc.json"
type = "aem-page"
+++

# Prepare the container-based target environment and import migration content

Prepare and assess your target container-based Ansible Automation Platform environment, and import and reconcile your migrated content.

## Prepare and assess the target environment

Transfer the migration artifact, install containerized Ansible Automation Platform, and configure the inventory file to match your source environment topology and database settings.

### Procedure

1.  Validate the file system home folder size and make sure it has enough space to transfer the artifact.
2.  Transfer the artifact to the nodes where you will be working by using `scp` or any preferred file transfer method. It is recommended that you work from the platform gateway node as it has access to most systems. However, if you have access or file system space limitations due to the PostgreSQL dumps, work from the database node instead.
3.  Download the latest version of containerized Ansible Automation Platform from the [Ansible Automation Platform download page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software).
4.  Validate the artifact checksum.
5.  Extract the artifact on the home folder for the user running the containers.

```
$ cd ~
```

```
$ sha256sum --check artifact.tar.sha256
```

```
$ tar xf artifact.tar
```

```
$ cd artifact
```

```
$ sha256sum --check sha256sum.txt
```

6.  Generate an inventory file for your containerized deployment. Configure the inventory file to match the same topology as the source environment. Configure the component database names and the `secret_key` values from the artifact’s `secrets.yml` file.

    You can do this in two ways:

  - Set the extra variables in the inventory file.
  - Use the `secrets.yml` file as an additional variables file when running the installation program.     1. Option 1: Extra variables in the inventory file

```
$ egrep 'pg_database|_key' inventory
controller_pg_database=<redacted>
controller_secret_key=<redacted>
gateway_pg_database=<redacted>
gateway_secret_key=<redacted>
hub_pg_database=<redacted>
hub_secret_key=<redacted>
__hub_database_fields=<redacted>
```
      Note:
                  The `__hub_database_fields` value comes from the `hub_db_fields_encryption_key` value in your secret.

    2. Option 2: Additional variables file

```
$ ansible-playbook -i inventory ansible.containerized_installer.install -e @~/artifact/secrets.yml -e "__hub_database_fields='{{ hub_db_fields_encryption_key }}'"
```

7.  Install and configure the containerized target environment.
8.  Verify PostgreSQL database version is on version 15.
9.  Create a backup of the initial containerized environment.

```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.backup
```

10.  Verify the fresh installation functions correctly.

## Import the migration content to the target environment

To import your migration content into the target environment, stop the containerized services, import the database dumps, and then restart the services.

### Procedure

1.  Stop the containerized services, except the database.   1.  In all nodes, if Performance Co-Pilot is configured, run the following command:
  

```
$ systemctl --user stop pcp
```

  2.  Access the automation controller node and run:
  

```
$ systemctl --user stop automation-controller-task automation-controller-web automation-controller-rsyslog
$ systemctl --user stop receptor
```

  3.  Access the automation hub node and run:
  

```
$ systemctl --user stop automation-hub-api automation-hub-content automation-hub-web automation-hub-worker-1 automation-hub-worker-2
```

  4.  Access the Event-Driven Ansible node and run:
  

```
$ systemctl --user stop automation-eda-scheduler automation-eda-daphne automation-eda-web automation-eda-api automation-eda-worker-1 automation-eda-worker-2 automation-eda-activation-worker-1 automation-eda-activation-worker-2
```

  5.  Access the platform gateway node and run:
  

```
$ systemctl --user stop automation-gateway automation-gateway-proxy
```

  6.  Access the platform gateway node when using standalone Redis, or all nodes from the Redis group in your inventory file when using clustered Redis, and run:
  

```
$ systemctl --user stop redis-unix redis-tcp
```
    Note:
            In an enterprise deployment, the components run on different nodes. Run the commands on each component node.

2.  Import database dumps to the containerized environment.   1.  If you are using an Ansible Automation Platform managed database, you must create a temporary container to run the `psql` and `pg_restore` commands. Run this command from the database node:
  

```
$ podman run -it --rm --name postgresql_restore_temp --network host --volume ~/aap/tls/extracted:/etc/pki/ca-trust/extracted:z --volume ~/aap/postgresql/server.crt:/var/lib/pgsql/server.crt:ro,z --volume ~/aap/postgresql/server.key:/var/lib/pgsql/server.key:ro,z --volume ~/artifact:/var/lib/pgsql/backups:ro,z registry.redhat.io/rhel8/postgresql-15:latest bash
```
    Note:
            The command above opens a shell inside the container named `postgresql_restore_temp` with the artifact mounted at `/var/lib/pgsql/backups`. Additionally, it mounts the PostgreSQL certificates to ensure that you can resolve the correct certificates.

        The command assumes the image `registry.redhat.io/rhel8/postgresql-15:latest` is available. If you are missing the image, check the available images for the user with `podman images ls`.

        It also assumes that the artifact is located in the current user’s home folder. If the artifact is located elsewhere, change the `~/artifact` with the required path.

  2.  If you are using a customer-provided (external) database, you can run the `psql` and `pg_restore` commands from any node that has these commands installed and that has access to the database. Reach out to your database administrator if you are unsure.
  3.  From inside the container, access the database and ensure the users have the `CREATEDB` role.

```
bash-4.4$ psql -h <pg_hostname> -U postgres
postgres=# \l
          Name           |     Owner     | Encoding |   Collate   |    Ctype    | ICU Locale | Locale Provider |   Access privileg
es
-------------------------+---------------+----------+-------------+-------------+------------+-----------------+------------------
-----
 automationedacontroller | eda           | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            |
 automationhub           | automationhub | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            |
 awx                     | awx           | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            |
 gateway                 | gateway       | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            |
...
```

  4.  For each component name, add the `CREATEDB` role to the `Owner`. For example:
  

```
postgres=# ALTER ROLE awx WITH CREATEDB;
postgres=# \q
```
        Replace `awx` with the database owner.

  5.  With the `CREATEDB` in place, access the path where the artifact is mounted, and run the `pg_restore` commands.

```
bash$ cd /var/lib/pgsql/backups
bash$ pg_restore --clean --create --no-owner -h <pg_hostname> -U <component_pg_user> -d template1 <component>/<component>.pgc
```

  6.  After the restore, remove the permissions from the user. For example:
  

```
postgres=# ALTER ROLE awx WITH NOCREATEDB;
postgres=# \q
```
        Replace `awx` with each user containing the role.

3.  Start the containerized services, except the database. Note:
      In an enterprise deployment, the components run on different nodes. Run the commands on each component node.

  1.  In all nodes, if Performance Co-Pilot is configured, run the following command:
  

```
$ systemctl --user start pcp
```

  2.  Access the automation controller node and run:
  

```
$ systemctl --user start automation-controller-task automation-controller-web automation-controller-rsyslog
$ systemctl --user start receptor
```

  3.  Access the automation hub node and run:
  

```
$ systemctl --user start automation-hub-api automation-hub-content automation-hub-web automation-hub-worker-1 automation-hub-worker-2
```

  4.  Access the Event-Driven Ansible node and run:
  

```
$ systemctl --user start automation-eda-scheduler automation-eda-daphne automation-eda-web automation-eda-api automation-eda-worker-1 automation-eda-worker-2  automation-eda-activation-worker-1 automation-eda-activation-worker-2
```

  5.  Access the platform gateway node and run:
  

```
$ systemctl --user start automation-gateway automation-gateway-proxy
```

  6.  Access the platform gateway node when using standalone Redis, or all nodes from the Redis group in your inventory when using clustered Redis, and run:
  

```
$ systemctl --user start redis-unix redis-tcp
```

## Reconcile the target environment post-import

Perform the following post-import reconciliation steps to verify your target environment functions correctly.

### Procedure

1.  Deprovision the platform gateway configuration.   - To deprovision platform gateway configuration, SSH to the host serving an `automation-gateway` container as the same rootless user from 4.2.6 and run the following to remove the platform gateway proxy configuration:

```
$ podman exec -it automation-gateway bash
$ aap-gateway-manage migrate
$ aap-gateway-manage shell_plus
>>> HTTPPort.objects.all().delete(); ServiceNode.objects.all().delete(); ServiceCluster.objects.all().delete()
```

2.  Transfer custom configurations and settings.   - Edit the inventory file and apply any relevant `extra_settings` to each component by using the `component_extra_settings`.

3.  Remove all resource server key secrets to be repopulated by the installer:
  

```
$ for i in `podman secret ls | egrep 'resource_server' | awk '{print $2}'`; do podman secret rm $i; done
```

4.  Re-run the installation program on the target environment by using the same inventory from the installation.
5.  Sync platform gateway resources if Event-Driven Ansible is present:
  

```
$ podman exec -it automation-eda-api bash
```

```
$ aap-eda-manage resource_sync
```

6.  Validate instances for automation execution.   1.  SSH to the host serving an `automation-controller-task` container as the rootless user, and run the following commands to validate and remove instances that are orphaned from the source artifact:
  

```
$ podman exec -it automation-controller-task bash
```

```
$ awx-manage list_instances
```

  2.  Find nodes that are no longer part of this cluster. A good indicator is nodes with 0 capacity as they have failed their health checks:
  

```
[ungrouped capacity=0]
    [DISABLED] node1.example.org capacity=0 node_type=hybrid version=X.Y.Z heartbeat="..."
    [DISABLED] node2.example.org capacity=0 node_type=execution version=ansible-runner-X.Y.Z heartbeat="..."
```

  3.  Remove those nodes with `awx-manage`, leaving only the `aap-controller-task` instance:
  

```
awx-manage deprovision_instance --hostname=node1.example.org
awx-manage deprovision_instance --hostname=node2.example.org
```

7.  Repair orphaned automation hub content links for Pulp.   - Run the following command from any host that has direct access to the automation hub address:

```
$ curl -d '{\"verify_checksums\": true }' -X POST -k https://<gateway url>/api/galaxy/pulp/api/v3/repair/ -u <gateway_admin_user>:<gateway_admin_password>
```

8.  Reconcile instance groups configuration:
  1.  Go to Automation Execution> (and then)Infrastructure> (and then)Instance Groups.
  2.  Select the **Instance Group** and then select the **Instances** tab.
  3.  Associate or disassociate instances as required.
9.  Reconcile decision environments and credentials:
  1.  Go to Automation Decisions> (and then)Decision Environments.
  2.  Edit each decision environment which references a registry URL either unrelated or no longer accessible to this new environment. For example, the automation hub decision environment might require modification for the target automation hub environment.
  3.  Select each associated credential to these decision environments and ensure their addresses align with the new environment.
10.  Reconcile execution environments and credentials:
  1.  Go to Automation Execution> (and then)Infrastructure> (and then)Execution Environments.
  2.  Check each execution environment image and verify their addresses against the new environment.
  3.  Go to Automation Execution> (and then)Infrastructure> (and then)Credentials.
  4.  Edit each credential and ensure that all environment specific information aligns with the new environment.
11.  Verify any further customizations or configurations after the migration, such as RBAC rules with instance groups.

## Validate the target environment

After completing the migration, validate that all components in your target environment function correctly.

### Procedure

1.  Verify all migrated components function correctly.   1.  Platform gateway: Access the Ansible Automation Platform URL at `https://<gateway_hostname>/` and verify that the dashboard loads correctly. Check that the platform gateway service is running and connected to automation controller.
  2.  Automation controller: Under **Automation Execution**, check that projects, inventories, and job templates are present and configured.
  3.  Automation hub: Under **Automation Content**, verify that collections, namespaces, and their contents are visible.
  4.  Event-Driven Ansible (if applicable): Under **Automation Execution Decisions**, verify that rule audits, rulebook activations, and projects are accessible.
  5.  For each component, check the logs to ensure there are no startup errors or warnings:
  

```
podman logs <container_name>
```

2.  Test workflows and automation processes.   1.  Run job templates: Run several key job templates, including those with dependencies on various credential types.
  2.  Test workflow templates: Run workflow templates to ensure that workflow nodes run in the correct order and that the workflow completes successfully.
  3.  Verify execution environments: Ensure that jobs run in the appropriate execution environments and can access required dependencies.
  4.  Check job artifacts: Verify that job artifacts are properly stored and accessible.
  5.  Validate job scheduling: Test scheduled jobs to ensure they run at the expected times.
3.  Validate user access and permissions.   1.  User authentication: Test login functionality with various user accounts to ensure authentication works correctly.
  2.  Role-based access controls: Verify that users have appropriate permissions for organizations, projects, inventories, and job templates.
  3.  Team memberships: Confirm that team memberships and team-based permissions are intact.
  4.  API access: Test API tokens and ensure that API access is functioning properly.
  5.  SSO integration (if applicable): Verify that Single Sign-On authentication is working correctly.
4.  Confirm content synchronization and availability.   1.  Collection synchronization: Check that you can synchronize collections from a remote.
  2.  Collection Upload: Check that you can upload collections.
  3.  Collection repositories: Verify that automation hub makes collections available and that execution environments can use them.
  4.  Project synchronization: Check that projects can sync content from source control repositories.
  5.  External content sources: Test synchronization from automation hub and Ansible Galaxy (if configured).
  6.  Execution environment availability: Confirm that all required execution environments exist and that execution nodes can access them.
  7.  Content dependencies: Verify that the system correctly resolves content dependencies when running jobs.
