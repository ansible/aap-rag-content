# 10. Patch releases
## 10.1. Ansible Automation Platform patch release September 23, 2025
### 10.1.5. Bug fixes




- Fixed an issue where the deployment was failing with "dict object has no attribute version". (AAP-46528)
- Fixed an issue where the Redis timeout configuration was overwritten by the Ansible Automation Platform Operator on reconciliation. The timeout for Redis connections has been added to the configuration and hard-coded to 300 seconds. (AAP-53309)
- The automation hub web init container now uses resource limits when enabled. (AAP-52934)
- Fixed a `    pulp_ansible` compatibility issue that was preventing the `    hub-api` pod from running migrations in the new container when upgrading to the latest 2.5 operator version. (AAP-49016)


