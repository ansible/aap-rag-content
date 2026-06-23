# Configure an external (customer provided) PostgreSQL database
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

