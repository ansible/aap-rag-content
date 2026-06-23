# Install automation dashboard to calculate savings (RHEL only)
## Install automation dashboard
### Configure automation dashboard

Integrate your Ansible Automation Platform instances into the automation dashboard configuration to collect and visualise data and gain insights into your automation.

#### Before you begin

- You have installed automation dashboard.
- You have verified that automation dashboard is running on HTTPS port 8447 on your Red Hat Enterprise Linux host. Note:

* This verification requires your Ansible Automation Platform login details.
* Port 8447 is enabled by default, but this is configurable.

#### Procedure

1.  Configure a personal access token. For more information, see [Configuring access to external applications with token-based authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication#gw-token-based-authentication "Token-based authentication permits authentication of third-party tools and services with the platform through integrated OAuth 2 token support. Ansible Automation Platform utilizes both OAuth Tokens and Personal Access Tokens (PATs).").
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

