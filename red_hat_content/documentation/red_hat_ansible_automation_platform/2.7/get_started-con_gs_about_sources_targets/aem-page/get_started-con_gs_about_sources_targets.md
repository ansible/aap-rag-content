+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-con_gs_about_sources_targets"
template = "docs/aem-title.html"
title = "Organize and define automation sources and targets - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-assembly_gs_auto_dev/", "Get started as an automation developer"]]
category = "Get started"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/get_started-con_gs_about_sources_targets/aem-page/get_started-con_gs_about_sources_targets.html"
last_crumb = "Organize and define automation sources and targets"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Organize and define automation sources and targets"
oversized = "false"
page_slug = "get_started-con_gs_about_sources_targets"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/get_started-con_gs_about_sources_targets"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/get_started-con_gs_about_sources_targets/toc/toc.json"
type = "aem-page"
+++

# Organize and define automation sources and targets

Projects and inventory files help you organize your automation sources and targets.

## Create an automation execution project

A project is a logical collection of playbooks. Projects are useful as a way to group your automation content according to the organizing principle of your choice.

### About this task

You can set up an automation execution project in the platform UI.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects.
2.  On the **Projects** page, click Create project to launch the **Create Project** window.
3.  Enter the appropriate details into the following required fields:

  - **Name** (required)
  - Optional: **Description**
  - **Organization** (required): A project must have at least one organization. Select one organization now to create the project. When the project is created you can add additional organizations.
  - Optional: **Execution Environment**: Enter the name of the execution environment or search from a list of existing ones to run this project.
  - **Source Control Type** (required): Select an SCM type associated with this project from the menu. Options in the following sections become available depending on the type chosen. For more information, see [Managing playbooks manually](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_controller_adding_a_project "You can create a logical collection of playbooks, called projects in automation controller.") or [Managing playbooks using source control](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_manage_playbooks_with_source_control#ref-projects-manage-playbooks-with-source-control "Choose one of the following options when managing playbooks by using source control:").
  - Optional: **Content Signature Validation Credential**: Use this field to enable content verification. Specify the GPG key to use for validating content signature during project synchronization. If the content has been tampered with, the job will not run. For more information, see [Project signing and verification](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_project_signing#assembly-controller-project-signing "Use project signing and verification in your project directory to sign files. You can then verify whether or not that content has changed in any way, or files have been added to, or removed from the project unexpectedly.").

4.  Click Create project.

## Create an automation decision project

Like automation execution projects, automation decision projects are logical collections of automation decision content. You can use the project function to organize your automation decision content in a way that makes sense to you.

### Before you begin

- You have set up any neccessary credentials. For more information, see [Setting up credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_eda_set_up_credential#eda-set-up-credential "Create a credential to securely store sensitive data (like tokens and passwords) required for rulebook activations to connect to source plugins or private registries.").
- You have an existing repository containing rulebooks that are integrated with playbooks contained in a repository to be used by automation controller.

### About this task

### Procedure

1.  From the navigation panel, select **Automation Decisions> (and then)Projects**.
2.  Click Create project.
3.  Enter the following information:

  - **Name**: Enter project name.
  - **Description**: This field is optional.
  - **Organization**: Select the organization associated with the project.
  - **Source control type**: Git is the only SCM type available for use.
  - **Proxy**: Proxy used to access HTTP or HTTPS servers.
  - **Source control branch/tag/commit**: Branch to checkout. Can also be tags, commit hashes, or arbitrary refs.
  - **Source control refspec**: A refspec to fetch. This parameter allows access to references through the branch field not otherwise available.
  - Optional: **Source control credential**: The token needed to use the source control URL.
  - **Content signature validation credential**: Enables content signing to verify that the content has remained secure during project syncing. If the content is tampered with, the job will not run.
  - **Options**: Checking the box next to **Verify SSL** verifies the SSL with HTTPS when the project is imported.

4.  Click Create project.

### What to do next

Your project is now created and can be managed in the **Projects** screen.

After saving the new project, the project’s details page is displayed. From there or the **Projects** list view, you can edit or delete it.

## About inventories

An inventory is a file listing the collection of hosts managed by Ansible Automation Platform.

### About this task

Organizations are assigned to inventories, while permissions to launch playbooks against inventories are controlled at the user or team level.

You can find inventories in the UI by navigating to Automation Execution> (and then)Infrastructure> (and then)Inventories. The Inventories window displays a list of the inventories that are currently available. You can sort the inventory list by name and search by inventory type, organization, description, inventory creators or modifiers, or additional criteria. Use the following procedure to create a new inventory.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories. The **Inventories** view displays a list of the inventories currently available.
2.  Click Create inventory, and from the list menu select the type of inventory you want to create.
3.  Enter the appropriate details into the following fields:

  - **Name**: Enter a name for the inventory.
  - Optional: **Description**: Enter a description.
  - **Organization**: Choose among the available organizations.
  - Only applicable to Smart Inventories: **Smart Host Filter**: Filters are similar to tags in that tags are used to filter certain hosts that contain those names. Therefore, to populate this field, specify a tag that contains the hosts you want, not the hosts themselves. Filters are case-sensitive. For more information, see [Smart host filters](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-ref_controller_smart_inventories#ref-controller-smart-host-filter "You can use a search filter to populate hosts for an inventory. This feature uses the fact searching feature.").
  - **Instance groups**: Select the instance group or groups for this inventory to run on. If the list is extensive, use the search to narrow the options. You can select multiple instance groups and sort them in the order that you want them run.
  - Optional: **Labels**: Add labels that describe this inventory, so they can be used to group and filter inventories and jobs.
  - Only applicable to constructed inventories: **Input inventories**: Specify the source inventories to include in this constructed inventory. Empty groups from input inventories are copied into the constructed inventory.
  - Optional and only applicable to constructed inventories: **Cache timeout (seconds)**:Set the length of time you want the cache plugin data to timeout.
  - Only applicable to constructed inventories: **Verbosity**: Control the level of output that Ansible produces as the playbook executes related to inventory sources associated with constructed inventories. Select the verbosity from Normal to various Verbose or Debug settings. This only appears in the "details" report view.     * Verbose logging includes the output of all commands.
    * Debug logging is exceedingly verbose and includes information on SSH operations that can be useful in certain support instances. Most users do not need to see debug mode output.
  - Only applicable to constructed inventories: **Limit**: Restricts the number of returned hosts for the inventory source associated with the constructed inventory. You can paste a group name into the limit field to only include hosts in that group. For more information, see the **Source variables** setting.
  - Only applicable to standard inventories: **Options**: Check the box next to **Prevent instance group fallback** to enable only the instance groups listed in the **Instance groups** field to execute the job. If unchecked, all available instances in the execution pool will be used based on the hierarchy described in [Control where a job runs](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_ug_controller_instance_groups#controller-control-job-run "Use instance groups to control job execution locations. While the controller automatically selects groups based on capacity, you can override this by associating groups with job templates, inventories, or organizations.") . Click the tooltip for more information. Note:
    Set the `prevent_instance_group_fallback` option for smart inventories through the API.

  - **Variables** (**Source variables** for constructed inventories):
    * **Variables**: Variable definitions and values to apply to all hosts in this inventory. Enter variables using either JSON or YAML syntax. Use the radio button to toggle between the two.
    * **Source variables** for constructed inventories are used to configure the constructed inventory plugin. Source variables create groups under the `groups` data key. The variable accepts Jinja2 template syntax, renders it for every host, makes a `true` or `false` evaluation, and includes the host in the group (from the key of the entry) if the result is `true`.

4.  Click Create inventory.

### What to do next

After creating the new inventory, you can proceed with configuring permissions, groups, hosts, sources, and viewing completed jobs, if applicable to the type of inventory.
