# Network ports and protocols
## Network ports and protocols diagram

The following architectural diagrams are example of a fully deployed Ansible Automation Platform with all possible components.

Note:

In some of the following use cases, hop nodes are used instead of a direct link from an execution node. Hop nodes are an option for connecting control and execution nodes. Hop nodes use minimal CPU and memory, so vertically scaling hop nodes does not impact system capacity.

**Container-based installations**

Note:

The following diagram shows connections between Ansible Automation Platform components. All external client traffic is routed through platform gateway. Direct external access to automation hub, Event-Driven Ansible, automation controller, and metrics service is not available. Metrics service is a required component in Ansible Automation Platform 2.7.

![Interaction of Ansible Automation Platform components on the network with information about the ports and protocols that are used in a container-based installation.](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/cont-network-ports-and-protocols-2-7.png)

