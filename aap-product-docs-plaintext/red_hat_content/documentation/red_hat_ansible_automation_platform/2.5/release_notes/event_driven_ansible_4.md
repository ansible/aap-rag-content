# 10. Patch releases
## 10.3. Ansible Automation Platform patch release June 9, 2025
### 10.3.5. Event-Driven Ansible




#### 10.3.5.1. Enhancements




- Rename env `    EDA_OIDC_TOKEN_URL` to `    DA_AUTOMATION_ANALYTICS_OIDC_TOKEN_URL` .(AAP-44862)


#### 10.3.5.2. Bug Fixes




- Fixed an issue where the activation containers were not removed after a node goes offline.(AAP-45831)
- Fixed an issue where the error reminding user to remap source with event stream should be under key source_mapping in the API return.(AAP-45105)
- Fixed an issue where special characters such as `    []` were not allowed in the activation name on OCP deployment.(AAP-44691)


