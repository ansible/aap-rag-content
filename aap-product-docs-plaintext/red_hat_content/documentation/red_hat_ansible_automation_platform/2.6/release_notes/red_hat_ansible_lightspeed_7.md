# 9. Patch releases
## 9.8. Ansible Automation Platform patch release November 5, 2025
### 9.8.1. Red Hat Ansible Lightspeed

#### 9.8.1.1. Bug Fixes

- A typo in the `containerfile` caused the **nginx** configuration file to be copied to a non-existent directory in operator-based installations, leading to the Lightspeed API service being unavailable due to incorrect port configuration. With this release, the typo has been fixed, ensuring the Lightspeed API service now listens on the correct port in operator-based installations, improving API endpoint accessibility.(AAP-56712)

