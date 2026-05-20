# 7. Troubleshooting RPM installation of Ansible Automation Platform
## 7.1. Gathering Ansible Automation Platform logs

Gather configuration, diagnostic, and troubleshooting data from all nodes in your Ansible Automation Platform environment by running the setup script with the `-s` flag. This crucial procedure generates an sos report, which contains the detailed diagnostic information Red Hat Technical Support engineers require to analyze and resolve service requests efficiently.

**Procedure**

1. Access the installation program folder with the inventory file and run the installation program setup script the following command:

`$ ./setup.sh -s`

With this command, you can connect to each node present in the inventory, install the `sos` tool, and generate new logs.


Note
If you are running the setup as a non-root user with sudo privileges, you can use the following command:

$ ANSIBLE_BECOME_METHOD='sudo'
ANSIBLE_BECOME=True ./setup.sh -s

2. *Optional*: If required, change the location of the `sos` report files.

The `sos` report files are copied to the `/tmp` folder for the current server. To change the location, specify the new location by using the following command:

$ ./setup.sh -e 'target_sos_directory=/path/to/files' -s

Where `target_sos_directory=/path/to/files` is used to specify the destination directory where the `sos` report will be saved. In this case, the `sos` report is stored in the directory `/path/to/files`.

3. Gather the files described on the playbook output and share with the support engineer or directly upload the `sos` report to Red Hat.

To create an `sos` report with additional information or directly upload the data to Red Hat, use the following command:

$ ./setup.sh -e 'case_number=0000000' -e 'clean=true' -e 'upload=true' -s

**Table 7.1. Parameter Reference Table**

| Parameter | Description | Default value |
| --- | --- | --- |
| <br> `case_number` | <br>  Specifies the support case number that you want. | <br>  - |
| <br> `clean` | <br>  Obfuscates sensitive data that might be present on the `sos` report. | <br> `false` |
| <br> `upload` | <br>  Automatically uploads the `sos` report data to Red Hat. | <br> `false` |
To learn more about the `sos` report tool, see: [What is an SOS report and how to create one in Red Hat Enterprise Linux?](https://access.redhat.com/solutions/3592)

# Appendix A. Inventory file variables

The following tables contain information about the variables used in Ansible Automation Platform’s installation `inventory` files. The tables include the variables that you can use for RPM-based installation and container-based installation.

## A.1. Ansible variables

The following variables control how Ansible Automation Platform interacts with remote hosts.

**Table A.1. Ansible variables**

| Variable | Description |
| --- | --- |
| <br> `ansible_connection` | <br>  The connection plugin used for the task on the target host. This can be the name of any Ansible connection plugin. <br>  SSH protocol types are `smart`, `ssh`, or `paramiko`. You can also use `local` to run tasks on the control node itself. <br>  Default = `smart` |
| <br> `ansible_host` | <br>  The IP address or name of the target host to use instead of `inventory_hostname`. |
| <br> `ansible_password` | <br>  The password to authenticate to the host. <br>  Do not store this variable in plain text. Always use a vault. |
| <br> `ansible_port` | <br>  The connection port number. <br>  The default for SSH is `22`. |
| <br> `ansible_scp_extra_args` | <br>  This setting is always appended to the default `scp` command line. |
| <br> `ansible_sftp_extra_args` | <br>  This setting is always appended to the default `sftp` command line. |
| <br> `ansible_shell_executable` | <br>  This sets the shell that the Ansible controller uses on the target machine and overrides the executable in `ansible.cfg` which defaults to `/bin/sh`. |
| <br> `ansible_shell_type` | <br>  The shell type of the target system. <br>  Do not use this setting unless you have set the `ansible_shell_executable` to a non-Bourne (sh) compatible shell. By default commands are formatted using sh-style syntax. Setting this to `csh` or `fish` causes commands executed on target systems to follow the syntax of those shells instead. |
| <br> `ansible_ssh_common_args` | <br>  This setting is always appended to the default command line for `sftp`, `scp`, and `ssh`. Useful to configure a `ProxyCommand` for a certain host or group. |
| <br> `ansible_ssh_executable` | <br>  This setting overrides the default behavior to use the system `ssh`. This can override the `ssh_executable` setting in `ansible.cfg`. |
| <br> `ansible_ssh_extra_args` | <br>  This setting is always appended to the default `ssh` command line. |
| <br> `ansible_ssh_pipelining` | <br>  Determines if SSH `pipelining` is used. <br>  This can override the `pipelining` setting in `ansible.cfg`. If using SSH key-based authentication, the key must be managed by an SSH agent. |
| <br> `ansible_ssh_private_key_file` | <br>  Private key file used by SSH. <br>  Useful if using multiple keys and you do not want to use an SSH agent. |
| <br> `ansible_user` | <br>  The user name to use when connecting to the host. <br>  Do not change this variable unless `/bin/sh` is not installed on the target machine or cannot be run from sudo. |
| <br> `inventory_hostname` | <br>  This variable takes the hostname of the machine from the inventory script or the Ansible configuration file. You cannot set the value of this variable. Because the value is taken from the configuration file, the actual runtime hostname value can vary from what is returned by this variable. |

**Additional resources**

- [Reviewing your Ansible configuration with automation content navigator](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_content_navigator/assembly-review-config-navigator_installing-devtools)

## A.2. Automation hub variables

Inventory file variables for automation hub.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br> `automationhub_admin_password` | <br> `hub_admin_password` | <br>  Automation hub administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/`, `”`, or `@`. | <br>  Required |  |
| <br> `automationhub_api_token` |  | <br>  Set the existing token for the installation program. For example, a regenerated token in the automation hub UI will invalidate an existing token. Use this variable to set that token in the installation program the next time you run the installation program. | <br>  Optional |  |
| <br> `automationhub_auto_sign_collections` | <br> `hub_collection_auto_sign` | <br>  If a collection signing service is enabled, collections are not signed automatically by default. Set this variable to `true` to sign collections by default. | <br>  Optional | <br> `false` |
| <br> `automationhub_backup_collections` |  | <br>  Ansible automation hub provides artifacts in `/var/lib/pulp`. These artifacts are automatically backed up by default. Set this variable to `false` to prevent backup or restore of `/var/lib/pulp`. | <br>  Optional | <br> `true` |
| <br> `automationhub_client_max_body_size` | <br> `hub_nginx_client_max_body_size` | <br>  Maximum allowed size for data sent to automation hub through NGINX. | <br>  Optional | <br> `20m` |
| <br> `automationhub_collection_download_count` |  | <br>  Denote whether or not the collection download count should be displayed in the UI. | <br>  Optional | <br> `false` |
| <br> `automationhub_collection_seed_repository` |  | <br>  Controls the type of content to upload when `hub_seed_collections` is set to `true`. Valid options include: `certified`, `validated` | <br>  Optional | <br>  Both certified and validated are enabled by default. |
| <br> `automationhub_collection_signing_service_key` | <br> `hub_collection_signing_key` | <br>  Path to the collection signing key file. | <br>  Required if a collection signing service is enabled. |  |
| <br> `automationhub_container_repair_media_type` |  | <br>  Denote whether or not to run the command `pulpcore-manager container-repair-media-type`. Valid options include: `true`, `false`, `auto` | <br>  Optional | <br> `auto` |
| <br> `automationhub_container_signing_service_key` | <br> `hub_container_signing_key` | <br>  Path to the container signing key file. | <br>  Required if a container signing service is enabled. |  |
| <br> `automationhub_create_default_collection_signing_service` | <br> `hub_collection_signing` | <br>  Set this variable to `true` to enable a collection signing service. | <br>  Optional | <br> `false` |
| <br> `automationhub_create_default_container_signing_service` | <br> `hub_container_signing` | <br>  Set this variable to `true` to enable a container signing service. | <br>  Optional | <br> `false` |
|  | <br> `hub_data_path_exclude` | <br>  automation hub backup path to exclude. | <br>  Optional | <br> `[]` |
| <br> `automationhub_disable_hsts` | <br> `hub_nginx_disable_hsts` | <br>  Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for automation hub. Set this variable to `true` to disable HSTS. | <br>  Optional | <br> `false` |
| <br> `automationhub_disable_https` | <br> `hub_nginx_disable_https` | <br>  Controls whether HTTPS is enabled or disabled for automation hub. Set this variable to `true` to disable HTTPS. | <br>  Optional | <br> `false` |
| <br> `automationhub_enable_api_access_log` |  | <br>  Controls whether logging is enabled or disabled at `/var/log/galaxy_api_access.log`. The file logs all user actions made to the platform, including username and IP address. Set this variable to `true` to enable this logging. | <br>  Optional | <br> `false` |
| <br> `automationhub_enable_unauthenticated_collection_access` |  | <br>  Controls whether read-only access is enabled or disabled for unauthorized users viewing collections or namespaces for automation hub. Set this variable to `true` to enable read-only access. | <br>  Optional | <br> `false` |
| <br> `automationhub_enable_unauthenticated_collection_download` |  | <br>  Controls whether or not unauthorized users can download read-only collections from automation hub. Set this variable to `true` to enable download of read-only collections. | <br>  Optional | <br> `false` |
| <br> `automationhub_firewalld_zone` | <br> `hub_firewall_zone` | <br>  The firewall zone where automation hub related firewall rules are applied. This controls which networks can access automation hub based on the zone’s trust level. | <br>  Optional | <br>  RPM = no default set. Container = `public`. |
| <br> `automationhub_force_change_admin_password` |  | <br>  Denote whether or not to require the change of the default administrator password for automation hub during installation. Set to `true` to require the user to change the default administrator password during installation. | <br>  Optional | <br> `false` |
| <br> `automationhub_importer_settings` | <br> `hub_galaxy_importer` | <br>  Dictionary of settings to pass to the `galaxy-importer.cfg` configuration file. These settings control how the `galaxy-importer` service processes and validates Ansible content. Example values include: `ansible-doc`, `ansible-lint`, and `flake8`. | <br>  Optional |  |
| <br> `automationhub_nginx_tls_files_remote` |  | <br>  Denote whether the web certificate sources are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br>  The value defined in `automationhub_tls_files_remote`. |
| <br> `automationhub_pg_cert_auth` | <br> `hub_pg_cert_auth` | <br>  Controls whether client certificate authentication is enabled or disabled on the automation hub PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | <br>  Optional | <br> `false` |
| <br> `automationhub_pg_database` | <br> `hub_pg_database` | <br>  Name of the PostgreSQL database used by automation hub. | <br>  Optional | <br>  RPM = `automationhub`. Container = `pulp` |
| <br> `automationhub_pg_host` | <br> `hub_pg_host` | <br>  Hostname of the PostgreSQL database used by automation hub. | <br>  Required | <br>  RPM = `127.0.0.1`. Container = no default. |
| <br> `automationhub_pg_password` | <br> `hub_pg_password` | <br>  Password for the automation hub PostgreSQL database user. Use of special characters for this variable is limited. The `!`, `#`, `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | <br>  Optional |  |
| <br> `automationhub_pg_port` | <br> `hub_pg_port` | <br>  Port number for the PostgreSQL database used by automation hub. | <br>  Optional | <br> `5432` |
| <br> `automationhub_pg_sslmode` | <br> `hub_pg_sslmode` | <br>  Controls the SSL/TLS mode to use when automation hub connects to the PostgreSQL database. Valid options include `verify-full`, `verify-ca`, `require`, `prefer`, `allow`, `disable`. | <br>  Optional | <br> `prefer` |
| <br> `automationhub_pg_username` | <br> `hub_pg_username` | <br>  Username for the automation hub PostgreSQL database user. | <br>  Optional | <br>  RPM = `automationhub`. Container = `pulp`. |
| <br> `automationhub_pgclient_sslcert` | <br> `hub_pg_tls_cert` | <br>  Path to the PostgreSQL SSL/TLS certificate file for automation hub. | <br>  Required if using client certificate authentication. |  |
| <br> `automationhub_pgclient_sslkey` | <br> `hub_pg_tls_key` | <br>  Path to the PostgreSQL SSL/TLS key file for automation hub. | <br>  Required if using client certificate authentication. |  |
| <br> `automationhub_pgclient_tls_files_remote` |  | <br>  Denote whether the PostgreSQL client certificate sources are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br>  The value defined in `automationhub_tls_files_remote`. |
| <br> `automationhub_require_content_approval` |  | <br>  Controls whether content signing is enabled or disabled for automation hub. By default when you upload collections to automation hub, an administrator must approve it before they are made available to users. To disable the content approval flow, set the variable to `false`. | <br>  Optional | <br> `true` |
| <br> `automationhub_restore_signing_keys` |  | <br>  Controls whether or not existing signing keys should be restored from a backup. Set to `false` to disable restoration of existing signing keys. | <br>  Optional | <br> `true` |
| <br> `automationhub_seed_collections` | <br> `hub_seed_collections` | <br>  Controls whether or not pre-loading of collections is enabled. When you run the bundle installer, validated content is uploaded to the `validated` repository, and certified content is uploaded to the `rh-certified` repository. By default, certified content and validated content are both uploaded. If you do not want to pre-load content, set this variable to `false`. For the RPM-based installer, if you only want one type of content, set this variable to `true` and set the `automationhub_collection_seed_repository` variable to the type of content you want to include. | <br>  Optional | <br> `true` |
| <br> `automationhub_ssl_cert` | <br> `hub_tls_cert` | <br>  Path to the SSL/TLS certificate file for automation hub. | <br>  Optional |  |
| <br> `automationhub_ssl_key` | <br> `hub_tls_key` | <br>  Path to the SSL/TLS key file for automation hub. | <br>  Optional |  |
| <br> `automationhub_tls_files_remote` | <br> `hub_tls_remote` | <br>  Denote whether the automation hub provided certificate files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
| <br> `automationhub_use_archive_compression` | <br> `hub_use_archive_compression` | <br>  Controls whether archive compression is enabled or disabled for automation hub. You can control this functionality globally by using `use_archive_compression`. | <br>  Optional | <br> `true` |
| <br> `automationhub_use_db_compression` | <br> `hub_use_db_compression` | <br>  Controls whether database compression is enabled or disabled for automation hub. You can control this functionality globally by using `use_db_compression`. | <br>  Optional | <br> `true` |
| <br> `automationhub_user_headers` | <br> `hub_nginx_user_headers` | <br>  List of additional NGINX headers to add to automation hub’s NGINX configuration. | <br>  Optional | <br> `[]` |
| <br> `ee_from_hub_only` |  | <br>  Controls whether automation hub is the only registry for execution environment images. If set to `true`, automation hub is the exclusive registry. If set to `false`, images are also pulled directly from Red Hat. | <br>  Optional | <br> `true` when using the bundle installer, otherwise `false`. |
| <br> `generate_automationhub_token` |  | <br>  Controls whether or not a token is generated for automation hub during installation. By default, a token is automatically generated during a fresh installation. If set to `true`, a token is regenerated during installation. | <br>  Optional | <br> `false` |
|  | <br> `hub_extra_settings` | <br>  Defines additional settings for use by automation hub during installation. <br>  For example:        hub_extra_settings=[{"setting": "REDIRECT_IS_HTTPS", "value": True}] | <br>  Optional | <br> `[]` |
| <br> `nginx_hsts_max_age` | <br> `hub_nginx_hsts_max_age` | <br>  Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for automation hub. | <br>  Optional | <br> `63072000` |
| <br> `pulp_secret` | <br> `hub_secret_key` | <br>  Secret key value used by automation hub to sign and encrypt data. | <br>  Optional |  |
|  | <br> `hub_azure_account_key` | <br>  Azure blob storage account key. | <br>  Required if using an Azure blob storage backend. |  |
|  | <br> `hub_azure_account_name` | <br>  Account name associated with the Azure blob storage. | <br>  Required when using an Azure blob storage backend. |  |
|  | <br> `hub_azure_container` | <br>  Name of the Azure blob storage container. | <br>  Optional | <br> `pulp` |
|  | <br> `hub_azure_extra_settings` | <br>  Defines extra parameters for the Azure blob storage backend. For more information about the list of parameters, see [django-storages documentation - Azure Storage](https://django-storages.readthedocs.io/en/latest/backends/azure.html#settings). | <br>  Optional | <br> `{}` |
|  | <br> `hub_collection_signing_pass` | <br>  Password for the automation content collection signing service. | <br>  Required if the collection signing service is protected by a passphrase. |  |
|  | <br> `hub_collection_signing_service` | <br>  Service for signing collections. | <br>  Optional | <br> `ansible-default` |
|  | <br> `hub_container_signing_pass` | <br>  Password for the automation content container signing service. | <br>  Required if the container signing service is protected by a passphrase. |  |
|  | <br> `hub_container_signing_service` | <br>  Service for signing containers. | <br>  Optional | <br> `container-default` |
|  | <br> `hub_nginx_http_port` | <br>  Port number that automation hub listens on for HTTP requests. | <br>  Optional | <br> `8081` |
|  | <br> `hub_nginx_https_port` | <br>  Port number that automation hub listens on for HTTPS requests. | <br>  Optional | <br> `8444` |
| <br> `nginx_tls_protocols` | <br> `hub_nginx_https_protocols` | <br>  Protocols that automation hub will support when handling HTTPS traffic. | <br>  Optional | <br> `[TLSv1.2, TLSv1.3]` |
|  | <br> `hub_pg_socket` | <br>  UNIX socket used by automation hub to connect to the PostgreSQL database. | <br>  Optional |  |
|  | <br> `hub_s3_access_key` | <br>  AWS S3 access key. | <br>  Required if using an AWS S3 storage backend. |  |
|  | <br> `hub_s3_bucket_name` | <br>  Name of the AWS S3 storage bucket. | <br>  Optional | <br> `pulp` |
|  | <br> `hub_s3_extra_settings` | <br>  Used to define extra parameters for the AWS S3 storage backend. For more information about the list of parameters, see [django-storages documentation - Amazon S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings). | <br>  Optional | <br> `{}` |
|  | <br> `hub_s3_secret_key` | <br>  AWS S3 secret key. | <br>  Required if using an AWS S3 storage backend. |  |
|  | <br> `hub_shared_data_mount_opts` | <br>  Mount options for the Network File System (NFS) share. | <br>  Optional | <br> `rw,sync,hard` |
|  | <br> `hub_shared_data_path` | <br>  Path to the Network File System (NFS) share with read, write, and execute (RWX) access. The value must match the format `host:dir`, for example `nfs-server.example.com:/exports/hub`. | <br>  Required if installing more than one instance of automation hub with a `file` storage backend. When installing a single instance of automation hub, it is optional. |  |
|  | <br> `hub_storage_backend` | <br>  Automation hub storage backend type. Possible values include: `azure`, `file`, `s3`. | <br>  Optional | <br> `file` |
|  | <br> `hub_workers` | <br>  Number of automation hub workers. | <br>  Optional | <br> `2` |

## A.3. Automation controller variables

Inventory file variables for automation controller.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br> `admin_email` | <br> `controller_admin_email` | <br>  Email address used by Django for the admin user for automation controller. | <br>  Optional | <br> `admin@example.com` |
| <br> `admin_password` | <br> `controller_admin_password` | <br>  Automation controller administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/`, `”`, or `@`. | <br>  Required |  |
| <br> `admin_username` | <br> `controller_admin_user` | <br>  Username used to identify and create the administrator user in automation controller. | <br>  Optional | <br> `admin` |
| <br> `automationcontroller_client_max_body_size` | <br> `controller_nginx_client_max_body_size` | <br>  Maximum allowed size for data sent to automation controller through NGINX. | <br>  Optional | <br> `5m` |
| <br> `automationcontroller_use_archive_compression` | <br> `controller_use_archive_compression` | <br>  Controls whether archive compression is enabled or disabled for automation controller. You can control this functionality globally by using `use_archive_compression`. | <br>  Optional | <br> `true` |
| <br> `automationcontroller_use_db_compression` | <br> `controller_use_db_compression` | <br>  Controls whether database compression is enabled or disabled for automation controller. You can control this functionality globally by using `use_db_compression`. | <br>  Optional | <br> `true` |
| <br> `awx_pg_cert_auth` | <br> `controller_pg_cert_auth` | <br>  Controls whether client certificate authentication is enabled or disabled on the automation controller PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | <br>  Optional | <br> `false` |
| <br> `controller_firewalld_zone` | <br> `controller_firewall_zone` | <br>  The firewall zone where automation controller related firewall rules are applied. This controls which networks can access automation controller based on the zone’s trust level. | <br>  Optional | <br> `public` |
| <br> `controller_nginx_tls_files_remote` |  | <br>  Denote whether the web certificate sources are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br>  The value defined in `controller_tls_files_remote`. |
| <br> `controller_pgclient_tls_files_remote` |  | <br>  Denote whether the PostgreSQL client certificate sources are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br>  The value defined in `controller_tls_files_remote`. |
| <br> `controller_tls_files_remote` | <br> `controller_tls_remote` | <br>  Denote whether the automation controller provided certificate files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
| <br> `nginx_disable_hsts` | <br> `controller_nginx_disable_hsts` | <br>  Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for automation controller. Set this variable to `true` to disable HSTS. | <br>  Optional | <br> `false` |
| <br> `nginx_disable_https` | <br> `controller_nginx_disable_https` | <br>  Controls whether HTTPS is enabled or disabled for automation controller. Set this variable to `true` to disable HTTPS. | <br>  Optional | <br> `false` |
| <br> `nginx_hsts_max_age` | <br> `controller_nginx_hsts_max_age` | <br>  Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for automation controller. | <br>  Optional | <br> `63072000` |
| <br> `nginx_http_port` | <br> `controller_nginx_http_port` | <br>  Port number that automation controller listens on for HTTP requests. | <br>  Optional | <br>  RPM = `80`. Container = `8080` |
| <br> `nginx_https_port` | <br> `controller_nginx_https_port` | <br>  Port number that automation controller listens on for HTTPS requests. | <br>  Optional | <br>  RPM = `443`. Container = `8443` |
| <br> `nginx_tls_protocols` | <br> `controller_nginx_https_protocols` | <br>  Protocols that automation controller supports when handling HTTPS traffic. | <br>  Optional | <br> `[TLSv1.2, TLSv1.3]` |
| <br> `nginx_user_headers` | <br> `controller_nginx_user_headers` | <br>  List of additional NGINX headers to add to automation controller’s NGINX configuration. | <br>  Optional | <br> `[]` |
|  | <br> `controller_create_preload_data` | <br>  Controls whether or not to create preloaded content during installation. | <br>  Optional | <br> `true` |
| <br> `node_state` |  | <br>  The status of a node or group of nodes. Valid options include `active`, `deprovision` to remove a node from a cluster, or `iso_migrate` to migrate a legacy isolated node to an execution node. | <br>  Optional | <br> `active` |
| <br> `node_type` | <br>  See `receptor_type` for the container equivalent variable. | <br>  For the `[automationcontroller]` group the two options are:    <br> `node_type=control` - The node only runs project and inventory updates, but not regular jobs. `node_type=hybrid` - The node runs everything. <br>  For the `[execution_nodes]` group the two options are:    <br> `node_type=hop` - The node forwards jobs to an execution node. `node_type=execution` - The node can run jobs. | <br>  Optional | <br>  For `[automationcontroller]` = `hybrid`, for `[execution_nodes]` = `execution` |
| <br> `peers` | <br>  See `receptor_peers` for the container equivalent variable. | <br>  Used to indicate which nodes a specific host or group connects to. Wherever this variable is defined, an outbound connection to the specific host or group is established. This variable can be a comma-separated list of hosts and groups from the inventory. This is resolved into a set of hosts that is used to construct the `receptor.conf` file. | <br>  Optional |  |
| <br> `pg_database` | <br> `controller_pg_database` | <br>  Name of the PostgreSQL database used by automation controller. | <br>  Optional | <br> `awx` |
| <br> `pg_host` | <br> `controller_pg_host` | <br>  Hostname of the PostgreSQL database used by automation controller. | <br>  Required |  |
| <br> `pg_password` | <br> `controller_pg_password` | <br>  Password for the automation controller PostgreSQL database user. Use of special characters for this variable is limited. The `!`, `#`, `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | <br>  Required if not using client certificate authentication. |  |
| <br> `pg_port` | <br> `controller_pg_port` | <br>  Port number for the PostgreSQL database used by automation controller. | <br>  Optional | <br> `5432` |
| <br> `pg_sslmode` | <br> `controller_pg_sslmode` | <br>  Controls the SSL/TLS mode to use when automation controller connects to the PostgreSQL database. Valid options include `verify-full`, `verify-ca`, `require`, `prefer`, `allow`, `disable`. | <br>  Optional | <br> `prefer` |
| <br> `pg_username` | <br> `controller_pg_username` | <br>  Username for the automation controller PostgreSQL database user. | <br>  Optional | <br> `awx` |
| <br> `pgclient_sslcert` | <br> `controller_pg_tls_cert` | <br>  Path to the PostgreSQL SSL/TLS certificate file for automation controller. | <br>  Required if using client certificate authentication. |  |
| <br> `pgclient_sslkey` | <br> `controller_pg_tls_key` | <br>  Path to the PostgreSQL SSL/TLS key file for automation controller. | <br>  Required if using client certificate authentication. |  |
| <br> `precreate_partition_hours` |  | <br>  Number of hours worth of events table partitions to pre-create before starting a backup to avoid `pg_dump` locks. | <br>  Optional | <br>  3 |
| <br> `uwsgi_listen_queue_size` | <br> `controller_uwsgi_listen_queue_size` | <br>  Number of requests `uwsgi` allows in the queue on automation controller until `uwsgi_processes` can serve them. | <br>  Optional | <br> `2048` |
| <br> `web_server_ssl_cert` | <br> `controller_tls_cert` | <br>  Path to the SSL/TLS certificate file for automation controller. | <br>  Optional |  |
| <br> `web_server_ssl_key` | <br> `controller_tls_key` | <br>  Path to the SSL/TLS key file for automation controller. | <br>  Optional |  |
|  | <br> `controller_event_workers` | <br>  Number of event workers that handle job-related events inside automation controller. | <br>  Optional | <br> `4` |
|  | <br> `controller_extra_settings` | <br>  Defines additional settings for use by automation controller during installation. <br>  For example:        controller_extra_settings=[{"setting": "USE_X_FORWARDED_HOST", "value": True}] | <br>  Optional | <br> `[]` |
|  | <br> `controller_license_file` | <br>  Path to the automation controller license file. |  |  |
|  | <br> `controller_percent_memory_capacity` | <br>  Memory allocation for automation controller. | <br>  Optional | <br> `1.0` (allocates 100% of the total system memory to automation controller) |
|  | <br> `controller_pg_socket` | <br>  UNIX socket used by automation controller to connect to the PostgreSQL database. | <br>  Optional |  |
|  | <br> `controller_secret_key` | <br>  Secret key value used by automation controller to sign and encrypt data. | <br>  Optional |  |

## A.4. Database variables

Inventory file variables for the database used with Ansible Automation Platform.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br> `install_pg_port` | <br> `postgresql_port` | <br>  Port number for the PostgreSQL database. | <br>  Optional | <br> `5432` |
| <br> `postgres_extra_settings` | <br> `postgresql_extra_settings` | <br>  Defines additional settings for use by PostgreSQL. <br>  Example usage for RPM:        postgresql_extra_settings={'ssl_ciphers': 'HIGH:!aNULL:!MD5'}  <br>  Example usage for containerized:        postgresql_extra_settings=[{"setting": "ssl_ciphers", "value": "HIGH:!aNULL:!MD5"}] | <br>  Optional |  |
| <br> `postgres_firewalld_zone` | <br> `postgresql_firewall_zone` | <br>  The firewall zone where PostgreSQL related firewall rules are applied. This controls which networks can access PostgreSQL based on the zone’s trust level. | <br>  Optional | <br>  RPM = no default set. Container = `public`. |
| <br> `postgres_max_connections` | <br> `postgresql_max_connections` | <br>  Maximum number of concurrent connections to the database if you are using an installer-managed database. For more information see [PostgreSQL database configuration and maintenance for automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-improving-performance#ref-controller-database-settings). | <br>  Optional | <br> `1024` |
| <br> `postgres_ssl_cert` | <br> `postgresql_tls_cert` | <br>  Path to the PostgreSQL SSL/TLS certificate file. | <br>  Optional |  |
| <br> `postgres_ssl_key` | <br> `postgresql_tls_key` | <br>  Path to the PostgreSQL SSL/TLS key file. | <br>  Optional |  |
| <br> `postgres_use_ssl` | <br> `postgresql_disable_tls` | <br>  Controls whether SSL/TLS is enabled or disabled for the PostgreSQL database. | <br>  Optional | <br> `false` |
|  | <br> `postgresql_admin_database` | <br>  Database name used for connections to the PostgreSQL database server. | <br>  Optional | <br> `postgres` |
|  | <br> `postgresql_admin_password` | <br>  Password for the PostgreSQL admin user. When used, the installation program creates each component’s database and credentials. | <br>  Required if using `postgresql_admin_username`. |  |
|  | <br> `postgresql_admin_username` | <br>  Username for the PostgreSQL admin user. When used, the installation program creates each component’s database and credentials. | <br>  Optional | <br> `postgres` |
|  | <br> `postgresql_effective_cache_size` | <br>  Memory allocation available (in MB) for caching data. | <br>  Optional |  |
|  | <br> `postgresql_keep_databases` | <br>  Controls whether or not to keep databases during uninstall. This variable applies to databases managed by the installation program only, and not external (customer-managed) databases. Set to `true` to keep databases during uninstall. | <br>  Optional | <br> `false` |
|  | <br> `postgresql_log_destination` | <br>  Destination for server log output. | <br>  Optional | <br> `/dev/stderr` |
|  | <br> `postgresql_password_encryption` | <br>  The algorithm for encrypting passwords. | <br>  Optional | <br> `scram-sha-256` |
|  | <br> `postgresql_shared_buffers` | <br>  Memory allocation (in MB) for shared memory buffers. | <br>  Optional |  |
|  | <br> `postgresql_tls_remote` | <br>  Denote whether the PostgreSQL provided certificate files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
|  | <br> `postgresql_use_archive_compression` | <br>  Controls whether archive compression is enabled or disabled for PostgreSQL. You can control this functionality globally by using `use_archive_compression`. | <br>  Optional | <br> `true` |

## A.5. Event-Driven Ansible controller variables

Inventory file variables for Event-Driven Ansible controller.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br> `automationedacontroller_activation_workers` | <br> `eda_activation_workers` | <br>  Number of workers used for ansible-rulebook activation pods in Event-Driven Ansible. | <br>  Optional | <br>  RPM = (# of cores or threads) * 2 + 1. Container = `2` |
| <br> `automationedacontroller_admin_email` | <br> `eda_admin_email` | <br>  Email address used by Django for the admin user for Event-Driven Ansible. | <br>  Optional | <br> `admin@example.com` |
| <br> `automationedacontroller_admin_password` | <br> `eda_admin_password` | <br>  Event-Driven Ansible administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/`, `”`, or `@`. | <br>  Required |  |
| <br> `automationedacontroller_admin_username` | <br> `eda_admin_user` | <br>  Username used to identify and create the administrator user in Event-Driven Ansible. | <br>  Optional | <br> `admin` |
| <br> `automationedacontroller_backend_gunicorn_workers` |  | <br>  Number of workers for handling the API served through Gunicorn on worker nodes. | <br>  Optional | <br> `2` |
| <br> `automationedacontroller_cache_tls_files_remote` |  | <br>  Denote whether the cache cert sources are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
| <br> `automationedacontroller_client_regen_cert` |  | <br>  Controls whether or not to regenerate Event-Driven Ansible client certificates for the platform cache. Set to `true` to regenerate Event-Driven Ansible client certificates. | <br>  Optional | <br> `false` |
| <br> `automationedacontroller_default_workers` | <br> `eda_workers` | <br>  Number of workers used in Event-Driven Ansible for application work. | <br>  Optional | <br>  Number of cores or threads |
| <br> `automationedacontroller_disable_hsts` | <br> `eda_nginx_disable_hsts` | <br>  Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for Event-Driven Ansible. Set this variable to `true` to disable HSTS. | <br>  Optional | <br> `false` |
| <br> `automationedacontroller_disable_https` | <br> `eda_nginx_disable_https` | <br>  Controls whether HTTPS is enabled or disabled for Event-Driven Ansible. Set this variable to `true` to disable HTTPS. | <br>  Optional | <br> `false` |
| <br> `automationedacontroller_event_stream_mtls` | <br> `eda_event_stream_mtls` | <br>  Controls whether event stream mutual TLS (mTLS) authentication is enabled or disabled for Event-Driven Ansible. Set this variable to `false` to disable mTLS authentication. | <br>  Optional | <br> `true` |
| <br> `automationedacontroller_event_stream_mtls_path` | <br> `eda_event_stream_mtls_prefix_path` | <br>  The prefix path for the event stream mTLS URLs. | <br>  Optional | <br> `/mtls/eda-event-streams` |
| <br> `automationedacontroller_event_stream_path` | <br> `eda_event_stream_prefix_path` | <br>  API prefix path used for Event-Driven Ansible event-stream through platform gateway. | <br>  Optional | <br> `/eda-event-streams` |
| <br> `automationedacontroller_firewalld_zone` | <br> `eda_firewall_zone` | <br>  The firewall zone where Event-Driven Ansible related firewall rules are applied. This controls which networks can access Event-Driven Ansible based on the zone’s trust level. | <br>  Optional | <br>  RPM = no default set. Container = `public`. |
| <br> `automationedacontroller_gunicorn_event_stream_workers` |  | <br>  Number of workers for handling event streaming for Event-Driven Ansible. | <br>  Optional | <br> `2` |
| <br> `automationedacontroller_gunicorn_workers` | <br> `eda_gunicorn_workers` | <br>  Number of workers for handling the API served through Gunicorn. | <br>  Optional | <br>  (Number of cores or threads) * 2 + 1 |
| <br> `automationedacontroller_http_port` | <br> `eda_nginx_http_port` | <br>  Port number that Event-Driven Ansible listens on for HTTP requests. | <br>  Optional | <br>  RPM = `80`. Container = `8082`. |
| <br> `automationedacontroller_https_port` | <br> `eda_nginx_https_port` | <br>  Port number that Event-Driven Ansible listens on for HTTPS requests. | <br>  Optional | <br>  RPM = `443`. Container = `8445`. |
| <br> `automationedacontroller_nginx_tls_files_remote` |  | <br>  Denote whether the web cert sources are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
| <br> `automationedacontroller_pg_cert_auth` | <br> `eda_pg_cert_auth` | <br>  Controls whether client certificate authentication is enabled or disabled on the Event-Driven Ansible PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | <br>  Optional | <br> `false` |
| <br> `automationedacontroller_pg_database` | <br> `eda_pg_database` | <br>  Name of the PostgreSQL database used by Event-Driven Ansible. | <br>  Optional | <br>  RPM = `automationedacontroller`. Container = `eda`. |
| <br> `automationedacontroller_pg_host` | <br> `eda_pg_host` | <br>  Hostname of the PostgreSQL database used by Event-Driven Ansible. | <br>  Required |  |
| <br> `automationedacontroller_pg_password` | <br> `eda_pg_password` | <br>  Password for the Event-Driven Ansible PostgreSQL database user. Use of special characters for this variable is limited. The `!`, `#`, `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | <br>  Required if not using client certificate authentication. |  |
| <br> `automationedacontroller_pg_port` | <br> `eda_pg_port` | <br>  Port number for the PostgreSQL database used by Event-Driven Ansible. | <br>  Optional | <br> `5432` |
| <br> `automationedacontroller_pg_sslmode` | <br> `eda_pg_sslmode` | <br>  Determines the level of encryption and authentication for client server connections. Valid options include `verify-full`, `verify-ca`, `require`, `prefer`, `allow`, `disable`. | <br>  Optional | <br> `prefer` |
| <br> `automationedacontroller_pg_username` | <br> `eda_pg_username` | <br>  Username for the Event-Driven Ansible PostgreSQL database user. | <br>  Optional | <br>  RPM = `automationedacontroller`. Container = `eda`. |
| <br> `automationedacontroller_pgclient_sslcert` | <br> `eda_pg_tls_cert` | <br>  Path to the PostgreSQL SSL/TLS certificate file for Event-Driven Ansible. | <br>  Required if using client certificate authentication. |  |
| <br> `automationedacontroller_pgclient_sslkey` | <br> `eda_pg_tls_key` | <br>  Path to the PostgreSQL SSL/TLS key file for Event-Driven Ansible. | <br>  Required if using client certificate authentication. |  |
| <br> `automationedacontroller_pgclient_tls_files_remote` |  | <br>  Denote whether the PostgreSQL client cert sources are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
| <br> `automationedacontroller_public_event_stream_url` | <br> `eda_event_stream_url` | <br>  URL for connecting to the event stream. The URL must start with the `http://` or `https://` prefix | <br>  Optional |  |
| <br> `automationedacontroller_redis_host` | <br> `eda_redis_host` | <br>  Hostname of the Redis host used by Event-Driven Ansible. | <br>  Optional | <br>  First node in the `[automationgateway]` inventory group |
| <br> `automationedacontroller_redis_password` | <br> `eda_redis_password` | <br>  Password for Event-Driven Ansible Redis. | <br>  Optional | <br>  Randomly generated string |
| <br> `automationedacontroller_redis_port` | <br> `eda_redis_port` | <br>  Port number for the Redis host for Event-Driven Ansible. | <br>  Optional | <br>  RPM = The value defined in platform gateway’s implementation (`automationgateway_redis_port`). Container = `6379` |
| <br> `automationedacontroller_redis_username` | <br> `eda_redis_username` | <br>  Username for Event-Driven Ansible Redis. | <br>  Optional | <br> `eda` |
| <br> `automationedacontroller_secret_key` | <br> `eda_secret_key` | <br>  Secret key value used by Event-Driven Ansible to sign and encrypt data. | <br>  Optional |  |
| <br> `automationedacontroller_ssl_cert` | <br> `eda_tls_cert` | <br>  Path to the SSL/TLS certificate file for Event-Driven Ansible. | <br>  Optional |  |
| <br> `automationedacontroller_ssl_key` | <br> `eda_tls_key` | <br>  Path to the SSL/TLS key file for Event-Driven Ansible. | <br>  Optional |  |
| <br> `automationedacontroller_tls_files_remote` | <br> `eda_tls_remote` | <br>  Denote whether the Event-Driven Ansible provided certificate files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
| <br> `automationedacontroller_trusted_origins` |  | <br>  List of host addresses in the form: `<scheme>//:<address>:<port>` for trusted Cross-Site Request Forgery (CSRF) origins. | <br>  Optional | <br> `[]` |
| <br> `automationedacontroller_use_archive_compression` | <br> `eda_use_archive_compression` | <br>  Controls whether archive compression is enabled or disabled for Event-Driven Ansible. You can control this functionality globally by using `use_archive_compression`. | <br>  Optional | <br> `true` |
| <br> `automationedacontroller_use_db_compression` | <br> `eda_use_db_compression` | <br>  Controls whether database compression is enabled or disabled for Event-Driven Ansible. You can control this functionality globally by using `use_db_compression`. | <br>  Optional | <br> `true` |
| <br> `automationedacontroller_user_headers` | <br> `eda_nginx_user_headers` | <br>  List of additional NGINX headers to add to Event-Driven Ansible’s NGINX configuration. | <br>  Optional | <br> `[]` |
| <br> `automationedacontroller_websocket_ssl_verify` |  | <br>  Controls whether or not to perform SSL verification for the Daphne WebSocket used by Podman to communicate from the pod to the host. Set to `false` to disable SSL verification. | <br>  Optional | <br> `true` |
| <br> `eda_node_type` | <br> `eda_type` | <br>  Event-Driven Ansible node type. Valid options include `api`, `event-stream`, `hybrid`, `worker`. | <br>  Optional | <br> `hybrid` |
|  | <br> `eda_debug` | <br>  Controls whether debug mode is enabled or disabled for Event-Driven Ansible. Set to `true` to enable debug mode for Event-Driven Ansible. | <br>  Optional | <br> `false` |
|  | <br> `eda_extra_settings` | <br>  Defines additional settings for use by Event-Driven Ansible during installation. <br>  For example:        eda_extra_settings=[{"setting": "RULEBOOK_READINESS_TIMEOUT_SECONDS", "value": 120}] | <br>  Optional | <br> `[]` |
|  | <br> `eda_nginx_client_max_body_size` | <br>  Maximum allowed size for data sent to Event-Driven Ansible through NGINX. | <br>  Optional | <br> `1m` |
|  | <br> `eda_nginx_hsts_max_age` | <br>  Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for Event-Driven Ansible. | <br>  Optional | <br> `63072000` |
| <br> `nginx_tls_protocols` | <br> `eda_nginx_https_protocols` | <br>  Protocols that Event-Driven Ansible supports when handling HTTPS traffic. | <br>  Optional | <br> `[TLSv1.2, TLSv1.3]` |
|  | <br> `eda_pg_socket` | <br>  UNIX socket used by Event-Driven Ansible to connect to the PostgreSQL database. | <br>  Optional |  |
| <br> `redis_disable_tls` | <br> `eda_redis_disable_tls` | <br>  Controls whether TLS is enabled or disabled for Event-Driven Ansible Redis. Set this variable to true to disable TLS. | <br>  Optional | <br> `false` |
|  | <br> `eda_redis_tls_cert` | <br>  Path to the Event-Driven Ansible Redis certificate file. | <br>  Optional |  |
|  | <br> `eda_redis_tls_key` | <br>  Path to the Event-Driven Ansible Redis key file. | <br>  Optional |  |
|  | <br> `eda_safe_plugins` | <br>  List of plugins that are allowed to run within Event-Driven Ansible. <br>  For more information, see [Adding a safe plugin variable to Event-Driven Ansible controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/assembly-platform-install-scenario#proc-add-eda-safe-plugin-var). | <br>  Optional | <br> `[]` |

## A.6. General variables

General inventory file variables for Ansible Automation Platform.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br> `aap_ca_cert_file` | <br> `ca_tls_cert` | <br>  Path to the user-provided CA certificate file. When you specify this variable, the installation program automatically generates TLS certificates for each Ansible Automation Platform service signed by this CA. You do not need to define individual service certificate variables (such as `gateway_tls_cert`, `controller_tls_cert`, or `hub_tls_cert`). For more information, see [Optional: Using custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/platform-system-requirements#proc-use-custom-tls-certificates_licensing-gw). | <br>  Optional |  |
| <br> `aap_ca_cert_files_remote` | <br> `ca_tls_remote` | <br>  Denote whether the CA certificate files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
| <br> `aap_ca_cert_size` |  | <br>  Bit size of the internally managed CA certificate private key. | <br>  Optional | <br> `4096` |
| <br> `aap_ca_key_file` | <br> `ca_tls_key` | <br>  Path to the key file for the CA certificate provided in `aap_ca_cert_file` (RPM) and `ca_tls_cert` (Container). The installation program uses this key to sign the automatically generated TLS certificates for each Ansible Automation Platform service. For more information, see [Optional: Using custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/platform-system-requirements#proc-use-custom-tls-certificates_licensing-gw). | <br>  Optional |  |
| <br> `aap_ca_passphrase_cipher` |  | <br>  Cipher used for signing the internally managed CA certificate private key. | <br>  Optional | <br> `aes256` |
| <br> `aap_ca_regenerate` |  | <br>  Denotes whether or not to regenerate the internally managed CA certificate key pair. | <br>  Optional | <br> `false` |
| <br> `aap_service_cert_size` |  | <br>  Bit size of the component key pair managed by the internal CA. | <br>  Optional | <br> `4096` |
| <br> `aap_service_regen_cert` |  | <br>  Denotes whether or not to regenerate the component key pair managed by the internal CA. | <br>  Optional | <br> `false` |
| <br> `aap_service_san_records` |  | <br>  A list of additional SAN records for signing a service. Assign these to components in the inventory file as host variables rather than group or all variables. All strings must also contain their corresponding SAN option prefix such as `DNS:` or `IP:`. | <br>  Optional | <br> `[]` |
| <br> `backup_dest` |  | <br>  Directory local to `setup.sh` for the final backup file. | <br>  Optional | <br>  The value defined in `setup_dir`. |
| <br> `backup_dir` | <br> `backup_dir` | <br>  Directory used to store backup files. | <br>  Optional | <br>  RPM = `/var/backups/automation-platform/`. Container = `~/backups` |
| <br> `backup_file_prefix` |  | <br>  Prefix used for the file backup name for the final backup file. | <br>  Optional | <br> `automation-platform-backup` |
| <br> `bundle_install` | <br> `bundle_install` | <br>  Controls whether or not to perform an offline or bundled installation. Set this variable to `true` to enable an offline or bundled installation. | <br>  Optional | <br> `false` if using the setup installation program. `true` if using the setup bundle installation program. |
| <br> `bundle_install_folder` | <br> `bundle_dir` | <br>  Path to the bundle directory used when performing a bundle install. | <br>  Required if `bundle_install=true` | <br>  RPM = `/var/lib/ansible-automation-platform-bundle`. Container = `<current_dir>/bundle`. |
| <br> `custom_ca_cert` | <br> `custom_ca_cert` | <br>  Path to the custom CA certificate file. Use this variable when you have manually provided TLS certificates for Ansible Automation Platform services (such as `gateway_tls_cert`, `controller_tls_cert`, or `hub_tls_cert`) that are signed by a custom CA. <br>  This variable adds the CA certificate to the environment to ensure proper authentication and trust of the manually provided certificates. This variable is not needed when using `ca_tls_cert` and `ca_tls_key`, which automatically generate TLS certificates. For more information, see [Optional: Using custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/platform-system-requirements#proc-use-custom-tls-certificates_licensing-gw). | <br>  Optional |  |
| <br> `enable_insights_collection` |  | <br>  The default install registers the node to the Red Hat Lightspeed for Red Hat Ansible Automation Platform for the Red Hat Ansible Automation Platform Service if the node is registered with Subscription Manager. Set to `false` to disable this functionality. | <br>  Optional | <br> `true` |
| <br> `registry_password` | <br> `registry_password` | <br>  Password credential for access to the registry source defined in `registry_url`. For more information, see [Setting registry_username and registry_password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/assembly-platform-install-scenario#proc-set-registry-username-password). | <br>  RPM = Required if you need a password to access `registry_url`. Container = Required for online installations if `registry_auth=true`. Not required for disconnected installations. |  |
| <br> `registry_url` | <br> `registry_url` | <br>  URL of the registry source from which to pull execution environment images. | <br>  Optional | <br> `registry.redhat.io` |
| <br> `registry_username` | <br> `registry_username` | <br>  Username credential for access to the registry source defined in `registry_url`. For more information, see [Setting registry_username and registry_password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/assembly-platform-install-scenario#proc-set-registry-username-password). | <br>  RPM = Required if you need a password to access `registry_url`. Container = Required for online installations if `registry_auth=true`. Not required for disconnected installations. |  |
| <br> `registry_verify_ssl` | <br> `registry_tls_verify` | <br>  Controls whether SSL/TLS certificate verification is enabled or disabled when making HTTPS requests. | <br>  Optional | <br> `true` |
| <br> `restore_backup_file` |  | <br>  Path to the tar file used for the platform restore. | <br>  Optional | <br> `{{ setup_dir }}/automation-platform-backup-latest.tar.gz` |
| <br> `restore_file_prefix` |  | <br>  Path prefix for the staged restore components. | <br>  Optional | <br> `automation-platform-restore` |
| <br> `routable_hostname` | <br> `routable_hostname` | <br>  Used if the machine running the installation program can only route to the target host through a specific URL. For example, if you use short names in your inventory, but the node running the installation program can only resolve that host by using a FQDN. If `routable_hostname` is not set, it defaults to `ansible_host`. If you do not set `ansible_host`, `inventory_hostname` is used as a last resort. This variable is used as a host variable for particular hosts and not under the `[all:vars]` section. | <br>  Optional |  |
| <br> `use_archive_compression` | <br> `use_archive_compression` | <br>  Controls at a global level whether the filesystem-related backup files are compressed before being sent to the host to run the backup operation. If set to `true`, a `tar.gz` file is generated on each Ansible Automation Platform host and then gzip compression is used. If set to `false`, a simple tar file is generated. <br>  You can control this functionality at a component level by using the `<component_name>_use_archive_compression` variables. | <br>  Optional | <br> `true` |
| <br> `use_db_compression` | <br> `use_db_compression` | <br>  Controls at a global level whether the database-related backup files are compressed before being sent to the host to run the backup operation. <br>  You can control this functionality at a component level by using the `<component_name>_use_db_compression` variables. | <br>  Optional | <br> `true` |
|  | <br> `ca_tls_key_passphrase` | <br>  Passphrase used to decrypt the key provided in `ca_tls_key`. | <br>  Optional |  |
|  | <br> `client_request_timeout` | <br>  Sets the HTTP timeout for end-user requests. The minimum value is `10` seconds. | <br>  Optional | <br> `30` |
|  | <br> `container_compress` | <br>  Compression software to use for compressing container images. | <br>  Optional | <br> `gzip` |
|  | <br> `container_keep_images` | <br>  Controls whether or not to keep container images when uninstalling Ansible Automation Platform. Set to `true` to keep container images when uninstalling Ansible Automation Platform. | <br>  Optional | <br> `false` |
|  | <br> `container_pull_images` | <br>  Controls whether or not to pull newer container images during installation. Set to `false` to prevent pulling newer container images during installation. | <br>  Optional | <br> `true` |
|  | <br> `images_tmp_dir` | <br>  The directory where the installation program temporarily stores container images during installation. | <br>  Optional | <br>  The system’s temporary directory. |
|  | <br> `pcp_firewall_zone` | <br>  The firewall zone where Performance Co-Pilot related firewall rules are applied. This controls which networks can access Performance Co-Pilot based on the zone’s trust level. | <br>  Optional | <br>  public |
|  | <br> `pcp_use_archive_compression` | <br>  Controls whether archive compression is enabled or disabled for Performance Co-Pilot. You can control this functionality globally by using `use_archive_compression`. | <br>  Optional | <br> `true` |
|  | <br> `registry_auth` | <br>  Controls whether to use registry authentication. When set to `true`, `registry_username` and `registry_password` are required. Not applicable for disconnected (bundled) installations. | <br>  Optional | <br> `true` |
|  | <br> `registry_ns_aap` | <br>  Ansible Automation Platform registry namespace. | <br>  Optional | <br> `ansible-automation-platform-26` |
|  | <br> `registry_ns_rhel` | <br>  RHEL registry namespace. | <br>  Optional | <br> `rhel8` |
|  | <br> `setup_monitoring` | <br>  Set to `true` to enable Performance Co-Pilot for system performance monitoring and data collection on Ansible Automation Platform control plane nodes. | <br>  Optional | <br> `false` |

## A.7. Image variables

Inventory file variables for images.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br> `extra_images` |  | <br>  Additional container images to pull from the configured container registry during deployment. | <br>  Optional | <br> `ansible-builder-rhel8` |
|  | <br> `controller_image` | <br>  Container image for automation controller. | <br>  Optional | <br> `controller-rhel9:latest` |
|  | <br> `de_extra_images` | <br>  Additional decision environment container images to pull from the configured container registry during deployment. | <br>  Optional | <br> `[]` |
|  | <br> `de_supported_image` | <br>  Supported decision environment container image. | <br>  Optional | <br> `de-supported-rhel9:latest` |
|  | <br> `eda_image` | <br>  Backend container image for Event-Driven Ansible. | <br>  Optional | <br> `eda-controller-rhel9:latest` |
|  | <br> `eda_web_image` | <br>  Front-end container image for Event-Driven Ansible. | <br>  Optional | <br> `eda-controller-ui-rhel9:latest` |
|  | <br> `ee_extra_images` | <br>  Additional execution environment container images to pull from the configured container registry during deployment. | <br>  Optional | <br> `[]` |
|  | <br> `ee_minimal_image` | <br>  Minimal execution environment container image. | <br>  Optional | <br> `ee-minimal-rhel9:latest` |
|  | <br> `ee_supported_image` | <br>  Supported execution environment container image. | <br>  Optional | <br> `ee-supported-rhel9:latest` |
|  | <br> `gateway_image` | <br>  Container image for platform gateway. | <br>  Optional | <br> `gateway-rhel9:latest` |
|  | <br> `gateway_proxy_image` | <br>  Container image for platform gateway proxy. | <br>  Optional | <br> `gateway-proxy-rhel9:latest` |
|  | <br> `hub_image` | <br>  Backend container image for automation hub. | <br>  Optional | <br> `hub-rhel9:latest` |
|  | <br> `hub_web_image` | <br>  Front-end container image for automation hub. | <br>  Optional | <br> `hub-web-rhel9:latest` |
|  | <br> `pcp_image` | <br>  Container image for Performance Co-Pilot. | <br>  Optional | <br> `pcp:latest` |
|  | <br> `postgresql_image` | <br>  Container image for PostgreSQL. | <br>  Optional | <br> `postgresql-15:latest` |
|  | <br> `receptor_image` | <br>  Container image for receptor. | <br>  Optional | <br> `receptor-rhel9:latest` |
|  | <br> `redis_image` | <br>  Container image for Redis. | <br>  Optional | <br> `redis-6:latest` |

## A.8. Platform gateway variables

Inventory file variables for platform gateway.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br> `automationgateway_admin_email` | <br> `gateway_admin_email` | <br>  Email address used by Django for the admin user for platform gateway. | <br>  Optional | <br> `admin@example.com` |
| <br> `automationgateway_admin_password` | <br> `gateway_admin_password` | <br>  Platform gateway administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/`, `”`, or `@`. | <br>  Required |  |
| <br> `automationgateway_admin_username` | <br> `gateway_admin_user` | <br>  Username used to identify and create the administrator user in platform gateway. The installation program uses this account to register services with platform gateway. If you have deleted the default `admin` user, set this variable to an existing system administrator account to avoid installation or upgrade failures. | <br>  Optional | <br> `admin` |
| <br> `automationgateway_cache_cert` | <br> `gateway_redis_tls_cert` | <br>  Path to the platform gateway Redis certificate file. | <br>  Optional |  |
| <br> `automationgateway_cache_key` | <br> `gateway_redis_tls_key` | <br>  Path to the platform gateway Redis key file. | <br>  Optional |  |
| <br> `automationgateway_cache_tls_files_remote` |  | <br>  Denote whether the cache client certificate files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br>  The value defined in `automationgateway_tls_files_remote` which defaults to `false`. |
| <br> `automationgateway_client_regen_cert` |  | <br>  Controls whether or not to regenerate platform gateway client certificates for the platform cache. Set to `true` to regenerate platform gateway client certificates. | <br>  Optional | <br> `false` |
| <br> `automationgateway_control_plane_port` | <br> `gateway_control_plane_port` | <br>  Port number for the platform gateway control plane. | <br>  Optional | <br> `50051` |
| <br> `automationgateway_disable_hsts` | <br> `gateway_nginx_disable_hsts` | <br>  Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for platform gateway. Set this variable to `true` to disable HSTS. | <br>  Optional | <br> `false` |
| <br> `automationgateway_disable_https` | <br> `gateway_nginx_disable_https` | <br>  Controls whether HTTPS is enabled or disabled for platform gateway. Set this variable to `true` to disable HTTPS. | <br>  Optional | <br>  RPM = The value defined in `disable_https` which defaults to `false`. Container = `false`. |
| <br> `automationgateway_firewalld_zone` | <br> `gateway_proxy_firewall_zone` | <br>  The firewall zone where platform gateway related firewall rules are applied. This controls which networks can access platform gateway based on the zone’s trust level. | <br>  Optional | <br>  RPM = no default set. Container = 'public'. |
| <br> `automationgateway_grpc_auth_service_timeout` | <br> `gateway_grpc_auth_service_timeout` | <br>  Timeout duration (in seconds) for requests made to the gRPC service on platform gateway. | <br>  Optional | <br> `30s` |
| <br> `automationgateway_grpc_server_max_threads_per_process` | <br> `gateway_grpc_server_max_threads_per_process` | <br>  Maximum number of threads that each gRPC server process can create to handle requests on platform gateway. | <br>  Optional | <br> `10` |
| <br> `automationgateway_grpc_server_processes` | <br> `gateway_grpc_server_processes` | <br>  Number of processes for handling gRPC requests on platform gateway. | <br>  Optional | <br> `5` |
| <br> `automationgateway_http_port` | <br> `gateway_nginx_http_port` | <br>  Port number that platform gateway listens on for HTTP requests. | <br>  Optional | <br>  RPM = `8080`. Container = `8083`. |
| <br> `automationgateway_https_port` | <br> `gateway_nginx_https_port` | <br>  Port number that platform gateway listens on for HTTPS requests. | <br>  Optional | <br>  RPM = `8443`. Container = `8446`. |
| <br> `automationgateway_main_url` | <br> `gateway_main_url` | <br>  URL of the main instance of platform gateway that clients connect to. Use if you are performing a clustered deployment and you need to use the URL of the load balancer instead of the component’s server. The URL must start with `http://` or `https://` prefix. | <br>  Optional |  |
| <br> `automationgateway_nginx_tls_files_remote` |  | <br>  Denote whether the web cert sources are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br>  The value defined in `automationgateway_tls_files_remote` which defaults to `false`. |
| <br> `automationgateway_pg_cert_auth` | <br> `gateway_pg_cert_auth` | <br>  Controls whether client certificate authentication is enabled or disabled on the platform gateway PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | <br>  Optional | <br> `false` |
| <br> `automationgateway_pg_database` | <br> `gateway_pg_database` | <br>  Name of the PostgreSQL database used by platform gateway. | <br>  Optional | <br>  RPM = `automationgateway`. Container = `gateway`. |
| <br> `automationgateway_pg_host` | <br> `gateway_pg_host` | <br>  Hostname of the PostgreSQL database used by platform gateway. | <br>  Required |  |
| <br> `automationgateway_pg_password` | <br> `gateway_pg_password` | <br>  Password for the platform gateway PostgreSQL database user. Use of special characters for this variable is limited. The `!`, `#`, `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | <br>  Optional |  |
| <br> `automationgateway_pg_port` | <br> `gateway_pg_port` | <br>  Port number for the PostgreSQL database used by platform gateway. | <br>  Optional | <br> `5432` |
| <br> `automationgateway_pg_sslmode` | <br> `gateway_pg_sslmode` | <br>  Controls the SSL mode to use when platform gateway connects to the PostgreSQL database. Valid options include `verify-full`, `verify-ca`, `require`, `prefer`, `allow`, `disable`. | <br>  Optional | <br> `prefer` |
| <br> `automationgateway_pg_username` | <br> `gateway_pg_username` | <br>  Username for the platform gateway PostgreSQL database user. | <br>  Optional | <br>  RPM = `automationgateway`. Container = `gateway` |
| <br> `automationgateway_pgclient_sslcert` | <br> `gateway_pg_tls_cert` | <br>  Path to the PostgreSQL SSL/TLS certificate file for platform gateway. | <br>  Required if using client certificate authentication. |  |
| <br> `automationgateway_pgclient_sslkey` | <br> `gateway_pg_tls_key` | <br>  Path to the PostgreSQL SSL/TLS key file for platform gateway. | <br>  Required if using client certificate authentication. |  |
| <br> `automationgateway_pgclient_tls_files_remote` |  | <br>  Denote whether the PostgreSQL client cert sources are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br>  The value defined in `automationgateway_tls_files_remote` which defaults to `false`. |
| <br> `automationgateway_redis_host` | <br> `gateway_redis_host` | <br>  Hostname of the Redis host used by platform gateway. | <br>  Optional | <br>  First node in the `[automationgateway]` inventory group. |
| <br> `automationgateway_redis_password` | <br> `gateway_redis_password` | <br>  Password for platform gateway Redis. | <br>  Optional | <br>  Randomly generated string. |
| <br> `automationgateway_redis_username` | <br> `gateway_redis_username` | <br>  Username for platform gateway Redis. | <br>  Optional | <br> `gateway` |
| <br> `automationgateway_secret_key` | <br> `gateway_secret_key` | <br>  Secret key value used by platform gateway to sign and encrypt data. | <br>  Optional |  |
| <br> `automationgateway_ssl_cert` | <br> `gateway_tls_cert` | <br>  Path to the SSL/TLS certificate file for platform gateway. | <br>  Optional |  |
| <br> `automationgateway_ssl_key` | <br> `gateway_tls_key` | <br>  Path to the SSL/TLS key file for platform gateway. | <br>  Optional |  |
| <br> `automationgateway_tls_files_remote` | <br> `gateway_tls_remote` | <br>  Denote whether the platform gateway provided certificate files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
| <br> `automationgateway_uwsgi_processes` | <br> `gateway_uwsgi_processes` | <br>  The number of `uwsgi` processes for the platform gateway container. The value is calculated based on the number of available vCPUs (virtual CPUs). | <br>  Optional | <br>  The number of vCPUs multiplied by two, plus one. |
| <br> `automationgateway_use_archive_compression` | <br> `gateway_use_archive_compression` | <br>  Controls whether archive compression is enabled or disabled for platform gateway. You can control this functionality globally by using `use_archive_compression`. | <br>  Optional | <br> `true` |
| <br> `automationgateway_use_db_compression` | <br> `gateway_use_db_compression` | <br>  Controls whether database compression is enabled or disabled for platform gateway. You can control this functionality globally by using `use_db_compression`. | <br>  Optional | <br> `true` |
| <br> `automationgateway_user_headers` | <br> `gateway_nginx_user_headers` | <br>  List of additional NGINX headers to add to platform gateway’s NGINX configuration. | <br>  Optional | <br> `[]` |
| <br> `automationgateway_verify_ssl` |  | <br>  Denotes whether or not to verify platform gateway’s web certificates when making calls from platform gateway to itself during installation. Set to `false` to disable web certificate verification. | <br>  Optional | <br> `true` |
| <br> `automationgatewayproxy_disable_https` | <br> `envoy_disable_https` | <br>  Controls whether or not HTTPS is disabled when accessing the platform UI. Set to `true` to disable HTTPS (HTTP is used instead). | <br>  Optional | <br>  RPM = The value defined in `disable_https` which defaults to `false`. Container = `false`. |
| <br> `automationgatewayproxy_http_port` | <br> `envoy_http_port` | <br>  Port number on which the Envoy proxy listens for incoming HTTP connections. | <br>  Optional | <br> `80` |
| <br> `automationgatewayproxy_https_port` | <br> `envoy_https_port` | <br>  Port number on which the Envoy proxy listens for incoming HTTPS connections. | <br>  Optional | <br> `443` |
| <br> `nginx_tls_protocols` | <br> `gateway_nginx_https_protocols` | <br>  Protocols that platform gateway will support when handling HTTPS traffic. | <br>  Optional | <br> `[TLSv1.2, TLSv1.3]` |
| <br> `redis_disable_tls` | <br> `gateway_redis_disable_tls` | <br>  Controls whether TLS is enabled or disabled for platform gateway Redis. Set this variable to `true` to disable TLS. | <br>  Optional | <br> `false` |
| <br> `redis_port` | <br> `gateway_redis_port` | <br>  Port number for the Redis host for platform gateway. | <br>  Optional | <br> `6379` |
|  | <br> `gateway_extra_settings` | <br>  Defines additional settings for use by platform gateway during installation. <br>  For example:        gateway_extra_settings=[{"setting": "OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']", "value": 600}] | <br>  Optional | <br> `[]` |
|  | <br> `gateway_nginx_client_max_body_size` | <br>  Maximum allowed size for data sent to platform gateway through NGINX. | <br>  Optional | <br> `5m` |
|  | <br> `gateway_nginx_hsts_max_age` | <br>  Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for platform gateway. | <br>  Optional | <br> `63072000` |
|  | <br> `gateway_uwsgi_listen_queue_size` | <br>  Number of requests `uwsgi` will allow in the queue on platform gateway until `uwsgi_processes` can serve them. | <br>  Optional | <br> `4096` |

## A.9. Receptor variables

Inventory file variables for Receptor.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br> `receptor_datadir` |  | <br>  The directory where receptor stores its runtime data and local artifacts. The target directory must be accessible to **awx** users. If the target directory is a temporary file system **tmpfs**, ensure it is remounted correctly after a reboot. Failure to do so results in the receptor no longer having a working directory. | <br>  Optional | <br> `/tmp/receptor` |
| <br> `receptor_listener_port` | <br> `receptor_port` | <br>  Port number that receptor listens on for incoming connections from other receptor nodes. | <br>  Optional | <br> `27199` |
| <br> `receptor_listener_protocol` | <br> `receptor_protocol` | <br>  Protocol that receptor will support when handling traffic. | <br>  Optional | <br> `tcp` |
| <br> `receptor_log_level` | <br> `receptor_log_level` | <br>  Controls the verbosity of logging for receptor. Valid options include: `error`, `warning`, `info`, or `debug`. | <br>  Optional | <br> `info` |
| <br> `receptor_tls` |  | <br>  Controls whether TLS is enabled or disabled for receptor. Set this variable to `false` to disable TLS. | <br>  Optional | <br> `true` |
| <br>  See `node_type` for the RPM equivalent variable. | <br> `receptor_type` | <br>  For the `[automationcontroller]` group the two options are:    <br> `receptor_type=control` - The node only runs project and inventory updates, but not regular jobs. `receptor_type=hybrid` - The node runs everything. <br>  For the `[execution_nodes]` group the two options are:    <br> `receptor_type=hop` - The node forwards jobs to an execution node. `receptor_type=execution` - The node can run jobs. | <br>  Optional | <br>  For the `[automationcontroller]` group: `hybrid`. For the `[execution_nodes]` group: `execution`. |
| <br>  See `peers` for the RPM equivalent variable | <br> `receptor_peers` | <br>  Used to indicate which nodes a specific host connects to. Wherever this variable is defined, an outbound connection to the specific host is established. The value must be a comma-separated list of hostnames. Do not use inventory group names. <br>  This is resolved into a set of hosts that is used to construct the `receptor.conf` file. <br>  For more information, see [Adding execution nodes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/advanced-configuration-containerized#adding-execution-nodes). | <br>  Optional | <br> `[]` |
|  | <br> `receptor_disable_signing` | <br>  Controls whether signing of communications between receptor nodes is enabled or disabled. Set this variable to `true` to disable communication signing. | <br>  Optional | <br> `false` |
|  | <br> `receptor_disable_tls` | <br>  Controls whether TLS is enabled or disabled for receptor. Set this variable to `true` to disable TLS. | <br>  Optional | <br> `false` |
|  | <br> `receptor_firewall_zone` | <br>  The firewall zone where receptor related firewall rules are applied. This controls which networks can access receptor based on the zone’s trust level. | <br>  Optional | <br> `public` |
|  | <br> `receptor_mintls13` | <br>  Controls whether or not receptor only accepts connections that use TLS 1.3 or higher. Set to `true` to only accept connections that use TLS 1.3 or higher. | <br>  Optional | <br> `false` |
|  | <br> `receptor_signing_private_key` | <br>  Path to the private key used by receptor to sign communications with other receptor nodes in the network. | <br>  Optional |  |
|  | <br> `receptor_signing_public_key` | <br>  Path to the public key used by receptor to sign communications with other receptor nodes in the network. | <br>  Optional |  |
|  | <br> `receptor_signing_remote` | <br>  Denote whether the receptor signing files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
|  | <br> `receptor_tls_cert` | <br>  Path to the TLS certificate file for receptor. | <br>  Optional |  |
|  | <br> `receptor_tls_key` | <br>  Path to the TLS key file for receptor. | <br>  Optional |  |
|  | <br> `receptor_tls_remote` | <br>  Denote whether the receptor provided certificate files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
|  | <br> `receptor_use_archive_compression` | <br>  Controls whether archive compression is enabled or disabled for receptor. You can control this functionality globally by using `use_archive_compression`. | <br>  Optional | <br> `true` |

## A.10. Redis variables

Inventory file variables for Redis.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br> `redis_cluster_ip` | <br> `redis_cluster_ip` | <br>  The IPv4 address used by the Redis cluster to identify each host in the cluster. When defining hosts in the `[redis]` group, use this variable to identify the IPv4 address if the default is not what you want. Specific to container: Redis clusters cannot use hostnames or IPv6 addresses. | <br>  Optional | <br>  RPM = Discovered IPv4 address from Ansible facts. If IPv4 address is not available, IPv6 address is used. Container = Discovered IPv4 address from Ansible facts. |
| <br> `redis_disable_mtls` |  | <br>  Controls whether mTLS is enabled or disabled for Redis. Set this variable to `true` to disable mTLS. | <br>  Optional | <br> `false` |
| <br> `redis_firewalld_zone` | <br> `redis_firewall_zone` | <br>  The firewall zone where Redis related firewall rules are applied. This controls which networks can access Redis based on the zone’s trust level. | <br>  Optional | <br>  RPM = no default set. Container = `public`. |
| <br> `redis_hostname` |  | <br>  Hostname used by the Redis cluster when identifying and routing the host. By default `routable_hostname` is used. | <br>  Optional | <br>  The value defined in `routable_hostname` |
| <br> `redis_mode` | <br> `redis_mode` | <br>  The Redis mode to use for your Ansible Automation Platform installation. Valid options include: `standalone` and `cluster`. For more information about Redis, see [Caching and queueing system](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/ha-redis_planning) in *Planning your installation*. | <br>  Optional | <br> `cluster` |
| <br> `redis_server_regen_cert` |  | <br>  Denotes whether or not to regenerate the Ansible Automation Platform managed TLS key pair for Redis. | <br>  Optional | <br> `false` |
| <br> `redis_tls_cert` | <br> `redis_tls_cert` | <br>  Path to the Redis server TLS certificate. | <br>  Optional |  |
| <br> `redis_tls_files_remote` | <br> `redis_tls_remote` | <br>  Denote whether the Redis provided certificate files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
| <br> `redis_tls_key` | <br> `redis_tls_key` | <br>  Path to the Redis server TLS certificate key. | <br>  Optional |  |
|  | <br> `redis_use_archive_compression` | <br>  Controls whether archive compression is enabled or disabled for Redis. You can control this functionality globally by using `use_archive_compression`. | <br>  Optional | <br> `true` |

## A.11. Red Hat Ansible Lightspeed variables

Configure Red Hat Ansible Lightspeed by setting inventory file variables during installation. Use this reference to determine which variables to set for your deployment requirements.

### A.11.1. Red Hat Ansible Lightspeed variables

Inventory file variables for Red Hat Ansible Lightspeed.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br>  N/A | <br> `lightspeed_admin_password` | <br>  Red Hat Ansible Lightspeed administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/`, `"`, or `@`. | <br>  Required |  |
| <br>  N/A | <br> `lightspeed_admin_user` | <br>  Username used to identify and create the Red Hat Ansible Lightspeed admin user. | <br>  Optional | <br> `admin` |
| <br>  N/A | <br> `lightspeed_chat_rate_throttle` | <br>  Chat rate throttle. | <br>  Optional | <br> `10/minute` |
| <br>  N/A | <br> `lightspeed_nginx_client_max_body_size` | <br>  Maximum allowed size for data sent to Red Hat Ansible Lightspeed through NGINX. | <br>  Optional | <br> `5m` |
| <br>  N/A | <br> `lightspeed_nginx_disable_hsts` | <br>  Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for Red Hat Ansible Lightspeed. Set this variable to `true` to disable HSTS. | <br>  Optional | <br> `false` |
| <br>  N/A | <br> `lightspeed_nginx_disable_https` | <br>  Controls whether HTTPS is enabled or disabled for Red Hat Ansible Lightspeed. Set this variable to `true` to disable HTTPS. | <br>  Optional | <br> `false` |
| <br>  N/A | <br> `lightspeed_nginx_hsts_max_age` | <br>  Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for Red Hat Ansible Lightspeed. | <br>  Optional | <br> `63072000` |
| <br>  N/A | <br> `lightspeed_nginx_http_port` | <br>  Port number that Red Hat Ansible Lightspeed listens on for HTTP requests. | <br>  Optional | <br> `8084` |
| <br>  N/A | <br> `lightspeed_nginx_https_port` | <br>  Port number that Red Hat Ansible Lightspeed listens on for HTTPS requests. | <br>  Optional | <br> `8447` |
| <br>  N/A | <br> `lightspeed_nginx_https_protocols` | <br>  Protocols that Red Hat Ansible Lightspeed will support when handling HTTPS traffic. | <br>  Optional | <br> `[TLSv1.2, TLSv1.3]` |
| <br>  N/A | <br> `lightspeed_nginx_user_headers` | <br>  Custom Nginx headers. List of additional NGINX headers to add to Red Hat Ansible Lightspeed’s NGINX configuration. | <br>  Optional | <br>  [] |
| <br>  N/A | <br> `lightspeed_nginx_read_timeout` | <br>  Sets the HTTP timeout for end-user requests. The minimum value is `10` seconds. | <br>  Optional | <br> `3600` |
| <br>  N/A | <br> `lightspeed_pg_cert_auth` | <br>  Controls whether client certificate authentication is enabled or disabled on the Red Hat Ansible Lightspeed PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | <br>  Optional | <br> `false` |
| <br>  N/A | <br> `lightspeed_pg_database` | <br>  Name of the PostgreSQL database used by Red Hat Ansible Lightspeed. | <br>  Optional | <br> `lightspeed` |
| <br>  N/A | <br> `lightspeed_pg_host` | <br>  Hostname of the PostgreSQL database used by Red Hat Ansible Lightspeed. | <br>  Required |  |
| <br>  N/A | <br> `lightspeed_pg_password` | <br>  Password for the Red Hat Ansible Lightspeed PostgreSQL database user. Use of special characters for this variable is limited. The `!`, `#`, `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_pg_port` | <br>  Port number for the PostgreSQL database used by Red Hat Ansible Lightspeed. | <br>  Optional | <br> `5432` |
| <br>  N/A | <br> `lightspeed_pg_sslmode` | <br>  Controls the SSL mode to use when platform gateway connects to the PostgreSQL database. Valid options include `verify-full`, `verify-ca`, `require`, `prefer`, `allow`, `disable`. | <br>  Optional | <br> `prefer` |
| <br>  N/A | <br> `lightspeed_pg_tls_cert` | <br>  Path to the PostgreSQL SSL/TLS certificate file for Red Hat Ansible Lightspeed. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_pg_tls_key` | <br>  Path to the PostgreSQL SSL/TLS key file for Red Hat Ansible Lightspeed. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_pg_username` | <br>  Username for the Red Hat Ansible Lightspeed PostgreSQL database user. | <br>  Optional | <br> `lightspeed` |
| <br>  N/A | <br> `lightspeed_secret_key` | <br>  Secret key value used by Red Hat Ansible Lightspeed to sign and encrypt data. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_tls_cert` | <br>  Path to the SSL/TLS certificate file for Red Hat Ansible Lightspeed. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_tls_key` | <br>  Path to the SSL/TLS key file for Red Hat Ansible Lightspeed. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_tls_remote` | <br>  Denote whether the Red Hat Ansible Lightspeed provided certificate files are local to the installation program (`false`) or on the remote component server (`true`). | <br>  Optional | <br> `false` |
| <br>  N/A | <br> `lightspeed_use_archive_compression` | <br>  Controls whether archive compression is enabled or disabled for Red Hat Ansible Lightspeed. You can control this functionality globally by using `use_archive_compression`. | <br>  Optional | <br> `true` |
| <br>  N/A | <br> `lightspeed_use_db_compression` | <br>  Controls whether database compression is enabled or disabled for Red Hat Ansible Lightspeed. You can control this functionality globally by using `use_db_compression`. | <br>  Optional | <br> `false` |

### A.11.2. Ansible Lightspeed coding assistant variables

Inventory file variables for Ansible Lightspeed coding assistant.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br>  N/A | <br> `lightspeed_wca_model_type` | <br>  IBM watsonx Code Assistant model deployment mode, cloud (`wca`) or on-premise (`wca-onprem`). | <br>  Optional | <br> `wca` |
| <br>  N/A | <br> `lightspeed_wca_model_url` | <br>  URL of the IBM watsonx Code Assistant model. For cloud deployment, the URL could be `https://api.dataplatform.test.cloud.ibm.com`. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_wca_model_api_key` | <br>  API key of the IBM watsonx Code Assistant model that was generated during the model installation. | <br>  Required |  |
| <br>  N/A | <br> `lightspeed_wca_model_id` | <br>  ID of the IBM watsonx Code Assistant model. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_wca_model_verify_ssl` | <br>  Denotes whether or not to verify IBM watsonx Code Assistant’s web certificates when making calls from Red Hat Ansible Lightspeed to itself during installation. Set to `false` to disable web certificate verification. | <br>  Optional | <br> `true` |
| <br>  N/A | <br> `lightspeed_wca_model_enable_anonymization` | <br>  Controls whether the anonymization of Personally Identifiable Information (PII) is enabled. PII information includes passwords, IP addresses, email addresses, and other sensitive data. <br>  When PII anonymization is enabled, users' personal information is modified to some generic values to protect their data and reduce the risk of data leaks. <br>  You can turn off the anonymization by specifying the value as `false` if you want to retain all original information as entered by users and improve the quality of the answers. <br>  If you set the value to `false` and the Ansible administrator is using Red Hat Ansible Lightspeed in hybrid mode (where the model is in IBM watsonx Code Assistant in IBM Cloud) then their users' PII is sent to IBM Cloud. | <br>  Optional | <br> `true` |
| <br>  N/A | <br> `lightspeed_wca_model_username` | <br>  For on-premise deployment only. The username you use to connect to an IBM Cloud Pak for Data deployment. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_wca_health_check` | <br>  Enables or disables IBM watsonx Code Assistant health check. | <br>  Optional | <br> `true` |
| <br>  N/A | <br> `lightspeed_wca_idp_url` | <br>  For cloud deployment only. The IBM watsonx Code Assistant Identity Provider (IdP) URL. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_wca_idp_login` | <br>  For cloud deployment only. The IBM watsonx Code Assistant Identity Provider (IdP) username. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_wca_idp_password` | <br>  For cloud deployment only. The IBM watsonx Code Assistant Identity Provider (IdP) password. | <br>  Optional |  |

### A.11.3. Ansible Lightspeed intelligent assistant variables

Inventory file variables for Ansible Lightspeed intelligent assistant.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br>  N/A | <br> `lightspeed_chatbot_model_url` | <br>  The inference API base URL on your LLM setup. For example, `https://your_inference_api/v1`. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_chatbot_model_verify_ssl` | <br>  Controls whether SSL/TLS certificate verification is enabled or disabled when making HTTPS requests. | <br>  Optional | <br> `true` |
| <br>  N/A | <br> `lightspeed_chatbot_default_provider` | <br>  The provider type of your LLM setup by using one of the following values:    <br>  Red Hat Enterprise Linux AI: `rhelai`  Red Hat OpenShift AI: `rhoai`  OpenAI: `openai`  Microsoft Azure OpenAI: `azure` | <br>  Optional | <br> `rhoai` |
| <br>  N/A | <br> `lightspeed_chatbot_model_extra_settings` | <br>  Use this parameter to pass a JSON dictionary of extra parameters to pass directly to the model provider, for settings not covered by other standard fields. <br>  If you want to use Microsoft Azure OpenAI as the LLM provider, specify the value as `'{"api_type": ""}'`. | <br>  Optional | <br> `{}` |
| <br>  N/A | <br> `lightspeed_chatbot_chatbot_max_tokens` | <br>  Maximum number of tokens to generate a chat response. | <br>  Optional | <br> `4096` |
| <br>  N/A | <br> `lightspeed_chatbot_http_port` | <br>  Port number that Ansible Lightspeed intelligent assistant listens on for HTTP requests. | <br>  Optional | <br> `8085` |
| <br>  N/A | <br> `lightspeed_chatbot_model_id` | <br>  The ID of the LLM model that is configured on your LLM setup. | <br>  Optional |  |
| <br>  N/A | <br> `lightspeed_chatbot_model_api_key` | <br>  The API token or the API key of your LLM setup. This token is sent along with the authorization header when an inference API is called. | <br>  Optional |  |

### A.11.4. Ansible Lightspeed intelligent assistant integration with MCP server variables

Inventory file variables for Ansible Lightspeed intelligent assistant integration with Model Context Protocol (MCP) server.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br>  N/A | <br> `lightspeed_mcp_controller_enabled` | <br>  Controls whether the Ansible Lightspeed MCP controller is enabled or disabled. | <br>  Optional | <br> `false` |
| <br>  N/A | <br> `lightspeed_mcp_controller_port` | <br>  Ansible Lightspeed MCP controller port. | <br>  Optional | <br> `8004` |
| <br>  N/A | <br> `lightspeed_mcp_lightspeed_enabled` | <br>  Ansible Lightspeed MCP lightspeed enabled. | <br>  Optional | <br> `false` |
| <br>  N/A | <br> `lightspeed_mcp_lightspeed_port` | <br>  Ansible Lightspeed MCP lightspeed port. | <br>  Optional | <br> `8005` |

## A.12. Ansible MCP server variables

The following variables govern the access granted to Ansible MCP server.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| <br>  N/A | <br> `mcp_allow_write_operations` | <br>  Determines whether the Ansible MCP server allows actions that modify state, such as launching jobs or updating templates through the external AI tool. <br>  By default, the variable’s value is set to `false`, so that the Ansible MCP server enables read-only operations and blocks all write operations. To enable the Ansible MCP server to perform write operations, change the value of the variable to `true`. | <br>  Optional | <br> `false` |
| <br>  N/A | <br> `mcp_ignore_certificate_errors` | <br>  Specifies whether to skip validation of SSL/TLS certificates when connecting to an MCP server over a secure transport (HTTPS/WSS). <br>  Set this parameter value to `true` to allow connections to servers with self-signed, expired, or otherwise untrusted certificates, primarily during local development or internal testing. | <br>  Optional | <br> `false` |
| <br>  N/A | <br> `mcp_tls_cert` | <br>  Path to the SSL/TLS certificate file for the Ansible MCP server. | <br>  Required if using client certificate authentication. |  |
| <br>  N/A | <br> `mcp_tls_key` | <br>  Path to the SSL/TLS key file for the Ansible MCP server. | <br>  Required if using client certificate authentication. |  |

# Legal Notice

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
