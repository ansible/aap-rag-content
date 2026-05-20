# 9. Patch releases
## 9.4. Ansible Automation Platform patch release January 21, 2026
### 9.4.4. Automation hub

#### 9.4.4.1. Bug Fixes

- Fixed an issue where the password field on the automation hub Django REST framework authentication page was missing the autocomplete attribute. As a consequence, the field did not align with security best practices regarding browser autofill. With this update, the password field uses the autocomplete="new-password" attribute. As a result, the automation hub API authentication page now complies with recommended security settings.(AAP-59912)

