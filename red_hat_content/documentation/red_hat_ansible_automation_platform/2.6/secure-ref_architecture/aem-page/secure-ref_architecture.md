+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_architecture"
title = "Plan your topology and networking configuration - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_hardening_aap/", "Harden the platform security posture"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-ref_architecture/aem-page/secure-ref_architecture.html"
last_crumb = "Plan your topology and networking configuration"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Plan your topology and networking configuration"
oversized = "false"
page_slug = "secure-ref_architecture"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-ref_architecture"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-ref_architecture/toc/toc.json"
type = "aem-page"
+++

# Plan your topology and networking configuration

Install Ansible Automation Platform using a tested deployment model. Choose between an enterprise reference architecture for high performance and scalability or a growth architecture for resource-constrained environments.

It is possible to install Ansible Automation Platform on different infrastructure reference architectures and with different environment configurations. Red Hat does not fully test architectures outside of published reference architectures. Red Hat recommends using a tested reference architecture for all new deployments and provides commercially reasonable support for deployments that meet minimum requirements.

The following diagram is a tested container enterprise architecture:

*Figure 1. Reference architecture overview*

![Infrastructure reference architecture that Red Hat has tested that customers can use when self-managing Ansible Automation Platform](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/cont-b-env-a.png)

When planning firewall or cloud network security group configurations related to Ansible Automation Platform, see the Network Ports section of your chosen topology in [Installation and deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/plan-ref_installation_deployment_models) to understand what network ports need to be opened on a firewall or security group.

For internet-connected systems, the [Network ports and protocols table](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/plan-assembly_network_ports_protocols#network-ports-protocols_table) defines the outgoing traffic requirements for services that Ansible Automation Platform can be configured to use, such as Red Hat automation hub, Red Hat Lightspeed for Ansible Automation Platform, Ansible Galaxy, the registry.redhat.io container image registry, and so on.

Restrict access to the ports used by the Ansible Automation Platform components to protected networks and clients. The following restrictions are highly recommended:

- Restrict the PostgreSQL database port (5432) on the database servers so that only the other Ansible Automation Platform component servers (automation controller, automation hub, Event-Driven Ansible controller) are permitted access.
- Restrict SSH access to the Ansible Automation Platform servers from the installation host and other trusted systems used for maintenance access to the Ansible Automation Platform servers.
- Restrict HTTPS access to the automation controller, automation hub, and Event-Driven Ansible controller from trusted networks and clients.

## DNS, NTP, and service planning

When installing Ansible Automation Platform, DNS and NTP configurations are crucial for a successful deployment and proper operation.

## DNS

Define a valid Fully Qualified Domain Name (FQDN) for all infrastructure nodes in your installation inventory file. Resolving these to a routable IP address in DNS passes installer checks and helps ensure a successful setup.

## DNS and load balancing

When using a load balancer with Ansible Automation Platform, an additional FQDN is required. For example, `aap.example.com` could be used for the load balancer to direct traffic to each platform gateway component defined in the installation inventory.
