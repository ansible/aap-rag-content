# Ansible Automation Platform 2.7 patch release August 24, 2026 (2.7-6)
## Automation controller

- Automation controller
* [CVE-2026-52902](https://access.redhat.com/security/cve/CVE-2026-52902) – path traversal via YAML !include directive. AAP-80013
- Automation controller (container image: ansible-automation-platform-27/controller-rhel9)
* [CVE-2026-44545](https://access.redhat.com/security/cve/CVE-2026-44545) – daphne: Denial of Service via excessive WebSocket message size. AAP-82613
* [CVE-2026-71365](https://access.redhat.com/security/cve/CVE-2026-71365) – webhook status callback SSRF leaks the Git PAT. AAP-86687
* [CVE-2026-44244](https://access.redhat.com/security/cve/CVE-2026-44244) – GitPython: Arbitrary code execution via injected newlines in Git configuration. AAP-88240
* [CVE-2026-71366](https://access.redhat.com/security/cve/CVE-2026-71366)– notification backends allow SSRF and credential leakage. AAP-86683
* [CVE-2026-71364](https://access.redhat.com/security/cve/CVE-2026-71364)– project archive extraction allows path traversal file writes. AAP-86690

