# Upgrade your containerized deployment of Ansible Automation Platform

Perform an upgrade of containerized Ansible Automation Platform.

## Before you begin

- You have reviewed the release notes for the associated release. For more information, see [Release notes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/platform_intro "Ansible Automation Platform unifies comprehensive automation capabilities, a robust ecosystem, and flexible deployment options into one strategic solution. It enables customers to automate and orchestrate workflows across domains for efficient, resilient, and consistent IT operations at scale.").
- You have a backup of your Ansible Automation Platform deployment. For more information, see [Back up containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment#backing-up-containerized-ansible-automation-platform "Perform a backup of your container-based installation of Ansible Automation Platform.").
- You have provisioned the `metrics_service` database if using an external database. Metrics service requires access to two databases:
* `metrics_service` database (read/write): Create a new database for metrics service data storage
* `awx`/automation controller database (read-only): Metrics service requires read-only access to the existing controller database

Important:

Ansible Automation Platform 2.7 requires metrics service when automation controller is present. Review the requirements below to determine if you need to provision additional infrastructure:

- **Growth topology (all-in-one):** No additional hardware required. Metrics service shares the existing host.
- **Multi-node deployments:** Provision a new dedicated host for metrics service with the following specifications:
* CPU: 2 vCPUs minimum, 4 vCPUs recommended
* RAM: 4 GB minimum, 8 GB recommended
* Storage: 20 GB minimum, 40 GB+ recommended (SSD preferred)

## Procedure

1.  Log in to the Red Hat Enterprise Linux host as your dedicated non-root user.
2.  Follow the steps in [Download Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_downloading_containerized_aap "Choose the installation program you need based on your Red Hat Enterprise Linux environment internet connectivity and download the installation program to your Red Hat Enterprise Linux host.") to download the latest version of containerized Ansible Automation Platform.
3.  Copy the downloaded installation program to your Red Hat Enterprise Linux Host.
4.  Edit the `inventory` file to add the required `[automationmetrics]` group and update any other parameters to match your required configuration.
You can keep the same parameters from your existing Ansible Automation Platform deployment, but you must add the `[automationmetrics]` inventory group.

Important:
The `[automationmetrics]` inventory group is required in Ansible Automation Platform 2.7 when `[automationcontroller]` is present. The installer will fail preflight checks if this group is missing.

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

5.  Add the following variables to the `[all:vars]` section:


```
# Metrics Service
automationmetrics_pg_host=<database_host>
automationmetrics_pg_database=metrics_service
automationmetrics_pg_username=metrics_service
automationmetrics_pg_password=<set your own>

# Read-only access to controller database
automationmetrics_controller_read_pg_host=<database_host>
automationmetrics_controller_read_pg_database=<controller_db_name>
automationmetrics_controller_read_pg_username=ms_awx_readonly
automationmetrics_controller_read_pg_password=<set your own>
```

For complete inventory examples, see [Container growth topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-task_install_metrics_service_with_containerized_installer "Enable and configure metrics service during containerized installation to automatically collect anonymized usage data and transmit it to Red Hat.") or [Container enterprise topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-con_understand_automation_dashboard_architecture "This module explains the automation dashboard architecture in Red Hat Ansible Automation Platform 2.7, including its integration with metrics service, deployment options, and Technology Preview limitations.").

6.  Run the `install` playbook:


```
$ ansible-playbook -i inventory ansible.containerized_installer.install
```

- If your privilege escalation requires a password to be entered, append `-K` to the command. You will then be prompted for the `BECOME` password.
- You can use increasing verbosity, up to 4 v's (`-vvvv`) to see the details of the installation process. However it is important to note that this can significantly increase installation time, so it is recommended that you use it only as needed or requested by Red Hat support.

## Results

After successful upgrade, metrics service is running on the host defined in the `[automationmetrics]` inventory group.

Verify metrics service is operational:

1. Check metrics service status by using the platform gateway.
2. Review metrics service logs for any errors.
