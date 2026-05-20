# 4. RPM topologies
## 4.2. RPM enterprise topology
### 4.2.3. Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

**Table 4.8. Network ports and protocols**

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Event-Driven Ansible | <br>  Automation hub |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Event-Driven Ansible | <br>  Automation controller |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Automation controller | <br>  Automation hub |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  HAProxy load balancer | <br>  Platform gateway |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Platform gateway | <br>  Automation controller |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Platform gateway | <br>  Automation hub |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Platform gateway | <br>  Event-Driven Ansible |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Execution node | <br>  Platform gateway |
| <br>  5432 | <br>  TCP | <br>  PostgreSQL | <br>  Event-Driven Ansible | <br>  External database |
| <br>  5432 | <br>  TCP | <br>  PostgreSQL | <br>  Platform gateway | <br>  External database |
| <br>  5432 | <br>  TCP | <br>  PostgreSQL | <br>  Automation hub | <br>  External database |
| <br>  5432 | <br>  TCP | <br>  PostgreSQL | <br>  Automation controller | <br>  External database |
| <br>  6379 | <br>  TCP | <br>  Redis | <br>  Event-Driven Ansible | <br>  Redis node |
| <br>  6379 | <br>  TCP | <br>  Redis | <br>  Platform gateway | <br>  Redis node |
| <br>  8443 | <br>  TCP | <br>  HTTPS | <br>  Platform gateway | <br>  Platform gateway |
| <br>  16379 | <br>  TCP | <br>  Redis | <br>  Redis node | <br>  Redis node |
| <br>  27199 | <br>  TCP | <br>  Receptor | <br>  Automation controller | <br>  Hop node and execution node |
| <br>  27199 | <br>  TCP | <br>  Receptor | <br>  Hop node | <br>  Execution node |

Note

If you change any port values by using inventory variables, refer to [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars) to review all default port values and ensure there are no port conflicts.

