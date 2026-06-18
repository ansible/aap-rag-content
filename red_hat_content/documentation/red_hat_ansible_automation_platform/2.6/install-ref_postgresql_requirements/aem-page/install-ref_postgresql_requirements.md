+++
title = "PostgreSQL requirements - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_postgresql_requirements"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_platform_install_overview/", "Install RPM-based Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_postgresql_requirements/aem-page/install-ref_postgresql_requirements.html"
last_crumb = "PostgreSQL requirements"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "PostgreSQL requirements"
oversized = "false"
page_slug = "install-ref_postgresql_requirements"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-ref_postgresql_requirements"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_postgresql_requirements/toc/toc.json"
type = "aem-page"
+++

# PostgreSQL requirements

Red Hat Ansible Automation Platform requires external (customer supported) databases to have International Components for Unicode (ICU) support. PostgreSQL user passwords are hashed with SCRAM-SHA-256 secure hashing algorithm before storing in the database.

To determine if your automation controller instance has access to the database, you can do so with the command, `awx-manage check_db` command.

Note:

- Automation controller data is stored in the database. Database storage increases with the number of hosts managed, number of jobs run, number of facts stored in the fact cache, and number of tasks in any individual job. For example, a playbook runs every hour (24 times a day) across 250 hosts, with 20 tasks, stores over 800000 events in the database every week.
- If not enough space is reserved in the database, the old job runs and facts must be cleaned on a regular basis. You can clean up from the UI at **Automation Execution > Administration > Management Jobs**.

## Verify ICU support

To verify that your PostgreSQL instance has ICU support enabled, run the following query:

```sql
SELECT collname FROM pg_collation WHERE
  collprovider = 'i' AND collname ilike '%icu' LIMIT 5;
```
If the query returns at least one result, ICU support is available. If the query returns no results, your PostgreSQL instance was compiled without ICU support and cannot be used with Ansible Automation Platform.

## PostgreSQL Configurations

Optionally, you can configure the PostgreSQL database as separate nodes that are not managed by the Red Hat Ansible Automation Platform installer. When the Ansible Automation Platform installer manages the database server, it configures the server with defaults that are generally recommended for most workloads. For more information about the settings you can use to improve database performance, see [Tune the PostgreSQL database for optimal performance](/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_database_settings#ref-controller-database-settings "Improve the performance of automation controller, by configuring the following configuration parameters in the database:").

## Set up an external database

Use the following procedure to configure an external PostgreSQL compliant database for use with an Ansible Automation Platform component, for example automation controller, Event-Driven Ansible, automation hub, and platform gateway.

### About this task

Important:

- When using an external database with Ansible Automation Platform, you must create and maintain that database. Ensure that you clear your external database when uninstalling Ansible Automation Platform.
- Red Hat Ansible Automation Platform 2.6 requires the external (customer supported) databases to have International Components for Unicode (ICU) support.
- During configuration of an external database, you must check the external database coverage. For more information, see [Red Hat Ansible Automation Platform Database Scope of Coverage](https://access.redhat.com/articles/4010491).

### Procedure

1.  Connect to a PostgreSQL compliant database server with superuser privileges.

```
# psql -h <hostname> -U superuser -p 5432 -d postgres <password_for_user_superuser>
```

2.  Where the default value for <hostname> is **hostname**:
  

```
-h hostname
--host=hostname
```

3.  Specify the hostname of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the UNIX-domain socket.

```
-d dbname
--dbname=dbname
```

4.  Specify the name of the database to connect to. This is equal to specifying `dbname` as the first non-option argument on the command line. The `dbname` can be a connection string. If so, connection string parameters override any conflicting command line options.

```
-U username
--username=username
```

5.  Connect to the database as the user `username` instead of the default (you must have permission to do so).
6.  Create the user, database, and password with the `createDB` or `administrator` role assigned to the user. For further information, see [Database Roles](https://www.postgresql.org/docs/13/user-manag.html).
7.  Run the installation program. If you are using a PostgreSQL database, the database is owned by the connecting user and must have a `createDB` or administrator role assigned to it.
8.  Check that you can connect to the created database with the credentials provided in the inventory file.
9.  Check the permission of the user. The user should have the `createDB` or administrator role.
10.  After you create the PostgreSQL users and databases for each component, add the database credentials and host details in the inventory file under the [all:vars] group.

```yaml
# Automation controller
pg_host=data.example.com
pg_database=<database name>
pg_port=<port_number>
pg_username=<set your own>
pg_password=<set your own>

    # Platform gateway
automationgateway_pg_host=aap.example.org
automationgateway_pg_database=<set your own>
automationgateway_pg_port=<port_number>
automationgateway_pg_username=<set your own>
automationgateway_pg_password=<set your own>

    # Automation hub
automationhub_pg_host=data.example.com
automationhub_pg_database=<database_name>
automationhub_pg_port=<port_number>
automationhub_pg_username=<username>
automationhub_pg_password=<password>

    # Event-Driven Ansible
automationedacontroller_pg_host=data.example.com
automationedacontroller_pg_database=<database_name>
automationedacontroller_pg_port=<port_number>
automationedacontroller_pg_username=<username>
automationedacontroller_pg_password=<password>
```

## Enable mutual TLS (mTLS) authentication

Enable mutual TLS authentication to secure PostgreSQL database connections with certificate-based verification. This protects against unauthorized access and man-in-the-middle attacks while meeting enterprise security and compliance requirements.

### Procedure

 To configure each component’s database with mTLS authentication, add the following variables to your inventory file under the `[all:vars]` group and ensure each component has a different TLS certificate and key:

```yaml
# Automation controller
pgclient_sslcert=/path/to/awx.cert
pgclient_sslkey=/path/to/awx.key
pg_sslmode=verify-full or verify-ca

# Platform gateway
automationgateway_pgclient_sslcert=/path/to/gateway.cert
automationgateway_pgclient_sslkey=/path/to/gateway.key
automationgateway_pg_sslmode=verify-full or verify-ca

# Automation hub
automationhub_pgclient_sslcert=/path/to/pulp.cert
automationhub_pgclient_sslkey=/path/to/pulp.key
automationhub_pg_sslmode=verify-full or verify-ca

# Event-Driven Ansible
automationedacontroller_pgclient_sslcert=/path/to/eda.cert
automationedacontroller_pgclient_sslkey=/path/to/eda.key
automationedacontroller_pg_sslmode=verify-full or verify-ca
```

## Use custom TLS certificates

Configure the installer to use custom TLS certificates and keys for all services instead of the default self-signed ones by setting the required inventory variables for certificates and keys.

### Procedure

-  To replace these with your own custom certificate and key, set the following inventory file variables:
  

```yaml
aap_ca_cert_file=<path_to_ca_tls_certificate>
aap_ca_key_file=<path_to_ca_tls_key>
```

-  If any of your certificates are signed by a custom Certificate Authority (CA), then you must specify the Certificate Authority’s certificate by using the `custom_ca_cert` inventory file variable:
  

```yaml
custom_ca_cert=<path_to_custom_ca_certificate>
```
  Note:
      If you have more than one custom CA certificate, combine them into a single file, then reference the combined certificate with the `custom_ca_cert` inventory file variable.

## Receptor certificate considerations

When using a custom certificate for Receptor nodes, the certificate requires the `otherName` field specified in the Subject Alternative Name (SAN) of the certificate with the value `1.3.6.1.4.1.2312.19.1`.

Receptor does not support the usage of wildcard certificates. Additionally, each Receptor certificate must have the host FQDN specified in its SAN for TLS hostname validation to be correctly performed.

## Enable the hstore extension

The database migration script uses `hstore` fields to store information, therefore the `hstore` extension must be enabled in the automation hub PostgreSQL database.

### About this task

This process is automatic when using the Ansible Automation Platform installer and a managed PostgreSQL server.

If the PostgreSQL database is external, you must enable the `hstore` extension in the automation hub PostgreSQL database manually before installation.

If the `hstore` extension is not enabled before installation, a failure raises during database migration.

### Procedure

1.  Check if the extension is available on the PostgreSQL server (automation hub database).

```
$ psql -d <automation hub database> -c "SELECT * FROM pg_available_extensions WHERE name='hstore'"
```

2.  Where the default value for `<automation hub database>` is `automationhub`. **Example output with `hstore` available**:

```
name  | default_version | installed_version |comment
------+-----------------+-------------------+---------------------------------------------------
 hstore | 1.7           |                   | data type for storing sets of (key, value) pairs
(1 row)
```
    **Example output with `hstore` not available**:

```
 name | default_version | installed_version | comment
------+-----------------+-------------------+---------
(0 rows)
```

3.  On a RHEL based server, the `hstore` extension is included in the `postgresql-contrib` RPM package, which is not installed automatically when installing the PostgreSQL server RPM package. To install the RPM package, use the following command:

```
dnf install postgresql-contrib
```

4.  Load the `hstore` PostgreSQL extension into the automation hub database with the following command:
  

```
$ psql -d <automation hub database> -c "CREATE EXTENSION hstore;"
```
    In the following output, the `installed_version` field lists the `hstore` extension used, indicating that `hstore` is enabled.

```
name | default_version | installed_version | comment
-----+-----------------+-------------------+------------------------------------------------------
hstore  |     1.7      |       1.7         | data type for storing sets of (key, value) pairs
(1 row)
```

## Benchmark storage performance for the Ansible Automation Platform PostgreSQL database

Use the Flexible I/O Tester (FIO) tool to verify that your storage system meets minimum Ansible Automation Platform PostgreSQL database requirements. FIO benchmarks read and write IOPS performance to help you evaluate storage capabilities.

### Before you begin

- You have installed the Flexible I/O Tester (`fio`) storage performance benchmarking tool. To install `fio`, run the following command as the root user:

```
# yum -y install fio
```

- You have adequate disk space to store the `fio` test data log files. The examples shown in the procedure require at least 60GB disk space in the `/tmp` directory:


  * `numjobs` sets the number of jobs run by the command.
  * `size=10G` sets the file size generated by each job.

- You have adjusted the value of the `size` parameter. Adjusting this value reduces the amount of test data.

### About this task

### Procedure

1.  Run a random write test:
  

```
$ fio --name=write_iops --directory=/tmp --numjobs=3 --size=10G \
--time_based --runtime=60s --ramp_time=2s --ioengine=libaio --direct=1 \
--verify=0 --bs=4K --iodepth=64 --rw=randwrite \
--group_reporting=1 > /tmp/fio_benchmark_write_iops.log \
2>> /tmp/fio_write_iops_error.log
```

2.  Run a random read test:
  

```
$ fio --name=read_iops --directory=/tmp \
--numjobs=3 --size=10G --time_based --runtime=60s --ramp_time=2s \
--ioengine=libaio --direct=1 --verify=0 --bs=4K --iodepth=64 --rw=randread \
--group_reporting=1 > /tmp/fio_benchmark_read_iops.log \
2>> /tmp/fio_read_iops_error.log
```

3.  Review the results:
      In the log files written by the benchmark commands, search for the line beginning with `iops`. This line shows the minimum, maximum, and average values for the test.

    The following example shows the line in the log file for the random read test:

```
$ cat /tmp/fio_benchmark_read_iops.log
read_iops: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
[…]
   iops        : min=50879, max=61603, avg=56221.33, stdev=679.97, samples=360
[…]
```
  Note:
      The above is a baseline to help evaluate the best case performance on your systems. Systems can and will change and performance may vary depending on what else is happening on your systems, storage or network at the time of testing. You must review, monitor, and revisit the log files according to your own business requirements, application workloads, and new demands.
