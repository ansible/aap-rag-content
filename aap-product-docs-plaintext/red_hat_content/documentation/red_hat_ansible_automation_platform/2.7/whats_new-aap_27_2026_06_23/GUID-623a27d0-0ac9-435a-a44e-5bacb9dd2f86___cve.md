# Ansible Automation Platform 2.7 Release Notes - June 23, 2026 (2.7-2)
## CVE

- **Event-Driven Ansible**
* [CVE-2026-11807](https://access.redhat.com/security/cve/cve-2026-11807) - A missing authorization vulnerability was found in the Event-Driven Ansible (EDA) websocket API. The websocket missing authorization allows credential theft via activation_id spoofing:
+ `eda-controller-rhel9`. AAP-78382
