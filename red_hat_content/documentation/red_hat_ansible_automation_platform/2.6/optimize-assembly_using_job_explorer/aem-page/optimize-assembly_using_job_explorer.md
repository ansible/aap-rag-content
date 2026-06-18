+++
title = "View data about automation jobs across your organization - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_using_job_explorer"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_user_data_tracking/", "Get insights on automation across your environment with Automation Analytics"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_using_job_explorer/aem-page/optimize-assembly_using_job_explorer.html"
last_crumb = "View data about automation jobs across your organization"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "View data about automation jobs across your organization"
oversized = "false"
page_slug = "optimize-assembly_using_job_explorer"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-assembly_using_job_explorer"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_using_job_explorer/toc/toc.json"
type = "aem-page"
+++

# View data about automation jobs across your organization

The **Job Explorer** provides a detailed view of jobs run on automation controller clusters across your organizations. You can access the **Job Explorer** by selecting Automation Analytics> (and then)Job Explorer from the navigation panel or using the drill-down view available across each of the application’s charts.

Using the **Job Explorer** you can:

- Filter the types of jobs running in a cluster or organization;
- Directly link out to templates on automation controller for further assessment;
- Identify and review job failures;
- View more details for top templates running on a cluster;
- Filter out nested workflows and jobs.


You can review the features and details of the **Job Explorer** in the following sections.

## Create a filtered and sorted view of jobs

You can view a list of jobs, filtered by attributes you choose, using the **Job Explorer**.

### About this task

Filter options include:

- Status
- Job
- Cluster
- Organization
- Inventory
- Template


You can sort results by any of the parameters from each column by using the directional arrows.

### Procedure

1.  From the navigation panel, select Automation Analytics> (and then)Job Explorer.
2.  In the filter toolbar, select **Job** from the **Filter by** list.
3.  In that same toolbar, select a time range. Job Explorer will now display jobs within that time range.
4.  To further refine results, return to the filter toolbar and select a different attribute to filter results by, including job status, cluster, or organization. The **Job Explorer** view updates and presents a list of jobs based on the attributes you selected.

## View more information about an individual job

You can view additional information about each individual job.

### Procedure

1.  Navigate to the job **Id/Name** column.
2.  Click the arrow icon.

## Review job details on automation controller

You can review job details on automation controller.

### Procedure

 Click the job in the **Id/Name** column to view the job itself on the automation controller job details page.
