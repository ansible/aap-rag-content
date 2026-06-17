+++
title = "Get insights on automation across your environment with Automation Analytics - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_user_data_tracking"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_user_data_tracking/", "Get insights on automation across your environment with Automation Analytics"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-con_user_data_tracking/aem-page/optimize-con_user_data_tracking.html"
last_crumb = "Get insights on automation across your environment with Automation Analytics"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Get insights on automation across your environment with Automation Analytics"
oversized = "false"
page_slug = "optimize-con_user_data_tracking"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-con_user_data_tracking"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-con_user_data_tracking/toc/toc.json"
type = "aem-page"
+++

# Get insights on automation across your environment with Automation Analytics

Usability data collection is included with automation controller to collect data to better understand how automation controller users specifically interact with automation controller, to help enhance future releases, and to continue streamlining your user experience.

Only users installing a trial of automation controller or a fresh installation of automation controller are opted-in for this data collection.

## Automation Analytics

When you imported your license for the first time, you were automatically opted in for the collection of data that powers Automation Analytics, a cloud service that is part of the Ansible Automation Platform subscription.

 Important:

For opt-in of Automation Analytics to have any effect, your instance of automation controller must be running on Red Hat Enterprise Linux.

As with Red Hat Lightspeed, Automation Analytics is built to collect the minimum amount of data needed. No credential secrets, personal data, automation variables, or task output is gathered.

When you imported your license for the first time, you were automatically opted in to Automation Analytics. To configure or disable this feature, see [Configuring Automation Analytics](/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_user_data_tracking#proc-controller-configure-analytics "When you imported your license for the first time, you were automatically opted in for the collection of data that powers Automation Analytics, a cloud service that is part of the Ansible Automation Platform subscription.").

By default, the data is collected every four hours. When you enable this feature, data is collected up to a month in arrears (or until the previous collection). You can turn off this data collection at any time in the **Miscellaneous System settings** of the System configuration window.

This setting can also be enabled through the API by specifying `INSIGHTS_TRACKING_STATE = true` in either of these endpoints:

-  `api/v2/settings/all`
-  `api/v2/settings/system`


The Automation Analytics generated from this data collection can be found on the [Red Hat Cloud Services](https://cloud.redhat.com) portal.

**Clusters** data is the default view. This graph represents the number of job runs across all automation controller clusters over a period of time. The previous example shows a span of a week in a stacked bar-style chart that is organized by the number of jobs that ran successfully and jobs that failed.

Alternatively, you can select a single cluster to view its job status information.

 ![Job run status](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/aa-job-run-status-over-time-period.png)

This multi-line chart represents the number of job runs for a single automation controller cluster for a specified period of time. The preceding example shows a span of a week, organized by the number of successfully running jobs and jobs that failed. You can specify the number of successful and failed job runs for a selected cluster over a span of one week, two weeks, and monthly increments.

On the clouds navigation panel, select Organization Statistics to view information for the following:

- Use by organization
- Job runs by organization
- Organization status


 Note:

The organization statistics page will be deprecated in a future release.

## Configure Automation Analytics

When you imported your license for the first time, you were automatically opted in for the collection of data that powers Automation Analytics, a cloud service that is part of the Ansible Automation Platform subscription.

### Before you begin

- A service account created with the **Automation Analytics Viewer** role in console.redhat.com. For more information, see [Creating a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct).

### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)System.
2.  Click Edit.
3.  In the field labeled **Red Hat Client ID for Analytics**, enter the client ID you received when you created your service account to retrieve subscription and content information.
4.  In the field labeled **Red Hat Client Secret for Analytics**, enter the client secret you received when you created your service account to send data to Automation Analytics.
5.  In the **Options** list select the checkbox to **Gather data for Automation Analytics**.
6.  Click Save.

### Results

After configuring the service account, run a test job to ensure everything is set up correctly.

1. From the navigation panel, select Automation Execution> (and then)Jobs to launch a job.
2. Check [analytics at console.redhat.com](https://console.redhat.com/ansible/automation-analytics/reports) to confirm that the data is being posted.

## Use automation calculator to determine automation savings

The automation calculator provides graphs, metrics and calculations that help you determine the total savings on your investment in automated processes.

### Calculate your automation savings

The **Automation Calculator** produces its default total savings figure based on estimates for each variable.

#### About this task

You can tune this calculation by providing more specific organizational cost information and adjusting the time values for each of the top templates.

 Note:

Automation savings calculations are not saved in Automation Analytics.

#### Procedure

1.  Under **Calculate your automation** enter cost information for:
  1.   **Manual process cost**
  2.   **Automated process cost**
2.  Under **Top templates**:
  1.  Adjust time values for top templates to provide time to manually perform each task that the template automates.

#### Results

**Total savings** updates based on the information you enter in each field.

### Top templates

**Top templates** lists the 25 most frequently run templates across all hosts in your environment.

Templates are listed in descending order starting with the highest run count. You can enter the time it takes to perform tasks manually that are automated by templates in the field adjacent to the run totals to produce a more accurate total savings. The default value is set to **60** minutes.

### Curate top templates

You can use the toggle switch for each template to show or hide it in the bar graph to compare performance and savings based on specific templates.

#### Procedure

 Click the toggle switch for each template to display or hide it.

#### Results

The bar graph on the **Automation Calculator** will update to display those top templates selected and **Total savings** will calculate based on those templates.

### View template details

View detailed information for each template in **Top templates** to learn more about the template’s context in the calculation of automation savings.

#### Procedure

 Click the **Info** icon for a job template to view template details.

Top template information includes the following:

- **Total elapsed sum** - Total run time of the template.
- **Success elapsed sum** - Total run time for successful template runs.
- **Failed elapsed sum** - Total run time for failed template runs.
- **Automation percentage** - The template accounts for this percentage of automation in your organization.
- **Associated organizations** - The template runs against these organizations.
- **Associated clusters** - Automation controller clusters the template runs on.
