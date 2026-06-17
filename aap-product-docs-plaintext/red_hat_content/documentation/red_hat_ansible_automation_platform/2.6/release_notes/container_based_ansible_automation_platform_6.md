# 9. Patch releases
## 9.9. Ansible Automation Platform patch release October 28, 2025
### 9.9.7. Container-based Ansible Automation Platform

#### 9.9.7.1. Enhancements

- Implemented preflight ansible-core version validation.(AAP-54932)

#### 9.9.7.2. Bug Fixes

- Fixed an issue where `REDHAT_CANDLEPIN_VERIFY` was not being used for the correct CA permissions so that the controller could not make requests to **subscription.rhsm.redhat.com**.(AAP-55180)

