+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_automation_savings_planner"
title = "Plan, track, and analyze returns with automation savings planner - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_user_data_tracking/", "Get insights on automation across your environment with Automation Analytics"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_automation_savings_planner/aem-page/optimize-assembly_automation_savings_planner.html"
last_crumb = "Plan, track, and analyze returns with automation savings planner"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Plan, track, and analyze returns with automation savings planner"
oversized = "false"
page_slug = "optimize-assembly_automation_savings_planner"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-assembly_automation_savings_planner"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_automation_savings_planner/toc/toc.json"
type = "aem-page"
+++

# Plan, track, and analyze returns with automation savings planner

An automation savings plan gives you the ability to plan, track, and analyze the potential efficiency and cost savings of your automation initiatives. Use automation analytics to create an automation savings plan by defining a list of tasks needed to complete an automation job.

You can then link your automation savings plans to an Ansible job template to accurately measure the time and cost savings upon completion of an automation job.

To create an automation savings plan, you can use the automation savings planner to prioritize the various automation jobs throughout your organization and understand the potential time and cost savings for your automation initiatives.

## Create a new automation savings plan

Create an automation savings plan by defining the tasks needed to complete an automation job by using the automation savings planner.

### Procedure

1.  From the navigation panel, select Automation Analytics> (and then)Savings Planner.
2.  Click Add Plan.
3.  Provide some information about your automation job:
  1.  Enter descriptive information, such as a name, description, and type of automation.
  2.  Enter technical information, such as the number of hosts, the duration to manually complete this job, and how often you complete this job.
  3.  Click Next.
4.  In the tasks section, list the tasks needed to complete this plan:
  1.  Enter each task in the field, then click Add.
  2.  Rearrange tasks by dragging the item up/down the tasks list.
  3.  Click Next.
5.  Select a template to link to this plan, then click Save. Note:
      The task list is for your planning purposes only, and does not currently factor into your automation savings calculation.

### Results

Your new savings plan is now created and displayed on the automation savings planner list view.

## Edit an existing savings plan

Edit any information about an existing savings plan by clicking on it from the savings planner list view.

### Procedure

1.  From the navigation panel, select Automation Analytics> (and then)Savings Planner.
2.  On the automation savings plan, click Click the More Actions icon **⋮**, then click Edit.
3.  Make any changes to the automation plan, then click Save.

## Link a savings plan to a job template

You can associate a job template to a savings plan to allow automation analytics to provide a more accurate time and cost savings estimate for completing this savings plan.

### Procedure

1.  From the navigation panel, select Automation Analytics> (and then)Savings Planner.
2.  Click the More Actions icon **⋮** and select **Link Template**.
3.  Click Save.

## Review savings calculations for your automation plans

The automation savings planner offers a calculation of how much time and money you can save by automating a job. Automation analytics takes data from the plan details and the associated job template to provide you with an accurate projection of your cost savings when you complete this savings plan.

To do so, navigate to your savings planner page, click the name of an existing plan, then navigate to the **Statistics** tab.

The statistics chart displays a projection of your monetary and time savings based on the information you provided when creating a savings plan. Primarily, the statistics chart subtracts the automated cost from the manual cost of executing the plan to provide the total resources saved upon automation. The chart then displays this data by year to show you the cumulative benefits for automating the plan over time.

Click between **Money** and **Time** to view the different types of savings for automating the plan.
