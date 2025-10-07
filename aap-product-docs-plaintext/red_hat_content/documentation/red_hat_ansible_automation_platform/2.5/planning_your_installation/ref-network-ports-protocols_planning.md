# Chapter 6. Network ports and protocols




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server in order for it to work. Ensure that these ports are available and are not blocked by the server firewall.

The following architectural diagram is an example of a fully deployed Ansible Automation Platform with all possible components.

Note
In some of the following use cases, hop nodes are used instead of a direct link from an execution node. Hop nodes are an option for connecting control and execution nodes. Hop nodes use minimal CPU and memory, so vertically scaling hop nodes does not impact system capacity.



Note
The following diagraam shows client initiated connections between Ansible Automation Platform components. Direct connections shown in the diagram between the Client and automation hub, Event-Driven Ansible, and automation controller only apply to systems upgraded from Red Hat Ansible Automation Platform 2.4 to Red Hat Ansible Automation Platform 2.5 to provide backward compatibility.




<span id="idm140401814442048"></span>
**Figure 6.1. Ansible Automation Platform Client initiated network ports and protocols**

![Interaction of Ansible Automation Platform components on the network with information about the ports and protocols that are used.](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Planning_your_installation-en-US/images/a20ef5c37cfe1b602560cf28cf3531de/network_client_initiated.png)




Note
The following diagram shows internally initiated connections between Ansible Automation Platform components for new installs Red Hat Ansible Automation Platform 2.5.




<span id="idm140401811129952"></span>
**Figure 6.2. Ansible Automation Platform Internally initiated network ports and protocols**

![Interaction of Ansible Automation Platform components on the network with information about the ports and protocols that are used.](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Planning_your_installation-en-US/images/4c4a35c6cfb3689e7b35e9f47901cb0f/network_internally_initiated.png)




The following table indicates the destination port and the direction of network traffic:

Note
The following default destination ports and installer inventory listed are configurable. If you choose to configure them to suit your environment, you might experience a change in behavior.




<span id="idm140401811123184"></span>
**Table 6.1. Network ports and protocols**

| Node | Port | Source | Protocol | Service | Required for | Installer Inventory Variable |
| --- | --- | --- | --- | --- | --- | --- |
| Automation hub | 22 | Installer node | TCP | SSH | Management of Ansible Automation Platform

- Install
- Configure
- Upgrade |  `ansible_port` |
| Automation hub | 80/443 | Installer node | TCP | HTTP/HTTPS | Enables installer node to push the execution environment image to automation hub when using the bundle installer. |  `ansible_port` |
| Automation hub | 80/443 | Automation controller | TCP | HTTP/HTTPS | Pull collections |  |
| Automation hub | 80/443 | Event-Driven Ansible node | TCP | HTTP/HTTPS | Pull container decision environments |  |
| Automation hub | 80/443 | Execution node | TCP | HTTP/HTTPS | Allows execution nodes to pull the execution environment image from automation hub |  |
| Automation hub | 80/443 | Gateway load balancer/Ingress node | TCP | HTTP/HTTPS | Only relevant if accessing the component directly from platform gateway |  `automationgateway_main_url` |
| Automation hub | 443 | Platform gateway | TCP | HTTPS | Link between platform gateway and Ansible Automation Platform components |  |
| Automation hub | 6379 | Event-Driven Ansible | TCP | Redis |  |  |
| Automation controller | 22 | Installer node | TCP | SSH | Management of Ansible Automation Platform

- Install
- Configure
- Upgrade |  `ansible_port` |
| Automation controller | 80/443 | Event-Driven Ansible | TCP | HTTP/HTTPS | Launch automation controller jobs |  |
| Automation controller | 80/443 | Platform gateway | TCP | HTTP/HTTPS | Link between platform gateway and Ansible Automation Platform components |  |
| Automation controller | 80/443 | Gateway load balancer/Ingress node | TCP | HTTP/HTTPS | Only relevant if accessing the component directly from Platform gateway |  |
| Automation controller | 27199 | Execution node | TCP | Receptor | Configurable

Mesh nodes directly peered to controllers.

Direct nodes involved.

The execution nodes support bidirectional communication through port 27199. This is established in RPM installations through the installation inventory. You can establish the connection in either direction. But communications once established are always bidirectional.

For more information on use of peers in inventory scripts, see [Defining automation mesh node types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/automation_mesh_for_vm_environments/index#defining-node-types) |  `receptor_listener_port`

`peers` |
| Event-Driven Ansible | 22 | Installer node | TCP | SSH | Management of Ansible Automation Platform

- Install
- Configure
- Upgrade |  `ansible_port` |
| Event-Driven Ansible | 80/443 | Platform gateway | TCP | HTTP/HTTPS | Link between platform gateway and Ansible Automation Platform components |  |
| Event-Driven Ansible | 80/443 | Gateway load balancer/Ingress node | TCP | HTTP/HTTPS | Only relevant if accessing the component directly from platform gateway | `automationgateway_main_url |
| Event-Driven Ansible | 8443 | Platform gateway | TCP | HTTPS | Receiving event stream traffic |  |
| Execution node | 22 | Installer node | TCP | SSH | Management of Ansible Automation Platform

- Install
- Configure
- Upgrade |  `ansible_port` |
| Execution node | 443 | Gateway load balancer/Ingress node | TCP | HTTPS |  |  `automationgateway_main_url` |
| Execution node | 27199 | Automation controller | TCP | Receptor | Configurable

Mesh nodes directly peered to controllers.

Direct nodes involved.

The execution nodes support bidirectional communication through port 27199. This is established in RPM installations through the installation inventory. You can establish the connection in either direction. But communications once established are always bidirectional.

For more information on use of peers in inventory scripts, see [Defining automation mesh node types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/automation_mesh_for_vm_environments/index#defining-node-types) |  `receptor_listener_port`

`peers` |
| Execution node | 27199 | OpenShift Container Platform | TCP | Receptor |  |  |
| Hop node | 22 | Installer node | TCP | SSH | Management of Ansible Automation Platform

- Install
- Configure
- Upgrade |  `ansible_port` |
| Hop node | 27199 | Automation controller | TCP | Receptor | Configurable ENABLE connections from hop nodes to Receptor port if relayed through hop nodes. |  `receptor_listener_port` |
| Hop node | 27199 | Execution node | TCP | Receptor | Configurable

Mesh nodes directly peered to controllers.

Direct nodes involved.

The execution nodes support bidirectional communication through port 27199. This is established in RPM installations through the installation inventory. You can establish the connection in either direction. But communications once established are always bidirectional.

For more information on use of peers in inventory scripts, see [Defining automation mesh node types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/automation_mesh_for_vm_environments/index#defining-node-types) |  `receptor_listener_port`

`peers` |
| Hybrid node | 22 | Installer node | TCP | SSH | Management of Ansible Automation Platform

- Install
- Configure
- Upgrade |  `ansible_port` |
| Hybrid node | 27199 | Automation controller | TCP | Receptor | Configurable ENABLE connections from automation controller to Receptor port if relayed through non-hop connected nodes. |  `receptor_listener_port`

`peers` |
| PostgreSQL database | 22 | Installer node | TCP | SSH | Management of Ansible Automation Platform

- Install
- Configure
- Upgrade |  `pg_port` |
| PostgreSQL database | 5432 | Automation controller | TCP | PostgreSQL | Open only if the internal database is used along with another component. Otherwise, this port should not be open. |  `automationcontroller_pg_port` |
| PostgreSQL database | 5432 | Event-Driven Ansible | TCP | PostgreSQL | Open only if the internal database is used along with another component. Otherwise, this port should not be open. |  `automationedacontroller_pg_port` |
| PostgreSQL | 5432 | Automation hub | TCP | PostgreSQL | Open only if the internal database is used along with another component. Otherwise, this port should not be open |  `automationhub_pg_port` |
| OpenShift Container Platform | 6443 | Automation controller | TCP | HTTP/HTTPS | Only required when using container groups to run jobs. | Host name of OpenShift API server |
| Redis node | 6379 | Automation controller | TCP | Redis | Job launching |  |
| Redis node | 6379 | Event-Driven Ansible | TCP | Redis | Job launching |  |
| Redis node | 6379 | Automation hub | TCP | Redis | Job launching |  |
| Redis node | 6379 | Platform gateway | TCP | Redis | Data storage and retrieval |  |
| Redis node | 16379 | Redis node | TCP | Redis | Redis cluster bus port for a resilient Redis configuration |  |
| Mesh ingress | 443 | Execution node | Receptor | HTTPS | If using mesh ingress, ensure that outbound HTTPS (port 443) is allowed from the execution nodes to the OpenShift route URL. |  |
| Platform gateway | 8443 | Platform gateway | TCP | HTTPS | nginx |  |




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







<span id="idm140401814468096"></span>
**Table 6.2. Red Hat Insights for Red Hat Ansible Automation Platform**

| URL | Required for |
| --- | --- |
|  [https://api.access.redhat.com:443](https://api.access.redhat.com) | General account services, subscriptions |
|  [https://cert-api.access.redhat.com:443](https://cert-api.access.redhat.com) | Insights data upload |
|  [https://cert.console.redhat.com:443](https://cert.console.redhat.com) | Inventory upload and Cloud Connector connection |
|  [https://console.redhat.com:443](https://console.redhat.com) | Access to Insights dashboard |





<span id="idm140401811872656"></span>
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





<span id="idm140401810863872"></span>
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



