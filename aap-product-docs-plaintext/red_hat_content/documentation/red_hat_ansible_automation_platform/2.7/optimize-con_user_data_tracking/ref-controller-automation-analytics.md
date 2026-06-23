# Get insights on automation across your environment with Automation Analytics
## Automation Analytics

When you imported your license for the first time, you were automatically opted in for the collection of data that powers Automation Analytics, a cloud service that is part of the Ansible Automation Platform subscription.

Important:

For opt-in of Automation Analytics to have any effect, your instance of automation controller must be running on Red Hat Enterprise Linux.

As with Red Hat Lightspeed, Automation Analytics is built to collect the minimum amount of data needed. No credential secrets, personal data, automation variables, or task output is gathered.

When you imported your license for the first time, you were automatically opted in to Automation Analytics. To configure or disable this feature, see [Configuring Automation Analytics](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_user_data_tracking#proc-controller-configure-analytics "When you imported your license for the first time, you were automatically opted in for the collection of data that powers Automation Analytics, a cloud service that is part of the Ansible Automation Platform subscription.").

By default, the data is collected every four hours. When you enable this feature, data is collected up to a month in arrears (or until the previous collection). You can turn off this data collection at any time in the **Miscellaneous System settings** of the System configuration window.

This setting can also be enabled through the API by specifying `INSIGHTS_TRACKING_STATE = true` in either of these endpoints:

-  `api/v2/settings/all`
-  `api/v2/settings/system`


The Automation Analytics generated from this data collection can be found on the [Red Hat Cloud Services](https://cloud.redhat.com) portal.

**Clusters** data is the default view. This graph represents the number of job runs across all automation controller clusters over a period of time. The previous example shows a span of a week in a stacked bar-style chart that is organized by the number of jobs that ran successfully and jobs that failed.

Alternatively, you can select a single cluster to view its job status information.

![Job run status](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/aa-job-run-status-over-time-period.png)

This multi-line chart represents the number of job runs for a single automation controller cluster for a specified period of time. The preceding example shows a span of a week, organized by the number of successfully running jobs and jobs that failed. You can specify the number of successful and failed job runs for a selected cluster over a span of one week, two weeks, and monthly increments.

On the clouds navigation panel, select Organization Statistics to view information for the following:

- Use by organization
- Job runs by organization
- Organization status


Note:

The organization statistics page will be deprecated in a future release.

