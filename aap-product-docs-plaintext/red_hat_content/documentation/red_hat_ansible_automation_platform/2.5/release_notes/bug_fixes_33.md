# 10. Patch releases
## 10.19. Ansible Automation Platform patch release October 28, 2024
### 10.19.2. Bug fixes




#### 10.19.2.1. Ansible Automation Platform




- Removed the **Legacy external password** option from the **Authentication Type** list. (AAP-31506)
- Ansible Galaxy’s `    sessionauth` class is now always the first in the list of authentication classes so that the platform UI can successfully authenticate. (AAP-32146)
-  [CVE-2024-10033](https://access.redhat.com/security/cve/CVE-2024-10033) - `    automation-gateway` : Fixed a Cross-site Scripting (XSS) vulnerability on the `    automation-gateway` component that allowed a malicious user to perform actions that impact users.
-  [CVE-2024-22189](https://access.redhat.com/security/cve/CVE-2024-22189) - `    receptor` : Resolved an issue in `    quic-go` that would allow an attacker to trigger a denial of service by sending a large number of `    NEW_CONNECTION_ID` frames that retire old connection IDs.


#### 10.19.2.2. Automation controller




-  [CVE-2024-41989](https://access.redhat.com/security/cve/CVE-2024-41989) - `    automation-controller` : Before this update, in Django, if `    floatformat` received a string representation of a number in scientific notation with a large exponent, it could lead to significant memory consumption. With this update, decimals with more than 200 digits are now returned as is.
-  [CVE-2024-45230](https://access.redhat.com/security/cve/CVE-2024-45230) - `    automation-controller` : Resolved an issue in Python’s Django `    urlize()` and `    urlizetrunc()` functions where excessive input with a specific sequence of characters would lead to denial of service.


#### 10.19.2.3. Automation hub




- Refactored the `    dynaconf` hooks to preserve the necessary authentication classes for Ansible Automation Platform 2.5 deployments. (AAP-31680)
- During role migrations, model permissions are now re-added to roles to preserve ownership. (AAP-31417)


#### 10.19.2.4. Ansible Automation Platform Operator




- The port is now correctly set when configuring the platform gateway cache `    redis_host` setting when using an external Redis cache. (AAP-33279)
- Added checksums to the automation hub deployments so that pods are cycled to pick up changes to the PostgreSQL configuration and galaxy server settings Kubernetes secrets. (AAP-33518)


#### 10.19.2.5. Container-based Ansible Automation Platform




- Fixed the uninstall playbook execution when the environment was already uninstalled. (AAP-32981)


