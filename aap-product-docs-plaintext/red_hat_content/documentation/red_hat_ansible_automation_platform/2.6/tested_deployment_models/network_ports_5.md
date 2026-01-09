# 4. RPM topologies
## 4.1. RPM growth topology
### 4.1.3. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.


<span id="idm140186612091872"></span>
**Table 4.4. Network ports and protocols**

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Automation controller | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Event-Driven Ansible |
| 80/443 | TCP | HTTP/HTTPS | Execution node | Platform gateway |
| 5432 | TCP | PostgreSQL | Event-Driven Ansible | Database |
| 5432 | TCP | PostgreSQL | Platform gateway | Database |
| 5432 | TCP | PostgreSQL | Automation hub | Database |
| 5432 | TCP | PostgreSQL | Automation controller | Database |
| 6379 | TCP | Redis | Event-Driven Ansible | Redis node |
| 6379 | TCP | Redis | Platform gateway | Redis node |
| 8443 | TCP | HTTPS | Platform gateway | Platform gateway |
| 27199 | TCP | Receptor | Automation controller | Execution node |




Note
If you change any port values by using inventory variables, refer to [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars) to review all default port values and ensure there are no port conflicts.



