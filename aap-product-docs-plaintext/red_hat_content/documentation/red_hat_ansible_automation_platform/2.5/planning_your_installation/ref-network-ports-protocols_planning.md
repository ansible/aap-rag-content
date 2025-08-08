# Chapter 6. Network ports and protocols




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server in order for it to work. Ensure that these ports are available and are not blocked by the server firewall.

The following architectural diagram is an example of a fully deployed Ansible Automation Platform with all possible components.

Note
In some of the following use cases, hop nodes are used instead of a direct link from an execution node. Hop nodes are an option for connecting control and execution nodes. Hop nodes use minimal CPU and memory, so vertically scaling hop nodes does not impact system capacity.



Note
Direct connections shown in the diagram between the Client and automation hub, Event-Driven Ansible, and automation controller only apply to systems upgraded from Red Hat Ansible Automation Platform 2.4 to Red Hat Ansible Automation Platform 2.5 to provide backward compatibility. The connection does not exist for Red Hat Ansible Automation Platform 2.5.



The following table indicates the destination port and the direction of network traffic:


<span id="idm140696950965584"></span>
**Figure 6.1. Ansible Automation Platform Network ports and protocols**

![Interaction of Ansible Automation Platform components on the network with information about the ports and protocols that are used.](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Planning_your_installation-en-US/images/8991674f3ce4f960ede12744714b30c1/aap-network-ports-protocols.png)




Note
The following default destination ports and installer inventory listed are configurable. If you choose to configure them to suit your environment, you might experience a change in behavior.




<span id="idm140696957063552"></span>
**Table 6.1. Network ports and protocols**

| Port | Protocol | Service | Source | Destination | Required for | Installer Inventory Variable |
| --- | --- | --- | --- | --- | --- | --- |
| 22 | TCP | SSH | Installer node | Automation hub | Installation (temporary) |  `ansible_port` |
| 22 | TCP | SSH | Installer node | Controller node | Installation (temporary) |  `ansible_port` |
| 22 | TCP | SSH | Installer node | Event-Driven Ansible node | Installation (temporary) |  `ansible_port` |
| 22 | TCP | SSH | Installer node | Execution node | Installation (temporary) |  `ansible_port` |
| 22 | TCP | SSH | Installer node | Hop node | Installation (temporary) |  `ansible_port` |
| 22 | TCP | SSH | Installer node | Hybrid node | Installation (temporary) |  `ansible_port` |
| 22 | TCP | SSH | Installer node | PostgreSQL database | Remote access during installation (temporary) |  `pg_port` |
| 80/443 | TCP | HTTP/HTTPS | Installer node | Automation hub | Allows installer node to push the execution environment image to automation hub when using the bundle installer. | Fixed value |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible node | Automation hub | Pull container decision environments | Fixed value |
| 80/443 | TCP | HTTP/HTTPS | Event-Driven Ansible node | Automation controller | Launch automation controller jobs | Fixed value |
| 80/443 | TCP | HTTP/HTTPS | Automation controller | Automation hub | Pull collections | Fixed value |
| 80/443 | TCP | HTTP/HTTPS | Execution node | Automation hub | Allows execution nodes to pull the execution environment image from automation hub. | Fixed value |
| 80/443 | TCP | HTTP/HTTPS | HA Proxy load balancer/Ingress Node | Platform gateway | This is the ingress above the platform gateway that is customer controlled and can load balance requests to multiple gateways. | This port is customer managed outside of Ansible Automation Platform. |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation controller | Link between gateway and Ansible Automation Platform components |  |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Automation hub | Link between gateway and Ansible Automation Platform components |  |
| 80/443 | TCP | HTTP/HTTPS | Platform gateway | Event-Driven Ansible | Link between gateway and Ansible Automation Platform components |  |
| 80/443 | TCP | HTTP/HTTPS | HA Proxy load balancer/Ingress Node | Automation controller | Only relevant if accessing the component directly from Platform gateway |  `automationgateway_main_url` |
| 80/443 | TCP | HTTP/HTTPS | HA Proxy load balancer/Ingress Node | Automation hub | Only relevant if accessing the component directly from Platform gateway |  `automationgatweway_main_url` |
| 80/443 | TCP | HTTP/HTTPS | HA Proxy load balancer/Ingress Node | Event-Driven Ansible | Only relevant if accessing the component directly from Platform gateway |  `automationgateway_main_url` |
| 443 | TCP | HTTPS | Remote execution node (Client) | Controller node | Web UI/API |  `nginx_https_port` |
| 5432 | TCP | PostgreSQL | Controller node | PostgreSQL database | Open only if the internal database is used along with another component. Otherwise, this port should not be open. |  `automationcontroller_pg_port` |
| 5432 | TCP | PostgreSQL | Event-Driven Ansible node | PostgreSQL database | Open only if the internal database is used along with another component. Otherwise, this port should not be open. |  `automationedacontroller_pg_port` |
| 5432 | TCP | PostgreSQL | Automation hub | PostgreSQL database | Open only if the internal database is used along with another component. Otherwise, this port should not be open. |  `automationhub_pg_port` |
| 5432 | TCP | PostgreSQL | Platform gateway | External database | Open only if the internal database is used along with another component. Otherwise, this port should not be open. |  `automationgateway_pg_port` |
| 6379 | TCP | Redis | Event-Driven Ansible | Redis node | Job launching |  |
| 6379 | TCP | Redis | Platform gateway | Redis node | Data storage and retrieval |  |
| 6443 | TCP | HTTP/HTTPS | Controller node | OpenShift Container Platform | Only required when using container groups to run jobs. | Host name of OpenShift API server |
| 8443 | TCP | HTTPS | Platform gateway | Platform gateway | nginx |  |
| 16379 | TCP | Redis | Redis nodes | Redis nodes | Redis cluster bus port for a resilient Redis configuration |  |
| 27199 | TCP | Receptor | Controller node | Execution node | Configurable

Mesh nodes directly peered to controllers.

Direct nodes involved. 27199 communication can be both ways (depending on installation inventory) for execution nodes |  `receptor_listener_port`

`peers` |
| 27199 | TCP | Receptor | Controller node | Hop node | Configurable

ENABLE connections from hop nodes to Receptor port if relayed through hop nodes. |  `receptor_listener_port`

`peers` |
| 27199 | TCP | Receptor | Controller node | Hybrid node | Configurable

ENABLE connections from controllers to Receptor port if relayed through non-hop connected nodes. |  `receptor_listener_port`

`peers` |
| 27199 | TCP | Receptor | Execution node | Hop node | Configurable

Mesh 27199 communication can be both ways (depending on installation inventory) for execution nodes

ALLOW connection from controller(s) to Receptor port |  `receptor_listener_port`

`peers` |
| 27199 | TCP | Receptor | Hop node | Execution node | Configurable

Mesh 27199 communication can be both ways (depending on installation inventory) for execution nodes |  `receptor_listener_port`

`peers` |
| 27199 | TCP | Receptor | Execution node | Controller node | Configurable

Mesh 27199 communication can be both ways (depending on installation inventory) for execution nodes

ALLOW connection from controller(s) to Receptor port |  `receptor_listener_port`

`peers` |
| 27199 | TCP | Receptor | OCP cluster | Execution node |  |  |
| 8443 | TCP | HTTPS | Platform gateway | Event-Driven Ansible node | Receiving event stream traffic |  |




Note
- Hybrid nodes act as a combination of control and execution nodes, and therefore Hybrid nodes share the connections of both.
- If `    receptor_listener_port` is defined, the machine also requires an available open port on which to establish inbound TCP connections, for example, 27199.
- It might be the case that some servers do not listen on receptor port (the default is 27199)

Suppose you have a Control plane with nodes A, B, C, D

The RPM installer creates a strongly connected peering between the control plane nodes with a least privileged approach and opens the tcp listener only on those nodes where it is required. All the receptor connections are bidirectional, so once the connection is created, the receptor can communicate in both directions.

The following is an example peering set up for three controller nodes:

Controller node A -→ Controller node B

Controller node A -→ Controller node C

Controller node B -→ Controller node C

You can force the listener by setting

`    receptor_listener=True`

However, a connection Controller B -→ A is likely to be rejected as that connection already exists.

This means that nothing connects to Controller A as Controller A is creating the connections to the other nodes, and the following command does not return anything on Controller A:

`    [root@controller1 ~]# ss -ntlp | grep 27199 [root@controller1 ~]#`







<span id="idm140696952219888"></span>
**Table 6.2. Red Hat Insights for Red Hat Ansible Automation Platform**

| URL | Required for |
| --- | --- |
|  [https://api.access.redhat.com:443](https://api.access.redhat.com) | General account services, subscriptions |
|  [https://cert-api.access.redhat.com:443](https://cert-api.access.redhat.com) | Insights data upload |
|  [https://cert.console.redhat.com:443](https://cert.console.redhat.com) | Inventory upload and Cloud Connector connection |
|  [https://console.redhat.com:443](https://console.redhat.com) | Access to Insights dashboard |





<span id="idm140696959081984"></span>
**Table 6.3. Automation Hub**

| URL | Required for |
| --- | --- |
|  [https://console.redhat.com:443](https://console.redhat.com) | General account services, subscriptions |
|  [https://catalog.redhat.com:443](https://catalog.redhat.com) | Indexing execution environments |
|  [https://sso.redhat.com:443](https://sso.redhat.com) | TCP |
| https://automation-hub-prd.s3.amazonaws.com
https://automation-hub-prd.s3.us-east-2.amazonaws.com | Firewall access |
|  [https://galaxy.ansible.com:443](https://galaxy.ansible.com) | Ansible Community curated Ansible content |
| https://ansible-galaxy-ng.s3.dualstack.us-east-1.amazonaws.com | Dual Stack IPv6 endpoint for Community curated Ansible content repository |
|  [https://registry.redhat.io:443](https://registry.redhat.io) | Access to container images provided by Red Hat and partners |
|  [https://cert.console.redhat.com:443](https://cert.console.redhat.com) | Red Hat and partner curated Ansible Collections |





<span id="idm140696952898384"></span>
**Table 6.4. Execution Environments (EE)**

| URL | Required for |
| --- | --- |
|  [https://registry.redhat.io:443](https://registry.redhat.io) | Access to container images provided by Red Hat and partners |
|  `cdn.quay.io:443` | Access to container images provided by Red Hat and partners |
|  `cdn01.quay.io:443` | Access to container images provided by Red Hat and partners |
|  `cdn02.quay.io:443` | Access to container images provided by Red Hat and partners |
|  `cdn03.quay.io:443` | Access to container images provided by Red Hat and partners |




Important
As of **April 1st, 2025** , `quay.io` is adding three additional endpoints. As a result, customers must adjust allow/block lists within their firewall systems lists to include the following endpoints:

-  `    cdn04.quay.io`
-  `    cdn05.quay.io`
-  `    cdn06.quay.io`


To avoid problems pulling container images, customers must allow outbound TCP connections (ports 80 and 443) to the following hostnames:

-  `    cdn.quay.io`
-  `    cdn01.quay.io`
-  `    cdn02.quay.io`
-  `    cdn03.quay.io`
-  `    cdn04.quay.io`
-  `    cdn05.quay.io`
-  `    cdn06.quay.io`


This change should be made to any firewall configuration that specifically enables outbound connections to `registry.redhat.io` or `registry.access.redhat.com` .

Use the hostnames instead of IP addresses when configuring firewall rules.

After making this change, you can continue to pull images from `registry.redhat.io` or `registry.access.redhat.com` . You do not require a `quay.io` login, or need to interact with the `quay.io` registry directly in any way to continue pulling Red Hat container images.

For more information, see [Firewall changes for container image pulls 2024/2025](https://access.redhat.com/articles/7084334) .



