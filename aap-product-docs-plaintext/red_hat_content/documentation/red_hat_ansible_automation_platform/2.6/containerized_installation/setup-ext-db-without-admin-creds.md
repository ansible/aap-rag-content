# 5. Advanced containerized deployment
## 5.6. Configuring an external (customer provided) PostgreSQL database
### 5.6.2. Setting up an external database without PostgreSQL admin credentials

If you do not have PostgreSQL admin credentials, then PostgreSQL users and databases need to be created for each component (platform gateway, automation controller, automation hub, and Event-Driven Ansible) before running the installation program.

**Procedure**

1. Connect to a PostgreSQL compliant database server with a user that has `SUPERUSER` privileges.

# psql -h <hostname> -U <username> -p <port_number>

For example:

# psql -h db.example.com -U superuser -p 5432

2. Create the user with a password and ensure the `CREATEDB` role is assigned to the user. For more information, see [Database Roles](https://www.postgresql.org/docs/13/user-manag.html).

CREATE USER <username> WITH PASSWORD <password> CREATEDB;

3. Create the database and add the user you created as the owner.

CREATE DATABASE <database_name> OWNER <username>;

4. When you have created the PostgreSQL users and databases for each component, you can supply them in the inventory file under the `[all:vars]` group.

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

