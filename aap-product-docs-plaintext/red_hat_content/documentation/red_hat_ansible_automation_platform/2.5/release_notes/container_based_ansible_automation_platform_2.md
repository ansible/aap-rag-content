# 10. Patch releases
## 10.2. Ansible Automation Platform patch release August 27, 2025
### 10.2.7. Container-based Ansible Automation Platform




#### 10.2.7.1. Enhancements




- Implemented **PostgreSQL** extra settings parameter on the installer.(AAP-51533)


#### 10.2.7.2. Bug Fixes




- Fixed an issue where the **PostgreSQL** version failed during preflight with a customer provided CA certificate.(AAP-50884)
- Fixed `    pcp` data permissions by migrating the data to a **Podman** volume instead of a bind mount.(AAP-50807)
- Fixed an issue where the backup script incorrectly Included `    .snapshot` directories in the automation hub backup.(AAP-50784)
- Fixed a bug where the **Redis** hostname fails to be set in a disconnected environment.(AAP-51532)
- Fixed an issue where there was no exclusion parameter for containerized backup, that allowed users to specify snapshot paths to be excluded from the backup process.(AAP-46767)


