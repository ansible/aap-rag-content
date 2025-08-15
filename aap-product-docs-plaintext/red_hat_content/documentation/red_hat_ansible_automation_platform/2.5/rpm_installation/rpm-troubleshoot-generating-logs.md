# 6. Troubleshooting RPM installation of Ansible Automation Platform
## 6.1. Gathering Ansible Automation Platform logs




With the `sos` utility, you can collect configuration, diagnostic, and troubleshooting data, and provide those files to Red Hat Technical Support. An `sos` report is a common starting point for Red Hat technical support engineers when performing analysis of a service request for the Ansible Automation Platform.

As part of the troubleshooting with Red Hat Support, you can collect the `sos` report for each node in your RPM-based installation of Ansible Automation Platform using the installation inventory and the installation program.

**Procedure**

1. Access the installation program folder with the inventory file and run the installation program setup script the following command:

`    $ ./setup.sh -s`

With this command, you can connect to each node present in the inventory, install the `    sos` tool, and generate new logs.

Note
If you are running the setup as a non-root user with sudo privileges, you can use the following command:


```
$ ANSIBLE_BECOME_METHOD='sudo'    ANSIBLE_BECOME=True ./setup.sh -s
```




1.  _Optional_ : If required, change the location of the `    sos` report files.

The `    sos` report files are copied to the `    /tmp` folder for the current server. To change the location, specify the new location by using the following command:


```
$ ./setup.sh -e 'target_sos_directory=/path/to/files' -s
```

Where `    target_sos_directory=/path/to/files` is used to specify the destination directory where the `    sos` report will be saved. In this case, the `    sos` report is stored in the directory `    /path/to/files` .


1. Gather the files described on the playbook output and share with the support engineer or directly upload the `    sos` report to Red Hat.

To create an `    sos` report with additional information or directly upload the data to Red Hat, use the following command:


```
$ ./setup.sh -e 'case_number=0000000' -e 'clean=true' -e 'upload=true' -s
```


<span id="idm140681245848336"></span>
**Table 6.1. Parameter Reference Table**

| Parameter | Description | Default value |
| --- | --- | --- |
|  `case_number` | Specifies the support case number that you want. | - |
|  `clean` | Obfuscates sensitive data that might be present on the `sos` report. |  `false` |
|  `upload` | Automatically uploads the `sos` report data to Red Hat. |  `false` |







To know more about the `sos` report tool, see the KCS article: [What is an sos report and how to create one in Red Hat Enterprise Linux?](https://access.redhat.com/solutions/3592)

# Appendix A. Inventory file variables




The following tables contain information about the variables used in Ansible Automation Platform’s installation `inventory` files. The tables include the variables that you can use for RPM-based installation and container-based installation.

## A.1. Ansible variables




The following variables control how Ansible Automation Platform interacts with remote hosts.


<span id="idm140681243208176"></span>
**Table A.1. Ansible variables**

| Variable | Description |
| --- | --- |
|  `ansible_connection` | The connection plugin used for the task on the target host. This can be the name of any Ansible connection plugin.

SSH protocol types are `smart` , `ssh` , or `paramiko` . You can also use `local` to run tasks on the control node itself.

Default = `smart` |
|  `ansible_host` | The IP address or name of the target host to use instead of `inventory_hostname` . |
|  `ansible_password` | The password to authenticate to the host.

Do not store this variable in plain text. Always use a vault. For more information, see [Keep vaulted variables safely visible](https://docs.ansible.com/ansible-core/devel/tips_tricks/ansible_tips_tricks.html#keep-vaulted-variables-safely-visible) . |
|  `ansible_port` | The connection port number.

The default for SSH is `22` . |
|  `ansible_scp_extra_args` | This setting is always appended to the default `scp` command line. |
|  `ansible_sftp_extra_args` | This setting is always appended to the default `sftp` command line. |
|  `ansible_shell_executable` | This sets the shell that the Ansible controller uses on the target machine and overrides the executable in `ansible.cfg` which defaults to `/bin/sh` . |
|  `ansible_shell_type` | The shell type of the target system.

Do not use this setting unless you have set the `ansible_shell_executable` to a non-Bourne (sh) compatible shell. By default commands are formatted using sh-style syntax. Setting this to `csh` or `fish` causes commands executed on target systems to follow the syntax of those shells instead. |
|  `ansible_ssh_common_args` | This setting is always appended to the default command line for `sftp` , `scp` , and `ssh` . Useful to configure a `ProxyCommand` for a certain host or group. |
|  `ansible_ssh_executable` | This setting overrides the default behavior to use the system `ssh` . This can override the `ssh_executable` setting in `ansible.cfg` . |
|  `ansible_ssh_extra_args` | This setting is always appended to the default `ssh` command line. |
|  `ansible_ssh_pipelining` | Determines if SSH `pipelining` is used.

This can override the `pipelining` setting in `ansible.cfg` . If using SSH key-based authentication, the key must be managed by an SSH agent. |
|  `ansible_ssh_private_key_file` | Private key file used by SSH.

Useful if using multiple keys and you do not want to use an SSH agent. |
|  `ansible_user` | The user name to use when connecting to the host.

Do not change this variable unless `/bin/sh` is not installed on the target machine or cannot be run from sudo. |
|  `inventory_hostname` | This variable takes the hostname of the machine from the inventory script or the Ansible configuration file. You cannot set the value of this variable. Because the value is taken from the configuration file, the actual runtime hostname value can vary from what is returned by this variable. |




**Additional resources**

-  [Ansible.Builtin](https://docs.ansible.com/ansible-core/devel/collections/ansible/builtin/index.html)
-  [Ansible Configuration Settings](https://docs.ansible.com/ansible-core/devel/reference_appendices/config.html)


## A.2. Automation hub variables




Inventory file variables for automation hub.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `automationhub_admin_password` |  `hub_admin_password` | Automation hub administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/` , `”` , or `@` . | Required |  |
|  `automationhub_api_token` |  | Set the existing token for the installation program. For example, a regenerated token in the automation hub UI will invalidate an existing token. Use this variable to set that token in the installation program the next time you run the installation program. | Optional |  |
|  `automationhub_auto_sign_collections` |  `hub_collection_auto_sign` | If a collection signing service is enabled, collections are not signed automatically by default. Set this variable to `true` to sign collections by default. | Optional |  `false` |
|  `automationhub_backup_collections` |  | Ansible automation hub provides artifacts in `/var/lib/pulp` . These artifacts are automatically backed up by default. Set this variable to `false` to prevent backup or restore of `/var/lib/pulp` . | Optional |  `true` |
|  `automationhub_client_max_body_size` |  `hub_nginx_client_max_body_size` | Maximum allowed size for data sent to automation hub through NGINX. | Optional |  `20m` |
|  `automationhub_collection_download_count` |  | Denote whether or not the collection download count should be displayed in the UI. | Optional |  `false` |
|  `automationhub_collection_seed_repository` |  | Controls the type of content to upload when `hub_seed_collections` is set to `true` . Valid options include: `certified` , `validated` | Optional | Both certified and validated are enabled by default. |
|  `automationhub_collection_signing_service_key` |  `hub_collection_signing_key` | Path to the collection signing key file. | Required if a collection signing service is enabled. |  |
|  `automationhub_container_repair_media_type` |  | Denote whether or not to run the command `pulpcore-manager container-repair-media-type` .
Valid options include: `true` , `false` , `auto` | Optional |  `auto` |
|  `automationhub_container_signing_service_key` |  `hub_container_signing_key` | Path to the container signing key file. | Required if a container signing service is enabled. |  |
|  `automationhub_create_default_collection_signing_service` |  `hub_collection_signing` | Set this variable to `true` to enable a collection signing service. | Optional |  `false` |
|  `automationhub_create_default_container_signing_service` |  `hub_container_signing` | Set this variable to `true` to enable a container signing service. | Optional |  `false` |
|  `automationhub_disable_hsts` |  `hub_nginx_disable_hsts` | Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for automation hub. Set this variable to `true` to disable HSTS. | Optional |  `false` |
|  `automationhub_disable_https` |  `hub_nginx_disable_https` | Controls whether HTTPS is enabled or disabled for automation hub. Set this variable to `true` to disable HTTPS. | Optional |  `false` |
|  `automationhub_enable_api_access_log` |  | Controls whether logging is enabled or disabled at `/var/log/galaxy_api_access.log` . The file logs all user actions made to the platform, including username and IP address. Set this variable to `true` to enable this logging. | Optional |  `false` |
|  `automationhub_enable_unauthenticated_collection_access` |  | Controls whether read-only access is enabled or disabled for unauthorized users viewing collections or namespaces for automation hub. Set this variable to `true` to enable read-only access. | Optional |  `false` |
|  `automationhub_enable_unauthenticated_collection_download` |  | Controls whether or not unauthorized users can download read-only collections from automation hub. Set this variable to `true` to enable download of read-only collections. | Optional |  `false` |
|  `automationhub_firewalld_zone` |  `hub_firewall_zone` | The firewall zone where automation hub related firewall rules are applied. This controls which networks can access automation hub based on the zone’s trust level. | Optional | RPM = no default set. Container = `public` . |
|  `automationhub_force_change_admin_password` |  | Denote whether or not to require the change of the default administrator password for automation hub during installation.
Set to `true` to require the user to change the default administrator password during installation. | Optional |  `false` |
|  `automationhub_importer_settings` |  `hub_galaxy_importer` | Dictionary of settings to pass to the `galaxy-importer.cfg` configuration file. These settings control how the `galaxy-importer` service processes and validates Ansible content. Example values include: `ansible-doc` , `ansible-lint` , and `flake8` . | Optional |  |
|  `automationhub_nginx_tls_files_remote` |  | Denote whether the web certificate sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `automationhub_tls_files_remote` . |
|  `automationhub_pg_cert_auth` |  `hub_pg_cert_auth` | Controls whether client certificate authentication is enabled or disabled on the automation hub PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | Optional |  `false` |
|  `automationhub_pg_database` |  `hub_pg_database` | Name of the PostgreSQL database used by automation hub. | Optional | RPM = `automationhub` . Container = `pulp` |
|  `automationhub_pg_host` |  `hub_pg_host` | Hostname of the PostgreSQL database used by automation hub. | Required | RPM = `127.0.0.1` . Container = no default. |
|  `automationhub_pg_password` |  `hub_pg_password` | Password for the automation hub PostgreSQL database user. Use of special characters for this variable is limited. The `!` , `#` , `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | Optional |  |
|  `automationhub_pg_port` |  `hub_pg_port` | Port number for the PostgreSQL database used by automation hub. | Optional |  `5432` |
|  `automationhub_pg_sslmode` |  `hub_pg_sslmode` | Controls the SSL/TLS mode to use when automation hub connects to the PostgreSQL database. Valid options include `verify-full` , `verify-ca` , `require` , `prefer` , `allow` , `disable` . | Optional |  `prefer` |
|  `automationhub_pg_username` |  `hub_pg_username` | Username for the automation hub PostgreSQL database user. | Optional | RPM = `automationhub` . Container = `pulp` . |
|  `automationhub_pgclient_sslcert` |  `hub_pg_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file for automation hub. | Required if using client certificate authentication. |  |
|  `automationhub_pgclient_sslkey` |  `hub_pg_tls_key` | Path to the PostgreSQL SSL/TLS key file for automation hub. | Required if using client certificate authentication. |  |
|  `automationhub_pgclient_tls_files_remote` |  | Denote whether the PostgreSQL client certificate sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `automationhub_tls_files_remote` . |
|  `automationhub_require_content_approval` |  | Controls whether content signing is enabled or disabled for automation hub. By default when you upload collections to automation hub, an administrator must approve it before they are made available to users. To disable the content approval flow, set the variable to `false` . | Optional |  `true` |
|  `automationhub_restore_signing_keys` |  | Controls whether or not existing signing keys should be restored from a backup. Set to `false` to disable restoration of existing signing keys. | Optional |  `true` |
|  `automationhub_seed_collections` |  `hub_seed_collections` | Controls whether or not pre-loading of collections is enabled. When you run the bundle installer, validated content is uploaded to the `validated` repository, and certified content is uploaded to the `rh-certified` repository. By default, certified content and validated content are both uploaded. If you do not want to pre-load content, set this variable to `false` . For the RPM-based installer, if you only want one type of content, set this variable to `true` and set the `automationhub_collection_seed_repository` variable to the type of content you want to include. | Optional |  `true` |
|  `automationhub_ssl_cert` |  `hub_tls_cert` | Path to the SSL/TLS certificate file for automation hub. | Optional |  |
|  `automationhub_ssl_key` |  `hub_tls_key` | Path to the SSL/TLS key file for automation hub. | Optional |  |
|  `automationhub_tls_files_remote` |  `hub_tls_remote` | Denote whether the automation hub provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationhub_use_archive_compression` |  `hub_use_archive_compression` | Controls whether archive compression is enabled or disabled for automation hub. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
|  `automationhub_use_db_compression` |  `hub_use_db_compression` | Controls whether database compression is enabled or disabled for automation hub. You can control this functionality globally by using `use_db_compression` . | Optional |  `true` |
|  `automationhub_user_headers` |  `hub_nginx_user_headers` | List of additional NGINX headers to add to automation hub’s NGINX configuration. | Optional |  `[]` |
|  `generate_automationhub_token` |  | Controls whether or not a token is generated for automation hub during installation. By default, a token is automatically generated during a fresh installation. If set to `true` , a token is regenerated during installation. | Optional |  `false` |
|  |  `hub_extra_settings` | Defines additional settings for use by automation hub during installation.

For example:

```
hub_extra_settings:
- setting: REDIRECT_IS_HTTPS
value: True
``` | Optional |  `[]` |
|  `nginx_hsts_max_age` |  `hub_nginx_hsts_max_age` | Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for automation hub. | Optional |  `63072000` |
|  `pulp_secret` |  `hub_secret_key` | Secret key value used by automation hub to sign and encrypt data. | Optional |  |
|  |  `hub_azure_account_key` | Azure blob storage account key. | Required if using an Azure blob storage backend. |  |
|  |  `hub_azure_account_name` | Account name associated with the Azure blob storage. | Required when using an Azure blob storage backend. |  |
|  |  `hub_azure_container` | Name of the Azure blob storage container. | Optional |  `pulp` |
|  |  `hub_azure_extra_settings` | Defines extra parameters for the Azure blob storage backend. For more information about the list of parameters, see [django-storages documentation - Azure Storage](https://django-storages.readthedocs.io/en/latest/backends/azure.html#settings) . | Optional |  `{}` |
|  |  `hub_collection_signing_pass` | Password for the automation content collection signing service. | Required if the collection signing service is protected by a passphrase. |  |
|  |  `hub_collection_signing_service` | Service for signing collections. | Optional |  `ansible-default` |
|  |  `hub_container_signing_pass` | Password for the automation content container signing service. | Required if the container signing service is protected by a passphrase. |  |
|  |  `hub_container_signing_service` | Service for signing containers. | Optional |  `container-default` |
|  |  `hub_nginx_http_port` | Port number that automation hub listens on for HTTP requests. | Optional |  `8081` |
|  |  `hub_nginx_https_port` | Port number that automation hub listens on for HTTPS requests. | Optional |  `8444` |
|  `nginx_tls_protocols` |  `hub_nginx_https_protocols` | Protocols that automation hub will support when handling HTTPS traffic. | Optional | RPM = `[TLSv1.2]` . Container = `[TLSv1.2, TLSv1.3]` . |
|  |  `hub_pg_socket` | UNIX socket used by automation hub to connect to the PostgreSQL database. | Optional |  |
|  |  `hub_s3_access_key` | AWS S3 access key. | Required if using an AWS S3 storage backend. |  |
|  |  `hub_s3_bucket_name` | Name of the AWS S3 storage bucket. | Optional |  `pulp` |
|  |  `hub_s3_extra_settings` | Used to define extra parameters for the AWS S3 storage backend. For more information about the list of parameters, see [django-storages documentation - Amazon S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings) . | Optional |  `{}` |
|  |  `hub_s3_secret_key` | AWS S3 secret key. | Required if using an AWS S3 storage backend. |  |
|  |  `hub_shared_data_mount_opts` | Mount options for the Network File System (NFS) share. | Optional |  `rw,sync,hard` |
|  |  `hub_shared_data_path` | Path to the Network File System (NFS) share with read, write, and execute (RWX) access. The value must match the format `host:dir` , for example `nfs-server.example.com:/exports/hub` . | Required if installing more than one instance of automation hub with a `file` storage backend. When installing a single instance of automation hub, it is optional. |  |
|  |  `hub_storage_backend` | Automation hub storage backend type. Possible values include: `azure` , `file` , `s3` . | Optional |  `file` |
|  |  `hub_workers` | Number of automation hub workers. | Optional |  `2` |


## A.3. Automation controller variables




Inventory file variables for automation controller.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `admin_email` |  `controller_admin_email` | Email address used by Django for the admin user for automation controller. | Optional |  `admin@example.com` |
|  `admin_password` |  `controller_admin_password` | Automation controller administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/` , `”` , or `@` . | Required |  |
|  `admin_username` |  `controller_admin_user` | Username used to identify and create the administrator user in automation controller. | Optional |  `admin` |
|  `automationcontroller_client_max_body_size` |  `controller_nginx_client_max_body_size` | Maximum allowed size for data sent to automation controller through NGINX. | Optional |  `5m` |
|  `automationcontroller_use_archive_compression` |  `controller_use_archive_compression` | Controls whether archive compression is enabled or disabled for automation controller. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
|  `automationcontroller_use_db_compression` |  `controller_use_db_compression` | Controls whether database compression is enabled or disabled for automation controller. You can control this functionality globally by using `use_db_compression` . | Optional |  `true` |
|  `awx_pg_cert_auth` |  `controller_pg_cert_auth` | Controls whether client certificate authentication is enabled or disabled on the automation controller PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | Optional |  `false` |
|  `controller_firewalld_zone` |  `controller_firewall_zone` | The firewall zone where automation controller related firewall rules are applied. This controls which networks can access automation controller based on the zone’s trust level. | Optional |  `public` |
|  `controller_nginx_tls_files_remote` |  | Denote whether the web certificate sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `controller_tls_files_remote` . |
|  `controller_pgclient_tls_files_remote` |  | Denote whether the PostgreSQL client certificate sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `controller_tls_files_remote` . |
|  `controller_tls_files_remote` |  `controller_tls_remote` | Denote whether the automation controller provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `nginx_disable_hsts` |  `controller_nginx_disable_hsts` | Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for automation controller. Set this variable to `true` to disable HSTS. | Optional |  `false` |
|  `nginx_disable_https` |  `controller_nginx_disable_https` | Controls whether HTTPS is enabled or disabled for automation controller. Set this variable to `true` to disable HTTPS. | Optional |  `false` |
|  `nginx_hsts_max_age` |  `controller_nginx_hsts_max_age` | Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for automation controller. | Optional |  `63072000` |
|  `nginx_http_port` |  `controller_nginx_http_port` | Port number that automation controller listens on for HTTP requests. | Optional | RPM = `80` . Container = `8080` |
|  `nginx_https_port` |  `controller_nginx_https_port` | Port number that automation controller listens on for HTTPS requests. | Optional | RPM = `443` . Container = `8443` |
|  `nginx_tls_protocols` |  `controller_nginx_https_protocols` | Protocols that automation controller supports when handling HTTPS traffic. | Optional | RPM = `[TLSv1.2]` . Container = `[TLSv1.2, TLSv1.3]` |
|  `nginx_user_headers` |  `controller_nginx_user_headers` | List of additional NGINX headers to add to automation controller’s NGINX configuration. | Optional |  `[]` |
|  |  `controller_create_preload_data` | Controls whether or not to create preloaded content during installation. | Optional |  `true` |
|  `node_state` |  | The status of a node or group of nodes. Valid options include `active` , `deprovision` to remove a node from a cluster, or `iso_migrate` to migrate a legacy isolated node to an execution node. | Optional |  `active` |
|  `node_type` | See `receptor_type` for the container equivalent variable. | For the `[automationcontroller]` group the two options are:

-  `    node_type=control` - The node only runs project and inventory updates, but not regular jobs.
-  `    node_type=hybrid` - The node runs everything.


For the `[execution_nodes]` group the two options are:

-  `    node_type=hop` - The node forwards jobs to an execution node.
-  `    node_type=execution` - The node can run jobs. | Optional | For `[automationcontroller]` = `hybrid` , for `[execution_nodes]` = `execution` |
|  `peers` | See `receptor_peers` for the container equivalent variable. | Used to indicate which nodes a specific host or group connects to. Wherever this variable is defined, an outbound connection to the specific host or group is established. This variable can be a comma-separated list of hosts and groups from the inventory. This is resolved into a set of hosts that is used to construct the `receptor.conf` file. | Optional |  |
|  `pg_database` |  `controller_pg_database` | Name of the PostgreSQL database used by automation controller. | Optional |  `awx` |
|  `pg_host` |  `controller_pg_host` | Hostname of the PostgreSQL database used by automation controller. | Required |  |
|  `pg_password` |  `controller_pg_password` | Password for the automation controller PostgreSQL database user. Use of special characters for this variable is limited. The `!` , `#` , `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | Required if not using client certificate authentication. |  |
|  `pg_port` |  `controller_pg_port` | Port number for the PostgreSQL database used by automation controller. | Optional |  `5432` |
|  `pg_sslmode` |  `controller_pg_sslmode` | Controls the SSL/TLS mode to use when automation controller connects to the PostgreSQL database. Valid options include `verify-full` , `verify-ca` , `require` , `prefer` , `allow` , `disable` . | Optional |  `prefer` |
|  `pg_username` |  `controller_pg_username` | Username for the automation controller PostgreSQL database user. | Optional |  `awx` |
|  `pgclient_sslcert` |  `controller_pg_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file for automation controller. | Required if using client certificate authentication. |  |
|  `pgclient_sslkey` |  `controller_pg_tls_key` | Path to the PostgreSQL SSL/TLS key file for automation controller. | Required if using client certificate authentication. |  |
|  `precreate_partition_hours` |  | Number of hours worth of events table partitions to pre-create before starting a backup to avoid `pg_dump` locks. | Optional | 3 |
|  `uwsgi_listen_queue_size` |  `controller_uwsgi_listen_queue_size` | Number of requests `uwsgi` allows in the queue on automation controller until `uwsgi_processes` can serve them. | Optional |  `2048` |
|  `web_server_ssl_cert` |  `controller_tls_cert` | Path to the SSL/TLS certificate file for automation controller. | Optional |  |
|  `web_server_ssl_key` |  `controller_tls_key` | Path to the SSL/TLS key file for automation controller. | Optional |  |
|  |  `controller_event_workers` | Number of event workers that handle job-related events inside automation controller. | Optional |  `4` |
|  |  `controller_extra_settings` | Defines additional settings for use by automation controller during installation.

For example:

```
controller_extra_settings:
- setting: USE_X_FORWARDED_HOST
value: true
``` | Optional |  `[]` |
|  |  `controller_license_file` | Path to the automation controller license file. |  |  |
|  |  `controller_percent_memory_capacity` | Memory allocation for automation controller. | Optional |  `1.0` (allocates 100% of the total system memory to automation controller) |
|  |  `controller_pg_socket` | UNIX socket used by automation controller to connect to the PostgreSQL database. | Optional |  |
|  |  `controller_secret_key` | Secret key value used by automation controller to sign and encrypt data. | Optional |  |


## A.4. Database variables




Inventory file variables for the database used with Ansible Automation Platform.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `install_pg_port` |  `postgresql_port` | Port number for the PostgreSQL database. | Optional |  `5432` |
|  `postgres_firewalld_zone` |  `postgresql_firewall_zone` | The firewall zone where PostgreSQL related firewall rules are applied. This controls which networks can access PostgreSQL based on the zone’s trust level. | Optional | RPM = no default set. Container = `public` . |
|  `postgres_max_connections` |  `postgresql_max_connections` | Maximum number of concurrent connections to the database if you are using an installer-managed database. For more information see [PostgreSQL database configuration and maintenance for automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-improving-performance#ref-controller-database-settings) . | Optional |  `1024` |
|  `postgres_ssl_cert` |  `postgresql_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file. | Optional |  |
|  `postgres_ssl_key` |  `postgresql_tls_key` | Path to the PostgreSQL SSL/TLS key file. | Optional |  |
|  `postgres_use_ssl` |  `postgresql_disable_tls` | Controls whether SSL/TLS is enabled or disabled for the PostgreSQL database. | Optional |  `false` |
|  |  `postgresql_admin_database` | Database name used for connections to the PostgreSQL database server. | Optional |  `postgres` |
|  |  `postgresql_admin_password` | Password for the PostgreSQL admin user. When used, the installation program creates each component’s database and credentials. | Required if using `postgresql_admin_username` . |  |
|  |  `postgresql_admin_username` | Username for the PostgreSQL admin user. When used, the installation program creates each component’s database and credentials. | Optional |  `postgres` |
|  |  `postgresql_effective_cache_size` | Memory allocation available (in MB) for caching data. | Optional |  |
|  |  `postgresql_keep_databases` | Controls whether or not to keep databases during uninstall. This variable applies to databases managed by the installation program only, and not external (customer-managed) databases. Set to `true` to keep databases during uninstall. | Optional |  `false` |
|  |  `postgresql_log_destination` | Destination for server log output. | Optional |  `/dev/stderr` |
|  |  `postgresql_password_encryption` | The algorithm for encrypting passwords. | Optional |  `scram-sha-256` |
|  |  `postgresql_shared_buffers` | Memory allocation (in MB) for shared memory buffers. | Optional |  |
|  |  `postgresql_tls_remote` | Denote whether the PostgreSQL provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  |  `postgresql_use_archive_compression` | Controls whether archive compression is enabled or disabled for PostgreSQL. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |


## A.5. Event-Driven Ansible controller variables




Inventory file variables for Event-Driven Ansible controller.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `automationedacontroller_activation_workers` |  `eda_activation_workers` | Number of workers used for ansible-rulebook activation pods in Event-Driven Ansible. | Optional | RPM = (# of cores or threads) * 2 + 1. Container = `2` |
|  `automationedacontroller_admin_email` |  `eda_admin_email` | Email address used by Django for the admin user for Event-Driven Ansible. | Optional |  `admin@example.com` |
|  `automationedacontroller_admin_password` |  `eda_admin_password` | Event-Driven Ansible administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/` , `”` , or `@` . | Required |  |
|  `automationedacontroller_admin_username` |  `eda_admin_user` | Username used to identify and create the administrator user in Event-Driven Ansible. | Optional |  `admin` |
|  `automationedacontroller_backend_gunicorn_workers` |  | Number of workers for handling the API served through Gunicorn on worker nodes. | Optional |  `2` |
|  `automationedacontroller_cache_tls_files_remote` |  | Denote whether the cache cert sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationedacontroller_client_regen_cert` |  | Controls whether or not to regenerate Event-Driven Ansible client certificates for the platform cache. Set to `true` to regenerate Event-Driven Ansible client certificates. | Optional |  `false` |
|  `automationedacontroller_default_workers` |  `eda_workers` | Number of workers used in Event-Driven Ansible for application work. | Optional | Number of cores or threads |
|  `automationedacontroller_disable_hsts` |  `eda_nginx_disable_hsts` | Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for Event-Driven Ansible. Set this variable to `true` to disable HSTS. | Optional |  `false` |
|  `automationedacontroller_disable_https` |  `eda_nginx_disable_https` | Controls whether HTTPS is enabled or disabled for Event-Driven Ansible. Set this variable to `true` to disable HTTPS. | Optional |  `false` |
|  `automationedacontroller_event_stream_path` |  `eda_event_stream_prefix_path` | API prefix path used for Event-Driven Ansible event-stream through platform gateway. | Optional |  `/eda-event-streams` |
|  `automationedacontroller_firewalld_zone` |  `eda_firewall_zone` | The firewall zone where Event-Driven Ansible related firewall rules are applied. This controls which networks can access Event-Driven Ansible based on the zone’s trust level. | Optional | RPM = no default set. Container = `public` . |
|  `automationedacontroller_gunicorn_event_stream_workers` |  | Number of workers for handling event streaming for Event-Driven Ansible. | Optional |  `2` |
|  `automationedacontroller_gunicorn_workers` |  `eda_gunicorn_workers` | Number of workers for handling the API served through Gunicorn. | Optional | (Number of cores or threads) * 2 + 1 |
|  `automationedacontroller_http_port` |  `eda_nginx_http_port` | Port number that Event-Driven Ansible listens on for HTTP requests. | Optional | RPM = `80` . Container = `8082` . |
|  `automationedacontroller_https_port` |  `eda_nginx_https_port` | Port number that Event-Driven Ansible listens on for HTTPS requests. | Optional | RPM = `443` . Container = `8445` . |
|  `automationedacontroller_max_running_activations` |  `eda_max_running_activations` | Number of maximum activations running concurrently per node. This is an integer that must be greater than 0. | Optional |  `12` |
|  `automationedacontroller_nginx_tls_files_remote` |  | Denote whether the web cert sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationedacontroller_pg_cert_auth` |  `eda_pg_cert_auth` | Controls whether client certificate authentication is enabled or disabled on the Event-Driven Ansible PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | Optional |  `false` |
|  `automationedacontroller_pg_database` |  `eda_pg_database` | Name of the PostgreSQL database used by Event-Driven Ansible. | Optional | RPM = `automationedacontroller` . Container = `eda` . |
|  `automationedacontroller_pg_host` |  `eda_pg_host` | Hostname of the PostgreSQL database used by Event-Driven Ansible. | Required |  |
|  `automationedacontroller_pg_password` |  `eda_pg_password` | Password for the Event-Driven Ansible PostgreSQL database user. Use of special characters for this variable is limited. The `!` , `#` , `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | Required if not using client certificate authentication. |  |
|  `automationedacontroller_pg_port` |  `eda_pg_port` | Port number for the PostgreSQL database used by Event-Driven Ansible. | Optional |  `5432` |
|  `automationedacontroller_pg_sslmode` |  `eda_pg_sslmode` | Determines the level of encryption and authentication for client server connections. Valid options include `verify-full` , `verify-ca` , `require` , `prefer` , `allow` , `disable` . | Optional |  `prefer` |
|  `automationedacontroller_pg_username` |  `eda_pg_username` | Username for the Event-Driven Ansible PostgreSQL database user. | Optional | RPM = `automationedacontroller` . Container = `eda` . |
|  `automationedacontroller_pgclient_sslcert` |  `eda_pg_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file for Event-Driven Ansible. | Required if using client certificate authentication. |  |
|  `automationedacontroller_pgclient_sslkey` |  `eda_pg_tls_key` | Path to the PostgreSQL SSL/TLS key file for Event-Driven Ansible. | Required if using client certificate authentication. |  |
|  `automationedacontroller_pgclient_tls_files_remote` |  | Denote whether the PostgreSQL client cert sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationedacontroller_public_event_stream_url` |  `eda_event_stream_url` | URL for connecting to the event stream. The URL must start with the `http://` or `https://` prefix | Optional |  |
|  `automationedacontroller_redis_host` |  `eda_redis_host` | Hostname of the Redis host used by Event-Driven Ansible. | Optional | First node in the `[automationgateway]` inventory group |
|  `automationedacontroller_redis_password` |  `eda_redis_password` | Password for Event-Driven Ansible Redis. | Optional | Randomly generated string |
|  `automationedacontroller_redis_port` |  `eda_redis_port` | Port number for the Redis host for Event-Driven Ansible. | Optional | RPM = The value defined in platform gateway’s implementation ( `automationgateway_redis_port` ). Container = `6379` |
|  `automationedacontroller_redis_username` |  `eda_redis_username` | Username for Event-Driven Ansible Redis. | Optional |  `eda` |
|  `automationedacontroller_secret_key` |  `eda_secret_key` | Secret key value used by Event-Driven Ansible to sign and encrypt data. | Optional |  |
|  `automationedacontroller_ssl_cert` |  `eda_tls_cert` | Path to the SSL/TLS certificate file for Event-Driven Ansible. | Optional |  |
|  `automationedacontroller_ssl_key` |  `eda_tls_key` | Path to the SSL/TLS key file for Event-Driven Ansible. | Optional |  |
|  `automationedacontroller_tls_files_remote` |  `eda_tls_remote` | Denote whether the Event-Driven Ansible provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationedacontroller_trusted_origins` |  | List of host addresses in the form: `&lt;scheme&gt;//:&lt;address&gt;:&lt;port&gt;` for trusted Cross-Site Request Forgery (CSRF) origins. | Optional |  `[]` |
|  `automationedacontroller_use_archive_compression` |  `eda_use_archive_compression` | Controls whether archive compression is enabled or disabled for Event-Driven Ansible. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
|  `automationedacontroller_use_db_compression` |  `eda_use_db_compression` | Controls whether database compression is enabled or disabled for Event-Driven Ansible. You can control this functionality globally by using `use_db_compression` . | Optional |  `true` |
|  `automationedacontroller_user_headers` |  `eda_nginx_user_headers` | List of additional NGINX headers to add to Event-Driven Ansible’s NGINX configuration. | Optional |  `[]` |
|  `automationedacontroller_websocket_ssl_verify` |  | Controls whether or not to perform SSL verification for the Daphne WebSocket used by Podman to communicate from the pod to the host. Set to `false` to disable SSL verification. | Optional |  `true` |
|  `eda_node_type` |  `eda_type` | Event-Driven Ansible node type. Valid options include `api` , `event-stream` , `hybrid` , `worker` . | Optional |  `hybrid` |
|  |  `eda_debug` | Controls whether debug mode is enabled or disabled for Event-Driven Ansible. Set to `true` to enable debug mode for Event-Driven Ansible. | Optional |  `false` |
|  |  `eda_extra_settings` | Defines additional settings for use by Event-Driven Ansible during installation.

For example:

```
eda_extra_settings:
- setting: RULEBOOK_READINESS_TIMEOUT_SECONDS
value: 120
``` | Optional |  `[]` |
|  |  `eda_nginx_client_max_body_size` | Maximum allowed size for data sent to Event-Driven Ansible through NGINX. | Optional |  `1m` |
|  |  `eda_nginx_hsts_max_age` | Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for Event-Driven Ansible. | Optional |  `63072000` |
|  `nginx_tls_protocols` |  `eda_nginx_https_protocols` | Protocols that Event-Driven Ansible supports when handling HTTPS traffic. | Optional | RPM = `[TLSv1.2]` . Container = `[TLSv1.2, TLSv1.3]` . |
|  |  `eda_pg_socket` | UNIX socket used by Event-Driven Ansible to connect to the PostgreSQL database. | Optional |  |
|  `redis_disable_tls` |  `eda_redis_disable_tls` | Controls whether TLS is enabled or disabled for Event-Driven Ansible Redis. Set this variable to true to disable TLS. | Optional |  `false` |
|  |  `eda_redis_tls_cert` | Path to the Event-Driven Ansible Redis certificate file. | Optional |  |
|  |  `eda_redis_tls_key` | Path to the Event-Driven Ansible Redis key file. | Optional |  |
|  |  `eda_safe_plugins` | List of plugins that are allowed to run within Event-Driven Ansible.

For more information, see [Adding a safe plugin variable to Event-Driven Ansible controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/assembly-platform-install-scenario#proc-add-eda-safe-plugin-var) . | Optional |  `[]` |


## A.6. General variables




General inventory file variables for Ansible Automation Platform.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `aap_ca_cert_file` |  `ca_tls_cert` | Path to the user provided CA certificate file used to generate SSL/TLS certificates for all Ansible Automation Platform services. For more information, see [Optional: Using custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/platform-system-requirements#optional_using_custom_tls_certificates) . | Optional |  |
|  `aap_ca_cert_files_remote` |  `ca_tls_remote` | Denote whether the CA certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `aap_ca_cert_size` |  | Bit size of the internally managed CA certificate private key. | Optional |  `4096` |
|  `aap_ca_key_file` |  `ca_tls_key` | Path to the key file for the CA certificate provided in `aap_ca_cert_file` (RPM) and `ca_tls_cert` (Container). For more information, see [Optional: Using custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/platform-system-requirements#optional_using_custom_tls_certificates) . | Optional |  |
|  `aap_ca_passphrase_cipher` |  | Cipher used for signing the internally managed CA certificate private key. | Optional |  `aes256` |
|  `aap_ca_regenerate` |  | Denotes whether or not to regenerate the internally managed CA certificate key pair. | Optional |  `false` |
|  `aap_service_cert_size` |  | Bit size of the component key pair managed by the internal CA. | Optional |  `4096` |
|  `aap_service_regen_cert` |  | Denotes whether or not to regenerate the component key pair managed by the internal CA. | Optional |  `false` |
|  `aap_service_san_records` |  | A list of additional SAN records for signing a service. Assign these to components in the inventory file as host variables rather than group or all variables. All strings must also contain their corresponding SAN option prefix such as `DNS:` or `IP:` . | Optional |  `[]` |
|  `backup_dest` |  | Directory local to `setup.sh` for the final backup file. | Optional | The value defined in `setup_dir` . |
|  `backup_dir` |  `backup_dir` | Directory used to store backup files. | Optional | RPM = `/var/backups/automation-platform/` . Container = `~/backups` |
|  `backup_file_prefix` |  | Prefix used for the file backup name for the final backup file. | Optional |  `automation-platform-backup` |
|  `bundle_install` |  `bundle_install` | Controls whether or not to perform an offline or bundled installation. Set this variable to `true` to enable an offline or bundled installation. | Optional |  `false` if using the setup installation program. `true` if using the setup bundle installation program. |
|  `bundle_install_folder` |  `bundle_dir` | Path to the bundle directory used when performing a bundle install. | Required if `bundle_install=true` | RPM = `/var/lib/ansible-automation-platform-bundle` . Container = `&lt;current_dir&gt;/bundle` . |
|  `custom_ca_cert` |  `custom_ca_cert` | Path to the custom CA certificate file. This is required if any of the TLS certificates you manually provided are signed by a custom CA. For more information, see [Optional: Using custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/platform-system-requirements#optional_using_custom_tls_certificates) . | Optional |  |
|  `enable_insights_collection` |  | The default install registers the node to the Red Hat Insights for Red Hat Ansible Automation Platform for the Red Hat Ansible Automation Platform Service if the node is registered with Subscription Manager. Set to `false` to disable this functionality. | Optional |  `true` |
|  `registry_password` |  `registry_password` | Password credential for access to the registry source defined in `registry_url` . For more information, see [Setting registry_username and registry_password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/assembly-platform-install-scenario#proc-set-registry-username-password) . | RPM = Required if you need a password to access `registry_url` . Container = Required if `registry_auth=true` . |  |
|  `registry_url` |  `registry_url` | URL of the registry source from which to pull execution environment images. | Optional |  `registry.redhat.io` |
|  `registry_username` |  `registry_username` | Username credential for access to the registry source defined in `registry_url` . For more information, see [Setting registry_username and registry_password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/assembly-platform-install-scenario#proc-set-registry-username-password) . | RPM = Required if you need a password to access `registry_url` . Container = Required if `registry_auth=true` . |  |
|  `registry_verify_ssl` |  `registry_tls_verify` | Controls whether SSL/TLS certificate verification is enabled or disabled when making HTTPS requests. | Optional |  `true` |
|  `restore_backup_file` |  | Path to the tar file used for the platform restore. | Optional |  `{{ setup_dir }}/automation-platform-backup-latest.tar.gz` |
|  `restore_file_prefix` |  | Path prefix for the staged restore components. | Optional |  `automation-platform-restore` |
|  `routable_hostname` |  `routable_hostname` | Used if the machine running the installation program can only route to the target host through a specific URL. For example, if you use short names in your inventory, but the node running the installation program can only resolve that host by using a FQDN. If `routable_hostname` is not set, it defaults to `ansible_host` . If you do not set `ansible_host` , `inventory_hostname` is used as a last resort. This variable is used as a host variable for particular hosts and not under the `[all:vars]` section. For further information, see [Assigning a variable to one machine: host variables](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#assigning-a-variable-to-one-machine-host-variables) . | Optional |  |
|  `use_archive_compression` |  `use_archive_compression` | Controls at a global level whether the filesystem-related backup files are compressed before being sent to the host to run the backup operation. If set to `true` , a `tar.gz` file is generated on each Ansible Automation Platform host and then gzip compression is used. If set to `false` , a simple tar file is generated.

You can control this functionality at a component level by using the `&lt;component_name&gt;_use_archive_compression` variables. | Optional |  `true` |
|  `use_db_compression` |  `use_db_compression` | Controls at a global level whether the database-related backup files are compressed before being sent to the host to run the backup operation.

You can control this functionality at a component level by using the `&lt;component_name&gt;_use_db_compression` variables. | Optional |  `true` |
|  |  `ca_tls_key_passphrase` | Passphrase used to decrypt the key provided in `ca_tls_key` . | Optional |  |
|  |  `client_request_timeout` | Sets the HTTP timeout for end-user requests. The minimum value is `10` seconds. | Optional |  `30` |
|  |  `container_compress` | Compression software to use for compressing container images. | Optional |  `gzip` |
|  |  `container_keep_images` | Controls whether or not to keep container images when uninstalling Ansible Automation Platform. Set to `true` to keep container images when uninstalling Ansible Automation Platform. | Optional |  `false` |
|  |  `container_pull_images` | Controls whether or not to pull newer container images during installation. Set to `false` to prevent pulling newer container images during installation. | Optional |  `true` |
|  |  `images_tmp_dir` | The directory where the installation program temporarily stores container images during installation. | Optional | The system’s temporary directory. |
|  |  `pcp_firewall_zone` | The firewall zone where Performance Co-Pilot related firewall rules are applied. This controls which networks can access Performance Co-Pilot based on the zone’s trust level. | Optional | public |
|  |  `pcp_use_archive_compression` | Controls whether archive compression is enabled or disabled for Performance Co-Pilot. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
|  |  `registry_auth` | Set whether or not to use registry authentication. When this variable is set to true, `registry_username` and `registry_password` are required. | Optional |  `true` |
|  |  `registry_ns_aap` | Ansible Automation Platform registry namespace. | Optional |  `ansible-automation-platform-26` |
|  |  `registry_ns_rhel` | RHEL registry namespace. | Optional |  `rhel8` |


## A.7. Image variables




Inventory file variables for images.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `extra_images` |  | Additional container images to pull from the configured container registry during deployment. | Optional |  `ansible-builder-rhel8` |
|  |  `controller_image` | Container image for automation controller. | Optional |  `controller-rhel8:latest` |
|  |  `de_extra_images` | Additional decision environment container images to pull from the configured container registry during deployment. | Optional |  `[]` |
|  |  `de_supported_image` | Supported decision environment container image. | Optional |  `de-supported-rhel8:latest` |
|  |  `eda_image` | Backend container image for Event-Driven Ansible. | Optional |  `eda-controller-rhel8:latest` |
|  |  `eda_web_image` | Front-end container image for Event-Driven Ansible. | Optional |  `eda-controller-ui-rhel8:latest` |
|  |  `ee_extra_images` | Additional execution environment container images to pull from the configured container registry during deployment. | Optional |  `[]` |
|  |  `ee_minimal_image` | Minimal execution environment container image. | Optional |  `ee-minimal-rhel8:latest` |
|  |  `ee_supported_image` | Supported execution environment container image. | Optional |  `ee-supported-rhel8:latest` |
|  |  `gateway_image` | Container image for platform gateway. | Optional |  `gateway-rhel8:latest` |
|  |  `gateway_proxy_image` | Container image for platform gateway proxy. | Optional |  `gateway-proxy-rhel8:latest` |
|  |  `hub_image` | Backend container image for automation hub. | Optional |  `hub-rhel8:latest` |
|  |  `hub_web_image` | Front-end container image for automation hub. | Optional |  `hub-web-rhel8:latest` |
|  |  `pcp_image` | Container image for Performance Co-Pilot. | Optional |  `pcp:latest` |
|  |  `postgresql_image` | Container image for PostgreSQL. | Optional |  `postgresql-15:latest` |
|  |  `receptor_image` | Container image for receptor. | Optional |  `receptor-rhel8:latest` |
|  |  `redis_image` | Container image for Redis. | Optional |  `redis-6:latest` |


## A.8. Platform gateway variables




Inventory file variables for platform gateway.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `automationgateway_admin_email` |  `gateway_admin_email` | Email address used by Django for the admin user for platform gateway. | Optional |  `admin@example.com` |
|  `automationgateway_admin_password` |  `gateway_admin_password` | Platform gateway administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/` , `”` , or `@` . | Required |  |
|  `automationgateway_admin_username` |  `gateway_admin_user` | Username used to identify and create the administrator user in platform gateway. | Optional |  `admin` |
|  `automationgateway_cache_cert` |  `gateway_redis_tls_cert` | Path to the platform gateway Redis certificate file. | Optional |  |
|  `automationgateway_cache_key` |  `gateway_redis_tls_key` | Path to the platform gateway Redis key file. | Optional |  |
|  `automationgateway_cache_tls_files_remote` |  | Denote whether the cache client certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `automationgateway_tls_files_remote` which defaults to `false` . |
|  `automationgateway_client_regen_cert` |  | Controls whether or not to regenerate platform gateway client certificates for the platform cache. Set to `true` to regenerate platform gateway client certificates. | Optional |  `false` |
|  `automationgateway_control_plane_port` |  `gateway_control_plane_port` | Port number for the platform gateway control plane. | Optional |  `50051` |
|  `automationgateway_disable_hsts` |  `gateway_nginx_disable_hsts` | Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for platform gateway. Set this variable to `true` to disable HSTS. | Optional |  `false` |
|  `automationgateway_disable_https` |  `gateway_nginx_disable_https` | Controls whether HTTPS is enabled or disabled for platform gateway. Set this variable to `true` to disable HTTPS. | Optional | RPM = The value defined in `disable_https` which defaults to `false` . Container = `false` . |
|  `automationgateway_firewalld_zone` |  `gateway_proxy_firewall_zone` | The firewall zone where platform gateway related firewall rules are applied. This controls which networks can access platform gateway based on the zone’s trust level. | Optional | RPM = no default set. Container = 'public'. |
|  `automationgateway_grpc_auth_service_timeout` |  `gateway_grpc_auth_service_timeout` | Timeout duration (in seconds) for requests made to the gRPC service on platform gateway. | Optional |  `30s` |
|  `automationgateway_grpc_server_max_threads_per_process` |  `gateway_grpc_server_max_threads_per_process` | Maximum number of threads that each gRPC server process can create to handle requests on platform gateway. | Optional |  `10` |
|  `automationgateway_grpc_server_processes` |  `gateway_grpc_server_processes` | Number of processes for handling gRPC requests on platform gateway. | Optional |  `5` |
|  `automationgateway_http_port` |  `gateway_nginx_http_port` | Port number that platform gateway listens on for HTTP requests. | Optional | RPM = `8080` . Container = `8083` . |
|  `automationgateway_https_port` |  `gateway_nginx_https_port` | Port number that platform gateway listens on for HTTPS requests. | Optional | RPM = `8443` . Container = `8446` . |
|  `automationgateway_main_url` |  `gateway_main_url` | URL of the main instance of platform gateway that clients connect to. Use if you are performing a clustered deployment and you need to use the URL of the load balancer instead of the component’s server. The URL must start with `http://` or `https://` prefix. | Optional |  |
|  `automationgateway_nginx_tls_files_remote` |  | Denote whether the web cert sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `automationgateway_tls_files_remote` which defaults to `false` . |
|  `automationgateway_pg_cert_auth` |  `gateway_pg_cert_auth` | Controls whether client certificate authentication is enabled or disabled on the platform gateway PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | Optional |  `false` |
|  `automationgateway_pg_database` |  `gateway_pg_database` | Name of the PostgreSQL database used by platform gateway. | Optional | RPM = `automationgateway` . Container = `gateway` . |
|  `automationgateway_pg_host` |  `gateway_pg_host` | Hostname of the PostgreSQL database used by platform gateway. | Required |  |
|  `automationgateway_pg_password` |  `gateway_pg_password` | Password for the platform gateway PostgreSQL database user. Use of special characters for this variable is limited. The `!` , `#` , `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | Optional |  |
|  `automationgateway_pg_port` |  `gateway_pg_port` | Port number for the PostgreSQL database used by platform gateway. | Optional |  `5432` |
|  `automationgateway_pg_sslmode` |  `gateway_pg_sslmode` | Controls the SSL mode to use when platform gateway connects to the PostgreSQL database. Valid options include `verify-full` , `verify-ca` , `require` , `prefer` , `allow` , `disable` . | Optional |  `prefer` |
|  `automationgateway_pg_username` |  `gateway_pg_username` | Username for the platform gateway PostgreSQL database user. | Optional | RPM = `automationgateway` . Container = `gateway` |
|  `automationgateway_pgclient_sslcert` |  `gateway_pg_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file for platform gateway. | Required if using client certificate authentication. |  |
|  `automationgateway_pgclient_sslkey` |  `gateway_pg_tls_key` | Path to the PostgreSQL SSL/TLS key file for platform gateway. | Required if using client certificate authentication. |  |
|  `automationgateway_pgclient_tls_files_remote` |  | Denote whether the PostgreSQL client cert sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `automationgateway_tls_files_remote` which defaults to `false` . |
|  `automationgateway_redis_host` |  `gateway_redis_host` | Hostname of the Redis host used by platform gateway. | Optional | First node in the `[automationgateway]` inventory group. |
|  `automationgateway_redis_password` |  `gateway_redis_password` | Password for platform gateway Redis. | Optional | Randomly generated string. |
|  `automationgateway_redis_username` |  `gateway_redis_username` | Username for platform gateway Redis. | Optional |  `gateway` |
|  `automationgateway_secret_key` |  `gateway_secret_key` | Secret key value used by platform gateway to sign and encrypt data. | Optional |  |
|  `automationgateway_ssl_cert` |  `gateway_tls_cert` | Path to the SSL/TLS certificate file for platform gateway. | Optional |  |
|  `automationgateway_ssl_key` |  `gateway_tls_key` | Path to the SSL/TLS key file for platform gateway. | Optional |  |
|  `automationgateway_tls_files_remote` |  `gateway_tls_remote` | Denote whether the platform gateway provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationgateway_use_archive_compression` |  `gateway_use_archive_compression` | Controls whether archive compression is enabled or disabled for platform gateway. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
|  `automationgateway_use_db_compression` |  `gateway_use_db_compression` | Controls whether database compression is enabled or disabled for platform gateway. You can control this functionality globally by using `use_db_compression` . | Optional |  `true` |
|  `automationgateway_user_headers` |  `gateway_nginx_user_headers` | List of additional NGINX headers to add to platform gateway’s NGINX configuration. | Optional |  `[]` |
|  `automationgateway_verify_ssl` |  | Denotes whether or not to verify platform gateway’s web certificates when making calls from platform gateway to itself during installation. Set to `false` to disable web certificate verification. | Optional |  `true` |
|  `automationgatewayproxy_disable_https` |  `envoy_disable_https` | Controls whether or not HTTPS is disabled when accessing the platform UI. Set to `true` to disable HTTPS (HTTP is used instead). | Optional | RPM = The value defined in `disable_https` which defaults to `false` . Container = `false` . |
|  `automationgatewayproxy_http_port` |  `envoy_http_port` | Port number on which the Envoy proxy listens for incoming HTTP connections. | Optional |  `80` |
|  `automationgatewayproxy_https_port` |  `envoy_https_port` | Port number on which the Envoy proxy listens for incoming HTTPS connections. | Optional |  `443` |
|  `nginx_tls_protocols` |  `gateway_nginx_https_protocols` | Protocols that platform gateway will support when handling HTTPS traffic. | Optional | RPM = `[TLSv1.2]` . Container = `[TLSv1.2, TLSv1.3]` . |
|  `redis_disable_tls` |  `gateway_redis_disable_tls` | Controls whether TLS is enabled or disabled for platform gateway Redis. Set this variable to `true` to disable TLS. | Optional |  `false` |
|  `redis_port` |  `gateway_redis_port` | Port number for the Redis host for platform gateway. | Optional |  `6379` |
|  |  `gateway_extra_settings` | Defines additional settings for use by platform gateway during installation.

For example:

```
gateway_extra_settings:
- setting: OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']
value: 600
``` | Optional |  `[]` |
|  |  `gateway_nginx_client_max_body_size` | Maximum allowed size for data sent to platform gateway through NGINX. | Optional |  `5m` |
|  |  `gateway_nginx_hsts_max_age` | Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for platform gateway. | Optional |  `63072000` |
|  |  `gateway_uwsgi_listen_queue_size` | Number of requests `uwsgi` will allow in the queue on platform gateway until `uwsgi_processes` can serve them. | Optional |  `4096` |


## A.9. Receptor variables




Inventory file variables for Receptor.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `receptor_datadir` |  | The directory where receptor stores its runtime data and local artifacts. The target directory must be accessible to **awx** users. If the target directory is a temporary file system **tmpfs** , ensure it is remounted correctly after a reboot. Failure to do so results in the receptor no longer having a working directory. | Optional |  `/tmp/receptor` |
|  `receptor_listener_port` |  `receptor_port` | Port number that receptor listens on for incoming connections from other receptor nodes. | Optional |  `27199` |
|  `receptor_listener_protocol` |  `receptor_protocol` | Protocol that receptor will support when handling traffic. | Optional |  `tcp` |
|  `receptor_log_level` |  `receptor_log_level` | Controls the verbosity of logging for receptor. Valid options include: `error` , `warning` , `info` , or `debug` . | Optional |  `info` |
|  `receptor_tls` |  | Controls whether TLS is enabled or disabled for receptor. Set this variable to `false` to disable TLS. | Optional |  `true` |
| See `node_type` for the RPM equivalent variable. |  `receptor_type` | For the `[automationcontroller]` group the two options are:

-  `    receptor_type=control` - The node only runs project and inventory updates, but not regular jobs.
-  `    receptor_type=hybrid` - The node runs everything.


For the `[execution_nodes]` group the two options are:

-  `    receptor_type=hop` - The node forwards jobs to an execution node.
-  `    receptor_type=execution` - The node can run jobs. | Optional | For the `[automationcontroller]` group: `hybrid` . For the `[execution_nodes]` group: `execution` . |
| See `peers` for the RPM equivalent variable |  `receptor_peers` | Used to indicate which nodes a specific host connects to. Wherever this variable is defined, an outbound connection to the specific host is established. The value must be a comma-separated list of hostnames. Do not use inventory group names.

This is resolved into a set of hosts that is used to construct the `receptor.conf` file. | Optional |  `[]` |
|  |  `receptor_disable_signing` | Controls whether signing of communications between receptor nodes is enabled or disabled. Set this variable to `true` to disable communication signing. | Optional |  `false` |
|  |  `receptor_disable_tls` | Controls whether TLS is enabled or disabled for receptor. Set this variable to `true` to disable TLS. | Optional |  `false` |
|  |  `receptor_firewall_zone` | The firewall zone where receptor related firewall rules are applied. This controls which networks can access receptor based on the zone’s trust level. | Optional |  `public` |
|  |  `receptor_mintls13` | Controls whether or not receptor only accepts connections that use TLS 1.3 or higher. Set to `true` to only accept connections that use TLS 1.3 or higher. | Optional |  `false` |
|  |  `receptor_signing_private_key` | Path to the private key used by receptor to sign communications with other receptor nodes in the network. | Optional |  |
|  |  `receptor_signing_public_key` | Path to the public key used by receptor to sign communications with other receptor nodes in the network. | Optional |  |
|  |  `receptor_signing_remote` | Denote whether the receptor signing files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  |  `receptor_tls_cert` | Path to the TLS certificate file for receptor. | Optional |  |
|  |  `receptor_tls_key` | Path to the TLS key file for receptor. | Optional |  |
|  |  `receptor_tls_remote` | Denote whether the receptor provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  |  `receptor_use_archive_compression` | Controls whether archive compression is enabled or disabled for receptor. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |


## A.10. Redis variables




Inventory file variables for Redis.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `redis_cluster_ip` |  `redis_cluster_ip` | The IPv4 address used by the Redis cluster to identify each host in the cluster. When defining hosts in the `[redis]` group, use this variable to identify the IPv4 address if the default is not what you want. Specific to container: Redis clusters cannot use hostnames or IPv6 addresses. | Optional | RPM = Discovered IPv4 address from Ansible facts. If IPv4 address is not available, IPv6 address is used. Container = Discovered IPv4 address from Ansible facts. |
|  `redis_disable_mtls` |  | Controls whether mTLS is enabled or disabled for Redis. Set this variable to `true` to disable mTLS. | Optional |  `false` |
|  `redis_firewalld_zone` |  `redis_firewall_zone` | The firewall zone where Redis related firewall rules are applied. This controls which networks can access Redis based on the zone’s trust level. | Optional | RPM = no default set. Container = `public` . |
|  `redis_hostname` |  | Hostname used by the Redis cluster when identifying and routing the host. By default `routable_hostname` is used. | Optional | The value defined in `routable_hostname` |
|  `redis_mode` |  `redis_mode` | The Redis mode to use for your Ansible Automation Platform installation. Valid options include: `standalone` and `cluster` . For more information about Redis, see [Caching and queueing system](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ha-redis_planning) in _Planning your installation_ . | Optional |  `cluster` |
|  `redis_server_regen_cert` |  | Denotes whether or not to regenerate the Ansible Automation Platform managed TLS key pair for Redis. | Optional |  `false` |
|  `redis_tls_cert` |  `redis_tls_cert` | Path to the Redis server TLS certificate. | Optional |  |
|  `redis_tls_files_remote` |  `redis_tls_remote` | Denote whether the Redis provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `redis_tls_key` |  `redis_tls_key` | Path to the Redis server TLS certificate key. | Optional |  |
|  |  `redis_use_archive_compression` | Controls whether archive compression is enabled or disabled for Redis. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |



<span id="idm140681255072992"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





