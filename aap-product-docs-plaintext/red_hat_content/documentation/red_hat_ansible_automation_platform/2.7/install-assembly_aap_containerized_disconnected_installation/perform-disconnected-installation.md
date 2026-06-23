# Install in a disconnected environment
## Obtain and configure RPM source dependencies
### Perform a disconnected installation

A disconnected installation installs containerized Ansible Automation Platform without requiring network access to external registries.

#### Before you begin

- You have prepared the Red Hat Enterprise Linux host
- You have obtained and configured the RPM source dependencies. The installation program uses your host system’s `dnf` package manager to resolve these dependencies.
- You have prepared the managed nodes
- You have downloaded the containerized Ansible Automation Platform setup bundle from the [Ansible Automation Platform download page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software).
- You understand that metrics service is a required component in Ansible Automation Platform 2.7 and will be installed automatically. Metrics service operates fully in disconnected environments without requiring internet access.

#### Procedure

1.  Log in to the Red Hat Enterprise Linux host as your non-root user.
2.  Update the inventory file by following the steps in [Configure the inventory file](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_configuring_inventory_file#configuring-inventory-file___inventory_file_for_online_installation_for_containerized_enterprise_topology). Note:
Do not include `registry_username` or `registry_password` in your inventory file for disconnected installations. These variables are only required for online installations. All container images are pre-packaged in the setup bundle.

3.  Ensure you include the following variables in your inventory file under the `[all:vars]` group:


```
bundle_install=true
# The bundle directory must include /bundle in the path
bundle_dir='{{ lookup("ansible.builtin.env", "PWD") }}/bundle'
```

4.  Follow the steps in [Install containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_installing_containerized_aap#installing-containerized-aap "Run the install playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.") to install containerized Ansible Automation Platform and verify your installation.

#### Metrics service in disconnected environments

Metrics service is a required component in Ansible Automation Platform 2.7 and is fully functional in disconnected environments. The service collects and stores automation metrics locally without requiring internet connectivity.

##### Data collection behavior

In disconnected environments, metrics service operates as follows:

**Local data collection and storage:**

- Metrics service collects automation activity data from automation controller
- All metrics data is stored in the local `metrics_service` database
- Users can access metrics dashboards and reports through the automation dashboard (when enabled)
- No internet connection is required for metrics collection or local analysis


**Optional data transmission to Red Hat:**

- By default, metrics service attempts to transmit anonymized usage data to Red Hat at `api.segment.io:443`
- In disconnected environments, this transmission fails silently and does not affect metrics service functionality
- You can disable data transmission by setting the `ANONYMIZED_DATA_COLLECTION` feature enabled flag to false by using the database

##### Disable data transmission only (recommended for opt-out)

To stop all data transmission to Red Hat while keeping the service installed and collecting local metrics, disable the `ANONYMIZED_DATA_COLLECTION` setting.

This method takes effect on the next scheduled task cycle and does not require a service restart.

**Database setting**

Connect to the metrics service database and update the dynamic settings table:

```
UPDATE dynamic_settings_setting
SET current_value = 'false'
WHERE setting_key = 'ANONYMIZED_DATA_COLLECTION';
```
This change takes effect immediately. No restart is required.

**What happens when data transmission is disabled**

- The `daily_anonymize_and_prepare` task skips execution on its next scheduled run.
- No data is transmitted to Segment.com.
- Local hourly collection, daily snapshots, rollup, and cleanup tasks continue to run normally (controlled by the separate `METRICS_COLLECTION` flag).
- Any data already collected but not yet transmitted is not sent. It is purged during the next scheduled cleanup cycle.
- System maintenance tasks (database cleanup, health checks) continue to run.

##### Firewall configuration for disconnected environments

In disconnected environments, metrics service does not require outbound internet access. Ensure the following internal connectivity:

*Table 1. Metrics service network connectivity requirements*

| Source                | Destination                                | Port | Protocol | Purpose                             |
| --------------------- | ------------------------------------------ | ---- | -------- | ----------------------------------- |
| Metrics service       | PostgreSQL (metrics\_service database)     | 5432 | TCP      | Read/write metrics data             |
| Metrics service       | PostgreSQL (automationcontroller database) | 5432 | TCP      | Read-only access to automation data |
| Automation controller | Metrics service                            | 443  | TCP      | Internal metrics collection API     |


Note:

Port 443 outbound to `cert.console.redhat.com` is optional and only required if you want to enable anonymized data transmission to Red Hat (not applicable in disconnected environments).
