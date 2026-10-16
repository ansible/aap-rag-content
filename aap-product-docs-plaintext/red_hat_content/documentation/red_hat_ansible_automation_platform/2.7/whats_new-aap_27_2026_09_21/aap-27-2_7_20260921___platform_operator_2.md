# Ansible Automation Platform 2.7 patch release September 21, 2026 (2.7-9)
## Platform Operator

- Fixed an issue where EDA would get a 401 when running Controller job templates, due to a misconfigured automation_server_url value.Fixed an issue where EDA would get a 401 when running Controller job templates, due to a misconfigured automation_server_url value. (AAP-91353)
- Fixed an issue where the Gateway would incorrectly report healthy components (Controller, Hub, EDA) as failed when an HTTP/HTTPS proxy was configured, by ensuring generated Service names are included in the Gateway’s NO_PROXY whitelist. (AAP-91490)
