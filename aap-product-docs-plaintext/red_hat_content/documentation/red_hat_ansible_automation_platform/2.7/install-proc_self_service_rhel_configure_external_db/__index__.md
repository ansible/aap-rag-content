# Configure an external database

By default, the Ansible automation portal RHEL appliance runs a built-in PostgreSQL database. For production deployments, connect to an external PostgreSQL database.

## Before you begin

- A PostgreSQL database instance accessible from the appliance.
- A database user with the `CREATEDB` privilege.
- The database password.
- SSH access to the appliance.

## About this task

You can provide external database settings in the cloud-init user-data at first boot or configure the database after deployment. For the cloud-init template fields, see [External database cloud-init template](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_prerequisites "Before you deploy an Ansible automation portal RHEL appliance, verify that your environment meets the system, network, and access requirements.").

## Procedure

1.  Edit the configuration file:


```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

2.  Update the `backend.database` section:


```yaml
backend:
database:
connection:
host: *database-host*
port: 5432
user: *database-user*
ssl:
require: true
client: pg
```
The database user requires the `CREATEDB` privilege.

3.  Store the database password as a Podman secret:


```terminal
$ printf '%s' "*database-password*" | sudo podman secret create portal_postgresql_password -
```

4.  Restart the Ansible automation portal service:


```terminal
$ sudo systemctl restart portal
```

## Results

Check the portal logs to verify the database connection:

```terminal
$ sudo journalctl -u portal --no-pager | grep -i "database"
```
The output shows a successful database connection with no errors.
