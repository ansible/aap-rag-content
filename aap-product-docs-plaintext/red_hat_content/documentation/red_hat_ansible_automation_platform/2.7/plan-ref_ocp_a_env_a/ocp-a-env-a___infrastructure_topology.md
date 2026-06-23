# Operator growth topology
## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*
![Operator growth topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ocp-a-env-a-2_7.png)

Important:

While Redis and PostgreSQL can be installed as part of the operator-based installation process, the topology diagram represents a Red Hat supported topology where both Redis and PostgreSQL are external to Ansible Automation Platform.

Red Hat tests a Single Node OpenShift (SNO) cluster with these requirements:

*Table 1. Single Node OpenShift (SNO) cluster requirements*

| Requirement | Minimum requirement |
| ----------- | ------------------- |
| RAM         | 32 GB               |
| CPUs        | 16                  |
| Local disk  | 128 GB              |
| Disk IOPS   | 3000                |

*Table 2. Infrastructure topology components*

| Count | Component                                      |
| ----- | ---------------------------------------------- |
| <br>1 | <br>Automation controller web pod              |
| <br>1 | <br>Automation controller task pod             |
| <br>1 | <br>Automation hub web pod                     |
| <br>1 | <br>Automation hub API pod                     |
| <br>2 | <br>Automation hub content pod                 |
| <br>2 | <br>Automation hub worker pod                  |
| <br>1 | <br>Automation hub Redis pod                   |
| <br>1 | <br>Metrics service web pod                    |
| <br>1 | <br>Metrics service tasks pod                  |
| <br>1 | <br>Metrics service scheduler pod              |
| <br>1 | <br>Event-Driven Ansible API pod               |
| <br>1 | <br>Event-Driven Ansible activation worker pod |
| <br>1 | <br>Event-Driven Ansible default worker pod    |
| <br>1 | <br>Event-Driven Ansible event stream pod      |
| <br>1 | <br>Event-Driven Ansible scheduler pod         |
| <br>1 | <br>Platform gateway pod                       |
| <br>1 | <br>Database pod                               |
| <br>1 | <br>Redis pod                                  |


Note:

Metrics service is deployed automatically when the AnsibleAutomationPlatform Custom Resource (CR) includes metrics configuration. The operator creates a MetricsService CR (named `<aap-name>`-metrics) and manages three pods:

- `<aap-name>`- **metrics-web** - REST API for metrics and dashboard data
- `<aap-name>`- **metrics-tasks** - dispatcherd worker for background data collection
- `<aap-name>`- **metrics-scheduler** - APScheduler for periodic collection tasks (6-hourly schedule)


All database provisioning, secrets management, and routing configuration is handled automatically by the operators.

Note:

You can deploy multiple isolated instances of Ansible Automation Platform into the same Red Hat OpenShift Container Platform cluster. To do this, use a namespace-scoped deployment model (isolated within a namespace).

This approach allows you to use the same cluster for several deployments.

