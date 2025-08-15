# 10. Patch releases
## 10.1. Ansible Automation Platform patch release July 30, 2025
### 10.1.5. Container-based Ansible Automation Platform




#### 10.1.5.1. Enhancements




- Added an exclusion parameter for Container-based Ansible Automation Platform Backup, allowing users to specify snapshot paths to be excluded from the backup process.(AAP-50114)


#### 10.1.5.2. Bug Fixes




- Fixed the issue where execution instances removed from the inventory would still be visible on the Topology View.(AAP-48615)
- Fixed a bug when restoring automation hub to a new cluster when using NFS for the hub data filesystem.(AAP-48568)
- Fixed permission issues when restoring automation hub when using NFS storage.(AAP-50118)


