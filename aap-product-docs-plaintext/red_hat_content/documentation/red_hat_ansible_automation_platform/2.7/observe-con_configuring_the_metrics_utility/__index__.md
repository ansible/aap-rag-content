# Configure the `metrics-utility`

Configure the `metrics-utility` to gather and report usage data for your Ansible Automation Platform, both on Red Hat Enterprise Linux and OpenShift Container Platform.

## Configure the `metrics-utility` on Red Hat Enterprise Linux

You can configure the `metrics-utility` on a Red Hat Enterprise Linux system to gather and report usage metrics for automation controller.

### Before you begin

- **Subscription:** An active Ansible Automation Platform subscription.
- **Installation:** The `metrics-utility` tool is included by default with the Ansible Automation Platform installation on the automation controller node. No separate installation is required.
- **User privileges:** You must be logged in as the `root` user or the `awx` user to run the `metrics-utility` tool.


Important:

The `metrics-utility` requires read access to `/etc/tower/SECRET_KEY` to function correctly. Attempting to run this utility as a standard user (non-root or non-awx) results in a `PermissionError` and execution failure.

The following procedure gathers the relevant data and generate a [CCSP](https://connect.redhat.com/en/programs/certified-cloud-service-provider) report containing your usage metrics. You can configure these commands as `cron` jobs to ensure they run at the beginning of every month. See [How to schedule jobs using the Linux `cron` utility](https://www.redhat.com/sysadmin/linux-cron-command) for more on configuring using the cron syntax.

### Procedure

1.  Create two scripts in your user’s home directory to set correct variables to ensure that `metrics-utility` gathers all relevant data.   1.  In `/home/my-user/cron-gather`:


```
#!/bin/sh

# Specify the following variables to indicate where the report is deposited in your file system
export METRICS_UTILITY_SHIP_TARGET=directory
export METRICS_UTILITY_SHIP_PATH=/awx_devel/awx-dev/metrics-utility/shipped_data/billing

# Run the following command to gather and store the data in the provided SHIP_PATH directory:
metrics-utility gather_automation_controller_billing_data --ship --until=10m
```

2.  In `/home/my-user/cron-report`:


```
#!/bin/sh

# Specify the following variables to indicate where the report is deposited in your file system
export METRICS_UTILITY_SHIP_TARGET=directory
export METRICS_UTILITY_SHIP_PATH=/awx_devel/awx-dev/metrics-utility/shipped_data/billing

# Set these variables to generate a report:
export METRICS_UTILITY_REPORT_TYPE=CCSPv2
export METRICS_UTILITY_PRICE_PER_NODE=11.55 # in USD
export METRICS_UTILITY_REPORT_SKU=MCT3752MO
export METRICS_UTILITY_REPORT_SKU_DESCRIPTION="EX: Red Hat Ansible Automation Platform, Full Support (1 Managed Node, Dedicated, Monthly)"
export METRICS_UTILITY_REPORT_H1_HEADING="CCSP Reporting <Company>: ANSIBLE Consumption"
export METRICS_UTILITY_REPORT_COMPANY_NAME="Company Name"
export METRICS_UTILITY_REPORT_EMAIL="email@email.com"
export METRICS_UTILITY_REPORT_RHN_LOGIN="test_login"
export METRICS_UTILITY_REPORT_COMPANY_BUSINESS_LEADER="BUSINESS LEADER"
export METRICS_UTILITY_REPORT_COMPANY_PROCUREMENT_LEADER="PROCUREMENT LEADER"

# Build the report
metrics-utility build_report
```

2.  To ensure that these files are executable, run:
`chmod a+x /home/my-user/cron-gather /home/my-user/cron-report`

3.  To open the `cron` file for editing, run:
`crontab -e`

4.  To configure the run schedule, add the following parameters to the end of the file and specify how often you want `metrics-utility` to gather information and build a report using [cron syntax](https://www.redhat.com/sysadmin/linux-cron-command). In the following example, the `gather` command is configured to run every hour at 00 minutes. The `build_report` command is configured to run on the second day of each month at 4:00 AM.  `0 */1 * * * /home/my-user/cron-gather`

`0 4 2 * * /home/my-user/cron-report`

5.  Save and close the file.

### Results

Use the following verification steps to ensure correct configuration:

1. To confirm that your `cron` job entries have been saved correctly, run:

```
crontab -l
```

2. Inspect the `cron` log to verify that the `cron` daemon is executing the commands and that `metrics-utility` is producing output:

```
cat /var/log/cron
```
For reference, see the following example output:



```
May  8 09:45:03 ip-10-0-6-23 CROND[51623]: (root) CMDOUT (No billing data for month: 2024-04)
May  8 09:45:03 ip-10-0-6-23 CROND[51623]: (root) CMDEND (metrics-utility build_report)
May  8 09:45:19 ip-10-0-6-23 crontab[51619]: (root) END EDIT (root)
May  8 09:45:34 ip-10-0-6-23 crontab[51659]: (root) BEGIN EDIT (root)
May  8 09:46:01 ip-10-0-6-23 CROND[51688]: (root) CMD (metrics-utility gather_automation_controller_billing_data --ship --until=10m)
May  8 09:46:03 ip-10-0-6-23 CROND[51669]: (root) CMDOUT (/tmp/9e3f86ee-c92e-4b05-8217-72c496e6ffd9-2024-05-08-093402+0000-2024-05-08-093602+0000-0.tar.gz)
May  8 09:46:03 ip-10-0-6-23 CROND[51669]: (root) CMDEND (metrics-utility gather_automation_controller_billing_data --ship --until=10m)
May  8 09:46:26 ip-10-0-6-23 crontab[51659]: (root) END EDIT (root)
```
The generated report will have the default name `CCSP-<YEAR>-<MONTH>.xlsx` and is saved in the ship path that you specified in step 1a.

Note:

Time and date might vary depending on how your configure the run schedule.

## Configure the `metrics-utility` on OpenShift Container Platform from the Ansible Automation Platform operator

The `metrics-utility` is a command-line tool that collects and reports metrics from your OpenShift Container Platform cluster to your automation controller instance.

`metrics-utility` is included in the OpenShift Container Platform image beginning with version 4.12, 4.512, and 4.6. If your system does not have `metrics-utility` installed, update your OpenShift image to the latest version.

Complete the following steps to configure the run schedule for `metrics-utility` on OpenShift Container Platform using the Ansible Automation Platform operator:

### Create a ConfigMap in the OpenShift UI YAML view

Learn how to create a ConfigMap in the OpenShift UI YAML view to inject configuration data for the `metrics-utility` cronjobs.

#### Before you begin

- A running OpenShift cluster
- An operator-based installation of Ansible Automation Platform on OpenShift Container Platform.


Note:

`metrics-utility` runs as indicated by the parameters you set in the configuration file. You cannot run the utility manually on OpenShift Container Platform.

#### About this task

To inject the `metrics-utility` cronjobs with configuration data, and create a ConfigMap in the OpenShift UI YAML view:

#### Procedure

1.  From the navigation panel, select ConfigMaps.
2.  Click Create ConfigMap.
3.  On the next screen, select the YAML view tab.
4.  In the YAML field, enter the following parameters with the appropriate variables set:


```
apiVersion: v1
kind: ConfigMap
metadata:
name: automationcontroller-metrics-utility-configmap
data:
METRICS_UTILITY_SHIP_TARGET: directory
METRICS_UTILITY_SHIP_PATH: /metrics-utility
METRICS_UTILITY_REPORT_TYPE: CCSPv2
METRICS_UTILITY_PRICE_PER_NODE: '11' # in USD
METRICS_UTILITY_REPORT_SKU: MCT3752MO
METRICS_UTILITY_REPORT_SKU_DESCRIPTION: "EX: Red Hat Ansible Automation Platform, Full Support (1 Managed Node, Dedicated, Monthly)"
METRICS_UTILITY_REPORT_H1_HEADING: "CCSP Reporting <Company>: ANSIBLE Consumption"
METRICS_UTILITY_REPORT_COMPANY_NAME: "Company Name"
METRICS_UTILITY_REPORT_EMAIL: "email@email.com"
METRICS_UTILITY_REPORT_RHN_LOGIN: "test_login"
METRICS_UTILITY_REPORT_COMPANY_BUSINESS_LEADER: "BUSINESS LEADER"
METRICS_UTILITY_REPORT_COMPANY_PROCUREMENT_LEADER: "PROCUREMENT LEADER"
```

5.  Click Create.

#### Results

- To verify that the ConfigMap was created and `metrics-utility` is installed, select **ConfigMap** from the navigation panel and search for your ConfigMap in the list.

### Deploy automation controller

automation controller includes a `metrics-utility` cronjob that gathers usage information and generates a report at specified intervals.

#### About this task

To deploy automation controller and specify variables for how often `metrics-utility` gathers usage information and generates a report, use the following procedure:

#### Procedure

1.  From the navigation panel, select **Installed Operators**.
2.  Select **Ansible Automation Platform**.
3.  In the Operator details, select the automation controller tab.
4.  Click Create automation controller.
5.  Select the YAML view option. The YAML now shows the default parameters for automation controller. The relevant parameters for `metrics-utility` are the following:
| **Parameter**                                       | **Variable**                |
| --------------------------------------------------- | --------------------------- |
| <br>  **`metrics_utility_enabled`**                 | <br>True.                   |
| <br>  **`metrics_utility_cronjob_gather_schedule`** | <br>`@hourly` or `@daily`.  |
| <br>  **`metrics_utility_cronjob_report_schedule`** | <br>`@daily` or `@monthly`. |

6.  Find the `metrics_utility_enabled` parameter and change the variable to true.
7.  Find the `metrics_utility_cronjob_gather_schedule` parameter and enter a variable for how often the utility should gather usage information (for example, `@hourly` or `@daily`).
8.  Find the `metrics_utility_cronjob_report_schedule` parameter and enter a variable for how often the utility generates a report (for example, `@daily` or `@monthly`).
9.  Click Create.

## Configure the `metrics-utility` on a manual containerized installation of Ansible Automation Platform

The `metrics-utility` tool generates performance metrics and reports for Ansible Automation Platform installations.

`metrics-utility` is included in the OpenShift Container Platform image beginning with version 4.12, 4.512, and 4.6. If your system does not have `metrics-utility` installed, update your OpenShift image to the latest version.

Use the following steps to configure `metrics-utility` on a manual containerized installation Ansible Automation Platform:

1. Enable and configure `metrics-utility` in the inventory file.
2. Apply your `metrics-utility` configuration.
3. Verify the `systemctl` timer.
4. Verify the data collection.
5. Locate the generated reports.


Note:

You must have an active Ansible Automation Platform subscription

**Minimum resource requirements**

Using the `metrics-utility` tool on a containerized installation of Ansible Automation Platform requires the following resources:

- CPU: 1 dedicated CPU core
* 100% of 1 core used during execution
- Memory:
* Minimum: 256 MB RAM (supports up to ~10,000 job host summaries)
* Recommended: 512 MB RAM (standard deployments)
* Large-scale: 1 GB RAM (supports up to ~100,000 job host summaries)
Note:
Memory requirements scale with the number of hosts and jobs processed.

- Execution time: Report generation typically completes within 10-30 seconds, depending on data volume

### Enable and configure the `metrics-utility` in the inventory file

Modify your Ansible Automation Platform inventory file to enable and configure `metrics-utility`.

#### Procedure

1.  Modify your inventory file to enable `metrics-utility` container deployment by adding the following line under the `[automationcontroller]` section:


```
metrics_utility_enabled=true
```
This setting instructs the installation program to create and configure two dedicated `automation-controller-metrics-utility` containers as part of your Ansible Automation Platform deployment. One of these containers is used to collect the data, and the other is used to build the report. If your Ansible Automation Platform deployment has already been configured, re-run the installation script to activate the container.

2.  Configure the reporting parameters by adding the `metrics_utility_extra_settings` variable. This variable controls where reports are saved, what they contain, and other metadata.

```
metrics_utility_extra_settings=[
{"setting": "METRICS_UTILITY_SHIP_TARGET", "value": "directory"},
{"setting": "METRICS_UTILITY_SHIP_PATH", "value": "~/aap/controller/data/metrics/"},
{"setting": "METRICS_UTILITY_REPORT_TYPE", "value": "CCSPv2"},
{"setting": "METRICS_UTILITY_PRICE_PER_NODE", "value": "100"},
{"setting": "METRICS_UTILITY_REPORT_COMPANY_NAME", "value": "My Company Inc"},
{"setting": "METRICS_UTILITY_REPORT_EMAIL", "value": "admin@mycompany.com"},
{"setting": "METRICS_UTILITY_REPORT_SKU", "value": "MCT3752MO"}]
```

3.  Optional: Override the default data gathering schedule by adding the following variables with your `systemd timer` expressions:

Note:
`systemd timer` expressions differ from `cron` expressions.

```
# Gathers data every 30 minutes
metrics_utility_cronjob_gather_schedule=*:0/30
# Generates the report at midnight on the 2nd of the month
metrics_utility_cronjob_report_schedule=*-*-02 00:00:00
```

## Apply your `metrics-utility` configuration

If you are running `metrics-utility` on a new installation, you do not need to take any additional actions to apply your configuration.

### About this task

If you are applying your `metrics-utility` configuration to an existing deployment, you must re-run the Ansible Automation Platform installer script. Re-running the script reads the updated inventory file, deploys the `automation-controller-metrics-utility` container, and creates the `systemd` user services and timers necessary to automate data collection and reporting. Use the following verification steps to ensure your `metrics-utility` configuration has been applied and is running correctly:

### Procedure

-  Verify your `systemctl` timer.
-  Verify data collection.
-  Locate generated reports.

### Results

1. Run the following command to verify that your `systemctl timer` job entries were saved correctly:

```
systemctl --user list-timers --no-pager | grep metrics-utility
```
**Example output:**

```
Wed 2025-08-13 10:45:00 IST 8min left Wed 2025-08-13 10:30:04 IST 6min ago   metrics-utility-build-report.timer metrics-utility-build-report.service
Wed 2025-08-13 10:45:00 IST 8min left Wed 2025-08-13 10:30:04 IST 6min ago   metrics-utility-gather.timer   	metrics-utility-gather.service
```

2. Use the following command to verify data collection by inspecting the output logs of the services you are running:

```
systemctl --user status metrics-utility-gather.service
```
**Example output:**

```
metrics-utility-gather.service - Podman metrics-utility-gather.service
Loaded: loaded (/home/aap/.config/systemd/user/metrics-utility-gather.service; disabled; preset: disabled)
Active: inactive (dead) since Wed 2025-08-13 10:00:06 IST; 5min ago
Duration: 2.008s
TriggeredBy: ● metrics-utility-gather.timer
Docs: man:podman-generate-systemd(1)
Process: 1472847 ExecStart=/usr/bin/podman start metrics-utility-gather (code=exited, status=0/SUCCESS)
Process: 1472927 ExecStop=/usr/bin/podman stop -t 10 metrics-utility-gather (code=exited, status=0/SUCCESS)
Process: 1472937 ExecStopPost=/usr/bin/podman stop -t 10 metrics-utility-gather (code=exited, status=0/SUCCESS)
Main PID: 1472874 (code=exited, status=0/SUCCESS)
CPU: 197ms

Aug 13 10:00:04 aap.example.org podman[1472847]: metrics-utility-gather
Aug 13 10:00:04 aap.example.org systemd[993]: Started Podman metrics-utility-gather.service.
Aug 13 10:00:05 aap.example.org metrics-utility-gather[1472874]: 2025-08-13 09:00:05,806 INFO 	[-] awx.main.analytics /tmp/3292ca44-3314-4f>
Aug 13 10:00:05 aap.example.org metrics-utility-gather[1472874]: /tmp/3292ca44-3314-4f0b-b3f6-ba4a1e47a2b1-2025-08-13-083505+0000-2025-08-13-0>
Aug 13 10:00:05 aap.example.org metrics-utility-gather[1472874]: 2025-08-13 09:00:05,808 INFO 	[-] awx.main.analytics /tmp/3292ca44-3314-4f>
Aug 13 10:00:05 aap.example.org metrics-utility-gather[1472874]: /tmp/3292ca44-3314-4f0b-b3f6-ba4a1e47a2b1-2025-08-13-083505+0000-2025-08-13-0>
Aug 13 10:00:06 aap.example.org podman[1472912]: 2025-08-13 10:00:06.169271763 +0100 IST m=+0.019922418 container died 5dc8d5674f1d1745258530f>
Aug 13 10:00:06 aap.example.org podman[1472912]: 2025-08-13 10:00:06.187584135 +0100 IST m=+0.038234790 container cleanup 5dc8d5674f1d17452585>
Aug 13 10:00:06 aap.example.org podman[1472927]: metrics-utility-gather
Aug 13 10:00:06 aap.example.org podman[1472937]: metrics-utility-gather
```

3. Locate the generated reports. Reports are saved in the directory you specified in the `METRICS_UTILITY_SHIP_PATH` setting.   - Path: Using the example provided in this document, the report path would be `/aap/controller/data/metrics/`.
- Filename: The report name follows the format `CCSP-<YEAR>-<MONTH>.xlsx`. For example, a report generated for August, 2025 would be named `CCSP-2025-08.xlsx`.
