# 1. View key usage metrics with automation dashboard
## 1.9. Cost and savings analysis metrics




The costs and savings analysis generates the following metrics to quantify the return on investment (ROI) derived from automation execution.


<span id="idm140120299852592"></span>
**Table 1.1. Costs and Savings Output Metrics**

| Metric | Description |
| --- | --- |
|  **Cost of manual automation** | Total cost if all jobs were run manually. Calculated as: (Manual time in minutes × Host executions) × Average labor cost per minute. |
|  **Cost of automated execution** | Total cost of running jobs on Ansible Automation Platform. Calculated as: (Running time in minutes × Prorated subscription cost per minute). |
|  **Total savings/cost avoided** | The difference between manual and automated costs. |
|  **Total hours saved/avoided** | Time saved by automation compared to manual execution. |
|  **Time taken to manually execute (min)** | Estimated manual execution time in minutes. |
|  **Time taken to create automation (min)** | Estimated time spent creating or authoring the automation (for example, writing playbooks or setting up jobs). Included in cost calculations when enabled in settings. |
|  **Hourly rate for manually running the job ($)** | The hourly labor cost used to estimate the expense of running jobs manually. Used to calculate manual cost and savings. |
|  **Monthly cost of running Ansible Automation Platform** | Monthly cost of running the Ansible Automation Platform. This value includes license, labor and infrastructure costs to run Ansible Automation Platform. It is used to calculate the automation savings |




