# 9. Patch releases
## 9.7. Ansible Automation Platform patch release November 19, 2025
### 9.7.7. RPM-based Ansible Automation Platform

#### 9.7.7.1. Enhancements

Event-Driven Ansible event-stream mTLS configuration added to installer.(AAP-46070)

#### 9.7.7.2. Bug Fixes

- Fixed an issue where the installer failed during the execution environment image upload when there was no automation hub node in inventory.(AAP-56892)

- Fixed an issue with extra log content. platform gateway logs in */var/log/ansible-automation-platform/gateway* have been refactored, there is now more separation of the logs for various components:


- *control-plane-supervisor.log* ← Messages from `supervisorctl` about the control-plane (new)
- *control-plane.log* ← Django logs for the control-plane (new, extracted from gateway.log)
- *gateway.log* ← Django logs for gateway (existing, had items removed)
- *uwsgi.log* ← UWSGI logs for the {Gateeway} (new, extracted from gateeay.log)
- *envoy.log* ← The proxy log (existing, unchanged).(AAP-30549)

