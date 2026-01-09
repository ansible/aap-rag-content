# 10. Patch releases
## 10.11. Ansible Automation Platform patch release April 9, 2025
### 10.11.4. Known Issues




- This section provides information about known issues in Ansible Automation Platform 2.5. Upgrade issues with the RPM installer.
- Upgrading from Red Hat Enterprise Linux 9.4 to Red Hat Enterprise Linux 9.5 or later fails when running platform gateway version 2.5.20250409 or later. To upgrade to Red Hat Enterprise Linux 9.5 or later, follow the steps in this [KCS article](https://access.redhat.com/solutions/7112819) .
- When upgrading Ansible Automation Platform 2.5, you must use the RPM installer version 2.5-11 or later. If you use an older installer, the installation might fail. If you encounter a failed installation using an earlier version of the installer, rerun the installation with version 2.5-11 or later.


