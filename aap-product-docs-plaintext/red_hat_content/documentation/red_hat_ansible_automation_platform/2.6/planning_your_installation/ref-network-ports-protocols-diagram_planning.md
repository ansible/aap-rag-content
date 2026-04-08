# 6. Network ports and protocols
## 6.1. Network ports and protocols diagram




The following architectural diagrams are example of a fully deployed Ansible Automation Platform with all possible components.

Note
In some of the following use cases, hop nodes are used instead of a direct link from an execution node. Hop nodes are an option for connecting control and execution nodes. Hop nodes use minimal CPU and memory, so vertically scaling hop nodes does not impact system capacity.



**RPM based installations**

Note
The following diagram shows client initiated connections between Ansible Automation Platform components. Direct connections shown in the diagram between the Client and automation hub, Event-Driven Ansible, and automation controller only apply when systems are upgraded from Red Hat Ansible Automation Platform 2.4 to Red Hat Ansible Automation Platform 2.6. This provides backward compatibility.



**Ansible Automation Platform Client initiated network ports and protocols**

![Interaction of Ansible Automation Platform components on the network with information about the ports and protocols that are used.](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_installation-en-US/images/3cd1c22300f25811a5d2a90368305ec1/network_client_initiated.png)


Note
The following diagram shows internally initiated connections between Ansible Automation Platform components for new installs Red Hat Ansible Automation Platform 2.6.



**Ansible Automation Platform Internally initiated network ports and protocols**

![Interaction of Ansible Automation Platform components on the network with information about the ports and protocols that are used.](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_installation-en-US/images/0582e6be28242ff238584e9838486de6/network_internally_initiated.png)


**Container-based installations**

Note
The following diagram shows connections between Ansible Automation Platform components for a container-based installation Red Hat Ansible Automation Platform 2.6.



**Containerized Ansible Automation Platform network ports and protocols**

![Interaction of Ansible Automation Platform components on the network with information about the ports and protocols that are used in a container-based installation.](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_installation-en-US/images/c3c5631359abe6b71d13dd43217fcfce/Container-network_internally_initiated.png)


