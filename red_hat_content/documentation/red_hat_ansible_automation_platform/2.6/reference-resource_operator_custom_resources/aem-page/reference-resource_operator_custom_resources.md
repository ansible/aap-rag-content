+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-resource_operator_custom_resources"
title = "Resource Operator custom resources - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-ansible_automation_platform_custom_resources/", "Ansible Automation Platform custom resources"]]
category = "Reference"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/reference-resource_operator_custom_resources/aem-page/reference-resource_operator_custom_resources.html"
last_crumb = "Resource Operator custom resources"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Resource Operator custom resources"
oversized = "false"
page_slug = "reference-resource_operator_custom_resources"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/reference-resource_operator_custom_resources"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/reference-resource_operator_custom_resources/toc/toc.json"
type = "aem-page"
+++

# Resource Operator custom resources

The Resource Operator provides custom resources that enable you to manage automation controller resources directly from your Kubernetes cluster using a declarative, GitOps-compatible workflow.

Resource Operator custom resources connect to the platform gateway to create and manage automation resources such as jobs, templates, projects, inventories, credentials, schedules, and workflows. All Resource Operator custom resources require a `connection_secret` that references a Kubernetes secret containing the platform gateway URL and an OAuth2 token.

By defining automation resources as Kubernetes custom resources, you can manage them alongside your other cluster resources using standard Kubernetes tools and practices, including version control and continuous delivery pipelines.

## Resource Operator custom resources [tower.ansible.com/v1alpha1]

The Resource Operator custom resources enable you to manage automation controller resources directly from your Kubernetes cluster. These custom resources connect to the platform gateway to create and manage jobs, templates, projects, inventories, credentials, schedules, and workflows.

### Connection secret

All Resource Operator custom resources require a `connection_secret` field that references a Kubernetes secret containing the platform gateway URL and an OAuth2 token. Create this secret before using any Resource Operator custom resources.

```
apiVersion: v1
kind: Secret
metadata:
  name: aap-access
  type: Opaque
stringData:
  token: <generated-token>
  host: https://my-aap-gateway.example.com/
```

### AnsibleJob

Launches a job or workflow job template on the automation controller instance specified in the connection secret.

| Field                    | Type    | Description                                                                                              | Default |
| ------------------------ | ------- | -------------------------------------------------------------------------------------------------------- | ------- |
| `connection_secret`      | String  | Name of the Kubernetes secret containing the platform gateway connection details. Required.              | -       |
| `job_template_name`      | String  | Name of the job template to launch. Specify either this or `workflow_template_name`.                     | -       |
| `workflow_template_name` | String  | Name of the workflow job template to launch. Specify either this or `job_template_name`.                 | -       |
| `inventory`              | String  | Name of the inventory to use. Prompt on launch must be enabled on the template.                          | -       |
| `extra_vars`             | Object  | Extra variables to pass to the job as key-value pairs. Prompt on launch must be enabled on the template. | -       |
| `job_tags`               | String  | Comma-separated list of tags to run, for example `"provision,install,configuration"`.                    | -       |
| `skip_tags`              | String  | Comma-separated list of tags to skip, for example `"configuration,restart"`.                             | -       |
| `runner_image`           | String  | Container image for the runner pod.                                                                      | -       |
| `runner_version`         | String  | Version of the runner image to use.                                                                      | -       |
| `job_ttl`                | Integer | Time to live in seconds for the job resource after completion.                                           | -       |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleJob
metadata:
  generateName: demo-job-1
spec:
  connection_secret: aap-access
  job_template_name: Demo Job Template
  inventory: Demo Inventory
  extra_vars:
    test_var: test
  job_tags: "provision,install"
```

### JobTemplate

Creates a job template on the automation controller.

| Field                    | Type   | Description                                                                                 | Default |
| ------------------------ | ------ | ------------------------------------------------------------------------------------------- | ------- |
| `connection_secret`      | String | Name of the Kubernetes secret containing the platform gateway connection details. Required. | -       |
| `job_template_name`      | String | Name of the job template to create.                                                         | -       |
| `job_template_project`   | String | Name of the project to associate with the job template.                                     | -       |
| `job_template_playbook`  | String | Name of the playbook file to run.                                                           | -       |
| `job_template_inventory` | String | Name of the inventory to associate with the job template.                                   | -       |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: JobTemplate
metadata:
  name: jobtemplate-4
spec:
  connection_secret: aap-access
  job_template_name: ExampleJobTemplate4
  job_template_project: Demo Project
  job_template_playbook: hello_world.yml
  job_template_inventory: Demo Inventory
```

### AnsibleProject

Creates a project (a logical collection of Ansible playbooks) on the automation controller.

| Field                | Type   | Description                                                                                 | Default        |
| -------------------- | ------ | ------------------------------------------------------------------------------------------- | -------------- |
| `connection_secret`  | String | Name of the Kubernetes secret containing the platform gateway connection details. Required. | -              |
| `repo`               | String | URL of the source control repository.                                                       | -              |
| `branch`             | String | Branch of the source control repository to use.                                             | -              |
| `name`               | String | Display name for the project in the automation controller.                                  | -              |
| `scm_type`           | String | Source control type, for example `git`.                                                     | -              |
| `organization`       | String | Organization the project belongs to.                                                        | -              |
| `description`        | String | Description of the project.                                                                 | -              |
| `runner_pull_policy` | String | Image pull policy for the runner pod. Options: `Always`, `Never`, `IfNotPresent`.           | `IfNotPresent` |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleProject
metadata:
  name: git
spec:
  connection_secret: aap-access
  repo: https://github.com/ansible/ansible-tower-samples
  branch: main
  name: ProjectDemo-git
  scm_type: git
  organization: Default
```

### AnsibleInventory

Creates an inventory on the automation controller.

| Field               | Type   | Description                                                                                             | Default   |
| ------------------- | ------ | ------------------------------------------------------------------------------------------------------- | --------- |
| `connection_secret` | String | Name of the Kubernetes secret containing the platform gateway connection details. Required.             | -         |
| `name`              | String | Display name for the inventory.                                                                         | -         |
| `description`       | String | Description of the inventory.                                                                           | -         |
| `organization`      | String | Organization the inventory belongs to.                                                                  | -         |
| `state`             | String | Desired state of the inventory. Options: `present`, `absent`.                                           | `present` |
| `instance_groups`   | Array  | List of instance groups to associate with the inventory.                                                | -         |
| `variables`         | Object | Inventory variables as key-value pairs. Supports strings, booleans, numbers, lists, and nested objects. | -         |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleInventory
metadata:
  name: inventory-new
spec:
  connection_secret: aap-access
  name: newinventory
  organization: Default
  state: present
  variables:
    env: production
    region: us-east-1
```

### AnsibleCredential

Creates a credential on the automation controller for authenticating with external systems.

| Field                | Type   | Description                                                                                 | Default        |
| -------------------- | ------ | ------------------------------------------------------------------------------------------- | -------------- |
| `connection_secret`  | String | Name of the Kubernetes secret containing the platform gateway connection details. Required. | -              |
| `name`               | String | Display name for the credential.                                                            | -              |
| `organization`       | String | Organization the credential belongs to.                                                     | -              |
| `description`        | String | Description of the credential.                                                              | -              |
| `type`               | String | Credential type, for example `Machine`, `Amazon Web Services`.                              | -              |
| `ssh_username`       | String | SSH username for Machine type credentials.                                                  | -              |
| `ssh_secret`         | String | Name of a Kubernetes secret containing the SSH private key for Machine type credentials.    | -              |
| `username_secret`    | String | Name of a Kubernetes secret containing the username for cloud credentials.                  | -              |
| `password_secret`    | String | Name of a Kubernetes secret containing the password for cloud credentials.                  | -              |
| `runner_pull_policy` | String | Image pull policy for the runner pod.                                                       | `IfNotPresent` |


**Example (SSH):**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleCredential
metadata:
  name: ssh-cred
spec:
  connection_secret: aap-access
  name: ssh-cred
  organization: Default
  type: "Machine"
  ssh_username: "ansible"
  ssh_secret: my-ssh-secret
```

### AnsibleSchedule

Creates a schedule on the automation controller to run a job template at specified intervals.

| Field                  | Type   | Description                                                                                                                                  | Default        |
| ---------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `connection_secret`    | String | Name of the Kubernetes secret containing the platform gateway connection details. Required.                                                  | -              |
| `name`                 | String | Display name for the schedule.                                                                                                               | -              |
| `rrule`                | String | Recurrence rule in iCalendar RRULE format defining the schedule, for example `DTSTART:20210101T000000Z RRULE:FREQ=DAILY;INTERVAL=1;COUNT=1`. | -              |
| `unified_job_template` | String | Name of the job template or workflow to schedule.                                                                                            | -              |
| `runner_pull_policy`   | String | Image pull policy for the runner pod.                                                                                                        | `IfNotPresent` |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleSchedule
metadata:
  name: schedule
spec:
  connection_secret: aap-access
  name: "Demo Schedule"
  rrule: "DTSTART:20210101T000000Z RRULE:FREQ=DAILY;INTERVAL=1;COUNT=1"
  unified_job_template: "Demo Job Template"
```

### AnsibleWorkflow

Creates a workflow on the automation controller.

| Field                    | Type   | Description                                                                                 | Default        |
| ------------------------ | ------ | ------------------------------------------------------------------------------------------- | -------------- |
| `connection_secret`      | String | Name of the Kubernetes secret containing the platform gateway connection details. Required. | -              |
| `workflow_template_name` | String | Name of the workflow template.                                                              | -              |
| `inventory`              | String | Name of the inventory to associate with the workflow.                                       | -              |
| `runner_pull_policy`     | String | Image pull policy for the runner pod.                                                       | `IfNotPresent` |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleWorkflow
metadata:
  name: workflow
spec:
  connection_secret: aap-access
  workflow_template_name: Demo Job Template
  inventory: Demo Inventory
```

### WorkflowTemplate

Creates a workflow job template that links together a sequence of job templates on the automation controller.

| Field               | Type   | Description                                                                                                                                                               | Default |
| ------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `connection_secret` | String | Name of the Kubernetes secret containing the platform gateway connection details. Required.                                                                               | -       |
| `name`              | String | Display name for the workflow template.                                                                                                                                   | -       |
| `description`       | String | Description of the workflow template.                                                                                                                                     | -       |
| `organization`      | String | Organization the workflow template belongs to.                                                                                                                            | -       |
| `inventory`         | String | Default inventory for the workflow template.                                                                                                                              | -       |
| `workflow_nodes`    | Array  | List of workflow nodes defining the sequence of jobs. Each node contains an `identifier` and a `unified_job_template` object with `name`, `type`, and `inventory` fields. | -       |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: WorkflowTemplate
metadata:
  name: workflowtemplate-sample
spec:
  connection_secret: aap-access
  name: ExampleWorkflow
  organization: Default
  inventory: Demo Inventory
  workflow_nodes:
  - identifier: node101
    unified_job_template:
      name: Demo Job Template
      type: job_template
  - identifier: node102
    unified_job_template:
      name: Demo Job Template
      type: job_template
```

### AnsibleInstanceGroup

Creates an instance group on the automation controller for organizing and managing execution capacity.

| Field                | Type   | Description                                                                                 | Default        |
| -------------------- | ------ | ------------------------------------------------------------------------------------------- | -------------- |
| `connection_secret`  | String | Name of the Kubernetes secret containing the platform gateway connection details. Required. | -              |
| `name`               | String | Display name for the instance group.                                                        | -              |
| `runner_pull_policy` | String | Image pull policy for the runner pod.                                                       | `IfNotPresent` |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleInstanceGroup
metadata:
  name: my-instance-group
spec:
  connection_secret: aap-access
  name: production-instances
```
