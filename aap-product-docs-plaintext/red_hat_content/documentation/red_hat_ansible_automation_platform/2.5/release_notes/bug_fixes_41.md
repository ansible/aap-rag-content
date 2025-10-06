# 10. Patch releases
## 10.17. Ansible Automation Platform patch release January 15, 2025
### 10.17.2. Bug fixes




#### 10.17.2.1. CVE




With this update, the following CVEs have been addressed:

-  [CVE-2024-52304](https://access.redhat.com/security/cve/cve-2024-52304)  `    python3.11-aiohttp` : `    aiohttp` vulnerable to request smuggling due to incorrect parsing of chunk extensions.(AAP-36192)
-  [CVE-2024-55565](https://access.redhat.com/security/cve/cve-2024-55565)  `    automation-gateway` : `    nanoid` mishandles non-integer values.(AAP-37168)
-  [CVE-2024-53908](https://access.redhat.com/security/cve/cve-2024-53908)  `    automation-controller` : Potential SQL injection in `    HasKey(lhs, rhs)` on Oracle.(AAP-36769)
-  [CVE-2024-53907](https://access.redhat.com/security/cve/cve-2024-53907)  `    automation-controller` : Potential denial-of-service in `    django.utils.html.strip_tags()` .(AAP-36756)
-  [CVE-2024-11407](https://access.redhat.com/security/cve/cve-2024-11407)  `    automation-controller` : Denial-of-Service through data corruption in `    gRPC-C++` .(AAP-36745)
-  [CVE-2024-52304](https://access.redhat.com/security/cve/cve-2024-52304)  `    ansible-lightspeed-container` : `    aiohttp` vulnerable to request smuggling due to incorrect parsing of chunk extensions.(AAP-36185)
-  [CVE-2024-56201](https://access.redhat.com/security/cve/cve-2024-56201)  `    ansible-lightspeed-container` : Jinja has a sandbox breakout through malicious filenames.(AAP-38079)
-  [CVE-2024-56326](https://access.redhat.com/security/cve/cve-2024-56326)  `    ansible-lightspeed-container` : Jinja has a sandbox breakout through indirect reference to format method.(AAP-38056)
-  [CVE-2024-11407](https://access.redhat.com/security/cve/cve-2024-11407)  `    ansible-lightspeed-container` : Denial-of-Service through data corruption in `    gRPC-C++` .(AAP-36744)


#### 10.17.2.2. Red Hat Ansible Automation Platform




- Fixed **not found** error that occurred occasionally when navigating through the form wizards.(AAP-37495)
- Fixed an issue where installing `    ansible-core` no longer installs `    python3-jmespath` on Red Hat Enterprise Linux 8.(AAP-18251)
- Fixed an issue where `    ID_KEY` attribute was improperly used to determine the username field in social auth pipelines.(AAP-38300)
- Fixed an issue where authenticator could create a **userid** and return a non-viable **authenticator_uid** .(AAP-38021)
- Fixed an issue where a private key was displayed in plain text when downloading the OpenAPI schema file. This was not the private key used by gateway, but a random default key.(AAP-37843)


#### 10.17.2.3. Automation controller




- Fixed an issue that did not allow sending `    job_lifecycle` logs to external aggregators.(AAP-37537)
- Fixed an issue where there was a date comparison mismatch for traceback from `    host_metric_summary_monthly` task.(AAP-37487)
- Fixed an issue where the scheduled jobs with count set to a **non-zero** value would run unexpectedly. (AAP-37290)
- Fixed an issue where a project’s requirements.yml could revert to a prior state in a cluster. (AAP-37228)
- Fixed an issue where there would be an occasional error creating the event partition table before starting a job, when a large number of jobs were launched quickly. (AAP-37227)
- Fixed an issue where temporary receptor files were not cleaned up after a job completed on nodes. (AAP-36904)
- Fixed an issue where **POST** to `    /api/controller/login/` via the gateway resulted in a fatal response.(AAP-33911)
- Fixed an issue when a job template was launched, the named URL returned a **404** error code.(AAP-37025)


##### 10.17.2.3.1. Container-based Ansible Automation Platform




- Fixed an issue where the receptor TLS certificate content was not validated during the preflight role execution ensuring that the **x509 Subject Alt Name** (SAN) field contains the required ISO Object Identifier (OID) 1.3.6.1.4.1.2312.19.1. (AAP-37880)
- Fixed an issue where the **Postgresql SSL** mode variables for controller, Event-Driven Ansible, gateway and automation hub were not validated during the preflight role execution. (AAP-37352)
- Fixed an issue where the Ansible Automation Platform containerized setup installation would upload collections when inventory growth in the AIO installation was used.(AAP-38372)
- Fixed an issue where the throttle capacity of controller in an AIO installation would allow for performance degradation.(AAP-38207)


#### 10.17.2.4. RPM-based Ansible Automation Platform




- Fixed an issue where adding a new automation hub host to an upgraded environment has caused the installation to fail. (AAP-38204)
- Fixed an issue where the link to the documents in the installer **README.md** was broken. (AAP-37627)
- Fixed an issue where the Gateway API status on Event-Driven Ansible proxy component returned **404** errors. (AAP-32816)


