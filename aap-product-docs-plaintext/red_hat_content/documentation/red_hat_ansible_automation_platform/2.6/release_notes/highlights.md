# 9. Patch releases
## 9.2. Ansible Automation Platform patch release March 25, 2026
### 9.2.2. Highlights

**Expanded audit and access logging**

Introduces and extends audit logging for users, teams, organizations, role assignments, dynamic preferences, and direct component access, improving traceability of administrative and configuration changes. AAP-67043, AAP-66919, AAP-66800, AAP-66668

**Platform-wide move to Django 5.2 LTS**

Upgrades Django for gateway, Automation hub, Automation controller, and Red Hat Ansible Lightspeed components to Django 5.2 LTS, aligning with a supported, more secure framework baseline.

Note

Due to this upgrade, all users must use a new installer for both containerized and RPM versions.

AAP-68587, AAP-68135, AAP-60155, AAP-59873, AAP-60388, AAP-64430

**Security hardening through CVE remediation**

Resolves multiple vulnerabilities in UI, automation controller, gateway proxy, automation hub, Red Hat Ansible Lightspeed, and packaging, including issues in Axios, Authlib, Pillow, pyasn1, cryptography, jsonpath, AIOHTTP, express-rate-limit, and Go’s crypto/tls and net/url libraries. AAP-69040, AAP-68686, AAP-68683, AAP-68529, AAP-68526, AAP-67735, AAP-67503, AAP-66903, AAP-66695, AAP-66655, AAP-66636, AAP-65713, AAP-65711, AAP-65695, AAP-65507, AAP-65506, AAP-65505, AAP-65475, AAP-65474, AAP-65473, AAP-65472, AAP-65412, AAP-65411, AAP-65410, AAP-65409, AAP-65224, AAP-64902, AAP-61921

**Improved stability and performance across services**

Addresses issues impacting UI responsiveness, containerized installer behavior after Django upgrades, constructed inventory and facts handling, credential validation in Event-Driven Ansible, database restore flows in platform operators, and certificate handling in execution environments. AAP-69005, AAP-68843, AAP-68842, AAP-68841, AAP-68135, AAP-68079, AAP-67759, AAP-67749, AAP-67579, AAP-67552, AAP-67550, AAP-67549, AAP-67548, AAP-67498, AAP-67460, AAP-67371, AAP-67230, AAP-67081, AAP-67080, AAP-67079, AAP-67078, AAP-67038, AAP-66864, AAP-66845, AAP-66806, AAP-66706, AAP-66579, AAP-66400, AAP-66106, AAP-66105, AAP-66104, AAP-66102, AAP-65109, AAP-65081, AAP-64996, AAP-64630, AAP-64146, AAP-60313, AAP-60238, AAP-58769, AAP-58535, AAP-22149

This update rebases the containerized installer to `ansible.platform` collection version 2.6.20260306, aligning the installer with the current Ansible Automation Platform 2.6 collection release. AAP-67548

