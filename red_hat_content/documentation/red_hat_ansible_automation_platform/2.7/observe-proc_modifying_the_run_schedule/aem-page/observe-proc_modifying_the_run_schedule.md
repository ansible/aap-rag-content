+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-proc_modifying_the_run_schedule"
title = "Configure the metrics-utility to run at specific times - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-assembly_metrics_utility/", "Generate consumption-based billing reports with the metrics-utility"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/observe-proc_modifying_the_run_schedule/aem-page/observe-proc_modifying_the_run_schedule.html"
last_crumb = "Configure the metrics-utility to run at specific times"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure the metrics-utility to run at specific times"
oversized = "false"
page_slug = "observe-proc_modifying_the_run_schedule"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/observe-proc_modifying_the_run_schedule"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/observe-proc_modifying_the_run_schedule/toc/toc.json"
type = "aem-page"
+++

# Configure the `metrics-utility` to run at specific times

You can configure `metrics-utility` to run at specified times and intervals. Run frequency is expressed in cronjobs. For more information on the cron utility, see [How to schedule jobs using the Linux `Cron` utility](https://www.redhat.com/sysadmin/linux-cron-command).

## About this task

To modify the run schedule on Red Hat Enterprise Linux and on OpenShift Container Platform, use one of the following procedures:

## Procedure

1.  From the command line, run:
       `crontab -e`

2.  After the code editor has opened, update the `gather` and `build` parameters using cron syntax as shown below:
       `*/2 * * * * metrics-utility gather_automation_controller_billing_data --ship --until=10m`

     `*/5 * * * * metrics-utility build_report`

3.  Save and close the file.

## Modify the run schedule on OpenShift Container Platform from the Ansible Automation Platform operator

To adjust the execution schedule of the `metrics-utility` within your Ansible Automation Platform deployment running on OpenShift Container Platform, use the following procedure.

### Procedure

1.  From the navigation panel, select Workloads> (and then)Deployments.
2.  On the next screen, select **automation-controller-operator-controller-manager**.
3.  Beneath the heading **Deployment Details**, click the down arrow button to change the number of pods to zero. This pauses the deployment so you can update the running schedule.
4.  From the navigation panel, select **Installed Operators**.
5.  From the list of installed operators, select Ansible Automation Platform.
6.  On the next screen, select the automation controller tab.
7.  From the list displayed, select your automation controller instance.
8.  On the next screen, select the `YAML` tab.
9.  In the `YAML` file, find the following parameters and enter a variable representing how often `metrics-utility` should gather data and how often it should produce a report:
       `metrics_utility_cronjob_gather_schedule:`

     `metrics_utility_cronjob_report_schedule:`

10.  Click Save.
11.  From the navigation menu, select Deployments and then select **automation-controller-operator-controller-manager**.
12.  Increase the number of pods to 1.
13.  To verify that you have changed the `metrics-utility` running schedule successfully, you can take one or both of the following steps:
  1.  Return to the `YAML` file and ensure that the previously described parameters reflect the correct variables.
  2.  From the navigation menu, select Workloads> (and then)Cronjobs and ensure that your cronjobs show the updated schedule.
