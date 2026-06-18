+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflows"
template = "docs/aem-title.html"
title = "Understand how to configure workflows - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflow_job_templates/", "Orchestrate complex automation with workflow job templates"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflows/aem-page/develop-assembly_ug_controller_workflows.html"
last_crumb = "Understand how to configure workflows"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Understand how to configure workflows"
oversized = "false"
page_slug = "develop-assembly_ug_controller_workflows"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflows"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflows/toc/toc.json"
type = "aem-page"
+++

# Understand how to configure workflows

Workflows enable you to configure a sequence of disparate job templates (or workflow templates) that might or might not share inventory, playbooks, or permissions.

Workflows have `admin` and `execute` permissions, similar to job templates. A workflow accomplishes the task of tracking the full set of jobs that were part of the release process as a single unit.

Job or workflow templates are linked together using a graph-like structure called nodes. These nodes can be jobs, project syncs, or inventory syncs. A template can be part of different workflows or used multiple times in the same workflow. A copy of the graph structure is saved to a workflow job when you launch the workflow.

The following example shows a workflow that has all three, and a workflow job template:


![Node in workflow](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-node-all-scenarios-wf.png)  


As the workflow runs, jobs are spawned from the node’s linked template. Nodes linking to a job template which has prompt-driven fields (job_type, job_tags, skip_tags, limit) can contain those fields, and is not prompted on launch. Job templates that prompt for a credential or inventory, without defaults, are not available for inclusion in a workflow.

## Workflow scenarios and considerations

Workflows in automation controller allow you to string together multiple job templates and other workflows into a single job run. This section describes several workflow scenarios and considerations to remember when building workflows.

When building workflows, consider the following:

- A root node is set to **ALWAYS** by default and cannot be edited.

![Node always](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-root-node-always.png)  


- A node can have multiple parents, and children can be linked to any of the states of success, failure, or always. If always, then the state is neither success nor failure. States apply at the node level, not at the workflow job template level. A workflow job is marked as successful unless it is canceled or encounters an error.

![Sibling nodes all edge types](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-sibling-nodes-all-edge-types.png)  


- If you remove a job or workflow template within the workflow, the nodes previously connected to those deleted, automatically get connected upstream and retain the edge type as in the following example:

![Node delete scenario](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-node-delete-scenario.png)  


- You can have a convergent workflow, where multiple jobs converge into one. In this scenario, any of the jobs or all of them must complete before the next one runs, as shown in the following example:  
![Node convergence](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-wf-node-convergence.png)  
  * In this example, automation controller runs the first two job templates in parallel. When they both finish and succeed as specified, the third downstream (convergence node), triggers.
- Prompts for inventory and surveys apply to workflow nodes in workflow job templates.
- If you launch from the API, running a `get` command displays a list of warnings and highlights missing components. The following image illustrates a basic workflow for a workflow job template:

![Workflow diagram](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-workflow-diagram.png)  


- It is possible to launch several workflows simultaneously, and set a schedule for when to launch them. You can set notifications on workflows, such as when a job completes, similar to that of job templates.


 Note:

Job slicing is intended to scale job executions horizontally.

If you enable job slicing on a job template, it divides the inventory to be acted on in the number of slices configured at launch time. Then starts a job for each slice.

For more information see the Job slicing section.

- You can build a recursive workflow, but if automation controller detects an error, it stops at the time the nested workflow attempts to run.
- Artifacts gathered in jobs in the sub-workflow are passed to downstream nodes.
- An inventory can be set at the workflow level, or prompt for inventory on launch.
- When launched, all job templates in the workflow that have `ask_inventory_on_launch=true` use the workflow level inventory.
- Job templates that do not prompt for inventory ignore the workflow inventory and run against their own inventory.
- If a workflow prompts for inventory, schedules and other workflow nodes can provide the inventory.
- In a workflow convergence scenario, `set_stats` data is merged in an undefined way, therefore you must set unique keys.

## Workflow extra variables

Workflows use surveys to define `extra_vars` for the playbooks within the workflow. These variables are combined with job template data to provide consistent configuration across all spawned jobs.

Workflows use the same behavior (hierarchy) of variable precedence as job templates with the exception of three additional variables. See the [Automation controller Variable Precedence Hierarchy](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_controller_job_template_variables#controller-extra-variables "You can pass extra variables to a automation controller job template in several ways, including through surveys and the API.") in the Extra variables section of Job templates. The three additional variables include:

- Workflow job template extra variables
- Workflow job template survey (defaults)
- Workflow job launch extra variables


Workflows included in a workflow follow the same variable precedence, they only inherit variables if they are specifically prompted for, or defined as part of a survey.

In addition to the workflow `extra_vars`, jobs and workflows run as part of a workflow can inherit variables in the artifacts dictionary of a parent job in the workflow (also combining with ancestors further upstream in its branch).

If you use the `set_stats` module in your playbook, you can produce results that can be consumed downstream by another job.

**Example** Notifying users as to the success or failure of an integration run. In this example, there are two playbooks that can be combined in a workflow to exercise artifact passing:

- invoke_set_stats.yml: first playbook in the workflow:

```
---
- hosts: localhost
  tasks:
    - name: "Artifact integration test results to the web"
      local_action: 'shell curl -F "file=@integration_results.txt" https://file.io'
      register: result


    - name: "Artifact URL of test results to Workflows"
      set_stats:
        data:
          integration_results_url:  "{{ (result.stdout|from_json).link }}"
```


- use_set_stats.yml: second playbook in the workflow:

```
---
- hosts: localhost
  tasks:
    - name: "Get test results from the web"
      uri:
        url: "{{ integration_results_url }}"
        return_content: true
      register: results


    - name: "Output test results"
      debug:
        msg: "{{ results.content }}"
```
The `set_stats` module processes this workflow as follows:

1. The contents of an integration result is uploaded to the web.
2. Through the `invoke_set_stats` playbook, `set_stats` is then invoked to artifact the URL of the uploaded `integration_results.txt` into the Ansible variable `integration_results_url`.
3. The second playbook in the workflow consumes the Ansible extra variable `integration_results_url`. It calls out to the web by using the URI module to get the contents of the file uploaded by the previous job template job. Then, it prints out the contents of the obtained file.


 Note:

For artifacts to work, keep the default setting, `per_host = False` in the `set_stats` module.
