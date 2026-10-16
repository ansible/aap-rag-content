# Capture telemetry data for the Ansible self-service portal
## Configure automation dashboard post-installation

Activate dashboard data collection with automatic historical data backfill to generate comprehensive usage and ROI reports without reinstalling the platform or losing historical automation activity data.

### Before you begin

- Red Hat Ansible Automation Platform 2.7 installed and operational
- Metrics service installed and running
- For containerized: access to the installer inventory file
- For operator: `kubectl` or `oc` access and edit permissions on the AnsibleAutomationPlatform CR

### About this task

This procedure enables automation dashboard on an existing Red Hat Ansible Automation Platform 2.7 installation without platform downtime or service disruption. When you enable dashboard collection post-installation, metrics service automatically backfills up to 90 days of historical data from the Controller database, allowing the dashboard UI to display historical trends within hours of enablement. This zero-disruption activation eliminates the need to reinstall the platform and enables hourly automated collection for ongoing dashboard metrics after backfill completion, providing comprehensive usage and ROI reports using both historical and current automation activity data.

### Procedure

Choose your deployment method and follow the corresponding procedure

- For containerized installation, follow the containerized procedure
- For operator deployment, follow the operator procedure

### Results

After completing the procedure for your deployment method, dashboard is enabled and historical data backfill begins automatically.

