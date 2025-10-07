# 2. System requirements
## 2.6. PostgreSQL requirements
### 2.6.2. Setting up an external (customer supported) database




Important
- When using an external database with Ansible Automation Platform, you must create and maintain that database. Ensure that you clear your external database when uninstalling Ansible Automation Platform.
- Red Hat Ansible Automation Platform 2.5 uses PostgreSQL 15 and requires the external (customer supported) databases to have ICU support.
- During configuration of an external database, you must check the external database coverage. For more information, see [Red Hat Ansible Automation Platform Database Scope of Coverage](https://access.redhat.com/articles/4010491) .




Red Hat Ansible Automation Platform 2.5 uses PostgreSQL 15 and requires the external (customer supported) databases to have ICU support. Use the following procedure to configure an external PostgreSQL compliant database for use with an Ansible Automation Platform component, for example automation controller, Event-Driven Ansible, automation hub, and platform gateway.

**Procedure**

1. Connect to a PostgreSQL compliant database server with superuser privileges.


```
# psql -h &lt;db.example.com&gt; -U superuser -p 5432 -d postgres &lt;Password for user superuser&gt;:
```


1. Where the default value for <hostname> is **hostname** :


```
-h hostname    --host=hostname
```


1. Specify the hostname of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the UNIX-domain socket.


```
-d dbname    --dbname=dbname
```


1. Specify the name of the database to connect to. This is equal to specifying `    dbname` as the first non-option argument on the command line. The `    dbname` can be a connection string. If so, connection string parameters override any conflicting command line options.


```
-U username    --username=username
```


1. Connect to the database as the user `    username` instead of the default (you must have permission to do so).
1. Create the user, database, and password with the `    createDB` or `    administrator` role assigned to the user. For further information, see [Database Roles](https://www.postgresql.org/docs/13/user-manag.html) .
1. Run the installation program. If you are using a PostgreSQL database, the database is owned by the connecting user and must have a `    createDB` or administrator role assigned to it.
1. Check that you can connect to the created database with the credentials provided in the inventory file.
1. Check the permission of the user. The user should have the `    createDB` or administrator role.
1. After you create the PostgreSQL users and databases for each component, add the database credentials and host details in the inventory file under the [all:vars] group.


```
# Automation controller    pg_host=data.example.com    pg_database=&lt;database name&gt;    pg_port=&lt;port_number&gt;    pg_username=&lt;set your own&gt;    pg_password=&lt;set your own&gt;        # Platform gateway    automationgateway_pg_host=aap.example.org    automationgateway_pg_database=&lt;set your own&gt;    automationgateway_pg_port=&lt;port_number&gt;    automationgateway_pg_username=&lt;set your own&gt;    automationgateway_pg_password=&lt;set your own&gt;        # Automation hub    automationhub_pg_host=data.example.com    automationhub_pg_database=&lt;database_name&gt;    automationhub_pg_port=&lt;port_number&gt;    automationhub_pg_username=&lt;username&gt;    automationhub_pg_password=&lt;password&gt;        # Event-Driven Ansible    automationedacontroller_pg_host=data.example.com    automationedacontroller_pg_database=&lt;database_name&gt;    automationedacontroller_pg_port=&lt;port_number&gt;    automationedacontroller_pg_username=&lt;username&gt;    automationedacontroller_pg_password=&lt;password&gt;
```




