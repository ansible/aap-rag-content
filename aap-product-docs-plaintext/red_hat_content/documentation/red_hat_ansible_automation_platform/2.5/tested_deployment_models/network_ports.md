# 2. RPM topologies
## 2.1. RPM growth topology
### 2.1.3. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server for it to work. Ensure that these ports are available and are not blocked by the server firewall.


<span id="idm139937749852144"></span>
**Table 2.4. Network ports and protocols**

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Automation controller | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation controller |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation hub |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Event-Driven Ansible |
| 5432 | TCP | PostgreSQL | Event-Driven Ansible | Database |
| 5432 | TCP | PostgreSQL | Platform gateway | Database |
| 5432 | TCP | PostgreSQL | Automation hub | Database |
| 5432 | TCP | PostgreSQL | Automation controller | Database |
| 6379 | TCP | Redis | Event-Driven Ansible | Redis node |
| 6379 | TCP | Redis | Platform gateway | Redis node |
| 8443 | TCP | HTTPS | Platform gateway | Platform gateway |
| 27199 | TCP | Receptor | Automation controller | Execution node |




