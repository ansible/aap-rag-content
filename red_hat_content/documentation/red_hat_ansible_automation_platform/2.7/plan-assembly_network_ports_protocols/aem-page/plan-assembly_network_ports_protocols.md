+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-assembly_network_ports_protocols"
template = "docs/aem-title.html"
title = "Network ports and protocols - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-assembly_overview_tested_deployment_models/", "Choose a deployment method and topology"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-assembly_network_ports_protocols/aem-page/plan-assembly_network_ports_protocols.html"
last_crumb = "Network ports and protocols"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Network ports and protocols"
oversized = "false"
page_slug = "plan-assembly_network_ports_protocols"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-assembly_network_ports_protocols"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-assembly_network_ports_protocols/toc/toc.json"
type = "aem-page"
+++

# Network ports and protocols

Red Hat Ansible Automation Platform uses several ports to communicate with its services.
These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server in order for it to work.

## Network ports and protocols diagram

The following architectural diagrams are example of a fully deployed Ansible Automation Platform with all possible components.

Note:

In some of the following use cases, hop nodes are used instead of a direct link from an execution node. Hop nodes are an option for connecting control and execution nodes. Hop nodes use minimal CPU and memory, so vertically scaling hop nodes does not impact system capacity.

 **Container-based installations**

Note:

The following diagram shows connections between Ansible Automation Platform components. All external client traffic is routed through platform gateway. Direct external access to automation hub, Event-Driven Ansible, automation controller, and metrics service is not available. Metrics service is a required component in Ansible Automation Platform 2.7.

![Interaction of Ansible Automation Platform components on the network with information about the ports aand protocols that are used in a container-based installation](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/Ports-and-network-2.7.png)

## Network ports and protocols table

The following table indicates the destination port and the direction of network traffic:

Note:

- The following default destination ports and installer inventory listed are configurable. If you choose to configure them to suit your environment, you might experience a change in behavior.
- Port 443 is the industry standard for HTTPS. Port 80 is not mandatory, but is included for environments that might want to have an unsecure connection.

- Use Port 80 if you set any of `controller_nginx_disable_https`, `hub_nginx_disable_https` or `eda_nginx_disable_https` to `true`. See [Security-relevant variables in the installation inventory](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_installation#ref-security-variables-install-inventory "Customize the installation inventory file to define your Ansible Automation Platform architecture and change the initial configuration of its components.")

 **For RPM-based installations (deprecated — removed in Ansible Automation Platform 2.7)**

- Use Port 80 if you set any of `nginx_disable_https`, `automationhub_disable_https` or `automationedacontroller_disable_https` to `true`. See [Security-relevant variables in the installation inventory](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_installation#ref-security-variables-install-inventory "Customize the installation inventory file to define your Ansible Automation Platform architecture and change the initial configuration of its components.")

The following table shows container-based installation ports and inventory variables in **bold** text.

 **Network ports and protocols**

| Destination                                          | Port       | Source                             | Protocol | Service                                                                                                                          | Required for                                                                                                                                                                                             | Installer Inventory Variable                                                                                                                 |
| ---------------------------------------------------- | ---------- | ---------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Platform gateway                                     | 80<br>443  | Client/External                    | TCP      | HTTP for port 80 (if `*_nginx_disable_https=true`)<br>HTTP/HTTPS<br>TLS 1.2+ for port 443.                                       | All external user and API traffic. Platform gateway is the sole entry point for Ansible Automation Platform.                                                                                             | gateway\_main\_url                                                                                                                           |
| Automation hub                                       | 22         | Installer node                     | TCP      | SSH                                                                                                                              | Management (Install, Configure, Upgrade)                                                                                                                                                                 | ansible\_port                                                                                                                                |
| Automation hub                                       | 80<br>443  | Installer node                     | TCP      | HTTP<br>HTTPS                                                                                                                    | Enables installer node to push the execution environment image to automation hub when using the bundle installer.                                                                                        | ansible\_port                                                                                                                                |
| Automation hub                                       | 80<br>443  | Automation controller              | TCP      | HTTP<br>HTTPS                                                                                                                    | Pull collections                                                                                                                                                                                         |                                                                                                                                              |
| Automation hub                                       | 80<br>443  | Event-Driven Ansible node          | TCP      | HTTP<br>HTTPS                                                                                                                    | Pull container decision environments                                                                                                                                                                     |                                                                                                                                              |
| Platform gateway                                     | 80<br>443  | Execution node                     | TCP      | HTTP<br>HTTPS                                                                                                                    | Allows execution nodes to pull the execution environment image from automation hub through platform gateway                                                                                              |                                                                                                                                              |
| Automation hub                                       | 8444       | Platform gateway                   | TCP      | HTTPS<br>TLS 1.2+ (encrypted via NGINX)                                                                                          | Link between platform gateway and Ansible Automation Platform components                                                                                                                                 |                                                                                                                                              |
| Automation hub                                       | 6379       | Event-Driven Ansible               | TCP      | Redis                                                                                                                            | Event processing                                                                                                                                                                                         |                                                                                                                                              |
| Automation controller                                | 22         | Installer node                     | TCP      | SSH                                                                                                                              | Management (Install, Configure, Upgrade)                                                                                                                                                                 | ansible\_port                                                                                                                                |
| Automation controller                                | 80<br>443  | Event-Driven Ansible               | TCP      | HTTP<br>HTTPS                                                                                                                    | Launch automation controller jobs                                                                                                                                                                        |                                                                                                                                              |
| Automation controller                                | 80<br>8443 | Platform gateway                   | TCP      | HTTP<br>Unencrypted if `controller_nginx_disable_https=true` for Port 80<br>HTTPS<br>TLS 1.2+ (encrypted via NGINX for Port 8443 | Link between platform gateway and Ansible Automation Platform components                                                                                                                                 |                                                                                                                                              |
| Automation controller                                | 27199      | Execution node                     | TCP      | Receptor                                                                                                                         | Used for Mesh peering and communication. See [Defining automation mesh node types](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_planning_mesh#defining-node-types "The examples in this section demonstrate how to set the node type for the hosts in your inventory file."). | receptor\_port<br>receptor\_peers                                                                                                            |
| Event-Driven Ansible                                 | 22         | Installer node                     | TCP      | SSH                                                                                                                              | Management (Install, Configure, Upgrade)                                                                                                                                                                 | ansible\_port                                                                                                                                |
| Event-Driven Ansible                                 | 80<br>8445 | Platform gateway                   | TCP      | HTTP<br>HTTPS TLS 1.2+ (encrypted via NGINX)                                                                                     | Secure communication for EDA service                                                                                                                                                                     |                                                                                                                                              |
| Event-Driven Ansible                                 | 8443       | Platform gateway                   | TCP      | HTTPS (TLS 1.2+ or mTLS 1.2+)                                                                                                    | Receiving event stream traffic. (`mTLS when eda_event_stream_mtls=true`)                                                                                                                                 |                                                                                                                                              |
| Execution node                                       | 22         | Installer node                     | TCP      | SSH                                                                                                                              | Management (Install, Configure, Upgrade)                                                                                                                                                                 | ansible\_port                                                                                                                                |
| Execution node                                       | 8443       | Gateway load balancer/Ingress node | TCP      | HTTPS                                                                                                                            |                                                                                                                                                                                                          | gateway\_main\_url                                                                                                                           |
| Execution node                                       | 27199      | Automation controller              | TCP      | Receptor                                                                                                                         | Used for Mesh peering and communication. See [Defining automation mesh node types](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_planning_mesh#defining-node-types "The examples in this section demonstrate how to set the node type for the hosts in your inventory file."). | receptor\_port<br>receptor\_peers                                                                                                            |
| Execution node                                       | 27199      | OpenShift Container Platform       | TCP      | Receptor                                                                                                                         |                                                                                                                                                                                                          |                                                                                                                                              |
| Hop node                                             | 22         | Installer node                     | TCP      | SSH                                                                                                                              | Management (Install, Configure, Upgrade)                                                                                                                                                                 | ansible\_port                                                                                                                                |
| Hop node                                             | 27199      | Automation controller              | TCP      | Receptor                                                                                                                         | ENABLE connections from hop nodes to Receptor port if relayed through hop nodes. See [Defining automation mesh node types](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_planning_mesh#defining-node-types "The examples in this section demonstrate how to set the node type for the hosts in your inventory file."). | receptor\_port<br>receptor\_peers                                                                                                            |
| Hop node                                             | 27199      | Execution node                     | TCP      | Receptor                                                                                                                         | Used for Mesh peering and communication. See [Defining automation mesh node types](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_planning_mesh#defining-node-types "The examples in this section demonstrate how to set the node type for the hosts in your inventory file."). | receptor\_port<br>receptor\_peers                                                                                                            |
| Hybrid node                                          | 22         | Installer node                     | TCP      | SSH                                                                                                                              | Management (Install, Configure, Upgrade)                                                                                                                                                                 | `ansible_port`                                                                                                                               |
| Hybrid node                                          | 27199      | Automation controller              | TCP      | Receptor                                                                                                                         | ENABLE connections from automation controller to Receptor port if relayed through non-hop connected nodes. See [Defining automation mesh node types](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_planning_mesh#defining-node-types "The examples in this section demonstrate how to set the node type for the hosts in your inventory file."). | receptor\_port<br>receptor\_peers                                                                                                            |
| PostgreSQL database                                  | 22         | Installer node                     | TCP      | SSH                                                                                                                              | Management (Install, Configure, Upgrade)                                                                                                                                                                 | `pg_port`                                                                                                                                    |
| PostgreSQL database                                  | 5432       | Automation controller              | TCP      | PostgreSQL                                                                                                                       | Required only if the installer-managed database is used with another component. Otherwise, this port should not be open.                                                                                 | controller\_pg\_port                                                                                                                         |
| PostgreSQL database                                  | 5432       | Event-Driven Ansible               | TCP      | PostgreSQL                                                                                                                       | Required only if the installer-managed database is used with another component. Otherwise, this port should not be open.                                                                                 | eda\_pg\_port                                                                                                                                |
| PostgreSQL                                           | 5432       | Automation hub                     | TCP      | PostgreSQL                                                                                                                       | Required only if the installer-managed database is used with another component. Otherwise, this port should not be open.                                                                                 | hub\_pg\_port                                                                                                                                |
| PostgreSQL database                                  | 5432       | Metrics service                    | TCP      | PostgreSQL                                                                                                                       | Required only if the installer-managed database is used with another component. Otherwise, this port should not be open.                                                                                 | automationmetrics\_pg\_port<br>metrics\_pg\_port                                                                                             |
| PostgreSQL database (read-only)                      | 5432       | Metrics service                    | TCP      | PostgreSQL                                                                                                                       | Read-only connection to automation controller database. Required for metrics service to correlate automation activity with resource metrics. Uses `ms_awx_readonly` user.                                | automationcontroller\_pg\_host<br>controller\_pg\_host<br>automationcontroller\_pg\_username (ms\_awx\_readonly)<br>controller\_pg\_username |
| OpenShift Container Platform (RPM only — deprecated) | 6443       | Automation controller              | TCP      | HTTP/HTTPS                                                                                                                       | Only required when using container groups to run jobs.                                                                                                                                                   | Hostname of OpenShift API server                                                                                                             |
| Redis node                                           | 6379       | Automation controller              | TCP      | Redis                                                                                                                            | Job launching                                                                                                                                                                                            |                                                                                                                                              |
| Redis node                                           | 6379       | Event-Driven Ansible               | TCP      | Redis                                                                                                                            | Job launching                                                                                                                                                                                            |                                                                                                                                              |
| Redis node                                           | 6379       | Automation hub                     | TCP      | Redis                                                                                                                            | Job launching                                                                                                                                                                                            |                                                                                                                                              |
| Redis node                                           | 6379       | Platform gateway                   | TCP      | Redis (TLS/mTLS optional (via separate Redis configuration)                                                                      | Data storage and retrieval                                                                                                                                                                               |                                                                                                                                              |
| Redis node                                           | 16379      | Redis node                         | TCP      | Redis                                                                                                                            | Redis cluster bus port for a resilient Redis configuration                                                                                                                                               |                                                                                                                                              |
| Mesh ingress                                         | 443        | Execution node                     | Receptor | HTTPS                                                                                                                            | If using mesh ingress, ensure that outbound HTTPS (port 443) is allowed from the execution nodes to the OpenShift route URL.                                                                             |                                                                                                                                              |
| Platform gateway                                     | 80<br>8444 | Automation hub                     | TCP      | HTTP<br>HTTPS TLS 1.2+ (encrypted via NGINX)                                                                                     | Secure communication for hub API and content distribution                                                                                                                                                |                                                                                                                                              |
| Platform gateway                                     | 8443       | Platform gateway                   | TCP      | HTTPS                                                                                                                            | Internal gateway-to-gateway HA communication (TLS 1.2+ encryption)                                                                                                                                       |                                                                                                                                              |
| Ansible MCP server                                   | 443        | Client/External                    | TCP      | HTTPS                                                                                                                            | Model Context Protocol client connections and API traffic.                                                                                                                                               |                                                                                                                                              |
| Gateway Load balancer                                | 443        | Ansible MCP server                 | TCP      | HTTPS                                                                                                                            | MCP server to Ansible Automation Platform communication                                                                                                                                                  |                                                                                                                                              |

Note:

- Hybrid nodes act as a combination of control and execution nodes, and therefore Hybrid nodes share the connections of both.
- If `receptor_port` is defined, the machine also requires an available open port on which to establish inbound TCP connections, for example, 27199.

## Network ports and protocols firewalls

The following tables provide information about configuring firewalls for Red Hat Ansible Automation Platform components.

 **Red Hat Insights for Red Hat Ansible Automation Platform**

| URL                                                                          | Required for                                    |
| ---------------------------------------------------------------------------- | ----------------------------------------------- |
| [https://api.access.redhat.com:443](https://api.access.redhat.com)           | General account services, subscriptions         |
| [https://cert-api.access.redhat.com:443](https://cert-api.access.redhat.com) | Insights data upload                            |
| [https://cert.console.redhat.com:443](https://cert.console.redhat.com)       | Inventory upload and Cloud Connector connection |
| [https://console.redhat.com:443](https://console.redhat.com)                 | Access to Insights dashboard                    |

 **Automation Hub**

| URL                                                            | Required for                                                              |
| -------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [https://console.redhat.com:443](https://console.redhat.com)   | General account services, subscriptions                                   |
| [https://sso.redhat.com:443](https://sso.redhat.com)           | TCP                                                                       |
| https://automation-hub-prd.s3.us-east-2.amazonaws.com          | Firewall access                                                           |
| [https://galaxy.ansible.com:443](https://galaxy.ansible.com)   | Ansible Community curated Ansible content                                 |
| https://ansible-galaxy-ng.s3.dualstack.us-east-1.amazonaws.com | Dual Stack IPv6 endpoint for Community curated Ansible content repository |

 **Execution Environments (EE)**

| URL                                                          | Required for                                                |
| ------------------------------------------------------------ | ----------------------------------------------------------- |
| [https://registry.redhat.io:443](https://registry.redhat.io) | Access to container images provided by Red Hat and partners |
| `cdn.quay.io:443`                                            | Access to container images provided by Red Hat and partners |
| `cdn01.quay.io:443`                                          | Access to container images provided by Red Hat and partners |
| `cdn02.quay.io:443`                                          | Access to container images provided by Red Hat and partners |
| `cdn03.quay.io:443`                                          | Access to container images provided by Red Hat and partners |

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

| Port number | Protocol   | Service  | Source                               | Destination                               |
| ----------- | ---------- | -------- | ------------------------------------ | ----------------------------------------- |
| 80/443      | HTTP/HTTPS | Receptor | Execution node                       | OpenShift Container Platform mesh ingress |
| 80/443      | HTTP/HTTPS | Receptor | Hop node                             | OpenShift Container Platform mesh ingress |
| 27199       | TCP        | Receptor | OpenShift Container Platform cluster | Execution node                            |
| 27199       | TCP        | Receptor | OpenShift Container Platform cluster | Hop node                                  |
