+++
title = "Add new hosts as automation targets - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_hosts"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-define_where_automation_runs_with_host_and_node_groupings/", "Define where automation runs with host and node groupings"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_hosts/aem-page/administer-assembly_controller_hosts.html"
last_crumb = "Add new hosts as automation targets"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Add new hosts as automation targets"
oversized = "false"
page_slug = "administer-assembly_controller_hosts"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_hosts"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_hosts/toc/toc.json"
type = "aem-page"
+++

# Add new hosts as automation targets

A host is a system managed by Ansible Automation Platform, which might include a physical, virtual, cloud-based server, or other device.

Typically a host is an operating system instance.

Hosts are grouped in inventories and are sometimes referred to as a “nodes”.

Ansible works against multiple managed nodes or “hosts” in your infrastructure at the same time, using a list or group of lists known as an inventory.

Once your inventory is defined, use patterns to select the hosts or groups you want Ansible to run against.

## Create a host

Learn how to create a new host by providing a name, selecting an inventory, and optionally defining a description and associated variables.

### About this task

To create a new host.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Hosts.
2.  Click Create host.
3.  On the **Create Host** page enter the following information:

  - **Name**: Enter a name for your host.
  - (Optional) **Description**: Enter a description for your host.
  - **Inventory**: Select the inventory for this host to belong to.
  - **Variables**: Enter the inventory file variables associated with your host.

4.  Click Create host to save your changes.

## View the host details

Examine the Host details shown below for a job run.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Hosts. The **Hosts** page displays the following information about the host or hosts affected by recent job runs.
2.  Selecting a particular host displays the **Details** page for that host, with the following information:

  - The **Name** of the Host.
  - The **Inventory** associated with that host. Selecting this inventory displays details of the inventory.
  - When the Host was **Created** and by whom. Selecting the creator displays details of the creator.
  - When the Host was **Last modified**. Selecting the creator displays details of the creator.
  - **Variables** associated with the Host. You can display the variables in YAML or JSON format.

3.  Click Edit host to edit details of the host.   - Select the **Facts** tab to display facts associated with the host.
  - Select the **Groups** tab to display the Groups associated with the host.     * Click Associate groups to associate a group with the host.
  - Select the **Jobs** tab to display the Jobs which ran on the host.     * Click the ![Expand](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/arrow.png) icon to display details of the job.  
![Details of job associated with a host](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/hosts_jobs_details.png)  
