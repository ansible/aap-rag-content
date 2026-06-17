+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/plan-assembly_network_ports_protocols"
title = "Network ports and protocols - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/plan-assembly_overview_tested_deployment_models/", "Choose a deployment method and topology"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/plan-assembly_network_ports_protocols/aem-page/plan-assembly_network_ports_protocols.html"
last_crumb = "Network ports and protocols"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Network ports and protocols"
oversized = "false"
page_slug = "plan-assembly_network_ports_protocols"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/plan-assembly_network_ports_protocols"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/plan-assembly_network_ports_protocols/toc/toc.json"
type = "aem-page"
+++

# Network ports and protocols

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server in order for it to work.

## Network ports and protocols diagram

The following architectural diagrams are example of a fully deployed Ansible Automation Platform with all possible components.

 Note:

In some of the following use cases, hop nodes are used instead of a direct link from an execution node. Hop nodes are an option for connecting control and execution nodes. Hop nodes use minimal CPU and memory, so vertically scaling hop nodes does not impact system capacity.

 **RPM based installations**

 Note:

The following diagram shows client initiated connections between Ansible Automation Platform components. Direct connections shown in the diagram between the Client and automation hub, Event-Driven Ansible, and automation controller only apply when systems are upgraded from Red Hat Ansible Automation Platform 2.4 to Red Hat Ansible Automation Platform 2.6. This provides backward compatibility.

 **Ansible Automation Platform Client initiated network ports and protocols**


![Interaction of Ansible Automation Platform components on the network with information about the ports and protocols that are used.](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/network-client-initiated.png)  


 Note:

The following diagram shows internally initiated connections between Ansible Automation Platform components for new installs Red Hat Ansible Automation Platform 2.6.

 **Ansible Automation Platform Internally initiated network ports and protocols**


![Interaction of Ansible Automation Platform components on the network with information about the ports and protocols that are used.](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/network-internally-initiated.png)  


 **Container-based installations**

 Note:

The following diagram shows connections between Ansible Automation Platform components for a container-based installation Red Hat Ansible Automation Platform 2.6.

 **Containerized Ansible Automation Platform network ports and protocols**


![Interaction of Ansible Automation Platform components on the network with information about the ports and protocols that are used in a container-based installation.](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/container-initiation-diagram.png)  

## Network ports and protocols table

The following table indicates the destination port and the direction of network traffic:

 Note:

- The following default destination ports and installer inventory listed are configurable. If you choose to configure them to suit your environment, you might experience a change in behavior.
- Port 443 is the industry standard for HTTPS. Port 80 is not mandatory, but is included for environments that might want to have an unsecure connection.


 **For RPM-based installations**

- Use Port 80 if you set any of `nginx_disable_https`, `automationhub_disable_https` or `automationedacontroller_disable_https` to `true`. See [Security-relevant variables in the installation inventory](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_installation#ref-security-variables-install-inventory "Customize the installation inventory file to define your Ansible Automation Platform architecture and change the initial configuration of its components.")


 **For container-based installations**

- Use Port 80 if you set any of `controller_nginx_disable_https`, `hub_nginx_disable_https` or `eda_nginx_disable_https` to `true`. See [Security-relevant variables in the installation inventory](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_installation#ref-security-variables-install-inventory "Customize the installation inventory file to define your Ansible Automation Platform architecture and change the initial configuration of its components.")

The following table shows container-based installation ports and inventory variables in **bold** text.

 **Network ports and protocols**

| Destination                                 | Port                                 | Source                                 | Protocol     | Service        | Required for                                                                                                                                                                                                                                                                                                                                                                            | Installer Inventory Variable                                                         |
| ------------------------------------------- | ------------------------------------ | -------------------------------------- | ------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| <br>Automation hub                          | <br>22                               | <br>Installer node                     | <br>TCP      | <br>SSH        | <br>Management (Install, Configure, Upgrade)                                                                                                                                                                                                                                                                                                                                            | <br>ansible\_port                                                                    |
| <br>Automation hub                          | <br>80/443                           | <br>Installer node                     | <br>TCP      | <br>HTTP/HTTPS | <br>Enables installer node to push the execution environment image to automation hub when using the bundle installer.                                                                                                                                                                                                                                                                   | <br>ansible\_port                                                                    |
| <br>Automation hub                          | <br>80/443                           | <br>Automation controller              | <br>TCP      | <br>HTTP/HTTPS | <br>Pull collections                                                                                                                                                                                                                                                                                                                                                                    |                                                                                      |
| <br>Automation hub                          | <br>80/443                           | <br>Event-Driven Ansible node          | <br>TCP      | <br>HTTP/HTTPS | <br>Pull container decision environments                                                                                                                                                                                                                                                                                                                                                |                                                                                      |
| <br>Automation hub                          | <br>80/443                           | <br>Execution node                     | <br>TCP      | <br>HTTP/HTTPS | <br>Allows execution nodes to pull the execution environment image from automation hub                                                                                                                                                                                                                                                                                                  |                                                                                      |
| <br>Automation hub                          | <br>80/443                           | <br>Gateway load balancer/Ingress node | <br>TCP      | <br>HTTP/HTTPS | <br>Accessing the component directly from platform gateway                                                                                                                                                                                                                                                                                                                              | <br>automationgateway\_main\_url<br> **gateway\_main\_url**                          |
| <br>Automation hub                          | <br>443<br>**8444**                  | <br>Platform gateway                   | <br>TCP      | <br>HTTPS      | <br>Link between platform gateway and Ansible Automation Platform components                                                                                                                                                                                                                                                                                                            |                                                                                      |
| <br>Automation hub                          | <br>6379                             | <br>Event-Driven Ansible               | <br>TCP      | <br>Redis      | <br>Event processing                                                                                                                                                                                                                                                                                                                                                                    |                                                                                      |
| <br>Automation controller                   | <br>22                               | <br>Installer node                     | <br>TCP      | <br>SSH        | <br>Management (Install, Configure, Upgrade)                                                                                                                                                                                                                                                                                                                                            | <br>ansible\_port                                                                    |
| <br>Automation controller                   | <br>80/443                           | <br>Event-Driven Ansible               | <br>TCP      | <br>HTTP/HTTPS | <br>Launch automation controller jobs                                                                                                                                                                                                                                                                                                                                                   |                                                                                      |
| <br>Automation controller                   | <br>80/443<br>**80/8443**<br>80/8443 | <br>Platform gateway                   | <br>TCP      | <br>HTTP/HTTPS | <br>Link between platform gateway and Ansible Automation Platform components                                                                                                                                                                                                                                                                                                            |                                                                                      |
| <br>Automation controller                   | <br>80/443                           | <br>Gateway load balancer/Ingress node | <br>TCP      | <br>HTTP/HTTPS | <br>Accessing the component directly from Platform gateway                                                                                                                                                                                                                                                                                                                              |                                                                                      |
| <br>Automation controller                   | <br>27199                            | <br>Execution node                     | <br>TCP      | <br>Receptor   | <br>Used for Mesh peering and communication. See [Defining automation mesh node types](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_planning_mesh#defining-node-types "The examples in this section demonstrate how to set the node type for the hosts in your inventory file.").                                                                   | <br>receptor\_listener\_port<br>peers<br> **receptor\_port**<br> **receptor\_peers** |
| <br>Event-Driven Ansible                    | <br>22                               | <br>Installer node                     | <br>TCP      | <br>SSH        | <br>Management (Install, Configure, Upgrade)                                                                                                                                                                                                                                                                                                                                            | <br>ansible\_port                                                                    |
| <br>Event-Driven Ansible                    | <br>80/443<br>**80/8445**            | <br>Platform gateway                   | <br>TCP      | <br>HTTP/HTTPS | <br>Link between platform gateway and Ansible Automation Platform components                                                                                                                                                                                                                                                                                                            |                                                                                      |
| <br>Event-Driven Ansible                    | <br>80/443                           | <br>Gateway load balancer/Ingress node | <br>TCP      | <br>HTTP/HTTPS | <br>Accessing the component directly from platform gateway                                                                                                                                                                                                                                                                                                                              | <br>automationgateway\_main\_url<br> **gateway\_main\_url**                          |
| <br>Event-Driven Ansible                    | <br>80/443<br>**8443**               | <br>Platform gateway                   | <br>TCP      | <br>HTTPS      | <br>Receiving event stream traffic                                                                                                                                                                                                                                                                                                                                                      |                                                                                      |
| <br>Execution node                          | <br>22                               | <br>Installer node                     | <br>TCP      | <br>SSH        | <br>Management (Install, Configure, Upgrade)                                                                                                                                                                                                                                                                                                                                            | <br>ansible\_port                                                                    |
| <br>Execution node                          | <br>443<br>**8443**                  | <br>Gateway load balancer/Ingress node | <br>TCP      | <br>HTTPS      |                                                                                                                                                                                                                                                                                                                                                                                         | <br>automationgateway\_main\_url<br> **gateway\_main\_url**                          |
| <br>Execution node                          | <br>27199                            | <br>Automation controller              | <br>TCP      | <br>Receptor   | <br>Used for Mesh peering and communication. See [Defining automation mesh node types](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_planning_mesh#defining-node-types "The examples in this section demonstrate how to set the node type for the hosts in your inventory file.").                                                                   | <br>receptor\_listener\_port<br>peers<br> **receptor\_port**<br> **receptor\_peers** |
| <br>Execution node                          | <br>27199                            | <br>OpenShift Container Platform       | <br>TCP      | <br>Receptor   |                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                      |
| <br>Hop node                                | <br>22                               | <br>Installer node                     | <br>TCP      | <br>SSH        | <br>Management (Install, Configure, Upgrade)                                                                                                                                                                                                                                                                                                                                            | <br>ansible\_port                                                                    |
| <br>Hop node                                | <br>27199                            | <br>Automation controller              | <br>TCP      | <br>Receptor   | <br>ENABLE connections from hop nodes to Receptor port if relayed through hop nodes. See [Defining automation mesh node types](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_planning_mesh#defining-node-types "The examples in this section demonstrate how to set the node type for the hosts in your inventory file.").                           | <br>receptor\_listener\_port<br>peers<br> **receptor\_port**<br> **receptor\_peers** |
| <br>Hop node                                | <br>27199                            | <br>Execution node                     | <br>TCP      | <br>Receptor   | <br>Used for Mesh peering and communication. See [Defining automation mesh node types](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_planning_mesh#defining-node-types "The examples in this section demonstrate how to set the node type for the hosts in your inventory file.").                                                                   | <br>receptor\_listener\_port<br>peers<br> **receptor\_port**<br> **receptor\_peers** |
| <br>Hybrid node                             | <br>22                               | <br>Installer node                     | <br>TCP      | <br>SSH        | <br>Management (Install, Configure, Upgrade)                                                                                                                                                                                                                                                                                                                                            | <br> `ansible_port`                                                                  |
| <br>Hybrid node                             | <br>27199                            | <br>Automation controller              | <br>TCP      | <br>Receptor   | <br>ENABLE connections from automation controller to Receptor port if relayed through non-hop connected nodes. See [Defining automation mesh node types](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_planning_mesh#defining-node-types "The examples in this section demonstrate how to set the node type for the hosts in your inventory file."). | <br>receptor\_listener\_port<br>peers<br> **receptor\_port**<br> **receptor\_peers** |
| <br>PostgreSQL database                     | <br>22                               | <br>Installer node                     | <br>TCP      | <br>SSH        | <br>Management (Install, Configure, Upgrade)                                                                                                                                                                                                                                                                                                                                            | <br> `pg_port`                                                                       |
| <br>PostgreSQL database                     | <br>5432                             | <br>Automation controller              | <br>TCP      | <br>PostgreSQL | <br>Required only if the internal database is used with another component. Otherwise, this port should not be open.                                                                                                                                                                                                                                                                     | <br>automationcontroller\_pg\_port<br> **controller\_pg\_port**                      |
| <br>PostgreSQL database                     | <br>5432                             | <br>Event-Driven Ansible               | <br>TCP      | <br>PostgreSQL | <br>Required only if the internal database is used with another component. Otherwise, this port should not be open.                                                                                                                                                                                                                                                                     | <br>automationedacontroller\_pg\_port<br> **eda\_pg\_port**                          |
| <br>PostgreSQL                              | <br>5432                             | <br>Automation hub                     | <br>TCP      | <br>PostgreSQL | <br>Required only if the internal database is used with another component. Otherwise, this port should not be open                                                                                                                                                                                                                                                                      | <br>automationhub\_pg\_port<br> **hub\_pg\_port**                                    |
| <br>OpenShift Container Platform (RPM only) | <br>6443                             | <br>Automation controller              | <br>TCP      | <br>HTTP/HTTPS | <br>Only required when using container groups to run jobs.                                                                                                                                                                                                                                                                                                                              | <br>Hostname of OpenShift API server                                                 |
| <br>Redis node                              | <br>6379                             | <br>Automation controller              | <br>TCP      | <br>Redis      | <br>Job launching                                                                                                                                                                                                                                                                                                                                                                       |                                                                                      |
| <br>Redis node                              | <br>6379                             | <br>Event-Driven Ansible               | <br>TCP      | <br>Redis      | <br>Job launching                                                                                                                                                                                                                                                                                                                                                                       |                                                                                      |
| <br>Redis node                              | <br>6379                             | <br>Automation hub                     | <br>TCP      | <br>Redis      | <br>Job launching                                                                                                                                                                                                                                                                                                                                                                       |                                                                                      |
| <br>Redis node                              | <br>6379                             | <br>Platform gateway                   | <br>TCP      | <br>Redis      | <br>Data storage and retrieval                                                                                                                                                                                                                                                                                                                                                          |                                                                                      |
| <br>Redis node                              | <br>16379                            | <br>Redis node                         | <br>TCP      | <br>Redis      | <br>Redis cluster bus port for a resilient Redis configuration                                                                                                                                                                                                                                                                                                                          |                                                                                      |
| <br>Mesh ingress                            | <br>443                              | <br>Execution node                     | <br>Receptor | <br>HTTPS      | <br>If using mesh ingress, ensure that outbound HTTPS (port 443) is allowed from the execution nodes to the OpenShift route URL.                                                                                                                                                                                                                                                        |                                                                                      |
| <br>Platform gateway                        | <br>80/443<br>**80/8444**            | <br>Automation hub                     | <br>TCP      | <br>HTTPS      | <br>Link between platform gateway and Ansible Automation Platform components                                                                                                                                                                                                                                                                                                            |                                                                                      |
| <br>Platform gateway                        | <br>8443                             | <br>Platform gateway                   | <br>TCP      | <br>HTTPS      | <br>nginx                                                                                                                                                                                                                                                                                                                                                                               |                                                                                      |


 Note:

- Hybrid nodes act as a combination of control and execution nodes, and therefore Hybrid nodes share the connections of both.
- If `receptor_listener_port` is defined, the machine also requires an available open port on which to establish inbound TCP connections, for example, 27199.

## Network ports and protocols firewalls

The following tables provide information about configuring firewalls for Red Hat Ansible Automation Platform components.

 **Red Hat Insights for Red Hat Ansible Automation Platform**

| URL                                                                               | Required for                                        |
| --------------------------------------------------------------------------------- | --------------------------------------------------- |
| <br> [https://api.access.redhat.com:443](https://api.access.redhat.com)           | <br>General account services, subscriptions         |
| <br> [https://cert-api.access.redhat.com:443](https://cert-api.access.redhat.com) | <br>Insights data upload                            |
| <br> [https://cert.console.redhat.com:443](https://cert.console.redhat.com)       | <br>Inventory upload and Cloud Connector connection |
| <br> [https://console.redhat.com:443](https://console.redhat.com)                 | <br>Access to Insights dashboard                    |


 **Automation Hub**

| URL                                                                                                    | Required for                                                                  |
| ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| <br> [https://console.redhat.com:443](https://console.redhat.com)                                      | <br>General account services, subscriptions                                   |
| <br> [https://catalog.redhat.com:443](https://catalog.redhat.com)                                      | <br>Indexing execution environments                                           |
| <br> [https://sso.redhat.com:443](https://sso.redhat.com)                                              | <br>TCP                                                                       |
| <br>https://automation-hub-prd.s3.amazonaws.com, https://automation-hub-prd.s3.us-east-2.amazonaws.com | <br>Firewall access                                                           |
| <br> [https://galaxy.ansible.com:443](https://galaxy.ansible.com)                                      | <br>Ansible Community curated Ansible content                                 |
| <br>https://ansible-galaxy-ng.s3.dualstack.us-east-1.amazonaws.com                                     | <br>Dual Stack IPv6 endpoint for Community curated Ansible content repository |
| <br> [https://registry.redhat.io:443](https://registry.redhat.io)                                      | <br>Access to container images provided by Red Hat and partners               |
| <br> [https://cert.console.redhat.com:443](https://cert.console.redhat.com)                            | <br>Red Hat and partner curated Ansible Collections                           |


 **Execution Environments (EE)**

| URL                                                               | Required for                                                    |
| ----------------------------------------------------------------- | --------------------------------------------------------------- |
| <br> [https://registry.redhat.io:443](https://registry.redhat.io) | <br>Access to container images provided by Red Hat and partners |
| <br> `cdn.quay.io:443`                                            | <br>Access to container images provided by Red Hat and partners |
| <br> `cdn01.quay.io:443`                                          | <br>Access to container images provided by Red Hat and partners |
| <br> `cdn02.quay.io:443`                                          | <br>Access to container images provided by Red Hat and partners |
| <br> `cdn03.quay.io:443`                                          | <br>Access to container images provided by Red Hat and partners |


 Important:

As of **April 1st, 2025**, `quay.io` is adding three additional endpoints. As a result, customers must adjust allow/block lists within their firewall systems lists to include the following endpoints:

-  `cdn04.quay.io`
-  `cdn05.quay.io`
-  `cdn06.quay.io`


To avoid problems pulling container images, customers must allow outbound TCP connections (ports 80 and 443) to the following hostnames:

-  `cdn.quay.io`
-  `cdn01.quay.io`
-  `cdn02.quay.io`
-  `cdn03.quay.io`
-  `cdn04.quay.io`
-  `cdn05.quay.io`
-  `cdn06.quay.io`


This change should be made to any firewall configuration that specifically enables outbound connections to `registry.redhat.io` or `registry.access.redhat.com`.

Use the hostnames instead of IP addresses when configuring firewall rules.

After making this change, you can continue to pull images from `registry.redhat.io` or `registry.access.redhat.com`. You do not require a `quay.io` login, or need to interact with the `quay.io` registry directly in any way to continue pulling Red Hat container images.

For more information, see [Firewall changes for container image pulls 2024/2025](https://access.redhat.com/articles/7084334).

## Automation mesh node requirements

Automation mesh is an overlay network that distributes automation work across large and distributed collections of workers through peer-to-peer node connections. Included are the tested system configurations and network port requirements for mesh nodes.

### Tested system configurations

Each automation mesh VM has been tested with these requirements: 16 GB RAM, 4 CPUs, 60 GB local disk, and 3000 IOPS.

### Network ports

Automation mesh uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 1. Network ports and protocols*

| Port number | Protocol       | Service      | Source                                   | Destination                                   |
| ----------- | -------------- | ------------ | ---------------------------------------- | --------------------------------------------- |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor | <br>Execution node                       | <br>OpenShift Container Platform mesh ingress |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor | <br>Hop node                             | <br>OpenShift Container Platform mesh ingress |
| <br>27199   | <br>TCP        | <br>Receptor | <br>OpenShift Container Platform cluster | <br>Execution node                            |
| <br>27199   | <br>TCP        | <br>Receptor | <br>OpenShift Container Platform cluster | <br>Hop node                                  |
