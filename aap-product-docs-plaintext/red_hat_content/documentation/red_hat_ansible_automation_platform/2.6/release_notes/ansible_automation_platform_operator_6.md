# 9. Patch releases
## 9.3. Ansible Automation Platform patch release February 25, 2026
### 9.3.4. Ansible Automation Platform Operator

#### 9.3.4.1. Enhancements

- Increased envoy request timeout from 1 second to 5 seconds.(AAP-64420)

#### 9.3.4.2. Bug Fixes

- Fixed an issue with Automation hub file data not restored in the correct directory.(AAP-65961)
- Fixed an issue where custom PostgreSQL settings could not be applied to the Ansible Automation Platform Operator. Added command configuration to PostgreSQL `statefulset` configuration when `postgres_extra_args` is defined.(AAP-65487)
- Fixed an issue where there was a missing `resource_requirement` in the **nginx** container configured in the EDA event stream deployment.(AAP-64007)
- Fixed an issue where Kubernetes Secret values were being printed in operator logs.(AAP-62943)
- Fixed an issue with an extra_settings to allow customizing the LOGGING level for the Gateway Operator.(AAP-62938)

