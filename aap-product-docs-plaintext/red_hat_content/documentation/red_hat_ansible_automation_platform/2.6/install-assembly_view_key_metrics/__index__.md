# Install automation dashboard to calculate savings (RHEL only)

By effectively using automation dashboard, you can gain valuable insights into your Ansible Automation Platform usage and drive continuous improvement in your automation practices.

## About the automation dashboard

The automation dashboard utility is a web-based container application that provides key metrics related to job execution, efficiency, and the value derived from automation.

Automation dashboard uses automation metrics to supply automation usage data from Ansible Automation Platform. This data helps you compare the cost of performing tasks manually to the cost of performing tasks through automation, allowing you to show what savings are achievable through automation.

**Key benefits**

Automation dashboard helps you:

- Get a clear overview of the automation occurring in your environment.
- Track metrics such as time saved and errors reduced, to quantify the benefits of automation.
- Analyze job execution times and failure rates to pinpoint areas for automation improvement.
- Use the generated data to make informed decisions about automation strategy, resource allocation, and prioritization of automation projects.


**Automation Dashboard and Red Hat Ansible Automation Platform 2.7**

In Red Hat Ansible Automation Platform 2.7, two dashboard solutions are available:

- **Native Automation Dashboard (Technology Preview):** Integrated into Red Hat Ansible Automation Platform 2.7 as part of the Metrics Service. Suitable for single Red Hat Ansible Automation Platform instance monitoring with integrated Red Hat Ansible Automation Platform UI experience.
- **Standalone automation dashboard:** This guide describes the standalone utility, which continues to be supported in Red Hat Ansible Automation Platform 2.7 and later releases. Use the standalone utility when you need:
* Multi-instance monitoring (aggregating data across multiple Red Hat Ansible Automation Platform deployments)
* Independent dashboard infrastructure separate from Red Hat Ansible Automation Platform installation
* Dashboard for Red Hat Ansible Automation Platform versions prior to 2.7

## Choose between standalone and native dashboard (Red Hat Ansible Automation Platform 2.7+)

If you are running Red Hat Ansible Automation Platform 2.7, two dashboard options are available. Use this guidance to determine which dashboard solution meets your needs.

**Use standalone automation dashboard when:**

- **Multi-cluster monitoring is required:** You need to aggregate data across multiple Red Hat Ansible Automation Platform deployments (for example, production, staging, and development environments)
- **Using Red Hat Ansible Automation Platform version is 2.4, 2.5, or 2.6:** Native dashboard is only available in Red Hat Ansible Automation Platform 2.7
- **Independent infrastructure preferred:** You want dashboard infrastructure separate from Red Hat Ansible Automation Platform installation (for example, different security zones, independent scaling, disaster recovery isolation)


**Use native Automation Dashboard (Red Hat Ansible Automation Platform 2.7) when:**

- **Single Red Hat Ansible Automation Platform instance monitoring:** You only need to monitor one Red Hat Ansible Automation Platform deployment
- **Integrated experience preferred:** You want dashboard integrated into Red Hat Ansible Automation Platform unified UI with Gateway authentication
- **No additional infrastructure:** You do not want to deploy separate VMs or containers for dashboard
- **Using a new Red Hat Ansible Automation Platform 2.7 deployment:** You are installing Red Hat Ansible Automation Platform 2.7 for the first time

## Coexistence

Both dashboard solutions can run simultaneously. For example, you might use:

- **Standalone dashboard:** For aggregated view across multiple Red Hat Ansible Automation Platform environments
- **Native dashboard:** For detailed single-instance view of your Red Hat Ansible Automation Platform 2.7 production cluster

## Architecture comparison

**Standalone dashboard infrastructure:**

- Separate RHEL host or VM
- Dedicated PostgreSQL database
- Independent Redis instance
- Podman containerized deployment
- Manual OAuth2 token configuration
- Pulls data by using Red Hat Ansible Automation Platform API


**Native dashboard infrastructure (Technology Preview):**

- Integrated with Metrics Service (no separate VM)
- Uses Metrics Service PostgreSQL database
- Automatic Gateway authentication
- Enabled by using installer flag
- Data collected by Metrics Service backend

## Migration considerations

Important:

There is no automatic migration path from standalone dashboard to native dashboard in Red Hat Ansible Automation Platform 2.7. If you plan to transition from standalone to native dashboard in the future:

- Continue using standalone dashboard until multi-instance support is added to native dashboard (planned for future GA release)
- Contact Red Hat Support for guidance on migration planning

## Install automation dashboard

Install automation dashboard to collect and analyze key metrics related to job execution, efficiency, and automation savings across your Ansible Automation Platform deployments.

### Before you begin

- One of the following tested configurations:
* RHEL 9 or RHEL 10 on x86 or ARM-based physical or virtual hosts.
* With an external database: PostgreSQL v15 database. Important:
Do not install automation dashboard on the same host(s) as Ansible Automation Platform.

- Automation dashboard installation has been tested with the following configuration:
* 80 GB hard drive (depending on data growth)
* 4 vCPUs x 16 GB RAM
* Disk IOPS - 3000
* Handle up to 10,000 jobs/month and 47M summaries/month
* Connects to three Ansible Automation Platform deployments of the same version
- Access to *baseos* and *Ansible Automation Platformstream* repository packages for the RHEL 9 or RHEL 10 host.
- A non-root login account to the RHEL 9 or RHEL 10 host for installation.   * The login account requires `sudo` access to root.
* By default, we use the `$HOMEDIR` of the user account.
- URL details for access to your Ansible Automation Platform instances.
- One of the following supported Red Hat Ansible Automation Platform versions:
* Red Hat Ansible Automation Platform 2.4
* Red Hat Ansible Automation Platform 2.5
* Red Hat Ansible Automation Platform 2.6
* Red Hat Ansible Automation Platform 2.7
- An Ansible Automation Platform OAuth2 token, which is used for communication between the Ansible Automation Platform instances and automation dashboard.
- Access to download the installation bundle providing installation components for the automation dashboard.
- Open firewall access to allow for bidirectional communication between Ansible Automation Platform instances and the automation dashboard.   * This includes HTTPS/443 (or your Ansible Automation Platform configured port) from the dashboard to the Ansible Automation Platform instance(s).
* Port 8447 is the default ingress port for the automation dashboard. This port can be configured during installation.
* RHEL firewall ports that might block 5432 to PostgreSQL.
- A supported version of `ansible-core` installed on supported RHEL versions.

### Procedure

1.  Download the latest installer tar file from access.redhat.com. Navigate to Downloads > Red Hat Ansible Automation Platform Product Software.
2.  Copy the installation source file to your RHEL 9 or RHEL 10 host.
3.  Extract the installation source. This will require ~500Mb. of disk space. Throughout this example we will use the ec2-user home directory: `/home/<username>`.

```bash
tar -xzvf ansible-automation-dashboard-containerized-setup-bundle-0.1-x86_64.tar.gz
cd ansible-automation-dashboard-containerized-setup/
```

4.  Install the required `ansible-core` package.

```bash
cd ansible-automation-dashboard-containerized-setup
sudo dnf install ansible-core
```

5.  Create an application `client_id/client_secret` in your Ansible Automation Platform instance:
1.  Create an OAuth2 application using the following steps :

1. **For Ansible 2.4**:
- Navigate to <https://AAP_CONTROLLER_FQDN/#/applications>
2. **For Ansible 2.5, 2.6, and 2.7**:
- Navigate to <https://AAP_GATEWAY_FQDN/access/applications>
Note:
In Red Hat Ansible Automation Platform 2.5 and later, OAuth2 applications are managed through Red Hat Ansible Automation Platform Gateway, not directly in the automation controller.

3. Add the following information:
- **Name**: automation-dashboard-sso
- **Authorization grant type**: authorization-code
- **Organization**: Default
- **Redirect URIs**: <https://AUTOMATION_DASHBOARD_FQDN/auth-callback>
- **Client type**: Confidential
Note:
The values for **Name**, **Organization**, and HTTPS port number for Ansible Automation Platform are configurable. The examples provided in this document assume use of port 443.

2.  Save the `client_id` and `client_secret information` inputs into the inventory file.
3.  Create an Ansible Automation Platform access token:

1. Navigate to `https://AAP_GATEWAY_FQDN/#/users/<id>/tokens`, and create a token using the following information:
- OAuth application: automation-dashboard-sso
- Scope: read
2. Store the access token and refresh token values. `clusters.yaml` uses these tokens.

6.  Copy the example inventory and change it before running the installation program.

```bash
cp -i inventory.example inventory
vi inventory
```
Important:

- This is an example tested inventory containing default values for Ansible Automation Platform 2.4, 2.5, 2.6, and 2.7.
- You must change the following values to use this inventory configuration in your environment:
* Change the RHEL 9 or RHEL 10 host occurrences from `host.example.com` to your FQDN host
* Change the phrase `TODO` to match your passwords within all `_admin_password` or `_pg_password` values.
* Change the `dashboard_pg_host` value to the IP address or DNS name of the database server.
- For more information, see the [Inventory variables](/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-inventory_file_variables_for_automation_dashboard#GUID-91739484-5e4b-43a7-a0f2-72ef805f6535 "The inventory variables required by the automation dashboard installation program are described in the following table:") section of this document.

```bash
# This is our automation dashboard front-end application
[automationdashboard]
host.example.com ansible_connection=local

# These are required vars for the installation and should not be removed
[automationdashboard:vars]
# Configure AAP OAuth2 authentication.
# aap_auth_provider_name - name as shown on login page.
aap_auth_provider_name=Ansible Automation Platform
# aap_auth_provider_protocol - http or https
aap_auth_provider_protocol=https
# AAP version - 2.4, 2.5, 2.6 or 2.7
aap_auth_provider_aap_version=2.7
# aap_auth_provider_host - AAP IP or DNS name, with optional port
aap_auth_provider_host=my-aap.example.com
# aap_auth_provider_check_ssl - enforce TLS check or not.
aap_auth_provider_check_ssl=true
# aap_auth_provider_client_id and aap_auth_provider_client_secret -
# they are obtained from AAP when OAuth2 application is created in AAP.
aap_auth_provider_client_id=TODO
aap_auth_provider_client_secret=TODO

# Specify amount of old data to synchronize after installation.
# The initial_sync_days=N requests N days of old data, counting from "today".
# The initial_sync_since requests data from the specified date until "today".
# If both are specified, the initial_sync_since will be used.
initial_sync_days=1
# initial_sync_since=2025-08-08

# Hide warnings when insecure https request are made.
# Use this if your AAP uses self-signed TLS certificate.
# show_urllib3_insecure_request_warning=False

# Force clean install-like
# dashboard_update_secret=true

# HTTP/HTTPS settings
# nginx_disable_https=true
# Change nginx_http_port or nginx_https_port if you want to access dashboard on a different TCP port.
# nginx_http_port=8083
# nginx_https_port=8447
# TLS certificate configuration
# The dashboard_tls_cert needs:
#   - contain server certificate, intermediate CA certificates and root CA certificate.
#   - the server certificate must be the first one in the file.
# dashboard_tls_cert=/path/to/tls/dashboard.crt
# dashboard_tls_key=/path/to/tls/dashboard.key

# Enable Django DEBUG.
# django_debug=True

[database]
host.example.com ansible_connection=local
[redis]
host.example.com ansible_connection=local

[all:vars]
redis_mode=standalone

[all:vars]
postgresql_admin_username=postgres
postgresql_admin_password=TODO

# registry_username=
# registry_password=
# AAP Dashboard - mandatory
# --------------------------
dashboard_pg_containerized=True
dashboard_admin_password=TODO
# The value of dashboard_pg_host needs to resolve to an IP address of the database.
# It cannot be localhost or 127.0.0.1.
# It can be IP address of the server.

dashboard_pg_host=host.example.com
dashboard_pg_username=aapdashboard
dashboard_pg_password=TODO
dashboard_pg_database=aapdashboard

bundle_install=true
#
# Relevant if bundle_install=false
# Set container_image_update to True to fetch most recent container images from registry.
# container_image_update=True
#
# Relevant if bundle_install=true
# <full path to the bundle directory>
bundle_dir='{{ lookup("ansible.builtin.env", "PWD") }}/bundle'
# AAP Dashboard - optional
# --------------------------
# Set to True to expose Django admin page.
# nginx_dashboard_admin_exposed=False
```

7.  Install the required Ansible collections. You must complete this step to prevent module resolution errors during the installation.


```
ansible-galaxy collection install -r requirements.yml
```

8.  Run the installation program.

```bash
ansible-playbook -i inventory ansible.containerized_installer.dashboard_install --ask-become-pass
```

### Results

For reference, see the following example output:

```text
PLAY RECAP *********************************************************************************************************************************************
ec2-54-147-26-173.compute-1.amazonaws.com : ok=126  changed=51   unreachable=0    failed=0    skipped=42   rescued=0    ignored=0
localhost                  : ok=12   changed=0    unreachable=0    failed=0    skipped=9    rescued=0    ignored=0
```
Alternative configurations are possible (for example, the database for automation dashboard can be set on a different host). This requires additional changes to variables in the inventory file. Consult the [Inventory variables](/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-inventory_file_variables_for_automation_dashboard#GUID-91739484-5e4b-43a7-a0f2-72ef805f6535 "The inventory variables required by the automation dashboard installation program are described in the following table:") section of this document for available variables.

### Configure automation dashboard

Integrate your Ansible Automation Platform instances into the automation dashboard configuration to collect and visualise data and gain insights into your automation.

#### Before you begin

- You have installed automation dashboard.
- You have verified that automation dashboard is running on HTTPS port 8447 on your Red Hat Enterprise Linux host. Note:

* This verification requires your Ansible Automation Platform login details.
* Port 8447 is enabled by default, but this is configurable.

#### Procedure

1.  Configure a personal access token. For more information, see [Configuring access to external applications with token-based authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_token_based_authentication#gw-token-based-authentication "Token-based authentication permits authentication of third-party tools and services with the platform through integrated OAuth 2 token support. Ansible Automation Platform utilizes both OAuth Tokens and Personal Access Tokens (PATs).").
2.  Create or update the `clusters.yaml` file. You must include the `access_token`, `refresh_token`, `client_id`, and `client_secret` to enable persistent authentication and automatic token rotation.

```yaml
clusters:
- protocol: https
address: <aap_controller_url>
port: 443
access_token: <access_token_string>
refresh_token: <refresh_token_string>
client_id: <client_id_string>
client_secret: <client_secret_string>
verify_ssl: false
name: <unique_cluster_name>
```
Note:
For Red Hat Ansible Automation Platform 2.7 Users: If you only need to monitor a single Red Hat Ansible Automation Platform 2.7 instance, consider using the native Automation Dashboard integrated into Red Hat Ansible Automation Platform 2.7 instead of standalone dashboard. Native dashboard provides an integrated UI experience with Red Hat Ansible Automation Platform Gateway authentication. However, if you need to aggregate data across multiple Red Hat Ansible Automation Platform instances (regardless of version), continue using this standalone dashboard utility.

**Configuring TLS verification**

When configuring the `verify_ssl` parameter, choose the setting that matches your Ansible Automation Platform certificate type:

- **Commercial certificates:** Set `verify_ssl: true`.
- **Self-signed certificates:** Set `verify_ssl: false`. Note:
The automation dashboard cannot verify self-signed certificates against a custom Certificate Authority (CA).

3.  You can add one or more Ansible Automation Platform instances (of the same Ansible Automation Platform version) into the automation dashboard configuration for pulling and combining data by using the following:

Note:
If you only have one Ansible Automation Platform instance, then remove the second entry.

```bash
---
clusters:
- protocol: https            <--- Normally https
address: my-aap.example.com  <--- Can use IP or FQDN without http(s)://
port: 443                <--- Normally 443
access_token: sampleToken    <--- Your preconfigured Ansible Automation Platform read access token
Platform read access token
refresh_token: myRefreshToken
client_id: myClientID
client_secret: myClientSecret
verify_ssl: false        <--- Can be used when using self signed certs
sync_schedules:
- name: Every 5 minutes sync
rrule: DTSTART;TZID=Europe/Ljubljana:20250630T070000 FREQ=MINUTELY;INTERVAL=5
enabled: true
# If there is one Ansible Automation Platform instance, then remove the second entry below.
# Alternately. If there is more than one AAP instance to connect, copy additional entries.
- protocol: https
address: aap2.example.com
port: 443
access_token: WRn2swiqg5spEwUndDkrJoCeg4Qwuw
verify_ssl: true
sync_schedules:
- name: Every 5 minutes sync
rrule: DTSTART;TZID=Europe/Ljubljana:20250630T070000 FREQ=MINUTELY;INTERVAL=5
enabled: true
```
Note:
The `access_token`, `refresh_token`, and `client_secret` are stored in the automation dashboard database. These values are encrypted for security.

4.  Load and activate your automation dashboard configuration. You must copy the configuration file to the container’s `/tmp/` directory. The system automatically removes the file from the container after successful processing.

```bash
podman cp clusters.yaml automation-dashboard-web:/tmp
podman exec -it automation-dashboard-web /venv/bin/python manage.py setclusters /tmp/clusters.yaml
```
Note:
If the system cannot remove the file from the /tmp/ directory, it displays an error message and continues running.
Note:
**Token Rotation:** The automation dashboard rotates tokens internally for security but does not update your local `clusters.yaml` file. If you must re-run the `setclusters` command later, your defined tokens might be expired.

To retrieve the current valid tokens, run the following command and save the output to a new file:

```bash
podman exec -it automation-dashboard-web /venv/bin/python manage.py getclusters --decrypt > clusters_current.yaml
```

### Synchronize data to automation dashboard

Synchronize data from your connected Ansible Automation Platform clusters to the automation dashboard to view the latest automation metrics.

#### Before you begin

- You have installed automation dashboard.
- You have configured the `clusters.yaml` file with your platform details.

#### Procedure

1.  Identify the running automation dashboard container:


```terminal
$ podman ps | grep automation-dashboard-web
```

2.  Run the synchronization command using one of the following methods:


- **Interactive mode:** Run `syncdata` without arguments. You must confirm the synchronization request when prompted.

```terminal
$ podman exec -it automation-dashboard-web /venv/bin/python manage.py syncdata
```

- **Noninteractive mode:** Use the `--since` and `--until` flags to define the date range. This method bypasses the user prompt and is required for automated scripts or `cron` jobs.

```terminal
$ podman exec -it automation-dashboard-web /venv/bin/python manage.py syncdata --since=2024-01-01 --until=2024-06-30
```

#### Results

1. Verify that the terminal displays the success message: `Successfully created Sync task for Cluster <cluster_url>`.
2. Refresh automation dashboard in your browser to view the updated metrics.

### Verify cluster access tokens

After you configure and load your cluster data, verify the stored access tokens for debugging purposes.

#### Procedure

1.  Use the `getclusters` management command with the `--decrypt` option to display the stored `access_token` and `refresh_token` in plain text.
2.  Run the following command inside the `automation-dashboard-web` container:


```bash
podman exec -it automation-dashboard-web /venv/bin/python ./manage.py getclusters --decrypt
```

3.  Review the output to confirm that the stored tokens are correct and up-to-date.

```bash
clusters:
- protocol: https
address: my-aap.example.com
port: 443
access_token: sampleToken
refresh_token: myRefreshToken
client_id: myClientID
client_secret: myClientSecret
verify_ssl: false
sync_schedules:
- name: Every 5 minutes sync
rrule: DTSTART;TZID=Europe/Ljubljana:20250630T070000 FREQ=MINUTELY;INTERVAL=5
enabled: true
```
Note:
Displaying the encrypted `access_token` and `refresh_token` in plain text for debugging requires the `--decrypt` flag. Do not use this command on unsecured systems.

You can write output produced by `./manage.py getclusters --decrypt` to a file `clusters.yaml` and use it as input for `./manage.py setclusters clusters.yaml`.

#### Results

If you come across error messages during installation, consult the following table:

| Issue         | Possible Cause                                                                                                               | Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>401 error | <br>This is an unauthorized access message indicating authentication errors such as wrong credentials or tokens.             | <br>Verify that your access token is correct in `clusters.yaml`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <br>401 error | <br>A temporary 401 error is expected behavior when the token expires, followed immediately by trying to refresh.            | <br>If the automatic token refresh fails (for example, due to invalid `client_secret` or `refresh_token`), use the `getclusters``--decrypt` command to manually verify that the credentials stored in the database match those in your source `clusters.yaml` file. If they do not match, re-run the `setclusters` command with the correct configuration. You can only use the refresh token once. If you need to execute `setclusters` because of invalid access token, create new access and refresh tokens, and use them in your source `clusters.yaml`. |
| <br>404 error | <br>This is a “not found” message indicating that something is not configured correctly or pointing to the correct endpoint. | <br>Verify that your Ansible Automation Platform instance URLs used in `clusters.yaml` are correct.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |


A successful installation should be running the following three container services:

```bash
podman ps --all --format "{{.Names}}"

postgresql
automation-dashboard-task
automation-dashboard-web
```
You can check your container logs by running the following:

```bash
journalctl CONTAINER_NAME=container (where container equals one of postgresql automation-dashboard-task or automation-dashboard-web)

For example:
journalctl CONTAINER_NAME=automation-dashboard-task
May 22 13:02:07 automation-dashboard automation-dashboard-task[1607]: [wait-for-migrations-dashboard.sh] Waiting for database migrations...
May 22 13:02:07 automation-dashboard automation-dashboard-task[1607]: [wait-for-migrations-dashboard.sh] Attempt 1
May 22 13:02:10 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:10,636 periodic 2 140568371550016 Starting sync task.
May 22 13:02:10 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:10,636 periodic 2 140568371550016 Retrieving clusters inform>
May 22 13:02:10 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:10,747 periodic 2 140568371550016 Retrieved 1 clusters.
May 22 13:02:10 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:10,761 periodic 2 140568371550016 Retrieving data from clust>
May 22 13:02:10 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:10,761 connector 2 140568371550016 Checking Ansible Automation Platform version at h>
May 22 13:02:10 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:10,761 connector 2 140568371550016 Checking if is Ansible Automation Platform 2.5 at>
May 22 13:02:10 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:10,761 connector 2 140568371550016 Pinging api https://ec2-3>
May 22 13:02:10 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:10,761 connector 2 140568371550016 Executing GET request to >
May 22 13:02:13 automation-dashboard automation-dashboard-task[1607]: ERROR 2025-05-22 13:02:13,820 connector 2 140568371550016 GET request failed with >
May 22 13:02:13 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:13,821 connector 2 140568371550016 Checking if is Ansible Automation Platform 2.4 at>
May 22 13:02:13 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:13,821 connector 2 140568371550016 Pinging api https://ec2-3>
May 22 13:02:13 automation-dashboard automation-dashboard-task[1607]: INFO 2025-05-22 13:02:13,821 connector 2 140568371550016 Executing GET request to >
May 22 13:02:16 automation-dashboard automation-dashboard-task[1607]: ERROR 2025-05-22 13:02:16,892 connector 2 140568371550016 GET request failed with ...
```
The following log snippet shows a successful token refresh:

Note:

This log snippet omits timestamps and hostname for brevity.

**Example**

```bash
journalctl CONTAINER_NAME=automation-dashboard-task
INFO Checking if is AAP 2.5 ... 2.6 at https://app.example.com:443
INFO Pinging api https://app.example.com:443/api/gateway/v1/ping/
INFO Detected AAP version AAP 2.6 at https://app.example.com:443
INFO Executing GET request to https://app.example.com:443/api/controller/v2/organizations/?page_size=100&page=1
ERROR GET request failed with status 401
INFO Token refresh POST request succeeded with status 201
ERROR GET after reauth response.status_code=200
INFO Executing GET request to https://app.example.com:443/api/controller/v2/job_templates/?page_size=200&page=1
Executing GET request to https://app.example.com:443/api/controller/v2/jobs/?page_size=100&page=1&order_by=finished&finished__gt=2025-10-23T13:01:09.768681Z
```
Check how the services are running by using `systemd`:

```bash
systemctl status --user

● automation-dashboard
State: running
Units: 76 loaded (incl. loaded aliases)
Jobs: 0 queued
Failed: 0 units
Since: Thu 2025-05-22 13:02:07 UTC; 22min ago
systemd: 252-51.el9
CGroup: /user.slice/user-1000.slice/user@1000.service
├─app.slice
│ ├─automation-dashboard-task.service
│ │ └─1607 /usr/bin/conmon --api-version 1 -c 84e46532e8ca31b0cadb037479289d030103aa01b7a1591e62b83b17f031e47d -u 84e46532e8ca31b0cadb037479>
│ ├─automation-dashboard-web.service
│ │ └─1608 /usr/bin/conmon --api-version 1 -c d060f3e3fb2b4c4c5c588149253beed83c78ccc9c9a8c1bf4c96157142a210dc -u d060f3e3fb2b4c4c5c58814925>
│ ├─dbus-broker.service
│ │ ├─1621 /usr/bin/dbus-broker-launch --scope user
│ │ └─1624 dbus-broker --log 4 --controller 9 --machine-id 612db98503014199bfd8c788c8d3da58 --max-bytes 100000000000000 --max-fds 2500000000>
│ └─postgresql.service
│   └─1614 /usr/bin/conmon --api-version 1 -c eec61745cb6fc3a89a4f7475d7ef63b5899699157d943c2f16a3243311927bef -u eec61745cb6fc3a89a4f7475d7>
├─init.scope
│ ├─1093 /usr/lib/systemd/systemd --user
│ └─1128 "(sd-pam)"
└─user.slice
├─libpod-84e46532e8ca31b0cadb037479289d030103aa01b7a1591e62b83b17f031e47d.scope
│ └─container
│   ├─1619 /usr/bin/dumb-init -- /usr/bin/launch_dashboard_task.sh
│   └─1681 /venv/bin/python periodic.py
├─libpod-d060f3e3fb2b4c4c5c588149253beed83c78ccc9c9a8c1bf4c96157142a210dc.scope
│ └─container
│   ├─1617 /usr/bin/dumb-init -- /usr/bin/launch_dashboard_web.sh
│   ├─1646 /usr/bin/python3.9 /usr/local/bin/supervisord -c /etc/supervisord_dashboard_web.conf
│   ├─1877 /bin/bash /usr/local/bin/stop-supervisor
│   ├─1878 "nginx: master process nginx -g daemon off;"
│   ├─1879 /venv/bin/uwsgi /etc/tower/uwsgi.ini
│   ├─1880 "nginx: worker process"
│   ├─1881 "nginx: worker process"
│   ├─1882 "nginx: worker process"
│   ├─1883 "nginx: worker process"
│   ├─1884 /venv/bin/uwsgi /etc/tower/uwsgi.ini
│   ├─1885 /venv/bin/uwsgi /etc/tower/uwsgi.ini
│   ├─1886 /venv/bin/uwsgi /etc/tower/uwsgi.ini
│   ├─1887 /venv/bin/uwsgi /etc/tower/uwsgi.ini
│   └─1888 /venv/bin/uwsgi /etc/tower/uwsgi.ini
├─libpod-eec61745cb6fc3a89a4f7475d7ef63b5899699157d943c2f16a3243311927bef.scope
│ └─container
│   ├─1623 postgres
│   ├─1869 "postgres: logger "
│   ├─1871 "postgres: checkpointer "
│   ├─1872 "postgres: background writer "
│   ├─1873 "postgres: walwriter "
│   ├─1874 "postgres: autovacuum launcher "
│   ├─1875 "postgres: stats collector "
│   ├─1876 "postgres: logical replication launcher "
│   └─1889 "postgres: aapdashboard aapdashboard 172.31.28.99(39338) idle"
└─podman-pause-b6c4e853.scope
└─1359 catatonit -P
```

### Uninstall automation dashboard

Uninstall automation dashboard and its dependencies by using a single command, ensuring a clean removal from your host.

#### Procedure

Run the following command to uninstall automation dashboard and its dependencies, including the PostgreSQL database container:

```bash
ansible-playbook -i inventory
ansible.containerized_installer.dashboard_uninstall
```


Note:

Uninstalling automation dashboard permanently deletes all collected metrics data, saved reports, and the PostgreSQL database.
