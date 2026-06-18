+++
title = "Policy enforcement input and output options - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-ref_pac_inputs_outputs"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-integrate_with_the_external_policy_engine_open_policy_agent__opa_/", "Integrate with the external policy engine Open Policy Agent (OPA)"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-ref_pac_inputs_outputs/aem-page/integrate-ref_pac_inputs_outputs.html"
last_crumb = "Policy enforcement input and output options"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Policy enforcement input and output options"
oversized = "false"
page_slug = "integrate-ref_pac_inputs_outputs"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-ref_pac_inputs_outputs"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-ref_pac_inputs_outputs/toc/toc.json"
type = "aem-page"
+++

# Policy enforcement input and output options

Use the following inputs and outputs to craft policies for use in policy enforcement.

*Table 1. Input data*

| **Input**                    | **Type**                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `id`                    | <br>Integer             | <br>The job’s unique identifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <br> `name`                  | <br>String              | <br>Job template name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <br> `created`               | <br>Datetime (ISO 8601) | <br>Timestamp indicating when the job was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <br> `created by`            | <br>Object              | <br>Information about the user who created the job.<br>`id`(integer): Unique identifier for the user`username`(string): creator username`is_superuser`(boolean): indicates if the user is a superuser                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <br> `credentials`           | <br>List of objects     | <br>Credentials associated with job execution.<br>`id` (integer): the credential’s unique identifier`name` (string): credential name`description` (string): credential description`organization` (integer or null): organization identifier associated with the credential`credential_type` (integer): credential type identifier`managed` (boolean): indicates if the credential is managed internally`kind` (string): credential type ( such as `ssh`, `cloud`, or `kubernetes`)                                                                                                                                                                                                                                                                                                                        |
| <br> `execution_environment` | <br>Object              | <br>Details about the execution environment used for the job.<br>`id` (integer): the execution environment’s unique identifier`name` (string): execution environment name`image` (string): container image used for execution`pull` (string): pull policy for the execution environment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <br> `extra_vars`            | <br>JSON                | <br>Extra variables provided for job execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <br> `forks`                 | <br>Integer             | <br>The number of parallel processes used for job execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <br> `hosts_count`           | <br>Integer             | <br>The number of hosts targeted by the job.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <br> `instance_group`        | <br>Object              | <br>Information about the instance group handling the job, including:<br>`id` (integer): the instance group’s unique identifier`name` (string): the instance group name`capacity` (integer): the available capacity in the group`jobs_running` (integer): the number of currently running jobs`jobs_total` (integer): total jobs handled by the group`max_concurrent_jobs` (integer): maximum concurrent jobs allowed`max_forks` (integer): maximum forks allowed                                                                                                                                                                                                                                                                                                                                         |
| <br> `inventory`             | <br>Object              | <br>Inventory details used in the job execution, including:<br>`id` (integer): the inventory’s unique identifier`name` (string): The inventory’s name`description` (string): inventory description`kind` (string): the inventory type`total_hosts` (integer): the total number of hosts in the inventory`total_groups` (integer): the total number of groups in the inventory`has_inventory_sources` (boolean): indicates if the inventory has external sources`total_inventory_sources` (integer): the number of external inventory sources`has_active_failures` (boolean): indicates if there are active failures in the inventory`hosts_with_active_failures` (boolean): the number of hosts with active failures`inventory_sources` (array): external inventory sources associated with the inventory |
| <br> `job_template`          | <br>Object              | <br>Information about the job template, including:<br>`id` (integer): the job template’s unique identifier`name` (string): the job template’s name`job_type` (string): type of job (for example, `run`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <br> `job_type`              | <br>Choice (String)     | <br>Type of job execution. Allowed values are:<br> `run` `check` `scan`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <br> `job_type_name`         | <br>String              | <br>Human-readable name for the job type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <br> `labels`                | <br>List of objects     | <br>Labels associated with the job, including:<br>`id` (integer): the label’s unique identifier`name` (string): the label name`organization` (object): the organization associated with the label     `id` (integer): the organization’s unique identifier  `name` (string): the organization name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <br> `launch_type`           | <br>Choice (String)     | <br>How the job was launched. Allowed values include:<br>`manual`: manual`relaunch`: relaunch`callback`: callback`scheduled`: scheduled`dependency`: dependency`workflow`: workflow`webhook`: webhook`sync`: sync`scm`: SCM update                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <br> `limit`                 | <br>String              | <br>The limit applied to the job execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <br> `launched_by`           | <br>Object              | <br>Information about the user who launched the job, including:<br>`id` (integer): the user’s unique identifier`name` (string): the user name`type` (type): the user type (for example, `user` or `system`)`url` (string): the user’s API URL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <br> `organization`          | <br>Object              | <br>Information about the organization associated with the job, including:<br>`id` (integer): the organization’s unique identifier`name` (name): the organization’s name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <br> `playbook`              | <br>String              | <br>The playbook used in the job execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <br> `project`               | <br>Object              | <br>Details about the project associated with the job, including:<br>`id` (integer): the project’s unique identifier`name` (string): the project name`status` (choice-string): the project status     `successful`: Successful  `failed`: failed  `error`: error `scm_type`(string): source control type (such as`git`, or `svn`)`scm_url` (string): the source control repository URL`scm_branch` (string): the branch used in the repository`scm_refspec` (string): RefSpec for the repository`scm_clean` (boolean): whether the SCM is cleaned before updates`scm_track_submodules` (boolean): whether submodules are tracked`scm_delete_on_update` (boolean): whether SCM deletes files on update                                                                                                     |
| <br> `scm_branch`            | <br>String              | <br>The specific branch to use for SCM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <br> `scm_revision`          | <br>String              | <br>SCM revision used for the job.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <br> `workflow_job`          | <br>Object              | <br>Workflow job details, if the job is part of a workflow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <br> `workflow_job_template` | <br>Object              | <br>Workflow job template details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |


The following code block shows example input data from a demo job template launch:

```rego
{
  "id": 70,
  "name": "Demo Job Template",
  "created": "2025-03-19T19:07:03.329426Z",
  "created_by": {
    "id": 1,
    "username": "admin",
    "is_superuser": true,
    "teams": []
  },
  "credentials": [
    {
      "id": 3,
      "name": "Example Machine Credential",
      "description": "",
      "organization": null,
      "credential_type": 1,
      "managed": false,
      "kind": "ssh",
      "cloud": false,
      "kubernetes": false
    }
  ],
  "execution_environment": {
    "id": 2,
    "name": "Default execution environment",
    "image": "registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:b9f60d9ebbbb5fdc394186574b95dea5763b045ceff253815afeb435c626914d",
    "pull": ""
  },
  "extra_vars": {
    "example": "value"
  },
  "forks": 0,
  "hosts_count": 0,
  "instance_group": {
    "id": 2,
    "name": "default",
    "capacity": 0,
    "jobs_running": 1,
    "jobs_total": 38,
    "max_concurrent_jobs": 0,
    "max_forks": 0
  },
  "inventory": {
    "id": 1,
    "name": "Demo Inventory",
    "description": "",
    "kind": "",
    "total_hosts": 1,
    "total_groups": 0,
    "has_inventory_sources": false,
    "total_inventory_sources": 0,
    "has_active_failures": false,
    "hosts_with_active_failures": 0,
    "inventory_sources": []
  },
  "job_template": {
    "id": 7,
    "name": "Demo Job Template",
    "job_type": "run"
  },
  "job_type": "run",
  "job_type_name": "job",
  "labels": [
    {
      "id": 1,
      "name": "Demo label",
      "organization": {
        "id": 1,
        "name": "Default"
      }
    }
  ],
  "launch_type": "workflow",
  "limit": "",
  "launched_by": {
    "id": 1,
    "name": "admin",
    "type": "user",
    "url": "/api/v2/users/1/"
  },
  "organization": {
    "id": 1,
    "name": "Default"
  },
  "playbook": "hello_world.yml",
  "project": {
    "id": 6,
    "name": "Demo Project",
    "status": "successful",
    "scm_type": "git",
    "scm_url": "https://github.com/ansible/ansible-tower-samples",
    "scm_branch": "",
    "scm_refspec": "",
    "scm_clean": false,
    "scm_track_submodules": false,
    "scm_delete_on_update": false
  },
  "scm_branch": "",
  "scm_revision": "",
  "workflow_job": {
    "id": 69,
    "name": "Demo Workflow"
  },
  "workflow_job_template": {
    "id": 10,
    "name": "Demo Workflow",
    "job_type": null
  }
}
```

*Table 2. Output data*

| **Input**         | **Type**            | **Description**                               |
| ----------------- | ------------------- | --------------------------------------------- |
| <br> `allowed`    | <br>Boolean         | <br>Indicates whether the action is permitted |
| <br> `violations` | <br>List of strings | <br>Reasons why the action is not permitted   |


The following code block shows an example of expected output from the OPA policy query:

```rego
{
  "allowed": false,
  "violations": [
    "No job execution is allowed",
    ...
  ],
  ...
}
```
