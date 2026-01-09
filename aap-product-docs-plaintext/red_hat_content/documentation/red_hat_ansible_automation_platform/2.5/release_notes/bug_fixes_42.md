# 10. Patch releases
## 10.12. Ansible Automation Platform patch release March 26, 2025
### 10.12.2. Bug fixes




With this update, the following CVEs have been addressed:

-  [CVE-2025-27516](https://access.redhat.com/security/cve/cve-2025-27516)  `    python3.11-jinja2` : Jinja sandbox breakout through attr filter selecting format method.(AAP-42104)
-  [CVE-2025-26699](https://access.redhat.com/security/cve/CVE-2025-26699)  `    python3.11-django` : Potential denial-of-service vulnerability in `    django.utils.text.wrap()` .(AAP-42107)
-  [CVE-2025-26699](https://access.redhat.com/security/cve/CVE-2025-26699)  `    ansible-lightspeed-container` : Potential denial-of-service vulnerability in `    django.utils.text.wrap()` .(AAP-41138)
-  [CVE-2025-27516](https://access.redhat.com/security/cve/cve-2025-27516)  `    automation-controller` : Jinja sandbox breakout through attr filter selecting format method.(AAP-41692)
-  [CVE-2025-27516](https://access.redhat.com/security/cve/cve-2025-27516)  `    ansible-lightspeed-container` : Jinja sandbox breakout through attr filter selecting format method.(AAP-41690)


#### 10.12.2.1. Ansible Automation Platform




- Fixed an issue when migrating user accounts with invalid email addresses, the process would print a message showing the user name of the user whose email address has been removed.(AAP-41675)
- Fixed an issue that occurred after enabling `    automigration` of user accounts from the previous SSO authenticator to a new authenticator, the user accounts from other Ansible Automation Platform services such as automation controller or automation hub, were not properly merged into one account, and the account on those services deleted.(AAP-42146)


#### 10.12.2.2. Ansible Automation Platform Operator




- Fixed an issue where the legacy automation controller API information link on the automation controller redirect page was broken.(AAP-41510)
- Fixed an issue where Ansible Automation Platform backups would fail when writing `    yaml` to the PVC on OpenShift Container Platform clusters with OpenShift Container Platform Virtualization installed.(AAP-28609)


#### 10.12.2.3. Automation controller




- Fixed an issue where Insights projects were failing on OpenShift Container Platform on Ansible Automation Platform, due to incorrectly specifying the extra `    vars` path.(AAP-41874)
- Fixed an issue where the host metrics for dark, unreachable hosts were being collected.(AAP-41567)
- Fixed an issue where the system auditor could download the execution node install bundle.(AAP-37922)
- Fixed an issue where the host record was added to `    HostMetric` when the host had failures or unreachable tasks completed.(AAP-32094)


#### 10.12.2.4. Automation hub




- Fixed an issue where the user could not delete automation hub teams on the resource API.(AAP-42158)
- Fixed an issue where the `    retain_repo_versions` was null for the validated repos.(AAP-42005)


#### 10.12.2.5. RPM-based Ansible Automation Platform




- Fixed an issue where preflight was not accounting for `    automationgateway` being a CA server node.(AAP-41817)
- Fixed an issue where platform gateway installations resulted in failures in environments with IPv6 due to `    nginx` configuration timing.(AAP-41816)


