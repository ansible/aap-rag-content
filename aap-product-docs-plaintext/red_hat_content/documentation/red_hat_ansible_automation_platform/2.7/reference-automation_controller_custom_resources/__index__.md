# Automation controller custom resources

The automation controller operator provides custom resources for deploying, configuring, and protecting a standalone automation controller instance on OpenShift Container Platform.

The `AutomationController` custom resource deploys and configures automation controller independently of the full Ansible Automation Platform deployment. Use this custom resource when you need to manage automation controller as a standalone component rather than through the `AnsibleAutomationPlatform` resource.

The `AutomationControllerMeshIngress` custom resource creates a mesh ingress hop node inside the OpenShift cluster. This enables remote execution nodes outside the cluster to connect to automation controller through the automation mesh network.

The `AutomationControllerBackup` and `AutomationControllerRestore` custom resources manage data protection for standalone automation controller deployments. A backup captures the controller database and configuration. A restore recreates the controller from a previously created backup.

