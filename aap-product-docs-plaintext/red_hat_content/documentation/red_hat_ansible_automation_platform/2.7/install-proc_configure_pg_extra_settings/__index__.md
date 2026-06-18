# Configure custom PostgreSQL settings

The `postgres_extra_settings` variable allows you to pass a list of custom *name: value* pairs directly to the PostgreSQL configuration file `(/var/lib/pgsql/data/postgresql.conf)` within the database pod.

## Before you begin

- You have installed the Ansible Automation Platform Operator.

## About this task

## Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Go to **Operators → Installed Operators**.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select **All Instances** and go to your **Ansible Automation Platform** instance.
5.  Click the ⋮ icon and then select **Edit Ansible Automation Platform**.
6.  In the **YAML** view, locate the `spec:` section
7.  Add the `database` section and the required settings under `spec:`. The following example configures SSL ciphers and the maximum connections:


```bash
spec:
database:
postgres_extra_settings:
- name: max_connections
value: '1000'
```

8.  Click Save.

## Results

Inspect the PostgreSQL pod logs to verify the new settings.

Alternatively, you can run the following command to check the settings. Replace `<aap postgres pod>` with the name of your PostgreSQL pod.

```bash
$ oc exec -it <aap postgres pod> -- psql -d gateway -c "SHOW max_connections;"
```
