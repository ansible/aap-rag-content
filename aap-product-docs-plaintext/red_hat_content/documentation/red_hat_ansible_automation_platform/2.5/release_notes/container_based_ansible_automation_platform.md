# 10. Patch releases
## 10.1. Ansible Automation Platform patch release September 23, 2025
### 10.1.8. Container-based Ansible Automation Platform




#### 10.1.8.1. Bug Fixes




- Fixed an issue where the `    create_initial_data` command did not work during backup and restore onto different clusters for Event-Driven Ansible. (AAP-53382)
- Fixed an issue where scheduled tasks failed in private automation hub when using quotes in the task name. (AAP-53307)
- Uploading Ansible collections to private automation hub is no longer limited by the API pagination. (AAP-53526)


