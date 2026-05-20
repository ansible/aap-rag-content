# 9. Patch releases
## 9.3. Ansible Automation Platform patch release February 25, 2026
### 9.3.8. Container-based Ansible Automation Platform

#### 9.3.8.1. Enhancements

- Increased envoy request timeout from 1 second to 5 seconds.(AAP-64323)
- Added a retry mechanism when trying to get the Automation controller status.(AAP-64291)
- Fixed a compatibility issue when `jinja2` native is enabled on ansible-core.(AAP-62878)
- URL anchors in the inventory samples reflect official documentation.(AAP-55780)

#### 9.3.8.2. Bug Fixes

- Fixed automation gateway preflight check which doesn’t require `ansible_host` to be defined anymore.(AAP-65370)
- Fixed an issue where the installer did not make use of `ansible_user_dir` for receptor.(AAP-64452)
- Fixed an issue where disabling TLS on envoy no longer causes a controller connection error when running Merge organization task.(AAP-62904)
- Fixed an issue where the TLS verification when pushing container images to the Automation Hub registry and TLS was enabled.(AAP-62864)

