# 5. Advanced containerized deployment
## 5.6. Configuring an external (customer provided) PostgreSQL database
### 5.6.2. Setting up an external database without PostgreSQL admin credentials




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




