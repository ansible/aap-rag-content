# Configure an external database for Ansible Automation Platform
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

