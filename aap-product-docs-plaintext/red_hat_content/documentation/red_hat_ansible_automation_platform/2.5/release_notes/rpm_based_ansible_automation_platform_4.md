# 10. Patch releases
## 10.4. Ansible Automation Platform patch release July 2, 2025
### 10.4.11. RPM-based Ansible Automation Platform




#### 10.4.11.1. Bug Fixes




- Fixed an issue where redis-platform would not restart on restore.(AAP-47689)
- Fixed an issue where old service nodes were not removed from platform gateway when the installer ran with a new host or new host names.(AAP-47651)
- Fixed an issue where restore was failing when a non-default port was used for Ansible Automation Platform managed database.(AAP-47639)
- Fixed an issue where some pages didn’t render properly when non-default `    umask` was being used.(AAP-47377)
- Fixed an issue where the Event-Driven Ansible script was not starting `    nginx` on restart.(AAP-46511)
- Fixed an issue where the credentials associated to decision environments would not be updated with the site information defined in the source inventory during restore.(AAP-46271)
- Fixed an issue where the receptor certificate tasks would require switching to a receptor user.(AAP-46189)
- Fixed an issue where the firewall was not opening event stream ports.(AAP-45684)


