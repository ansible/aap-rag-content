# Set up event streams database user with PostgreSQL admin credentials

If you have PostgreSQL admin credentials configured in your inventory file, the installation program automatically creates the eda_event_stream database user and grants the necessary permissions.

## Procedure

Ensure the following variables are set in your inventory file under the `[all:vars]` group:

```
postgresql_admin_username=<set your own>
postgresql_admin_password=<set your own>
```
If these variables are already set, the installation program automatically creates the event streams database user using these admin credentials.
