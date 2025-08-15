# 10. Patch releases
## 10.2. Ansible Automation Platform patch release July 2, 2025
### 10.2.6. Automation controller




#### 10.2.6.1. Features




- Added AWX `    dispatcherd` integration.(AAP-45800)


#### 10.2.6.2. Bug Fixes




- Fixed a race condition where job templates with duplicate names in the same organization could be created.(AAP-45968)
- Fixed an issue where `    ole_user_assignments` failed to query for `    object_ansible_id` . Enabled query filtering for fields `    user_ansible_id` , `    team_ansible_id` , and `    object_ansible_id` on the role assignment API endpoints.(AAP-45443)
- Fixed an issue where some credential types were not populated after upgrading. This adds a new migration to accomplish this.(AAP-44233)
- Fixed an issue where there were large numbers of jobs queued that were stuck in waiting status.(AAP-44143)


