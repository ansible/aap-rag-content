# Ansible Automation Platform custom resources

The Ansible Automation Platform operator provides custom resources for deploying, backing up, and restoring a complete Ansible Automation Platform instance on OpenShift Container Platform.

The `AnsibleAutomationPlatform` custom resource is the top-level resource for deploying the platform. It manages all components, including automation controller, automation hub, Event-Driven Ansible, Ansible Lightspeed, and the platform gateway. Use this custom resource when you want the operator to manage the full platform deployment as a single unit.

The `AnsibleAutomationPlatformBackup` and `AnsibleAutomationPlatformRestore` custom resources manage data protection for the platform. A backup captures the state of all platform components and their databases. A restore recreates the platform from a previously created backup. You can configure backup settings globally or override them for individual components such as automation controller, automation hub, and Event-Driven Ansible.
