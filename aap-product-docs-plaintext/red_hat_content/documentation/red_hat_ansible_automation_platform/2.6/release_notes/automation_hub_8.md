# 9. Patch releases
## 9.6. Ansible Automation Platform patch release December 10, 2025
### 9.6.6. Automation hub

#### 9.6.6.1. Bug Fixes

- Fixed an issue with Automation hub authentication failure for users with the **Team Admin** role:


- Users assigned the **Team Admin** role can now successfully authenticate to Automation hub. Previously, these users would receive a **401** error when accessing Automation hub API endpoints due to an incompatibility between the **Team Admin** role and Automation hub’s internal permission system.(AAP-58898)

- Fixed an issue where the password field on the Automation hub Django REST framework authentication page was missing the autocomplete attribute. As a consequence, the field did not align with security best practices regarding browser autofill. With this update, the password field uses the `autocomplete="new-password"` attribute. As a result, the Automation hub API authentication page complies with recommended security settings.(AAP-59910)

- Previously, upgrades from Ansible Automation Platform 2.5 to 2.6 failed when API access logging was enabled. This occurred due to an incorrect import path in the galaxy-ng package. This release corrects the import path.(AAP-59886)

