# Details about data collected for Automation Analytics

Learn about the specific data that automation controller collects and sends to Red Hat when you enable Automation Analytics.

Automation Analytics collects the following classes of data from automation controller:

- Basic configuration, such as which features are enabled, and what operating system is being used
- Topology and status of the automation controller environment and hosts, including capacity and health
- Counts of automation resources:
* organizations, teams, and users
* inventories and hosts
* credentials (indexed by type)
* projects (indexed by type)
* templates
* schedules
* active sessions
* running and pending jobs
- Job execution details (start time, finish time, launch type, and success)
- Automation task details (success, host id, playbook/role, task name, and module used)


You can use `awx-manage gather_analytics` (without `--ship`) to inspect the data that automation controller sends, so that you can satisfy your data collection concerns. This creates a .tar file that contains the analytics data that is sent to Red Hat.

This file contains several JSON and CSV files. Each file contains a different set of analytics data.

## Automation Analytics Data Dictionary

Automation Analytics Data is sent to the Red Hat Hybrid Cloud Console (HCC) to provide detailed analytics on your automation.

The data dictionary outlines the information collected by Automation Analytics from the Red Hat Ansible Automation Platform automation controller, also known as Automation Execution.
