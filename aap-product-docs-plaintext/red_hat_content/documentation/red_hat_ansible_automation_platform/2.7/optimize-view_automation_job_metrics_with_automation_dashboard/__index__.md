# View automation job metrics with automation dashboard

Track automation job performance and demonstrate automation value with automation dashboard. Analyze job execution metrics and calculate cost savings to communicate the impact of your automation initiatives to stakeholders.

Viewing automation job metrics helps you to:

- **Monitor automation execution**: Track successful and failed jobs, unique hosts automated, and total automation hours to understand platform usage patterns.
- **Analyze automation adoption**: View top projects and users to identify high-value automation workflows and understand which teams drive automation adoption.
- **Demonstrate automation value**: Demonstrate return on investment to stakeholders by calculating cost savings from automation.

## Filter and save automation data for reporting

Automation dashboard provides filtering options to analyze your Ansible Automation Platform automation runs. You can select one or more filtering options to customize your report, select a time period and a currency, and save your report to your automation dashboard.

### Filters

Use the following filtering options to customize your report:

- **Template:** select one or more Job Templates
- **Organization:** select one or more Organizations
- **Project:** select one or more Projects
- **Label:** select one or more automation projects by label. Note:
You must preconfigure and assign labels to Ansible Automation Platform for display in automation dashboard.

### Time period and currency

After selecting your filters, select a time period for analysis, and select a currency to show automation savings.

- Use a shorter time period to analyze specific automation use cases.
- Use a longer time period to evaluate overall platform usage and automation growth.
- Changing the currency does not convert the values. You must manually update the **Monthly AAP cost** and **Hourly rate** to reflect the selected currency.

### Save a report

Use **Save as Report** to save the current configuration to your automation dashboard. You can retrieve saved reports any time by using **Select a Report**.

### Export automation reports

You can export your automation usage and ROI data as CSV or PDF files to share with stakeholders.

**Prerequisites**

You must have configured your **Monthly AAP cost** and **Hourly rate** in the settings to ensure accurate ROI data in the exported report.

**Procedure**

1. Select a saved report or use the filters to customize the current view.
2. Select a **Duration** for the data you want to export.
3. Click **Export as CSV**: Generates a spreadsheet of the raw data.
4. Click **Save as PDF**: Generates a formatted summary report.

## Summary of key automation data metrics

Automation dashboard displays a summary of the top and overview usage for your selected report. This includes the following data:

- **Successful jobs**: Number of job runs that completed without error in the selected period. Use the ratio between successful and failed jobs to track automation health and reliability over time.
- **Failed jobs**: Number of job runs that ended in failure in the selected period. Review failed jobs to fix playbooks, credentials, or inventory issues and improve success rates.
- **Hosts automated**: Number of hosts that executed at least one automation job in the selected period. Indicates how much of your inventory is actively automated and can help with license or capacity planning.
- **Hours of automation**: Sum of all job runtimes in the selected period. Reflects total automation workload and can inform capacity planning and resource allocation.
- **Number of times jobs were run**: Total number of job executions in the selected period, regardless of success or failure. Use this to understand automation volume, trends, and adoption over time.
- **Number of hosts jobs are running on**: Number of hosts that ran at least one job in the selected period. Complements run count by showing how broadly automation is applied across your inventory.
- **Top 5 projects**: Projects ranked by total job count in the selected period. Helps identify which projects are driving the most automation activity.
- **Top 5 users**: Users ranked by automation runs they triggered or that ran in their context in the selected period. Shows individual adoption and activity. Note:
Scheduled jobs can affect these results, because they do not represent a real, logged-in user.

## Calculate savings from automation

To calculate total savings, the cost and savings analysis compares manual labor costs against Ansible Automation Platform execution costs. The dashboard prorates the monthly subscription cost into daily reporting values.

### Procedure

1.  In the **Monthly AAP cost** field, enter the monthly cost of running the Ansible Automation Platform. This value includes license, labor, and infrastructure costs to run Ansible Automation Platform. It is used to calculate the automation savings.
2.  In the **Hourly rate for manually running the job ($)** field, enter the hourly labor cost used to estimate what it would cost to run these jobs manually. This is used to calculate manual cost and savings.
3.  Optional: Select **Time taken to create automation** to include the estimated time spent creating or authoring the automation (for example, writing playbooks, setting up jobs) before it could be run.
Automation dashboard calculates the following data points based on your inputs:

- **Cost of manual automation**: Total cost if all jobs were run manually.
- **Cost of automated execution**: Total cost of running jobs on Ansible Automation Platform.
- **Total savings/cost avoided**: Difference between manual and automated cost.
- **Total hours saved/avoided**: Time saved by automation vs manual execution.
- **Time taken to manually execute (min)**: Estimated manual execution time in minutes.
- **Time taken to create automation (min)**: Estimated time spent creating or authoring the automation (for example, writing playbooks, setting up jobs) before it could be run. Included in cost when the switch above is on.

### Results

Navigate to the Reports page to view the **Total savings** based on your updated cost configurations.
