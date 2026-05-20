# 9. Patch releases
## 9.3. Ansible Automation Platform patch release February 25, 2026
### 9.3.6. Automation controller

#### 9.3.6.1. Enhancements

- Fixed the job list endpoint to no longer load the job artifacts, resulting in better performance.(AAP-63489)

#### 9.3.6.2. Bug Fixes

- Fixed an issue where the AWX CLI `modify` command did not display available field flags for users who have an admin role on a specific resource but do not have permission to create new resources of that type.(AAP-65813)
- Fixed missing `RoleUserAssignment` openapi schema component.(AAP-60826)

