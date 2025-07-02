# 10. Patch releases
## 10.11. Ansible Automation Platform patch release January 29, 2025
### 10.11.1. Enhancements




#### 10.11.1.1. Ansible Automation Platform




- Using PostgreSQL TLS certificate authentication with an external database is now available.(AAP-38400)


#### 10.11.1.2. Event-Driven Ansible




- The `    ansible.eda` collection has been updated to 2.3.1.(AAP-39057)
- Users are now able to create a new Event-Driven Ansible credential by copying an existing one.(AAP-39249)
- Added support for **file** and **env** injectors for credentials.(AAP-39091)


#### 10.11.1.3. RPM-based Ansible Automation Platform




- Implemented certificate authentication support (mTLS) for external databases.


- Postgresql TLS certificate authentication is available for external databases.
- Postgresql TLS certificate authentication can be turned on/off (off by default for backward compatibility).
- Each component, automation controller, Event-Driven Ansible, platform gateway, and automation hub, now provides off the shelf (OTS) TLS certificate and key files (mandatory).(AAP-38400)



