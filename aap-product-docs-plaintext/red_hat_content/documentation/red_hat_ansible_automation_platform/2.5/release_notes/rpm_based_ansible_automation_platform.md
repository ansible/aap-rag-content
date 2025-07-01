# 10. Patch releases
## 10.2. Ansible Automation Platform patch release June 9, 2025
### 10.2.6. RPM-based Ansible Automation Platform




#### 10.2.6.1. Enhancements




- Setup will now retry automation gateway data migration attempts in case services take longer than expected to start.(AAP-46208)


#### 10.2.6.2. Bug Fixes




- Fixed an issue Event stream worker would not restart like other workers when running setup.sh.(AAP-46205)
- Fixed an issue where setup would not restart the podman socket whenever podman was reset.(AAP-46191)


