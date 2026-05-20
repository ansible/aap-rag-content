# 2. System requirements
## 2.7. PostgreSQL requirements
### 2.7.6. Enabling the hstore extension for the automation hub PostgreSQL database

The database migration script uses `hstore` fields to store information, therefore the `hstore` extension must be enabled in the automation hub PostgreSQL database.

This process is automatic when using the Ansible Automation Platform installer and a managed PostgreSQL server.

If the PostgreSQL database is external, you must enable the `hstore` extension in the automation hub PostgreSQL database manually before installation.

If the `hstore` extension is not enabled before installation, a failure raises during database migration.

**Procedure**

1. Check if the extension is available on the PostgreSQL server (automation hub database).

$ psql -d <automation hub database> -c "SELECT * FROM pg_available_extensions WHERE name='hstore'"

2. Where the default value for `<automation hub database>` is `automationhub`.

**Example output with `hstore` available**:

name  | default_version | installed_version |comment
------+-----------------+-------------------+---------------------------------------------------
hstore | 1.7           |                   | data type for storing sets of (key, value) pairs
(1 row)

**Example output with `hstore` not available**:

name | default_version | installed_version | comment
------+-----------------+-------------------+---------
(0 rows)

3. On a RHEL based server, the `hstore` extension is included in the `postgresql-contrib` RPM package, which is not installed automatically when installing the PostgreSQL server RPM package.

To install the RPM package, use the following command:

dnf install postgresql-contrib

4. Load the `hstore` PostgreSQL extension into the automation hub database with the following command:

$ psql -d <automation hub database> -c "CREATE EXTENSION hstore;"

In the following output, the `installed_version` field lists the `hstore` extension used, indicating that `hstore` is enabled.

name | default_version | installed_version | comment
-----+-----------------+-------------------+------------------------------------------------------
hstore  |     1.7      |       1.7         | data type for storing sets of (key, value) pairs
(1 row)

