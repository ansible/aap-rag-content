# Automation dashboard deployment options
## Standalone automation dashboard utility (RHEL only)

The standalone automation dashboard utility is installed and managed separately from the Ansible Automation Platform installer, and is supported on RHEL only. It has its own lifecycle, including installation, configuration, data synchronization, cluster access token verification, and uninstallation.

Use the standalone utility when you want to connect to multiple Ansible Automation Platform instances, including deployments on different Ansible Automation Platform versions (2.4 and later), and aggregate their savings data in a single dashboard.

Note:

The standalone utility cannot filter the dashboard UI by source Ansible Automation Platform instance.

