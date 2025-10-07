# 10. Patch releases
## 10.3. Ansible Automation Platform patch release July 30, 2025
### 10.3.4. Automation controller




#### 10.3.4.1. Enhancements




- Update the injectors for the Ansible Automation Platform credential type to work across collection.(AAP-47877)


#### 10.3.4.2. Bug Fixes




- Removed API version from hard-coded URL in inventory plugin.(AAP-48443)
- Fixed a **404** error for workflow nodes.(AAP-47362)
- Fixed an issue where the automation controller pod was not working after an upgrade to `    aap-operator.v2.5.0-0.1750901870` .(AAP-48771)


