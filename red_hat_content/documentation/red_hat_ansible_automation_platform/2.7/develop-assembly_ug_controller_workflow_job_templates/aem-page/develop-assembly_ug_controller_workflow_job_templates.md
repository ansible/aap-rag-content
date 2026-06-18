+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflow_job_templates"
title = "Orchestrate complex automation with workflow job templates - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflow_job_templates/", "Orchestrate complex automation with workflow job templates"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflow_job_templates/aem-page/develop-assembly_ug_controller_workflow_job_templates.html"
last_crumb = "Orchestrate complex automation with workflow job templates"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Orchestrate complex automation with workflow job templates"
oversized = "false"
page_slug = "develop-assembly_ug_controller_workflow_job_templates"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflow_job_templates"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflow_job_templates/toc/toc.json"
type = "aem-page"
+++

# Orchestrate complex automation with workflow job templates

A workflow job template links together a sequence of disparate resources that tracks the full set of jobs that were part of the release process as a single unit.

These resources include the following:

- Job templates
- Workflow job templates
- Project syncs
- Inventory source syncs


You can create both Job templates and Workflow job templates from Automation Execution> (and then)Templates.

For Job templates, see Job templates.

The **Automation Templates** page shows the workflow and job templates that are currently available.

Select the template name to display more information about the template, including when it last ran. This list is sorted alphabetically by name, but you can sort by other criteria, or search by various fields and attributes of a template.

From this screen you can launch ![Launch icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rightrocket.png) , edit ![Edit icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png), and duplicate ![Duplicate icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/copy.png) a workflow job template.

Only workflow templates have the workflow visualizer ![Workflow visualizer](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/visualizer.png) icon as a shortcut for accessing the workflow editor.


![Workflow templates home](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-templates-home.png)  


 Note:

Workflow templates can be used as building blocks for another workflow template. You can enable **Prompt on Launch** by setting up several settings in a workflow template, which you can edit at the workflow job template level. These do not affect the values assigned at the individual workflow template level. For further instructions, see the Workflow visualizer section.
