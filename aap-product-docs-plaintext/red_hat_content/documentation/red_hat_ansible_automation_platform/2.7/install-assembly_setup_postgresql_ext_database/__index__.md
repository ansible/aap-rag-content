# Configure an external (customer provided) PostgreSQL database

Set up an external (customer provided) PostgreSQL database for containerized Ansible Automation Platform to use your own database infrastructure.

There are two possible scenarios for setting up an external database:

1. An external database with PostgreSQL admin credentials
2. An external database without PostgreSQL admin credentials


Important:

- When using an external database with Ansible Automation Platform, you must create and support that database. Ensure that you clear your external database when uninstalling Ansible Automation Platform.
- Red Hat Ansible Automation Platform requires customer provided (external) database to have International Components for Unicode (ICU) support.
- During configuration of an external database, you must check the external database coverage. For more information, see *Red Hat Ansible Automation Platform Database Scope of Coverage* in the related information section.
- Metrics service requires two database connections: a dedicated `metrics_service` database (read/write) and read-only access to the automation controller database using the `ms_awx_readonly` user. You must create both before installation.
- The `[database]` group in your inventory file defines the Ansible Automation Platform managed database. When using an externally managed database, do not include the `[database]` group in your inventory file.

## Set up an external database with PostgreSQL admin credentials

If you have PostgreSQL admin credentials, you can supply them in the inventory file and the installation program creates the PostgreSQL users and databases for each component for you. The PostgreSQL admin account must have `SUPERUSER` privileges.

### Procedure

To configure the PostgreSQL admin credentials, add the following variables to the inventory file under the `[all:vars]` group:

```yaml
postgresql_admin_username=<set your own>
postgresql_admin_password=<set your own>
```

## Set up an external database without PostgreSQL admin credentials

If you do not have PostgreSQL admin credentials, then PostgreSQL users and databases need to be created for each component (platform gateway, automation controller, automation hub, Event-Driven Ansible, and metrics service) before running the installation program.

### Procedure

1.  Connect to a PostgreSQL compliant database server with a user that has `SUPERUSER` privileges.

```bash
# psql -h <hostname> -U <username> -p <port_number>
```
For example:

```bash
# psql -h db.example.com -U superuser -p 5432
```

2.  Create the user with a password and ensure the `CREATEDB` role is assigned to the user. For more information, see [Database Roles](https://www.postgresql.org/docs/13/user-manag.html).

```sql
CREATE USER <username> WITH PASSWORD <password> CREATEDB;
```

3.  Create the database and add the user you created as the owner.

```sql
CREATE DATABASE <database_name> OWNER <username>;
```

4.  When you have created the PostgreSQL users and databases for each component, you can supply them in the inventory file under the `[all:vars]` group.

```yaml
# Platform gateway
gateway_pg_host=aap.example.org
gateway_pg_database=<set your own>
gateway_pg_username=<set your own>
gateway_pg_password=<set your own>

# Automation controller
controller_pg_host=aap.example.org
controller_pg_database=<set your own>
controller_pg_username=<set your own>
controller_pg_password=<set your own>

# Automation hub
hub_pg_host=aap.example.org
hub_pg_database=<set your own>
hub_pg_username=<set your own>
hub_pg_password=<set your own>

# Event-Driven Ansible
eda_pg_host=aap.example.org
eda_pg_database=<set your own>
eda_pg_username=<set your own>
eda_pg_password=<set your own>

# Metrics service
automationmetrics_pg_host=aap.example.org
automationmetrics_pg_database=metrics_service
automationmetrics_pg_username=<set your own>
automationmetrics_pg_password=<set your own>

# Metrics service read-only access to controller database
automationmetrics_controller_read_pg_host=aap.example.org
automationmetrics_controller_read_pg_database=<controller database name>
automationmetrics_controller_read_pg_username=ms_awx_readonly
automationmetrics_controller_read_pg_password=<set your own>
```

## Set up metrics service database with cross-database permissions

Create the metrics service database and configure cross-database permissions to allow metrics service to store data and correlate metrics with automation activity.

### About this task

Metrics service requires access to two databases:

- **`metrics_service` database (read/write):** Stores collected metrics data
- **`automationcontroller` database (read-only):** Used to correlate metrics with automation activity


This dual-database architecture ensures metrics service can collect data while maintaining security isolation from the automation controller's operational database.

### Procedure

1.  Connect to your PostgreSQL database server with a user that has SUPERUSER privileges.


```
$ psql -h <hostname> -U <username> -p <port_number>
```

2.  Create the metrics service database and user.


```
CREATE USER metrics_service WITH PASSWORD '<secure_password>' CREATEDB;
CREATE DATABASE metrics_service OWNER metrics_service;
```

3.  Create a read-only user for accessing the automation controller database.


```
CREATE USER ms_awx_readonly WITH PASSWORD '<secure_password>';
```

4.  Grant the read-only user access to the automation controller database.


```
-- Connect to the automation controller database
\c <automationcontroller_database_name>

-- Grant connection privilege
GRANT CONNECT ON DATABASE <automationcontroller_database_name> TO ms_awx_readonly;

-- Grant usage on schema
GRANT USAGE ON SCHEMA public TO ms_awx_readonly;

-- Grant SELECT on all existing tables
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ms_awx_readonly;

-- Grant SELECT on future tables (automatic for new tables)
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO ms_awx_readonly;
```

5.  Add the metrics service database configuration to your inventory file under the `[all:vars]` group.


```
# Metrics service
automationmetrics_pg_host=aap.example.org
automationmetrics_pg_database=metrics_service
automationmetrics_pg_username=metrics_service
automationmetrics_pg_password=<secure_password>

# Metrics service read-only access to controller database
automationmetrics_controller_read_pg_host=aap.example.org
automationmetrics_controller_read_pg_database=<automationcontroller_database_name>
automationmetrics_controller_read_pg_username=ms_awx_readonly
automationmetrics_controller_read_pg_password=<secure_password>
```

Important:
The `ms_awx_readonly` user must be created with SELECT privileges on the automation controller database before running the Ansible Automation Platform installer. The installer does not create this user automatically.

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

## Optional: configure mutual TLS (mTLS) authentication for an external database

mTLS authentication is disabled by default. To configure each component’s database with mTLS authentication, add the following variables to your inventory file under the `[all:vars]` group and ensure each component has a different TLS certificate and key:

### Procedure

Add the following variables to your inventory file under the `[all:vars]` group:

```yaml
# Platform gateway
gateway_pg_cert_auth=true
gateway_pg_tls_cert=/path/to/gateway.cert
gateway_pg_tls_key=/path/to/gateway.key
gateway_pg_sslmode=verify-full

# Automation controller
controller_pg_cert_auth=true
controller_pg_tls_cert=/path/to/awx.cert
controller_pg_tls_key=/path/to/awx.key
controller_pg_sslmode=verify-full

# Automation hub
hub_pg_cert_auth=true
hub_pg_tls_cert=/path/to/pulp.cert
hub_pg_tls_key=/path/to/pulp.key
hub_pg_sslmode=verify-full

# Event-Driven Ansible
eda_pg_cert_auth=true
eda_pg_tls_cert=/path/to/eda.cert
eda_pg_tls_key=/path/to/eda.key
eda_pg_sslmode=verify-full

# Metrics service
automationmetrics_pg_cert_auth=true
automationmetrics_pg_tls_cert=/path/to/metrics.cert
automationmetrics_pg_tls_key=/path/to/metrics.key
automationmetrics_pg_sslmode=verify-full

# Metrics service read-only connection to controller
databaseautomationmetrics_controller_read_pg_cert_auth=true
automationmetrics_controller_read_pg_tls_cert=/path/to/metrics.cert
automationmetrics_controller_read_pg_tls_key=/path/to/metrics.key
automationmetrics_controller_read_pg_sslmode=verify-full
```
