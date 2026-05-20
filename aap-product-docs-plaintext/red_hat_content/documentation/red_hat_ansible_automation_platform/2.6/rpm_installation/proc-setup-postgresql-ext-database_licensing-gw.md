# 2. System requirements
## 2.7. PostgreSQL requirements
### 2.7.2. Setting up an external database

Red Hat Ansible Automation Platform 2.6 requires the external (customer supported) databases to have International Components for Unicode (ICU) support. Use the following procedure to configure an external PostgreSQL compliant database for use with an Ansible Automation Platform component, for example automation controller, Event-Driven Ansible, automation hub, and platform gateway.

Important

- When using an external database with Ansible Automation Platform, you must create and maintain that database. Ensure that you clear your external database when uninstalling Ansible Automation Platform.
- Red Hat Ansible Automation Platform 2.6 requires the external (customer supported) databases to have ICU support.
- During configuration of an external database, you must check the external database coverage. For more information, see [Red Hat Ansible Automation Platform Database Scope of Coverage](https://access.redhat.com/articles/4010491).

**Procedure**

1. Connect to a PostgreSQL compliant database server with superuser privileges.

# psql -h <hostname> -U superuser -p 5432 -d postgres <password_for_user_superuser>

2. Where the default value for <hostname> is **hostname**:

-h hostname
--host=hostname

3. Specify the hostname of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the UNIX-domain socket.

-d dbname
--dbname=dbname

4. Specify the name of the database to connect to. This is equal to specifying `dbname` as the first non-option argument on the command line. The `dbname` can be a connection string. If so, connection string parameters override any conflicting command line options.

-U username
--username=username

5. Connect to the database as the user `username` instead of the default (you must have permission to do so).

6. Create the user, database, and password with the `createDB` or `administrator` role assigned to the user. For further information, see [Database Roles](https://www.postgresql.org/docs/13/user-manag.html).

7. Run the installation program. If you are using a PostgreSQL database, the database is owned by the connecting user and must have a `createDB` or administrator role assigned to it.

8. Check that you can connect to the created database with the credentials provided in the inventory file.

9. Check the permission of the user. The user should have the `createDB` or administrator role.

10. After you create the PostgreSQL users and databases for each component, add the database credentials and host details in the inventory file under the [all:vars] group.

# Automation controller
pg_host=data.example.com
pg_database=<database name>
pg_port=<port_number>
pg_username=<set your own>
pg_password=<set your own>

# Platform gateway
automationgateway_pg_host=aap.example.org
automationgateway_pg_database=<set your own>
automationgateway_pg_port=<port_number>
automationgateway_pg_username=<set your own>
automationgateway_pg_password=<set your own>

# Automation hub
automationhub_pg_host=data.example.com
automationhub_pg_database=<database_name>
automationhub_pg_port=<port_number>
automationhub_pg_username=<username>
automationhub_pg_password=<password>

# Event-Driven Ansible
automationedacontroller_pg_host=data.example.com
automationedacontroller_pg_database=<database_name>
automationedacontroller_pg_port=<port_number>
automationedacontroller_pg_username=<username>
automationedacontroller_pg_password=<password>

