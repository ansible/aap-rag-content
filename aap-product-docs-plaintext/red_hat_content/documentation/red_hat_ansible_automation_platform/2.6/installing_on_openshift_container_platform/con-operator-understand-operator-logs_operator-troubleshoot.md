# 12. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 12.1. Understanding automation controller operator logs




When the operator deploys an **Automation Controller** instance, it runs an installer role inside the operator container. If the automation controller’s status is `Failed` , you must check the `automation-controller-operator` container logs. These logs provide the installer role’s output and are a critical first step in debugging deployment issues.

