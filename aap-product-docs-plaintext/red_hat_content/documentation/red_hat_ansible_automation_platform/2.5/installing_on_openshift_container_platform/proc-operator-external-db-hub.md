# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.3. Configuring automation hub on Red Hat OpenShift Container Platform web console
### 5.3.3. Configuring an external database for automation hub on Red Hat Ansible Automation Platform Operator




For users who prefer to deploy Ansible Automation Platform with an external database, they can do so by configuring a secret with instance credentials and connection information, then applying it to their cluster using the `oc create` command.

By default, the Ansible Automation Platform Operator automatically creates and configures a managed PostgreSQL pod in the same namespace as your Ansible Automation Platform deployment.

You can choose to use an external database instead if you prefer to use a dedicated node to ensure dedicated resources or to manually manage backups, upgrades, or performance tweaks.

Note
The same external database (PostgreSQL instance) can be used for both automation hub, automation controller, and platform gateway as long as the database names are different. In other words, you can have multiple databases with different names inside a single PostgreSQL instance.



The following section outlines the steps to configure an external database for your automation hub on a Ansible Automation Platform Operator.

**Prerequisite**

The external database must be a PostgreSQL database that is the version supported by the current release of Ansible Automation Platform. The external postgres instance credentials and connection information will need to be stored in a secret, which will then be set on the automation hub spec.


Note
Ansible Automation Platform 2.5 supports PostgreSQL 15.



**Procedure**

1. Create a `    postgres_configuration_secret` YAML file, following the template below:


```
apiVersion: v1    kind: Secret    metadata:      name: external-postgres-configuration      namespace: &lt;target_namespace&gt;<span id="CO1-10"><!--Empty--></span><span class="callout">1</span>stringData:      host: "&lt;external_ip_or_url_resolvable_by_the_cluster&gt;"<span id="CO1-11"><!--Empty--></span><span class="callout">2</span>port: "&lt;external_port&gt;"<span id="CO1-12"><!--Empty--></span><span class="callout">3</span>database: "&lt;desired_database_name&gt;"      username: "&lt;username_to_connect_as&gt;"      password: "&lt;password_to_connect_with&gt;"<span id="CO1-13"><!--Empty--></span><span class="callout">4</span>sslmode: "prefer"<span id="CO1-14"><!--Empty--></span><span class="callout">5</span>type: "unmanaged"    type: Opaque
```


1. Namespace to create the secret in. This should be the same namespace you want to deploy to.
1. The resolvable hostname for your database node.
1. External port defaults to `        5432` .
1. Value for variable `        password` should not contain single or double quotes (', ") or backslashes (\) to avoid any issues during deployment, backup or restoration.
1. The variable `        sslmode` is valid for `        external` databases only. The allowed values are: `        <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">prefer</span></strong></span>` , `        <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">disable</span></strong></span>` , `        <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">allow</span></strong></span>` , `        <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">require</span></strong></span>` , `        <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">verify-ca</span></strong></span>` , and `        <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">verify-full</span></strong></span>` .

1. Apply `    external-postgres-configuration-secret.yml` to your cluster using the `    oc create` command.


```
$ oc create -f external-postgres-configuration-secret.yml
```


1. When creating your `    AutomationHub` custom resource object, specify the secret on your spec, following the example below:


```
apiVersion: automationhub.ansible.com/v1beta1    kind: AutomationHub    metadata:      name: hub-dev    spec:      postgres_configuration_secret: external-postgres-configuration
```




#### 5.3.3.1. Enabling the hstore extension for the automation hub PostgreSQL database




The database migration script uses `hstore` fields to store information, therefore the `hstore` extension must be enabled in the automation hub PostgreSQL database.

This process is automatic when using the Ansible Automation Platform installer and a managed PostgreSQL server.

If the PostgreSQL database is external, you must enable the `hstore` extension in the automation hub PostgreSQL database manually before installation.

If the `hstore` extension is not enabled before installation, a failure raises during database migration.

**Procedure**

1. Check if the extension is available on the PostgreSQL server (automation hub database).


```
$ psql -d &lt;automation hub database&gt; -c "SELECT * FROM pg_available_extensions WHERE name='hstore'"
```


1. Where the default value for `    &lt;automation hub database&gt;` is `    automationhub` .

**Example output with `    hstore` available** :


```
name  | default_version | installed_version |comment    ------+-----------------+-------------------+---------------------------------------------------     hstore | 1.7           |                   | data type for storing sets of (key, value) pairs    (1 row)
```

**Example output with `    hstore` not available** :


```
name | default_version | installed_version | comment    ------+-----------------+-------------------+---------    (0 rows)
```


1. On a RHEL based server, the `    hstore` extension is included in the `    postgresql-contrib` RPM package, which is not installed automatically when installing the PostgreSQL server RPM package.

To install the RPM package, use the following command:


```
dnf install postgresql-contrib
```


1. Load the `    hstore` PostgreSQL extension into the automation hub database with the following command:


```
$ psql -d &lt;automation hub database&gt; -c "CREATE EXTENSION hstore;"
```

In the following output, the `    installed_version` field lists the `    hstore` extension used, indicating that `    hstore` is enabled.


```
name | default_version | installed_version | comment    -----+-----------------+-------------------+------------------------------------------------------    hstore  |     1.7      |       1.7         | data type for storing sets of (key, value) pairs    (1 row)
```




