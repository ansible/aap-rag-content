+++
title = "Tune the PostgreSQL database for optimal performance - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_database_settings"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_database_settings/", "Tune the PostgreSQL database for optimal performance"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_database_settings/aem-page/optimize-ref_controller_database_settings.html"
last_crumb = "Tune the PostgreSQL database for optimal performance"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Tune the PostgreSQL database for optimal performance"
oversized = "false"
page_slug = "optimize-ref_controller_database_settings"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_database_settings"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_database_settings/toc/toc.json"
type = "aem-page"
+++

# Tune the PostgreSQL database for optimal performance

Improve the performance of automation controller, by configuring the following configuration parameters in the database:

 **Maintenance**

The `VACUUM` and `ANALYZE` tasks are important maintenance activities that can impact performance. In normal PostgreSQL operation, tuples that are deleted or obsoleted by an update are not physically removed from their table; they remain present until a `VACUUM` is done. Therefore it’s necessary to do VACUUM periodically, especially on frequently-updated tables. `ANALYZE` collects statistics about the contents of tables in the database, and stores the results in the `pg_statistic` system catalog. Subsequently, the query planner uses these statistics to help determine the most efficient execution plans for queries. The autovacuuming PostgreSQL configuration parameter automates the execution of `VACUUM` and `ANALYZE` commands. Setting autovacuuming to **true** is a good practice. However, autovacuuming will not occur if there is never any idle time on the database. If it is observed that autovacuuming is not sufficiently cleaning up space on the database disk, then scheduling specific vacuum tasks during specific maintenance windows can be a solution.

 **Configuration parameters**

To improve the performance of the PostgreSQL server, configure the following *Grand Unified Configuration* (GUC) parameters that manage database memory. You can find these parameters inside the `$PDATA` directory in the `postgresql.conf` file, which manages the configurations of the database server.

- `shared_buffers`: determines how much memory is dedicated to the server for caching data. The default value for this parameter is 128 MB. When you modify this value, you must set it between 15% and 25% of the machine’s total RAM. Note:
      If you are compiling Postgres against OpenSSL 3.2, your system regresses to remove the parameter for User during startup. You can rectify this by using the BIO_get_app_data call instead of open_get_data. Only an administrator can make these changes, but it impacts all users connected to the PostgreSQL database. f you update your systems without the OpenSSL patch, you are not impacted, and you do not need to take action.

  Note:
      You must restart the database server after changing the value for `shared_buffers`.

  Warning:
      If you are compiling Postgres against OpenSSL 3.2, your system regresses to remove the parameter for User during startup. You can rectify this by using the BIO_get_app_data call instead of open_get_data. Only an administrator can make these changes, but it impacts all users connected to the PostgreSQL database.

    If you update your systems without the OpenSSL patch, you are not impacted, and you do not need to take action.

- `work_mem`: provides the amount of memory to be used by internal sort operations and hash tables before disk-swapping. Sort operations are used for order by, distinct, and merge join operations. Hash tables are used in hash joins and hash-based aggregation. The default value for this parameter is 4 MB. Setting the correct value of the `work_mem` parameter improves the speed of a search by reducing disk-swapping.   * Use the following formula to calculate the optimal value of the `work_mem` parameter for the database server:

```
Total RAM * 0.25 / max_connections
```
    Note:
    Setting a large `work_mem` can cause the PostgreSQL server to go out of memory (OOM) if there are too many open connections to the database.

- `max_connections`: specifies the maximum number of concurrent connections to the database server.
- `maintenance_work_mem`: provides the maximum amount of memory to be used by maintenance operations, such as vacuum, create index, and alter table add foreign key operations. The default value for this parameter is 64 MB. Use the following equation to calculate a value for this parameter:

```
Total RAM * 0.05
```
  Note:
      Set `maintenance_work_mem` higher than `work_mem` to improve performance for vacuuming.

## Encrypt plain text passwords in automation controller configuration files

Plain text passwords in automation controller configuration files pose a potential security risk.

Configuration files are kept in the /etc/tower/conf.d/ folder. Files used to reach the database, for example, save passwords without encryption. This means that anyone who can read this folder can see the passwords clearly.

While permissions protect these folders, some security reports say this protection is good inadequate. The fix is to encrypt each of these passwords separately.

## Encrypt the PostgreSQL password

Learn how to encrypt the PostgreSQL password used by automation controller for database connections.

### About this task

Perform the following steps on each node in the cluster:

### Procedure

1.  Edit `/etc/tower/conf.d/postgres.py` using:
  

```
$ vim /etc/tower/conf.d/postgres.py
```

2.  Add the following line to the top of the file.

```
from awx.main.utils import decrypt_value, get_encryption_key
```

3.  Remove the password value listed after 'PASSWORD': and replace it with the following line, replacing the supplied value of `$encrytpted..` with your own hash value:
  

```
decrypt_value(get_encryption_key('value'),'$encrypted$AESCBC$Z0FBQUFBQmNONU9BbGQ1VjJyNDJRVTRKaFRIR09Ib2U5TGdaYVRfcXFXRjlmdmpZNjdoZVpEZ21QRWViMmNDOGJaM0dPeHN2b194NUxvQ1M5X3dSc1gxQ29TdDBKRkljWHc9PQ=='),
```
  Note:
      The hash value in this step is the output value of `postgres_secret`.

4.  The full `postgres.py` resembles the following:
  

```
# Ansible Automation platform controller database settings. from awx.main.utils import decrypt_value, get_encryption_key DATABASES = { 'default': { 'ATOMIC_REQUESTS': True, 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'awx', 'USER': 'awx', 'PASSWORD': decrypt_value(get_encryption_key('value'),'$encrypted$AESCBC$Z0FBQUFBQmNONU9BbGQ1VjJyNDJRVTRKaFRIR09Ib2U5TGdaYVRfcXFXRjlmdmpZNjdoZVpEZ21QRWViMmNDOGJaM0dPeHN2b194NUxvQ1M5X3dSc1gxQ29TdDBKRkljWHc9PQ=='), 'HOST': '127.0.0.1', 'PORT': 5432, } }+
```
