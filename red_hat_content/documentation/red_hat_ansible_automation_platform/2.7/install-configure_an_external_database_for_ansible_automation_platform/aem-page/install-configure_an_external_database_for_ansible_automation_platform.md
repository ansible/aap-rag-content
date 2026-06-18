+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_ansible_automation_platform"
title = "Configure an external database for Ansible Automation Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_ansible_automation_platform/aem-page/install-configure_an_external_database_for_ansible_automation_platform.html"
last_crumb = "Configure an external database for Ansible Automation Platform"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure an external database for Ansible Automation Platform"
oversized = "false"
page_slug = "install-configure_an_external_database_for_ansible_automation_platform"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_ansible_automation_platform"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_ansible_automation_platform/toc/toc.json"
type = "aem-page"
+++

# Configure an external database for Ansible Automation Platform

Configure an external database for Ansible Automation Platform Operator to use your own database infrastructure.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

To configure an external database, create Kubernetes secrets with credentials for connecting to the database. The same external database (PostgreSQL instance) can be used for platform gateway, automation controller, automation hub, Event-Driven Ansible controller, and metrics service as long as the database names are different.

Note:

The automation hub database requires the `hstore` PostgreSQL extension.

## Configure an external database for platform gateway on Red Hat Ansible Automation Platform Operator

There are two scenarios for deploying Ansible Automation Platform with an external database:

### Before you begin

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information must be stored in a secret, which is then set on the platform gateway spec.

Note:

Ansible Automation Platform supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases.

If you choose to use an externally managed database with version 16 or 17 you must also rely on external backup and restore processes.

### About this task

| Scenario                              | Action required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>Fresh install                     | <br>You must specify a single external database instance for the platform to use for the following:<br>Platform gatewayAutomation controllerAutomation hubEvent-Driven AnsibleMetrics serviceRed Hat Ansible Lightspeed (If enabled)<br>See the *aap-configuring-external-db-all-default-components.yml* example in the [Custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#unique_2099983463 "Refer to the following custom resources you can use for various Ansible Automation Platform deployment scenarios.") section for help with this.<br>If using Red Hat Ansible Lightspeed, use the *aap-configuring-external-db-with-lightspeed-enabled.yml* example. |
| <br>Existing external database in 2.4 | <br>Your existing external database remains the same after upgrading but you must specify the `external-postgres-configuration-gateway` (spec.database.database\_secret) on the Ansible Automation Platform custom resource.<br>For detailed steps, see [Upgrading an external database for platform gateway on on Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_ansible_automation_platform#GUID-b94a38e1-9266-4338-a29a-1fd21ee08f5a "To upgrade from Ansible Automation Platform 2.4 to 2.6 with an external database, you must scale down your Operator deployment, upgrade your PostgreSQL, then scale your deployment back up.")        |


To deploy Ansible Automation Platform with an external database, you must first create a Kubernetes secret with credentials for connecting to the database.

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment. You can deploy Ansible Automation Platform with an external database instead of the managed PostgreSQL pod that the Ansible Automation Platform Operator automatically creates.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

Note:

The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, platform gateway, and metrics service as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.

The following section outlines the steps to configure an external database for your platform gateway on a Ansible Automation Platform Operator.

### Procedure

1.  Create a `postgres_configuration_secret` YAML file, following the template below:
  

```
apiVersion: v1
kind: Secret
metadata:
  name: external-postgres-configuration
  namespace: <target_namespace>
stringData:
  host: "<external_ip_or_url_resolvable_by_the_cluster>"
  port: "<external_port>"
  database: "<desired_database_name>"
  username: "<username_to_connect_as>"
  password: "<password_to_connect_with>"
  type: "unmanaged"
type: Opaque
```
    Where:

<target_namespace>
Namespace to create the secret in. This should be the same namespace you want to deploy to.

<external_ip_or_url_resolvable_by_the_cluster>
The resolvable hostname for your database node.

<external_port>
External port defaults to `5432`.

<password_to_connect_with>
Value for variable `password` should not contain single or double quotes (', ") or backslashes (\) to avoid any issues during deployment, backup or restoration.

2.  Apply `external-postgres-configuration-secret.yml` to your cluster using the `oc create` command.

```
$ oc create -f external-postgres-configuration-secret.yml
```
  Note:
      The following example is for a platform gateway deployment. To configure an external database for all components, use the *aap-configuring-external-db-all-default-components.yml* example in the [Custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#unique_2099983463 "Refer to the following custom resources you can use for various Ansible Automation Platform deployment scenarios.") section.

3.  When creating your `AnsibleAutomationPlatform` custom resource object, specify the secret on your spec, following the example below:
  

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: example-aap
  Namespace: aap
spec:
  database:
     database_secret: automation-platform-postgres-configuration
```

## Configure an external database for automation controller on Red Hat Ansible Automation Platform Operator

For users who prefer to deploy Ansible Automation Platform with an external database, they can do so by configuring a secret with instance credentials and connection information, then applying it to their cluster using the `oc create` command.

### Before you begin

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information must be stored in a secret, which is then set on the automation controller spec.

Note:

Ansible Automation Platform supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases.

If you choose to use an externally managed database with version 16 or 17 you must also rely on external backup and restore processes.

### About this task

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment. You can deploy Ansible Automation Platform with an external database instead of the managed PostgreSQL pod that the Ansible Automation Platform Operator automatically creates.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

Note:

The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, platform gateway, and metrics service as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.

The following section outlines the steps to configure an external database for your automation controller on a Ansible Automation Platform Operator.

### Procedure

1.  Create a `postgres_configuration_secret` YAML file, following the template below:
  

```
apiVersion: v1
kind: Secret
metadata:
  name: external-postgres-configuration
  namespace: <target_namespace>
stringData:
  host: "<external_ip_or_url_resolvable_by_the_cluster>"
  port: "<external_port>"
  database: "<desired_database_name>"
  username: "<username_to_connect_as>"
  password: "<password_to_connect_with>"
  sslmode: "prefer"
  type: "unmanaged"
type: Opaque
```
    When configuring the secret:

  - `namespace`: Specify the namespace to create the secret in. This should be the same namespace you want to deploy to.
  - `host`: Specify the resolvable hostname for your database node.
  - `port`: Specify the external port. The default is `5432`.
  - `password`: Ensure the password does not contain single or double quotes (', ") or backslashes (\) to avoid any issues during deployment, backup or restoration.
  - `sslmode`: This variable is valid for external databases only. The allowed values are: `prefer`, `disable`, `allow`, `require`, `verify-ca`, and `verify-full`.

2.  Apply `external-postgres-configuration-secret.yml` to your cluster using the `oc create` command.

```
$ oc create -f external-postgres-configuration-secret.yml
```

3.  When creating your `AnsibleAutomationPlatform` custom resource object, specify the secret under the `controller` section in your spec, following the example below:
  

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
spec:
  controller:
    name: controller-dev  # Optional: specify existing instance or custom name
    postgres_configuration_secret: external-postgres-configuration
```
  
  Note:
      If you have an existing automation controller instance, specify its name under `controller.name` to apply these settings to the existing instance. If you omit the `name` field, the operator will create a new instance with the default name pattern `<aap-instance-name>-controller`.

    For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")

## Configure an external database for automation hub on Red Hat Ansible Automation Platform Operator

For users who prefer to deploy Ansible Automation Platform with an external database, they can do so by configuring a secret with instance credentials and connection information, then applying it to their cluster using the `oc create` command.

### Before you begin

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information will need to be stored in a secret, which will then be set on the automation hub spec.

Note:

Ansible Automation Platform supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases.

If you choose to use an externally managed database with version 16 or 17 you must also rely on external backup and restore processes.

### About this task

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment.

You can choose to use an external database instead if you prefer to use a dedicated node to ensure dedicated resources or to manually manage backups, upgrades, or performance tweaks.

Note:

The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, and platform gateway as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.

The following section outlines the steps to configure an external database for your automation hub on a Ansible Automation Platform Operator.

### Procedure

1.  Create a `postgres_configuration_secret` YAML file, following the template below:
  

```
apiVersion: v1
kind: Secret
metadata:
  name: external-postgres-configuration
  namespace: <target_namespace> ①
stringData:
  host: "<external_ip_or_url_resolvable_by_the_cluster>" ②
  port: "<external_port>" ③
  database: "<desired_database_name>"
  username: "<username_to_connect_as>"
  password: "<password_to_connect_with>" ④
  sslmode: "prefer" ⑤
  type: "unmanaged"
type: Opaque
```
  1.  Namespace to create the secret in. This should be the same namespace you want to deploy to.
  2.  The resolvable hostname for your database node.
  3.  External port defaults to `5432`.
  4.  Value for variable `password` should not contain single or double quotes (', ") or backslashes (\) to avoid any issues during deployment, backup or restoration.
  5.  The variable `sslmode` is valid for `external` databases only. The allowed values are: `prefer`, `disable`, `allow`, `require`, `verify-ca`, and `verify-full`.

2.  Apply `external-postgres-configuration-secret.yml` to your cluster using the `oc create` command.

```
$ oc create -f external-postgres-configuration-secret.yml
```

3.  When creating your `AnsibleAutomationPlatform` custom resource object, specify the secret under the `hub` section in your spec, following the example below:
  

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
spec:
  hub:
    name: hub-dev  # Optional: specify existing instance or custom name
    postgres_configuration_secret: external-postgres-configuration
    storage_type: file
    file_storage_storage_class: <your-read-write-many-storage-class>
    file_storage_size: 10Gi
```
  
  Note:
      If you have an existing automation hub instance, specify its name under `hub.name` to apply these settings to the existing instance. If you omit the `name` field, the operator will create a new instance with the default name pattern `<aap-instance-name>-hub`.

    For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")

## Configure an external database for metrics service on Red Hat Ansible Automation Platform Operator

Metrics service is a required component in Ansible Automation Platform 2.7. For users who prefer to deploy metrics service with an external database, they can do so by configuring secrets with database credentials and connection information.

### Before you begin

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information must be stored in secrets, which are then set on the metrics service spec.

Note:

Ansible Automation Platform supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases. If you choose to use an externally managed database with version 16 or 17 you must also rely on external backup and restore processes.

### About this task

Metrics service requires access to two databases:

- **`metrics_service` database (read/write):** Stores collected metrics data
- **`automationcontroller` database (read-only):** Used to correlate metrics with automation activity


By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment. You can deploy metrics service with an external database instead of the managed PostgreSQL pod that the Ansible Automation Platform Operator automatically creates.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

Note:

The same external database (PostgreSQL instance) can be used for automation hub, automation controller, platform gateway, and metrics service as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.

The following section outlines the steps to configure an external database for metrics service on Ansible Automation Platform Operator.

### Procedure

1.  Create a `postgres_configuration_secret` YAML file for the `metrics_service` database, following the template below:
  

```
apiVersion: v1
kind: Secret
metadata:
  name: metrics-postgres-configuration
  namespace: <target_namespace>
stringData:
  host: "<external_ip_or_url_resolvable_by_the_cluster>"
  port: "<external_port>"
  database: "metrics_service"
  username: "<username_to_connect_as>"
  password: "<password_to_connect_with>"
  sslmode: "prefer"
  type: "unmanaged"
type: Opaque
```
      When configuring the secret:

  - **namespace:** Specify the namespace to create the secret in. This should be the same namespace you want to deploy to.
  - **host:** Specify the resolvable hostname for your database node.
  - **port:** Specify the external port. The default is 5432.
  - **database:** The database name for metrics service. Recommended: `metrics_service`
  - **password:** Ensure the password does not contain single or double quotes (`'`, `"`) or backslashes (`\`) to avoid any issues during deployment, backup or restoration.
  - **sslmode:** This variable is valid for external databases only. The allowed values are: `prefer`, `disable`, `allow`, `require`, `verify-ca`, and `verify-full`.

2.  Create a second secret for read-only access to the automation controller database:
  

```
apiVersion: v1
kind: Secret
metadata:
  name: metrics-controller-readonly-configuration
  namespace: <target_namespace>
stringData:
  host: "<external_ip_or_url_resolvable_by_the_cluster>"
  port: "<external_port>"
  database: "<controller_database_name>"
  username: "ms_awx_readonly"
  password: "<readonly_user_password>"
  sslmode: "prefer"
  type: "unmanaged"
type: Opaque
```
  
  Important:
  The `ms_awx_readonly` user must be created in your external database with SELECT privileges on the automation controller database before deployment. For instructions on creating this user, see Configure an external database for Ansible Automation Platform (containerized).

3.  Apply both secrets to your cluster using the `oc create` command:
  

```
$ oc create -f metrics-postgres-configuration.yml
$ oc create -f metrics-controller-readonly-configuration.yml
```

4.  When creating your AnsibleAutomationPlatform custom resource object, specify both secrets under the metrics section in your spec, following the example below:
  

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
spec:
  metrics:
    disabled: false
    postgres_configuration_secret: metrics-postgres-configuration
    awx_postgres_configuration_secret: metrics-controller-readonly-configuration
```
  
  Note:
  If you have an existing metrics service instance, specify its name under `metrics.name` to apply these settings to the existing instance. If you omit the name field, the operator will create a new instance with the default name pattern `<aap-instance-name>`-metrics.
    For more examples of Ansible Automation Platform custom resources, see Red Hat Ansible Automation Platform custom resources

### What to do next

**Additional considerations:**

- **Database user permissions:** The metrics service database user requires CREATEDB role to run database migrations during installation.
- **Cross-database permissions:** The `ms_awx_readonly` user must have SELECT privileges on all tables in the automation controller database's public schema, including future tables (use ALTER DEFAULT PRIVILEGES).
- **Storage sizing:** Plan for approximately 20-40 GB of database storage for the `metrics_service` database, depending on automation scale and retention policies.
- **Connection pooling:** For high-scale deployments, consider using connection pooling (such as PgBouncer) between metrics service and the external database.

## Upgrading an external database for platform gateway on Ansible Automation Platform

To upgrade from Ansible Automation Platform 2.4 to 2.6 with an external database, you must scale down your Operator deployment, upgrade your PostgreSQL, then scale your deployment back up.

### Before you begin

- A 2.4 automation controller and automation hub deployment with an external PostgreSQL 13 database
- A newly provisioned PostgreSQL 15 database for the new platform gateway component

### Procedure

1.  Create a secret `postgres-config-gateway` with PostgreSQL 15 credentials for the platform gatewaycomponent. For example:
  

```
apiVersion: v1
kind: Secret
metadata:
  name: postgres-config-gateway
  namespace: aap
stringData:
  host: "<DB_HOST_OR_IP>"
  port: "<DB_PORT>"     # default is 5432
  database: "<DB_NAME>" # for example "gateway"
  username: "<DB_USER>" # for example "gateway"
  password: "<DB_PASSWORD>"
  sslmode: "prefer"
  type: "unmanaged"
type: Opaque
```

2.  Add your newly created secret to your Ansible Automation Platform instance:
  

```
spec:
  postgres_configuration_secret: postgres-config-gateway
```

3.  Scale down your deployments in their respective namespaces using:
  

```
oc scale deployment --replicas=0 -n <component-namespace> <component-deployment>
```

4.  Automation contoller:
  1.  `automation-controller-operator-controller-manager`
  2.  `<controller-name>-controller-task`
  3.  `<controller-name>-controller-web`
5.  Automation hub:
  1.  `automation-hub-operator-controller-manager`
  2.  `<hub-name>-hub-api`
  3.  `<hub-name>-hub-content `
  4.  `<hub-name>-hub-redis`
  5.  `<hub-name>-hub-worker`
6.  The remaining operators:t
  1.  `ansible-lightspeed-operator-controller-manager`
  2.  `eda-server-operator-controller-manager`
  3.  `resource-operator-controller-manager`
7.  Upgrade your PostgreSQL 13 to PostgreSQL 15.
8.  Scale your deployments back up using:
  

```
oc scale deployment --replicas=1 -n <component-namespace> <component-deployment>
```

9.  Log into OpenShift Container Platform.
10.  Go to **Operators > Installed Operators**.
11.  Click the ⋮ icon next to your deployment and then click **Edit Subscription**
12.  From the **Details** tab, select **Update Channel**.
13.  Select **stable-2.6** as the channel and click **Save**.
14.  Deploy Ansible Automation Platform 2.6 using the following custom resource (CR):
  

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: aap
spec:

    database:
    database_secret: postgres-config-gateway

    controller:
    name: existing-controller

    eda:
    disabled: true

    hub:
    name: existing-hub
```

### Results

To verify your upgrade was successful, go to your users, collection, job history or similar and confirm that they are on the new 2.6 instance and in the new PostgreSQL 15 databases.

### What to do next

Note:

Metrics service is a new required component in Ansible Automation Platform 2.7. If you are upgrading from 2.4 to 2.6 or later, the operator will automatically provision a managed PostgreSQL database for metrics service unless you specify external database configuration.

To configure metrics service with an external database during upgrade, add the metrics section to your custom resource:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: aap
spec:

  database:
    database_secret: postgres-config-gateway

  controller:
    name: existing-controller

  eda:
    disabled: true

  hub:
    name: existing-hub

  metrics:
    disabled: false
    postgres_configuration_secret: metrics-postgres-configuration
    awx_postgres_configuration_secret: metrics-controller-readonly-configuration
```
Create the required secrets before applying this configuration.

## Enable the hstore extension

The database migration script uses `hstore` fields to store information, therefore the `hstore` extension must be enabled in the automation hub PostgreSQL database.

### About this task

This process is automatic when using the Ansible Automation Platform installer and a managed PostgreSQL server.

If the PostgreSQL database is external, you must enable the `hstore` extension in the automation hub PostgreSQL database manually before installation.

If the `hstore` extension is not enabled before installation, a failure raises during database migration.

### Procedure

1.  Check if the extension is available on the PostgreSQL server (automation hub database).

```
$ psql -d <automation hub database> -c "SELECT * FROM pg_available_extensions WHERE name='hstore'"
```

2.  Where the default value for `<automation hub database>` is `automationhub`. **Example output with `hstore` available**:

```
name  | default_version | installed_version |comment
------+-----------------+-------------------+---------------------------------------------------
 hstore | 1.7           |                   | data type for storing sets of (key, value) pairs
(1 row)
```
    **Example output with `hstore` not available**:

```
 name | default_version | installed_version | comment
------+-----------------+-------------------+---------
(0 rows)
```

3.  On a RHEL based server, the `hstore` extension is included in the `postgresql-contrib` RPM package, which is not installed automatically when installing the PostgreSQL server RPM package. To install the RPM package, use the following command:

```
dnf install postgresql-contrib
```

4.  Load the `hstore` PostgreSQL extension into the automation hub database with the following command:
  

```
$ psql -d <automation hub database> -c "CREATE EXTENSION hstore;"
```
    In the following output, the `installed_version` field lists the `hstore` extension used, indicating that `hstore` is enabled.

```
name | default_version | installed_version | comment
-----+-----------------+-------------------+------------------------------------------------------
hstore  |     1.7      |       1.7         | data type for storing sets of (key, value) pairs
(1 row)
```

## Troubleshoot an external database

When upgrading the Ansible Automation Platform Operator you may encounter an error like the following:

### About this task

```
NotImplementedError: can't parse timestamptz with DateStyle 'Redwood, SHOW_TIME': '18-MAY-23 20:33:55.765755 +00:00'
```
Errors like this occur when you have an external database with an unexpected DateStyle set. You can refer to the following steps to resolve this issue.

### Procedure

1.  Edit the `/var/lib/pgsql/data/postgres.conf` file on the database server:
  

```
# vi /var/lib/pgsql/data/postgres.conf
```

2.  Find and comment out the line:
  

```
#datestyle = 'Redwood, SHOW_TIME'
```

3.  Add the following setting immediately below the newly-commented line:
  

```
datestyle = 'iso, mdy'
```

4.  Save and close the `postgres.conf` file.
5.  Reload the database configuration:
  

```
# systemctl reload postgresql
```
  Note:
      Running this command does not disrupt database operations.
