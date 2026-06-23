# Container growth topology
## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*
![Container growth topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/cont-a-env-a-2_7.png)

Red Hat tests a single VM with these requirements:

*Table 1. Virtual machine requirements*

| Requirement    | Minimum requirement                                                                                                                                                                                                                                                                                                                                             |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>RAM        | 16 GB minimum, 20 GB recommended32 GB required for growth topology bundled installations with `hub_seed_collections=true`. Seeding the collections can take 45 or more minutes.    Note:     Metrics service adds approximately 4 GB RAM usage (2 GB minimum).                                                                                                  |
| <br>CPUs       | <br>4                                                                                                                                                                                                                                                                                                                                                           |
| <br>Local disk | Total available disk space: 80 GB (60 GB base + 20 GB for metrics service)Installation directory: 15 GB (if on a dedicated partition)`/var/tmp` for online installations: 1 GB`/var/tmp` for offline or bundled installations: 10 GBMetrics service database: 20 GB minimumTemporary directory (defaults to `/tmp`) for offline or bundled installations: 10 GB |
| <br>Disk IOPS  | <br>3000                                                                                                                                                                                                                                                                                                                                                        |

*Table 2. Infrastructure topology components*

| Purpose                                        | Example group names                                                                                      |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| <br>All Ansible Automation Platform components | `automationgateway` `automationcontroller` `automationhub` `automationeda``automationmetrics` `database` |


Note:

In the growth topology (all-in-one), metrics service runs on the same host as automation controller and other Ansible Automation Platform components. The installer deploys 3 metrics service containers:

- `automation-metrics-web` - REST API for metrics and dashboard data
- `automation-metrics-tasks` - dispatcherd worker for data collection
- `automation-metrics-scheduler` - APScheduler for periodic collection tasks

