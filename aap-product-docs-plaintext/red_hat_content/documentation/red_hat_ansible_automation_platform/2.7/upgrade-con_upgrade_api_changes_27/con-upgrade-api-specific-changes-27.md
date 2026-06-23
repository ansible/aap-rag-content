# API changes in Ansible Automation Platform 2.7
## Specific API changes

In Red Hat Ansible Automation Platform 2.7, all API access must go through the platform gateway hostname. Direct access to component hostnames has been removed.

| Old (Ansible Automation Platform 2.6)          | New (Ansible Automation Platform 2.7)             | Status   |
| ---------------------------------------------- | ------------------------------------------------- | -------- |
| `https://controller.example.com/api/v2/*`      | `https://gateway.example.com/api/controller/v2/*` | Required |
| `https://hub.example.com/api/automation-hub/*` | `https://gateway.example.com/api/galaxy/*`        | Required |
| `https://eda.example.com/api/eda/v1/*`         | `https://gateway.example.com/api/eda/v1/*`        | Required |


Note:

Attempting to access component hostnames directly (`controller.example.com`, `hub.example.com`, `eda.example.com`) returns HTTP 401 Unauthorized in Red Hat Ansible Automation Platform 2.7.

