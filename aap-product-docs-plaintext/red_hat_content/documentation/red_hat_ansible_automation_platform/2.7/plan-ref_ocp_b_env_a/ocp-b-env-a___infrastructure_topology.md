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

| Count   | Component                                                          |
| ------- | ------------------------------------------------------------------ |
| <br>1   | <br>Automation controller web pod                                  |
| <br>1   | <br>Automation controller task pod                                 |
| <br>1   | <br>Automation hub web pod                                         |
| <br>1   | <br>Automation hub API pod                                         |
| <br>2   | <br>Automation hub content pod                                     |
| <br>2   | <br>Automation hub worker pod                                      |
| <br>1   | <br>Automation hub Redis pod                                       |
| <br>1   | <br>Event-Driven Ansible API pod                                   |
| <br>2   | <br>Event-Driven Ansible activation worker pod                     |
| <br>2   | <br>Event-Driven Ansible default worker pod                        |
| <br>2   | <br>Event-Driven Ansible event stream pod                          |
| <br>1   | <br>Event-Driven Ansible scheduler pod                             |
| <br>1   | <br>Platform gateway pod                                           |
| <br>1   | <br>Metrics service web pod                                        |
| <br>1   | <br>Metrics service tasks pod                                      |
| <br>1   | <br>Metrics service scheduler pod                                  |
| <br>2   | <br>Mesh ingress pod                                               |
| <br>N/A | <br>Externally managed database service                            |
| <br>N/A | <br>Externally managed Redis                                       |
| <br>N/A | <br>Externally managed object storage service (for automation hub) |

