# 6. Network ports and protocols
## 6.2. Network ports and protocols table

The following table indicates the destination port and the direction of network traffic:

Note

- The following default destination ports and installer inventory listed are configurable. If you choose to configure them to suit your environment, you might experience a change in behavior.
- Port 443 is the industry standard for HTTPS. Port 80 is not mandatory, but is included for environments that might want to have an unsecure connection.

**For RPM-based installations**

- Use Port 80 if you set any of `nginx_disable_https`, `automationhub_disable_https` or `automationedacontroller_disable_https` to `true`. See [Security-relevant variables in the installation inventory](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#ref-security-variables-install-inventory_hardening-aap)

**For container-based installations**

- Use Port 80 if you set any of `controller_nginx_disable_https`, `hub_nginx_disable_https` or `eda_nginx_disable_https` to `true`. See [Security-relevant variables in the installation inventory](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#ref-security-variables-install-inventory_hardening-aap)

The following table shows container-based installation ports and inventory variables in **bold** text.

**Network ports and protocols**

| Destination | Port | Source | Protocol | Service | Required for | Installer Inventory Variable |
| --- | --- | --- | --- | --- | --- | --- |
| <br>  Automation hub | <br>  22 | <br>  Installer node | <br>  TCP | <br>  SSH | <br>  Management (Install, Configure, Upgrade) | <br>  ansible_port |
| <br>  Automation hub | <br>  80/443 | <br>  Installer node | <br>  TCP | <br>  HTTP/HTTPS | <br>  Enables installer node to push the execution environment image to automation hub when using the bundle installer. | <br>  ansible_port |
| <br>  Automation hub | <br>  80/443 | <br>  Automation controller | <br>  TCP | <br>  HTTP/HTTPS | <br>  Pull collections |  |
| <br>  Automation hub | <br>  80/443 | <br>  Event-Driven Ansible node | <br>  TCP | <br>  HTTP/HTTPS | <br>  Pull container decision environments |  |
| <br>  Automation hub | <br>  80/443 | <br>  Execution node | <br>  TCP | <br>  HTTP/HTTPS | <br>  Allows execution nodes to pull the execution environment image from automation hub |  |
| <br>  Automation hub | <br>  80/443 | <br>  Gateway load balancer/Ingress node | <br>  TCP | <br>  HTTP/HTTPS | <br>  Accessing the component directly from platform gateway | <br>  automationgateway_main_url <br> **gateway_main_url** |
| <br>  Automation hub | <br>  443 **8444** | <br>  Platform gateway | <br>  TCP | <br>  HTTPS | <br>  Link between platform gateway and Ansible Automation Platform components |  |
| <br>  Automation hub | <br>  6379 | <br>  Event-Driven Ansible | <br>  TCP | <br>  Redis | <br>  Event processing |  |
| <br>  Automation controller | <br>  22 | <br>  Installer node | <br>  TCP | <br>  SSH | <br>  Management (Install, Configure, Upgrade) | <br>  ansible_port |
| <br>  Automation controller | <br>  80/443 | <br>  Event-Driven Ansible | <br>  TCP | <br>  HTTP/HTTPS | <br>  Launch automation controller jobs |  |
| <br>  Automation controller | <br>  80/443 **80/8443** | <br>  Platform gateway | <br>  TCP | <br>  HTTP/HTTPS | <br>  Link between platform gateway and Ansible Automation Platform components |  |
| <br>  Automation controller | <br>  80/443 | <br>  Gateway load balancer/Ingress node | <br>  TCP | <br>  HTTP/HTTPS | <br>  Accessing the component directly from Platform gateway |  |
| <br>  Automation controller | <br>  27199 | <br>  Execution node | <br>  TCP | <br>  Receptor | <br>  Used for Mesh peering and communication. See [Defining automation mesh node types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/automation_mesh_for_vm_environments/index#defining-node-types). | <br>  receptor_listener_port <br>  peers <br> **receptor_port**<br> **receptor_peers** |
| <br>  Event-Driven Ansible | <br>  22 | <br>  Installer node | <br>  TCP | <br>  SSH | <br>  Management (Install, Configure, Upgrade) | <br>  ansible_port |
| <br>  Event-Driven Ansible | <br>  80/443 **80/8445** | <br>  Platform gateway | <br>  TCP | <br>  HTTP/HTTPS | <br>  Link between platform gateway and Ansible Automation Platform components |  |
| <br>  Event-Driven Ansible | <br>  80/443 | <br>  Gateway load balancer/Ingress node | <br>  TCP | <br>  HTTP/HTTPS | <br>  Accessing the component directly from platform gateway | <br>  automationgateway_main_url <br> **gateway_main_url** |
| <br>  Event-Driven Ansible | <br>  80/443 **8443** | <br>  Platform gateway | <br>  TCP | <br>  HTTPS | <br>  Receiving event stream traffic |  |
| <br>  Execution node | <br>  22 | <br>  Installer node | <br>  TCP | <br>  SSH | <br>  Management (Install, Configure, Upgrade) | <br>  ansible_port |
| <br>  Execution node | <br>  443 | <br>  Gateway load balancer/Ingress node | <br>  TCP | <br>  HTTPS |  | <br>  automationgateway_main_url <br> **gateway_main_url** |
| <br>  Execution node | <br>  27199 | <br>  Automation controller | <br>  TCP | <br>  Receptor | <br>  Used for Mesh peering and communication. See [Defining automation mesh node types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/automation_mesh_for_vm_environments/index#defining-node-types). | <br>  receptor_listener_port <br>  peers <br> **receptor_port**<br> **receptor_peers** |
| <br>  Execution node | <br>  27199 | <br>  OpenShift Container Platform | <br>  TCP | <br>  Receptor |  |  |
| <br>  Hop node | <br>  22 | <br>  Installer node | <br>  TCP | <br>  SSH | <br>  Management (Install, Configure, Upgrade) | <br>  ansible_port |
| <br>  Hop node | <br>  27199 | <br>  Automation controller | <br>  TCP | <br>  Receptor | <br>  ENABLE connections from hop nodes to Receptor port if relayed through hop nodes. See [Defining automation mesh node types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/automation_mesh_for_vm_environments/index#defining-node-types). | <br>  receptor_listener_port <br>  peers <br> **receptor_port**<br> **receptor_peers** |
| <br>  Hop node | <br>  27199 | <br>  Execution node | <br>  TCP | <br>  Receptor | <br>  Used for Mesh peering and communication. See [Defining automation mesh node types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/automation_mesh_for_vm_environments/index#defining-node-types). | <br>  receptor_listener_port <br>  peers <br> **receptor_port**<br> **receptor_peers** |
| <br>  Hybrid node | <br>  22 | <br>  Installer node | <br>  TCP | <br>  SSH | <br>  Management (Install, Configure, Upgrade) | <br> `ansible_port` |
| <br>  Hybrid node | <br>  27199 | <br>  Automation controller | <br>  TCP | <br>  Receptor | <br>  ENABLE connections from automation controller to Receptor port if relayed through non-hop connected nodes. See [Defining automation mesh node types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/automation_mesh_for_vm_environments/index#defining-node-types). | <br>  receptor_listener_port <br>  peers <br> **receptor_port**<br> **receptor_peers** |
| <br>  PostgreSQL database | <br>  22 | <br>  Installer node | <br>  TCP | <br>  SSH | <br>  Management (Install, Configure, Upgrade) | <br> `pg_port` |
| <br>  PostgreSQL database | <br>  5432 | <br>  Automation controller | <br>  TCP | <br>  PostgreSQL | <br>  Required only if the internal database is used with another component. Otherwise, this port should not be open. | <br>  automationcontroller_pg_port <br> **controller_pg_port** |
| <br>  PostgreSQL database | <br>  5432 | <br>  Event-Driven Ansible | <br>  TCP | <br>  PostgreSQL | <br>  Required only if the internal database is used with another component. Otherwise, this port should not be open. | <br>  automationedacontroller_pg_port <br> **eda_pg_port** |
| <br>  PostgreSQL | <br>  5432 | <br>  Automation hub | <br>  TCP | <br>  PostgreSQL | <br>  Required only if the internal database is used with another component. Otherwise, this port should not be open | <br>  automationhub_pg_port <br> **hub_pg_port** |
| <br>  OpenShift Container Platform (RPM only) | <br>  6443 | <br>  Automation controller | <br>  TCP | <br>  HTTP/HTTPS | <br>  Only required when using container groups to run jobs. | <br>  Hostname of OpenShift API server |
| <br>  Redis node | <br>  6379 | <br>  Automation controller | <br>  TCP | <br>  Redis | <br>  Job launching |  |
| <br>  Redis node | <br>  6379 | <br>  Event-Driven Ansible | <br>  TCP | <br>  Redis | <br>  Job launching |  |
| <br>  Redis node | <br>  6379 | <br>  Automation hub | <br>  TCP | <br>  Redis | <br>  Job launching |  |
| <br>  Redis node | <br>  6379 | <br>  Platform gateway | <br>  TCP | <br>  Redis | <br>  Data storage and retrieval |  |
| <br>  Redis node | <br>  16379 | <br>  Redis node | <br>  TCP | <br>  Redis | <br>  Redis cluster bus port for a resilient Redis configuration |  |
| <br>  Mesh ingress | <br>  443 | <br>  Execution node | <br>  Receptor | <br>  HTTPS | <br>  If using mesh ingress, ensure that outbound HTTPS (port 443) is allowed from the execution nodes to the OpenShift route URL. |  |
| <br>  Platform gateway | <br>  80/443 **80/8444** | <br>  Automation hub | <br>  TCP | <br>  HTTPS | <br>  Link between platform gateway and Ansible Automation Platform components |  |
| <br>  Platform gateway | <br>  8443 | <br>  Platform gateway | <br>  TCP | <br>  HTTPS | <br>  nginx |  |

Note

- Hybrid nodes act as a combination of control and execution nodes, and therefore Hybrid nodes share the connections of both.
- If `receptor_listener_port` is defined, the machine also requires an available open port on which to establish inbound TCP connections, for example, 27199.

