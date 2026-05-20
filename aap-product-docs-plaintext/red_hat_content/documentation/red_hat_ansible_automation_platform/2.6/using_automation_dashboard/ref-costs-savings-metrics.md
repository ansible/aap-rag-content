# 1. View key usage metrics with automation dashboard
## 1.9. Cost and savings analysis metrics

The costs and savings analysis generates the following metrics to quantify the return on investment (ROI) derived from automation execution.

**Table 1.1. Costs and Savings Output Metrics**

| Metric | Description |
| --- | --- |
| <br> **Cost of manual automation** | <br>  Total cost if all jobs were run manually. Calculated as: (Manual time in minutes × Host executions) × Average labor cost per minute. |
| <br> **Cost of automated execution** | <br>  Total cost of running jobs on Ansible Automation Platform. Calculated as: (Running time in minutes × Prorated subscription cost per minute). |
| <br> **Total savings/cost avoided** | <br>  The difference between manual and automated costs. |
| <br> **Total hours saved/avoided** | <br>  Time saved by automation compared to manual execution. |
| <br> **Time taken to manually execute (min)** | <br>  Estimated manual execution time in minutes. |
| <br> **Time taken to create automation (min)** | <br>  Estimated time spent creating or authoring the automation (for example, writing playbooks or setting up jobs). Included in cost calculations when enabled in settings. |
| <br> **Hourly rate for manually running the job ($)** | <br>  The hourly labor cost used to estimate the expense of running jobs manually. Used to calculate manual cost and savings. |
| <br> **Monthly cost of running Ansible Automation Platform** | <br>  Monthly cost of running the Ansible Automation Platform. This value includes license, labor and infrastructure costs to run Ansible Automation Platform. It is used to calculate the automation savings |

