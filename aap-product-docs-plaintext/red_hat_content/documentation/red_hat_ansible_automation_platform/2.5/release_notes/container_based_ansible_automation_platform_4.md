# 10. Patch releases
## 10.4. Ansible Automation Platform patch release July 2, 2025
### 10.4.8. Container-based Ansible Automation Platform




#### 10.4.8.1. Enhancements




- Validate that nodes are configured with at least 16G of RAM.(AAP-47542)
- Containerized Ansible Automation Platform now supports RHEL 10.(AAP-47083)


#### 10.4.8.2. Bug Fixes




- Fixed an issue where the TLS Certificate Authority (CA) certificate for Receptor mesh configuration when providing TLS certificates were not signed by the internal CA.(AAP-48065)
- Fixed a missing user parameter for the sos report command on the `    log_gathering` playbook.(AAP-47718)
- Fixed an issue where the `    jquery` version included in the redirect page did not match the version from the rest framework directory.(AAP-47074)


