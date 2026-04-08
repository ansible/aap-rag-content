# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.4. Configure static storage for Ansible Automation Platform
### 5.4.1. Understand static provisioning in the Ansible Automation Platform Operator




By default, the Ansible Automation Platform Operator uses dynamic provisioning to create the required storage for components such as the database and automation hub.

If your environment does not allow dynamic provisioning, you must use static provisioning.

With static provisioning, you manually create Persistent Volumes (PVs) and Persistent Volume Claims (PVCs) before you deploy the `AnsibleAutomationPlatform` custom resource. When the Operator starts the deployment, it searches the namespace for PVCs that match its internal naming conventions. If a matching PVC exists, the Operator binds to that claim instead of attempting to provision new storage.

Static provisioning also enables data persistence during redeployments. If you delete an `AnsibleAutomationPlatform` instance, the Operator does not delete the associated PVCs. You can redeploy the instance using the same name to reconnect to the existing data.

