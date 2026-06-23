# Event-Driven Ansible custom resources

The Event-Driven Ansible operator provides custom resources for deploying, configuring, and protecting a standalone Event-Driven Ansible instance on OpenShift Container Platform.

The `EDA` custom resource deploys and configures Event-Driven Ansible independently of the full Ansible Automation Platform deployment. Event-Driven Ansible enables event-driven automation workflows by connecting event sources to automation actions. Use this custom resource when you need to manage Event-Driven Ansible as a standalone component rather than through the `AnsibleAutomationPlatform` resource.

The `EDABackup` and `EDARestore` custom resources manage data protection for standalone Event-Driven Ansible deployments. A backup captures the Event-Driven Ansible database and configuration. A restore recreates the deployment from a previously created backup.

