# 5. Advanced containerized deployment
## 5.6. Configuring an external (customer provided) PostgreSQL database
### 5.6.3. Enabling the hstore extension for the automation hub PostgreSQL database




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




