# 9. Patch releases
## 9.9. Ansible Automation Platform patch release October 28, 2025
### 9.9.3. Ansible Automation Platform Operator

#### 9.9.3.1. Bug Fixes

- Fixed an issue where the Ansible Lightspeed API version did not work during Ansible Automation Platform idle.(AAP-54174)
- Fixed an issue that caused a failure to gather the job data from the controller API.(AAP-55632)
- Fixed a bug where the user could set an image without the respective version, causing the installation to enter an error loop.(AAP-55642)
- Fixed an issue where the backup and restore Ansible Automation Platform instance failed, from cluster A to cluster B, when restoring an upgraded AAP environment from 2.4.(AAP-55648)

