# 9. Patch releases
## 9.10. Ansible Automation Platform patch release October 16, 2025
### 9.10.3. Automation hub

#### 9.10.3.1. Bug Fixes

- Fixed a global galaxy team role migration issue that could occur during the post-migrate upgrade process.(AAP-55304)
- Fixed an issue caused by a constraint violation during migrations.(AAP-55309)
- Fixed an issue from `aap-gateway-manage,` `migrate_service_data`, that states **Role definition content type must be null to assign globally**, which was due to permissions in hub that failed validation.(AAP-55639)

