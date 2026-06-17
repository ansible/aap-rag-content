# 9. Patch releases
## 9.9. Ansible Automation Platform patch release October 28, 2025
### 9.9.5. Automation controller

#### 9.9.5.1. Enhancements

- Added support for Red Hat username and password for the subscription management API.(AAP-54975)

#### 9.9.5.2. Bug Fixes

- Fixes the `system_administrator` role creation race condition which most commonly happened on new Openshift deployments resulting in the default instance group not being created.(AAP-54963)
- Fixed an issue where the Controller container file was missing the metrics utility in version 2.6.(AAP-54948)
- Fixed an issue where the `awx.awx.license` appeared to succeed when given an invalid *pool/subscription*.(AAP-54768)
- Fixed an issue where the `ansible.platform` collection did not work with the default Red Hat Ansible Automation Platform credential type.(AAP-41000)
- Fixed an issue where there was a duplicate value (`subsystem_metrics_pipe_execute_seconds`) detected under *api/controller/v2/metrics/* on Ansible Automation Platform 2.5.(AAP-55621)
- Fixed an issue where the platform auditor did not have access to controller settings.(AAP-55607)

