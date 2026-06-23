# Automation hub custom resources

The automation hub operator provides custom resources for deploying, configuring, and protecting a standalone automation hub instance on OpenShift Container Platform.

The `AutomationHub` custom resource deploys and configures automation hub independently of the full Ansible Automation Platform deployment. Automation hub provides a centralized location for managing Ansible content collections, execution environments, and container images. Use this custom resource when you need to manage automation hub as a standalone component rather than through the `AnsibleAutomationPlatform` resource.

The `AutomationHubBackup` and `AutomationHubRestore` custom resources manage data protection for standalone automation hub deployments. A backup captures the hub database, content, and configuration. A restore recreates the hub from a previously created backup.

