# Configure an external (customer provided) PostgreSQL database
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

