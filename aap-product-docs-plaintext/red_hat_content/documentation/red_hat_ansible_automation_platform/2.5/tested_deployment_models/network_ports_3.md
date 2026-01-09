# 3. Container topologies
## 3.1. Container growth topology
### 3.1.3. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.


<span id="idm139972754796480"></span>
**Table 3.4. Network ports and protocols**

| Port number | Protocol | Service | Source | Destination | Description |
| --- | --- | --- | --- | --- | --- |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation hub | Pull container decision environments |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible | Automation controller | Launch automation controller jobs |
| 80/443 | TCP | HTTP/HTTPS | Automation controller | Automation hub | Pull collections and execution environment images |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation controller | Platform gateway to automation controller communication |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation hub | Platform gateway to automation hub communication |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Event-Driven Ansible | Platform gateway to Event-Driven Ansible communication |
| 5432 | TCP | PostgreSQL | Event-Driven Ansible | Database | Event-Driven Ansible database access |
| 5432 | TCP | PostgreSQL | Platform gateway | Database | Platform gateway database access |
| 5432 | TCP | PostgreSQL | Automation hub | Database | Automation hub database access |
| 5432 | TCP | PostgreSQL | Automation controller | Database | Automation controller database access |
| 6379 | TCP | Redis | Event-Driven Ansible | Redis container | Job launching and data storage for Event-Driven Ansible |
| 6379 | TCP | Redis | Platform gateway | Redis container | Data storage and retrieval for platform gateway services |
| 8443 | TCP | HTTPS | Platform gateway | Platform gateway | Internal gateway NGINX communication |
| 27199 | TCP | Receptor | Automation controller | Execution container | Mesh nodes connect directly to controllers. Allows two-way communication for job distribution. |
| 8080/8443 | TCP | HTTP/HTTPS | Platform gateway | Automation controller | Automation controller NGINX ports. You can configure these ports with the following inventory variables: `controller_nginx_http_port` , `controller_nginx_https_port` . |
| 8081/8444 | TCP | HTTP/HTTPS | Platform gateway | Automation hub | Automation hub NGINX ports. You can configure these ports with the following inventory variables: `hub_nginx_http_port` , `hub_nginx_https_port` . |
| 8082/8445 | TCP | HTTP/HTTPS | Platform gateway | Event-Driven Ansible | Event-Driven Ansible NGINX ports. You can configure these ports with the following inventory variables: `eda_nginx_http_port` , `eda_nginx_https_port` . |
| 8083/8446 | TCP | HTTP/HTTPS | Platform gateway | Platform gateway | Platform gateway NGINX ports. You can configure these ports with the following inventory variables: `gateway_nginx_http_port` , `gateway_nginx_https_port` . |




Note
If you change any port values by using inventory variables, refer to [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars) to review all default port values and ensure there are no port conflicts.



