# Upgrade your containerized deployment of Ansible Automation Platform

Perform an upgrade of containerized Ansible Automation Platform.

## Before you begin

- You have reviewed the upgrade planning information and determined your upgrade path. For more information, see [Determine your upgrade path](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-determine_your_upgrade_path "Use these reference tables to find the supported upgrade paths for your Ansible Automation Platform deployment.").
- You have reviewed the release notes for the associated release. For more information, see [Release notes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/../whats-new/platform-intro.html "Ansible Automation Platform unifies comprehensive automation capabilities, a robust ecosystem, and flexible deployment options into one strategic solution. It enables customers to automate and orchestrate workflows across domains for efficient, resilient, and consistent IT operations at scale.").
- You have a backup of your Ansible Automation Platform deployment. For more information, see [Back up containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment#backing-up-containerized-ansible-automation-platform "Perform a backup of your container-based installation of Ansible Automation Platform.").
- If you are deploying metrics service with an external database, you have provisioned the `metrics_service` database. Metrics service requires access to two databases:
* `metrics_service` database (read/write): Create a new database for metrics service data storage
* `awx/`automation controller database (read-only): Metrics service requires read-only access to the existing controller database

Important:

Ansible Automation Platform 2.7 requires metrics service when automation controller is present. Review the requirements below to determine if you need to provision additional infrastructure:

- **Growth topology (all-in-one):** No additional hardware required. Metrics service shares the existing host.
- **Multi-node deployments:** Provision a new dedicated host for metrics service with the following specifications:
* CPU: 2 vCPUs minimum, 4 vCPUs recommended
* RAM: 4 GB minimum, 8 GB recommended
* Storage: 20 GB minimum, 40 GB+ recommended (SSD preferred)
- **External database with event stream database user:** If you use an external PostgreSQL database, verify that a dedicated eda_event_stream database user exists on your Event-Driven Ansible database before upgrading. This user requires only CONNECT privileges and is required for event stream operations in Ansible Automation Platform 2.7. For more information, see [Configure an external database for event streams](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_event_streams "Event-Driven Ansible event streams require a dedicated PostgreSQL database user (eda_event_stream) for security and access control. This user must exist on the Event-Driven Ansible database and requires only CONNECT privileges.").

## Procedure

1. Log in to the Red Hat Enterprise Linux host as your dedicated non-root user.
2. Follow the steps in [Download Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_downloading_containerized_aap "Choose the installation program you need based on your Red Hat Enterprise Linux environment internet connectivity and download the installation program to your Red Hat Enterprise Linux host.") to download the latest version of containerized Ansible Automation Platform.
3. Copy the downloaded installation program to your Red Hat Enterprise Linux Host.
1. Edit the `inventory` file to add the required `[automationmetrics]` group and update any other parameters to match your required configuration.
You can keep the same parameters from your existing Ansible Automation Platform deployment, but you must add the `[automationmetrics]` inventory group unless you set `automationmetrics_skip_install=true`.

Important:

- The `[automationmetrics]` inventory group is required in Ansible Automation Platform 2.7 when `[automationcontroller]` is present unless you set `automationmetrics_skip_install=true ` in the `[all:vars]` section of your inventory file. Without either the inventory group or the skip variable, the installer fails preflight checks.
- If the automation metrics service is excluded:
* Automation dashboard is unavailable (no backend data source).
* No anonymized usage data is collected or transmitted to Red Hat.
* ROI calculations, automation savings metrics, and executive reporting data are not available.
Example for growth topology (all-in-one):

```
[automationmetrics]
aap.example.org
```

Example for multi-node deployment:

```
[automationmetrics]
metrics.example.org
```

Example to skip metrics-service installation:

```
[all:vars]
automationmetrics_skip_install=true
```

When `automationmetrics_skip_install=true` is set, omit the `[automationmetrics]` inventory group from your inventory file.

4. Add the following variables to the `[all:vars]` section:


```
# Metrics Service
automationmetrics_pg_host=<database_host>
automationmetrics_pg_database=metrics_service
automationmetrics_pg_username=metrics_service
automationmetrics_pg_password=<set your own>

# Read-only access to controller database
automationmetrics_controller_read_pg_host=<database_host>
automationmetrics_controller_read_pg_database=awx
automationmetrics_controller_read_pg_username=ms_awx_readonly
automationmetrics_controller_read_pg_password=<set your own>
```

Note:
The value of `automationmetrics_controller_read_pg_database` is either `awx` (the default) or the custom controller database name.
For complete inventory examples, see [Container growth topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-task_install_metrics_service_with_containerized_installer "Enable and configure metrics service during containerized installation to automatically collect anonymized usage data and transmit it to Red Hat.") or [Container enterprise topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_understand_automation_dashboard_architecture "This module explains the automation dashboard architecture in Red Hat Ansible Automation Platform 2.7, including its integration with metrics service, deployment options.").

5. Run the `install` playbook:


```
$ ansible-playbook -i inventory ansible.containerized_installer.install
```

- If your privilege escalation requires a password to be entered, append `-K` to the command. You will then be prompted for the `BECOME` password.
- You can use increasing verbosity, up to 4 v's (`-vvvv`) to see the details of the installation process. However it is important to note that this can significantly increase installation time, so it is recommended that you use it only as needed or requested by Red Hat support.

## Results

After a successful upgrade, your Ansible Automation Platform deployment is running the new version.

Verify that the platform is operational, including automation controller, platform gateway, and the other components in your deployment.

As part of this release, confirm that metrics service is also operational:

Verify metrics service is operational:

1. Check metrics service status by using the platform gateway.
2. Review metrics service logs for any errors.

## What to do next

After you have completed the upgrade, perform the following tasks:

- [Post-upgrade requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements#ref-post-upgrade-requirements "After upgrading to Ansible Automation Platform 2.7, update tokens, scripts, and integrations to use platform gateway for all external authentication and API access."): Update tokens, scripts, and integrations to use platform gateway for all external authentication and API access.
- [Upgrade metrics service](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-task_upgrade_metrics_service "Safely upgrade metrics service when upgrading Ansible Automation Platform to benefit from new features and bug fixes while maintaining continuous data collection."): If you installed metrics service, upgrade it to benefit from new features and bug fixes.
