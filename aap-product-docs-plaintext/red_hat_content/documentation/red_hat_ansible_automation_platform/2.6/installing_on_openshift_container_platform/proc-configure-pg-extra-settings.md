# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.1. Configuring platform gateway on Red Hat OpenShift Container Platform web console
### 5.1.5. Configuring custom PostgreSQL settings for Ansible Automation Platform




The `postgres_extra_settings` variable allows you to pass a list of custom _name: value_ pairs directly to the PostgreSQL configuration file `(/var/lib/pgsql/data/postgresql.conf)` within the database pod.

**Prerequisites**

- You have installed the Ansible Automation Platform Operator.


**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Go to **Operators → Installed Operators** .
1. Select your Ansible Automation Platform Operator deployment.
1. Select **All Instances** and go to your **Ansible Automation Platform** instance.
1. Click the ⋮ icon and then select **Edit Ansible Automation Platform** .
1. In the **YAML** view, locate the `    spec:` section
1. Add the `    database` section and the required settings under `    spec:` . The following example configures SSL ciphers and the maximum connections:


```
spec:      database:        postgres_extra_settings:          - name: max_connections            value: '1000'
```


1. ClickSave.


**Verification**

Inspect the PostgreSQL pod logs to verify the new settings.


Alternatively, you can run the following command to check the settings. Replace `&lt;aap postgres pod&gt;` with the name of your PostgreSQL pod.

+

```
$ oc exec -it &lt;aap postgres pod&gt; -- psql -d gateway -c "SHOW max_connections;"
```

