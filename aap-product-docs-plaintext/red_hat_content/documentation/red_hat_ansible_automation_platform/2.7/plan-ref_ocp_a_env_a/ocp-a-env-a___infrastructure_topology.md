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

| Count | Component                                  |
| ----- | ------------------------------------------ |
| 1     | Automation controller web pod              |
| 1     | Automation controller task pod             |
| 1     | Automation hub web pod                     |
| 1     | Automation hub API pod                     |
| 2     | Automation hub content pod                 |
| 2     | Automation hub worker pod                  |
| 1     | Automation hub Redis pod                   |
| 1     | Metrics service web pod                    |
| 1     | Metrics service tasks pod                  |
| 1     | Metrics service scheduler pod              |
| 1     | Event-Driven Ansible API pod               |
| 1     | Event-Driven Ansible activation worker pod |
| 1     | Event-Driven Ansible default worker pod    |
| 1     | Event-Driven Ansible event stream pod      |
| 1     | Event-Driven Ansible scheduler pod         |
| 1     | Platform gateway pod                       |
| 1     | Database pod                               |
| 1     | Redis pod                                  |

Note:

Metrics service is deployed automatically when the AnsibleAutomationPlatform Custom Resource (CR) includes metrics configuration. The operator creates a MetricsService CR (named `<aap-name>`-metrics) and manages three pods:

- `<aap-name>`- **metrics-web** - REST API for metrics and dashboard data
- `<aap-name>`- **metrics-tasks** - dispatcherd worker for background data collection
- `<aap-name>`- **metrics-scheduler** - APScheduler for periodic collection tasks (hourly and daily schedules)

All database provisioning, secrets management, and routing configuration is handled automatically by the operators.

Note:

You can deploy multiple isolated instances of Ansible Automation Platform into the same Red Hat OpenShift Container Platform cluster. To do this, use a namespace-scoped deployment model (isolated within a namespace).

This approach allows you to use the same cluster for several deployments.

