+++
title = "Schedule recurring automation - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_schedules"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_schedules/", "Schedule recurring automation"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_schedules/aem-page/develop-assembly_ug_controller_schedules.html"
last_crumb = "Schedule recurring automation"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Schedule recurring automation"
oversized = "false"
page_slug = "develop-assembly_ug_controller_schedules"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_schedules"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_schedules/toc/toc.json"
type = "aem-page"
+++

# Schedule recurring automation

From the navigation panel, click Automation Execution> (and then)Schedules to access your configured schedules. The schedules list can be sorted by any of the attributes from each column by using the directional arrows. You can also search by name, date, or the name of the month in which a schedule runs.

Use the **On** or **Off** toggle to stop an active schedule or activate a stopped schedule.

Click the Edit ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png) icon to edit a schedule.


![Schedules sample list](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-schedules-sample-list.png)  


If you are setting up a template, a project, or an inventory source, click the **Schedules** tab on the **Details** page for that resource, to configure schedules for these resources. When you create a schedule, it has the following parameters:

Name
Click the schedule name to open its details.

Related resource
Describes the function of the schedule.

Type
This identifies whether the schedule is associated with a source control update or a system-managed job schedule.

Next run
The next scheduled run of this task.

## Add a new schedule

You can create a new schedule for a job template, workflow job template, inventory source, project sync, or management job template.

### About this task

You can create schedules from a template, project, or inventory source, and directly on the main **Schedules** page.

To create a new schedule on the **Schedules** page:

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Schedules.
2.  Click Create schedule. This opens the **Create schedule** window.
3.  Select a **Resource type** onto which this schedule is applied. Select from:

  -  **Job template**
    * For **Job template** select a **Job template** from the menu.
  -  **Workflow job template**
    * For **Workflow job template** select a **Workflow job template** from the menu.
  -  **Inventory source**
    * For **Inventory source** select an **Inventory** and an **Inventory source** from the appropriate menu.
  -  **Project sync**
    * For **Project sync** select a **Project** from the menu.
  -  **Management job template**
    * For **Management job template** select a **Workflow job template** from the menu.

4.  For **Job template** and **Project sync** enter the appropriate details into the following fields:

  - **Schedule name**: Enter the name.

  - Optional: **Description**: Enter a description.

  - **Start date/time**: Enter the date and time to start the schedule.

  - **Time zone**: Select the time zone. The **Start date/time** that you enter must be in this time zone. The **Schedule Details** display when you establish a schedule, enabling you to review the schedule settings and a list of the scheduled occurrences in the selected **Local Time Zone**.

     Important:
            Jobs are scheduled in UTC. Repeating jobs that run at a specific time of day can move relative to a local time zone when Daylight Saving Time shifts occur. The system resolves the local time zone based time to UTC when the schedule is saved. To ensure your schedules are correctly created, set your schedules in UTC time.

5.  Click Next. The **Define rules** page is displayed.

## Add a new schedule from a resource page

You can create a new schedule from the **Schedules** tab of a resource page, such as a template, project, or inventory source.

### About this task

To create a new schedule from a resource page:

### Procedure

1.  Click the **Schedules** tab of the resource that you are configuring. This can be a template, project, or inventory source.
2.  Click Create schedule. This opens the **Create schedule** window.
3.  Enter the appropriate details into the following fields:

  - **Schedule name**: Enter the name.

  - Optional: **Description**: Enter a description.

  - **Start date/time**: Enter the date and time to start the schedule.

  - **Time zone**: Select the time zone. The **Start date/time** that you enter must be in this time zone. The **Schedule Details** display when you establish a schedule, enabling you to review the schedule settings and a list of the scheduled occurrences in the selected **Local Time Zone**.

     Important:
            Jobs are scheduled in UTC. Repeating jobs that run at a specific time of day can move relative to a local time zone when Daylight Saving Time shifts occur. The system resolves the local time zone based time to UTC when the schedule is saved. To ensure your schedules are correctly created, set your schedules in UTC time.

4.  Click Next. The **Define rules** page is displayed.

## Define rules for the schedule

After you create a schedule, you can define rules for when the schedule runs.

### Procedure

1.  Enter the following information:

  - **Frequency**: Enter how often the schedule runs.

  - **Interval**: Select the interval at which the rule will repeat.

  - **Week start**: Select the day of the week that you want the week to begin.

  - **Minutes of the hour**: Use this field to declare minute(s) of the hour that the schedule should run.

  - **Hours of day**: Use this field to declare the hours of day that the schedule should run.

  - **Days of the week**: Select the days of the week on which to run the schedule.

  - **Days of the month**: Select the months of the year on which to run the schedule

  - **Weeks of the year**: Use this field to declare numbered weeks of the year that the schedule should run.

  - **Months of the year**: Use this field to declare ordinal days number of the month that the schedule should run.

  - **Days of the year**: Use this field to declare ordinal number days of the year that the schedule should run.

  - **Occurrences**: Use this field to filter down indexed rules based on those declared using the form fields in the Rule section.

  - **Schedule ending type**: Use this field to select when the schedule is set to end. For more information, see the [link](https://datatracker.ietf.org/doc/html/rfc5545) to the `iCalendar RFC for bysetpos` field in the iCalendar documentation when you have set the rules for the schedule.

2.  Click Save rule. The **Schedule Rules** summary page is displayed.
3.  Click Add rule to add additional rules.
4.  Click Next. The **Schedule Exceptions** page is displayed.

## Set exceptions to the schedule

Define specific dates or times when automated jobs should skip execution by using schedule exceptions.

### Procedure

1.  On the **Schedule Exceptions** page, click Create exception. Use the same format as for the schedule rules to create a schedule exception.

2.  Click Next to save and review both the schedule and the exception.
