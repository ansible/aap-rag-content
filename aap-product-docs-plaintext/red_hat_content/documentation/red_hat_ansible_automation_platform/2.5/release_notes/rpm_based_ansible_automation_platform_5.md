# 10. Patch releases
## 10.5. Ansible Automation Platform patch release July 30, 2025
### 10.5.6. RPM-based Ansible Automation Platform




#### 10.5.6.1. Bug Fixes




- Event-Driven Ansible node type is now properly checked during restore.(AAP-49004)
- Fixed an issue where **gRPC** server port was not configured properly when non-default value was used.(AAP-48543)
- Fixed an issue where the firewall role logic improperly restricted Event-Driven Ansible event stream ports. Firewall ports are now restricted to event hosts, enhancing network security for Event-Driven Ansible users.(AAP-49792)
- Fixed an issue where the gunicorn timeout to Event-Driven Ansible API service unit was not passed.(AAP-49858)
- Fixed an issue where envoy, nginx, web server, and jwt token timeouts were not aligned, and caused issues where requests time out but work continues, or tokens expire before they are used.(AAP-49153)


