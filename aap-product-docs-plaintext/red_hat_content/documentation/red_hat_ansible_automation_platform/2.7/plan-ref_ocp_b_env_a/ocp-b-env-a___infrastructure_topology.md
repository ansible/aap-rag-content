# Operator enterprise topology
## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*
![Operator enterprise topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ocp-b-env-a-2_7.png)

Important:

While Redis and PostgreSQL can be installed as part of the operator-based installation process, the topology diagram represents a Red Hat supported topology where both Redis and PostgreSQL are external to Ansible Automation Platform.

This infrastructure topology describes an OpenShift Cluster with 3 primary nodes and 2 worker nodes.

Red Hat tests each OpenShift Worker node with these requirements:

*Table 1. OpenShift Worker node requirements*

| Requirement | Minimum requirement |
| ----------- | ------------------- |
| RAM         | 16 GB               |
| CPUs        | 4                   |
| Local disk  | 128 GB              |
| Disk IOPS   | 3000                |

*Table 2. Infrastructure topology components*

| Count | Component                                                      |
| ----- | -------------------------------------------------------------- |
| 1     | Automation controller web pod                                  |
| 1     | Automation controller task pod                                 |
| 1     | Automation hub web pod                                         |
| 1     | Automation hub API pod                                         |
| 2     | Automation hub content pod                                     |
| 2     | Automation hub worker pod                                      |
| 1     | Automation hub Redis pod                                       |
| 1     | Event-Driven Ansible API pod                                   |
| 2     | Event-Driven Ansible activation worker pod                     |
| 2     | Event-Driven Ansible default worker pod                        |
| 2     | Event-Driven Ansible event stream pod                          |
| 1     | Event-Driven Ansible scheduler pod                             |
| 1     | Platform gateway pod                                           |
| 1     | Metrics service web pod                                        |
| 1     | Metrics service tasks pod                                      |
| 1     | Metrics service scheduler pod                                  |
| 2     | Mesh ingress pod                                               |
| N/A   | Externally managed database service                            |
| N/A   | Externally managed Redis                                       |
| N/A   | Externally managed object storage service (for automation hub) |

