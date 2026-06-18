# Set up event streams database user without PostgreSQL admin credentials

If you do not have PostgreSQL admin credentials, you must manually create the eda_event_stream database user before running the installation program.

## Procedure

1.  Connect to your PostgreSQL database server with a user that has `SUPERUSER` privileges:


```
----
# psql -h <hostname> -U <username> -p <port_number>
----
```

For example:

```
----
# psql -h db.example.com -U superuser -p 5432
----
```

2.  Create the `eda_event_stream` database user and grant access to your database:


```
----
CREATE USER eda_event_stream WITH PASSWORD
'<eda_event_stream_password>';
GRANT CONNECT ON DATABASE <database_name> TO eda_event_stream;
----
```

3.  Add the following variables to your inventory file under the `[all:vars]` group, replacing the password with the value used in the previous step:


```
----
eda_event_stream_pg_username=eda_event_stream
eda_event_stream_pg_password=<eda_event_stream_password>
----
```
