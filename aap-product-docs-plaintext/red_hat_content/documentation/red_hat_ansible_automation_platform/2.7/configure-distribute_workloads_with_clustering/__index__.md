# Distribute workloads with clustering

Clustering is sharing load between hosts. Each instance must be able to act as an entry point for UI and API access.

Note:

Administrators can use load balancers in front of as many instances as they want and keep good data visibility. However, load balancing is optional, and it is possible to have ingress on one or all instances as needed.

Each instance must be able to join the automation controller cluster and to expand its ability to run jobs. This is a simple system where jobs can run anywhere rather than be directed on where to run. Also, you can group clustered instances into different pools or queues, called instance groups.

Ansible Automation Platform supports container-based clusters by using Kubernetes, meaning you can install new automation controller instances on this platform without any variation or diversion in functionality. You can create instance groups to point to a Kubernetes container.

The following operating systems are supported for establishing a clustered environment:

Supported operating systems

- Red Hat Enterprise Linux 8 or later
