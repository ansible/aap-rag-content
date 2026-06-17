# 2. Container topologies
## 2.2. Container enterprise topology
### 2.2.3. Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

**Table 2.8. Network ports and protocols**

| Port number | Protocol | Service | Source | Destination | Description |
| --- | --- | --- | --- | --- | --- |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Event-Driven Ansible | <br>  Automation hub | <br>  Pull container decision environments |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Event-Driven Ansible | <br>  Automation controller | <br>  Launch automation controller jobs |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Automation controller | <br>  Automation hub | <br>  Pull collections and execution environment images |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  HAProxy load balancer | <br>  Platform gateway | <br>  External load balancer access |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Platform gateway | <br>  Automation controller | <br>  Platform gateway to automation controller communication |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Platform gateway | <br>  Automation hub | <br>  Platform gateway to automation hub communication |
| <br>  80/443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Platform gateway | <br>  Event-Driven Ansible | <br>  Platform gateway to Event-Driven Ansible communication |
| <br>  5432 | <br>  TCP | <br>  PostgreSQL | <br>  Event-Driven Ansible | <br>  External database | <br>  Event-Driven Ansible database access |
| <br>  5432 | <br>  TCP | <br>  PostgreSQL | <br>  Platform gateway | <br>  External database | <br>  Platform gateway database access |
| <br>  5432 | <br>  TCP | <br>  PostgreSQL | <br>  Automation hub | <br>  External database | <br>  Automation hub database access |
| <br>  5432 | <br>  TCP | <br>  PostgreSQL | <br>  Automation controller | <br>  External database | <br>  Automation controller database access |
| <br>  6379 | <br>  TCP | <br>  Redis | <br>  Event-Driven Ansible | <br>  Redis node | <br>  Job launching and data storage for Event-Driven Ansible |
| <br>  6379 | <br>  TCP | <br>  Redis | <br>  Platform gateway | <br>  Redis node | <br>  Data storage and retrieval for platform gateway services |
| <br>  16379 | <br>  TCP | <br>  Redis | <br>  Redis node | <br>  Redis node | <br>  Redis cluster bus communication |
| <br>  27199 | <br>  TCP | <br>  Receptor | <br>  Automation controller | <br>  Hop node and execution node | <br>  Mesh nodes connect directly to controllers. Allows two-way communication for job distribution. |
| <br>  27199 | <br>  TCP | <br>  Receptor | <br>  Hop node | <br>  Execution node | <br>  Mesh nodes connect through hop nodes. Allows two-way communication in either direction. |
| <br>  8080/8443 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Platform gateway | <br>  Automation controller | <br>  Automation controller NGINX ports. You can configure these ports with the following inventory variables: `controller_nginx_http_port`, `controller_nginx_https_port`. |
| <br>  8081/8444 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Platform gateway | <br>  Automation hub | <br>  Automation hub NGINX ports. You can configure these ports with the following inventory variables: `hub_nginx_http_port`, `hub_nginx_https_port`. |
| <br>  8082/8445 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Platform gateway | <br>  Event-Driven Ansible | <br>  Event-Driven Ansible NGINX ports. You can configure these ports with the following inventory variables: `eda_nginx_http_port`, `eda_nginx_https_port`. |
| <br>  8083/8446 | <br>  TCP | <br>  HTTP/HTTPS | <br>  Platform gateway | <br>  Platform gateway | <br>  Platform gateway NGINX ports. You can configure these ports with the following inventory variables: `gateway_nginx_http_port`, `gateway_nginx_https_port`. |

Note

If you change any port values by using inventory variables, refer to [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars) to review all default port values and ensure there are no port conflicts.

