# 2. Hardening Ansible Automation Platform
## 2.1. Planning considerations
### 2.1.1. Ansible Automation Platform deployment topologies




Install Ansible Automation Platform 2.6 based on one of the documented tested deployment reference architectures defined in [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models) . Enterprise organizations should use one of the enterprise reference architectures for production deployments to ensure the highest level of uptime, performance, and continued scalability. Organizations or deployments that are resource constrained can use a "growth" reference architecture. Review the [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models) document to determine the reference architecture that best suits your requirements. The reference architecture chosen will include planning information such as an architecture diagram, the number of Red Hat Enterprise Linux servers required, the network ports and protocols used by the deployment, and load balancer information for enterprise architectures.

It is possible to install Ansible Automation Platform on different infrastructure reference architectures and with different environment configurations. Red Hat does not fully test architectures outside of published reference architectures. Red Hat recommends using a tested reference architecture for all new deployments and provides commercially reasonable support for deployments that meet minimum requirements.

The following diagram is a tested container enterprise architecture:


<span id="idm140608424125040"></span>
**Figure 2.1. Reference architecture overview**

![Infrastructure reference architecture that Red Hat has tested that customers can use when self-managing Ansible Automation Platform](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Hardening_and_compliance-en-US/images/704824d330eb8422156d4d7cf034ee52/cont-b-env-a.png)





<span id="con-network-firewall-services_hardening-aap"></span>
When planning firewall or cloud network security group configurations related to Ansible Automation Platform, see the "Network Ports" section of your chosen topology in [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models) to understand what network ports need to be opened on a firewall or security group.


For internet-connected systems, the [Networks and Protocols](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/ref-network-ports-protocols_planning) section of Planning your installation defines the outgoing traffic requirements for services that Ansible Automation Platform can be configured to use, such as Red Hat automation hub, Insights for Ansible Automation Platform, Ansible Galaxy, the registry.redhat.io container image registry, and so on.

Restrict access to the ports used by the Ansible Automation Platform components to protected networks and clients. The following restrictions are highly recommended:

- Restrict the PostgreSQL database port (5432) on the database servers so that only the other Ansible Automation Platform component servers (automation controller, automation hub, Event-Driven Ansible controller) are permitted access.
- Restrict SSH access to the Ansible Automation Platform servers from the [installation host](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/hardening_and_compliance/index#con-install-secure-host_hardening-aap) and other trusted systems used for maintenance access to the Ansible Automation Platform servers.
- Restrict HTTPS access to the automation controller, automation hub, and Event-Driven Ansible controller from trusted networks and clients.


