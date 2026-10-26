# Understand metrics service architecture
## Default behavior in Ansible Automation Platform 2.7

Metrics service is enabled by default in Ansible Automation Platform 2.7 for both operator-based (OpenShift) and containerized installations that include automation controller. It is deployed automatically as a required component when you install automation controller.

- **Containerized installations:** `[automationmetrics]` inventory group is required when installing Ansible Automation Platform if automationcontroller is present in the inventory file, unless `automationmetrics_skip_install=true` is set in `[all:vars]`
- **Operator installations:** Enabled when `metrics.disabled: false` is set in the AnsibleAutomationPlatform custom resource. Operator deployments do not support `automationmetrics_skip_install`; they use `metrics.disabled: true` in the CR instead.

