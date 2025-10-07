# Chapter 6. Clustering




Clustering is sharing load between hosts. Each instance must be able to act as an entry point for UI and API access. This must enable the automation controller administrators to use load balancers in front of as many instances as they want and keep good data visibility.

Note
Load balancing is optional, and it is entirely possible to have ingress on one or all instances as needed.



Each instance must be able to join the automation controller cluster and expand its ability to run jobs. This is a simple system where jobs can run anywhere rather than be directed on where to run. Also, you can group clustered instances into different pools or queues, called [Instance groups](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/controller-instance-groups) as described in _Using automation execution_ .

Ansible Automation Platform supports container-based clusters by using Kubernetes, meaning you can install new automation controller instances on this platform without any variation or diversion in functionality. You can create instance groups to point to a Kubernetes container. For more information, see the [Instance and container groups](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/controller-instance-and-container-groups) section in _Using automation execution_ .

**Supported operating systems**

The following operating systems are supported for establishing a clustered environment:

- Red Hat Enterprise Linux 8 or later


Note
Isolated instances are not supported in conjunction with running automation controller in OpenShift.



