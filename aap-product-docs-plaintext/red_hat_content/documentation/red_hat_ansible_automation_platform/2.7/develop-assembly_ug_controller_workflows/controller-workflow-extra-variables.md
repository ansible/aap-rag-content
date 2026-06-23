# Understand how to configure workflows
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
