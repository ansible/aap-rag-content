# 9. Patch releases
## 9.4. Ansible Automation Platform patch release January 21, 2026
### 9.4.5. Container-based Ansible Automation Platform

#### 9.4.5.1. Enhancements

- Added lTLS support to lightspeed chatbot service.(AAP-60900)

#### 9.4.5.2. Bug Fixes

- Fixed an issue where the system-prompt optimized for granite and OpenAI models.(AAP-60898)
- Fixed an issue where the containerized installer could not properly configure Redis in the IPv6 only environment. Added IPv6 support for different Ansible Automation Platform components within the containerized installer collection.(AAP-60532)
- Fixed an issue where the ansiblemcp uninstall is failing to stop containers.

