# Container enterprise topology
## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*
![Container enterprise topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/cont-b-env-a-2_7.png)

Red Hat tests each VM with these requirements:

*Table 1. Virtual machine requirements*

| Requirement | Minimum requirement                                                                                                                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RAM         | 16 GB                                                                                                                                                                                                    |
| CPUs        | 4                                                                                                                                                                                                        |
| Local disk  | Total available disk space: 60 GBInstallation directory: 15 GB (if on a dedicated partition)`/var/tmp` for online installations: 1 GB`/var/tmp` for offline or bundled installations: 3 GBTemporary directory (defaults to `/tmp`) for offline or bundled installations: 10 GB |
| Disk IOPS   | 3000                                                                                                                                                                                                     |

Note:

Hop nodes do not have a minimum RAM requirement. They route traffic through the automation mesh, and network latency is a more important factor than RAM or CPU.

*Table 2. Infrastructure topology components*

| VM count | Purpose                                                                 | Example VM group names |
| -------- | ----------------------------------------------------------------------- | ---------------------- |
| 2        | Platform gateway with colocated Redis                                   | `automationgateway`    |
| 2        | Automation controller                                                   | `automationcontroller` |
| 1        | Metrics service                                                         | `automationmetrics`    |
| 2        | Private automation hub with colocated Redis                             | `automationhub`        |
| 2        | Event-Driven Ansible with colocated Redis                               | `automationeda`        |
| 1        | Automation mesh hop node                                                | `execution_nodes`      |
| 2        | Automation mesh execution node                                          | `execution_nodes`      |
| 1        | Externally managed database service                                     | N/A                    |
| 1        | HAProxy load balancer in front of platform gateway (externally managed) | N/A                    |

Note:

- 6 VMs are required for a Redis high availability (HA) compatible deployment. When installing Ansible Automation Platform with the containerized installer, Redis can be colocated on any Ansible Automation Platform component VMs of your choice except for execution nodes or the PostgreSQL database. They might also be assigned VMs specifically for Redis use.
- External Redis is not supported for containerized Ansible Automation Platform.

