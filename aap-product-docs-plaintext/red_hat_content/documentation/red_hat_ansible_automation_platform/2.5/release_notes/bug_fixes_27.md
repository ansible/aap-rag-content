# 10. Patch releases
## 10.13. Ansible Automation Platform patch release January 29, 2025
### 10.13.2. Bug fixes




#### 10.13.2.1. CVE




With this update, the following CVEs have been addressed:

-  [CVE-2024-56326](https://access.redhat.com/security/cve/cve-2024-56326)  `    python3.11-jinja2` : Jinja has a sandbox breakout through indirect reference to format method.(AAP-38852)
-  [CVE-2024-56374](https://access.redhat.com/security/cve/CVE-2024-56374)  `    ansible-lightspeed-container` : Potential denial-of-service vulnerability in IPv6 validation.(AAP-38647)
-  [CVE-2024-56374](https://access.redhat.com/security/cve/CVE-2024-56374)  `    python3.11-django` : potential denial-of-service vulnerability in IPv6 validation.(AAP-38630)
-  [CVE-2024-53907](https://access.redhat.com/security/cve/cve-2024-53907)  `    python3.11-django` : Potential denial-of-service in django.utils.html.strip_tags().(AAP-38486)
-  [CVE-2024-56201](https://access.redhat.com/security/cve/cve-2024-56201)  `    python3.11-jinja2` : Jinja has a sandbox breakout through malicious filenames.(AAP-38331)
-  [CVE-2024-56374](https://access.redhat.com/security/cve/CVE-2024-56374)  `    automation-controller` : Potential denial-of-service vulnerability in IPv6 validation.(AAP-38648)
-  [CVE-2024-56201](https://access.redhat.com/security/cve/cve-2024-56201)  `    automation-controller` : Jinja has a sandbox breakout through malicious filenames.(AAP-38081)
-  [CVE-2024-56326](https://access.redhat.com/security/cve/cve-2024-56326)  `    automation-controller` : Jinja has a sandbox breakout through indirect reference to format method.(AAP-38058)


#### 10.13.2.2. Automation controller




- Fixed an issue where the order of source inventories was not respected by the collection `    ansible.controller` .(AAP-38524)
- Fixed an issue where an actively running job on an execution node may have had its folder deleted by a system task. This fix addresses some **Failed to JSON parse a line from worker stream** type errors.(AAP-38137)


#### 10.13.2.3. Container-based Ansible Automation Platform




- The inventory file variable **postgresql_admin_username** is no longer required when using an external database. If you do not have database administrator credentials, you can supply the database credentials for each component in the inventory file instead.(AAP-39077)


#### 10.13.2.4. Event-Driven Ansible




- Fixed an issue where the application version in the **openapi** spec was incorrectly set.(AAP-38392)
- Fixed an issue where activations were not properly updated in some scenarios with a high load of the system. (AAP-38374)
- Fixed an issue where users were unable to filter **Rule Audits** by rulebook activation name.(AAP-39253)
- Fixed an issue where the input field of the injector configuration could not be empty.(AAP-39086)


#### 10.13.2.5. RPM-based Ansible Automation Platform




- Fixed an issue where setting `    automationedacontroller_max_running_activations` could cause the installer to fail. (AAP-38708)
- Fixed an issue where the platform gateway services are not restarted when a dependency changes.(AAP-38918)
- Fixed an issue where the platform gateway could not be setup with custom SSL certificates.(AAP-38985)


