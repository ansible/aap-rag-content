# 2. Ansible Automation Platform containerized installation
## 2.7. Advanced configuration options
### 2.7.6. Setting up a customer provided (external) database




There are two possible scenarios for setting up an external database:

1. An external database with PostgreSQL admin credentials
1. An external database without PostgreSQL admin credentials


Important
- When using an external database with Ansible Automation Platform, you must create and maintain that database. Ensure that you clear your external database when uninstalling Ansible Automation Platform.
- Red Hat Ansible Automation Platform requires customer provided (external) database to have ICU support.
- During configuration of an external database, you must check the external database coverage. For more information, see [Red Hat Ansible Automation Platform Database Scope of Coverage](https://access.redhat.com/articles/4010491) .




#### 2.7.6.1. Setting up an external database with PostgreSQL admin credentials




If you have PostgreSQL admin credentials, you can supply them in the inventory file and the installation program creates the PostgreSQL users and databases for each component for you. The PostgreSQL admin account must have `SUPERUSER` privileges.

**Procedure**

- To configure the PostgreSQL admin credentials, add the following variables to the inventory file under the `    [all:vars]` group:


```
postgresql_admin_username=&lt;set your own&gt;    postgresql_admin_password=&lt;set your own&gt;
```




#### 2.7.6.2. Setting up an external database without PostgreSQL admin credentials




If you do not have PostgreSQL admin credentials, then PostgreSQL users and databases need to be created for each component (platform gateway, automation controller, automation hub, and Event-Driven Ansible) before running the installation program.

**Procedure**

1. Connect to a PostgreSQL compliant database server with a user that has `    SUPERUSER` privileges.


```
# psql -h &lt;hostname&gt; -U &lt;username&gt; -p &lt;port_number&gt;
```

For example:


```
# psql -h db.example.com -U superuser -p 5432
```


1. Create the user with a password and ensure the `    CREATEDB` role is assigned to the user. For more information, see [Database Roles](https://www.postgresql.org/docs/13/user-manag.html) .


```
CREATE USER &lt;username&gt; WITH PASSWORD &lt;password&gt; CREATEDB;
```


1. Create the database and add the user you created as the owner.


```
CREATE DATABASE &lt;database_name&gt; OWNER &lt;username&gt;;
```


1. When you have created the PostgreSQL users and databases for each component, you can supply them in the inventory file under the `    [all:vars]` group.


```
# Platform gateway    gateway_pg_host=aap.example.org    gateway_pg_database=&lt;set your own&gt;    gateway_pg_username=&lt;set your own&gt;    gateway_pg_password=&lt;set your own&gt;        # Automation controller    controller_pg_host=aap.example.org    controller_pg_database=&lt;set your own&gt;    controller_pg_username=&lt;set your own&gt;    controller_pg_password=&lt;set your own&gt;        # Automation hub    hub_pg_host=aap.example.org    hub_pg_database=&lt;set your own&gt;    hub_pg_username=&lt;set your own&gt;    hub_pg_password=&lt;set your own&gt;        # Event-Driven Ansible    eda_pg_host=aap.example.org    eda_pg_database=&lt;set your own&gt;    eda_pg_username=&lt;set your own&gt;    eda_pg_password=&lt;set your own&gt;
```




#### 2.7.6.3. Enabling the hstore extension for the automation hub PostgreSQL database




The database migration script uses `hstore` fields to store information, therefore the `hstore` extension must be enabled in the automation hub PostgreSQL database.

This process is automatic when using the Ansible Automation Platform installer and a managed PostgreSQL server.

If the PostgreSQL database is external, you must enable the `hstore` extension in the automation hub PostgreSQL database manually before installation.

If the `hstore` extension is not enabled before installation, a failure raises during database migration.

**Procedure**

1. Check if the extension is available on the PostgreSQL server (automation hub database).


```
$ psql -d &lt;automation hub database&gt; -c "SELECT * FROM pg_available_extensions WHERE name='hstore'"
```


1. Where the default value for `    &lt;automation hub database&gt;` is `    automationhub` .

**Example output with `    hstore` available** :


```
name  | default_version | installed_version |comment    ------+-----------------+-------------------+---------------------------------------------------     hstore | 1.7           |                   | data type for storing sets of (key, value) pairs    (1 row)
```

**Example output with `    hstore` not available** :


```
name | default_version | installed_version | comment    ------+-----------------+-------------------+---------    (0 rows)
```


1. On a RHEL based server, the `    hstore` extension is included in the `    postgresql-contrib` RPM package, which is not installed automatically when installing the PostgreSQL server RPM package.

To install the RPM package, use the following command:


```
dnf install postgresql-contrib
```


1. Load the `    hstore` PostgreSQL extension into the automation hub database with the following command:


```
$ psql -d &lt;automation hub database&gt; -c "CREATE EXTENSION hstore;"
```

In the following output, the `    installed_version` field lists the `    hstore` extension used, indicating that `    hstore` is enabled.


```
name | default_version | installed_version | comment    -----+-----------------+-------------------+------------------------------------------------------    hstore  |     1.7      |       1.7         | data type for storing sets of (key, value) pairs    (1 row)
```




#### 2.7.6.4. Optional: configuring mutual TLS (mTLS) authentication for an external database




mTLS authentication is disabled by default. To configure each component’s database with mTLS authentication, add the following variables to your inventory file under the `[all:vars]` group and ensure each component has a different TLS certificate and key:

**Procedure**

- Add the following variables to your inventory file under the `    [all:vars]` group:


```
# Platform gateway    gateway_pg_cert_auth=true    gateway_pg_tls_cert=/path/to/gateway.cert    gateway_pg_tls_key=/path/to/gateway.key    gateway_pg_sslmode=verify-full        # Automation controller    controller_pg_cert_auth=true    controller_pg_tls_cert=/path/to/awx.cert    controller_pg_tls_key=/path/to/awx.key    controller_pg_sslmode=verify-full        # Automation hub    hub_pg_cert_auth=true    hub_pg_tls_cert=/path/to/pulp.cert    hub_pg_tls_key=/path/to/pulp.key    hub_pg_sslmode=verify-full        # Event-Driven Ansible    eda_pg_cert_auth=true    eda_pg_tls_cert=/path/to/eda.cert    eda_pg_tls_key=/path/to/eda.key    eda_pg_sslmode=verify-full
```




