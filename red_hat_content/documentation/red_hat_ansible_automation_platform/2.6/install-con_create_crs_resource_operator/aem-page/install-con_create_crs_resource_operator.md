+++
title = "Create a custom resource for Resource Operator - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_create_crs_resource_operator"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-con_create_crs_resource_operator/aem-page/install-con_create_crs_resource_operator.html"
last_crumb = "Create a custom resource for Resource Operator"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Create a custom resource for Resource Operator"
oversized = "false"
page_slug = "install-con_create_crs_resource_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-con_create_crs_resource_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-con_create_crs_resource_operator/toc/toc.json"
type = "aem-page"
+++

# Create a custom resource for Resource Operator

Use the Resource Operator to manage Ansible Automation Platform resources directly from your Kubernetes cluster. This section provides the procedures for creating custom resources like **AnsibleJob**, **JobTemplate**, **AnsibleProject**, and more.

## Create an AnsibleJob custom resource

An AnsibleJob custom resource launches a job in the Ansible Automation Platform instance specified in the Kubernetes secret (automation controller host URL, token). You can launch an automation job on automation controller by creating an AnsibleJob resource.

### About this task

### Procedure

1.  Specify the connection secret and job template you want to launch.

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleJob
metadata:
  generateName: demo-job-1 # generate a unique suffix per 'kubectl create'
spec:
  connection_secret: aap-access
  job_template_name: Demo Job Template
```

2.  Configure features such as, inventory, extra variables, and time to live for the job.

```
spec:
  connection_secret: aap-access
  job_template_name: Demo Job Template
  inventory: Demo Inventory                    # Inventory prompt on launch needs to be enabled
  runner_image: quay.io/ansible/controller-resource-runner
  runner_version: latest
  job_ttl: 100
  extra_vars:                                  # Extra variables prompt on launch needs to be enabled
     test_var: test
  job_tags: "provision,install,configuration"  # Specify tags to run
  skip_tags: "configuration,restart"           # Skip tasks with a given tag
```
  Note:
      You must enable prompt on launch for inventories and extra variables if you are configuring those. To enable **Prompt on launch**, within the automation controller UI: From the Resources> (and then)Templates page, select your template and select the **Prompt on launch** checkbox next to **Inventory** and **Variables** sections.

3.  Launch a workflow job template with an AnsibleJob object by specifying the `workflow_template_name` instead of `job_template_name`:
  

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleJob
metadata:
  generateName: demo-job-1 # generate a unique suffix per 'kubectl create'
spec:
  connection_secret: aap-access
  workflow_template_name: Demo Workflow Template
```

## Create a JobTemplate custom resource

A job template is a definition and set of parameters for running an Ansible job. For more information see [Standardize and streamline automation with automation job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_job_templates "You can create both Job templates and Workflow job templates from Automation Execution > Templates .").

### About this task

### Procedure

 Create a job template on automation controller by creating a JobTemplate custom resource:

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

## Create an automation controller project custom resource

A Project is a logical collection of Ansible playbooks, represented in automation controller. For more information see [Logically group playbooks with projects](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_controller_projects "A project is a logical collection of Ansible playbooks, represented in automation controller.").

### About this task

### Procedure

 Create a project on automation controller by creating an automation controller project custom resource:

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleProject
metadata:
  name: git
spec:
  repo: https://github.com/ansible/ansible-tower-samples
  branch: main
  name: ProjectDemo-git
  scm_type: git
  organization: Default
  description: demoProject
  connection_secret: aap-access
  runner_pull_policy: IfNotPresent
```

## Create an automation controller schedule custom resource

Define an `AnsibleSchedule` custom resource to create a schedule on the automation controller, ensuring you specify the necessary `apiVersion`, `kind`, and a unique `metadata.name`.

### About this task

### Procedure

 Create a schedule on automation controller by creating an automation controller schedule custom resource:

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleSchedule
metadata:
  name: schedule
spec:
  connection_secret: aap-access
  runner_pull_policy: IfNotPresent
  name: "Demo Schedule"
  rrule: "DTSTART:20210101T000000Z RRULE:FREQ=DAILY;INTERVAL=1;COUNT=1"
  unified_job_template: "Demo Job Template"
```

## Create an automation controller workflow custom resource

Workflows enable you to configure a sequence of disparate job templates (or workflow templates) that may or may not share inventory, playbooks, or permissions. For more information see [Workflows in automation controller](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_workflows#controller-workflows "Workflows enable you to configure a sequence of disparate job templates (or workflow templates) that might or might not share inventory, playbooks, or permissions.") .

### About this task

### Procedure

 Create a workflow on automation controller by creating a workflow custom resource:

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleWorkflow
metadata:
  name: workflow
spec:
  inventory: Demo Inventory
  workflow_template_name: Demo Job Template
  connection_secret: aap-access
  runner_pull_policy: IfNotPresent
```

## Create an automation controller workflow template custom resource

A workflow job template links together a sequence of disparate resources to track the full set of jobs that were part of the release process as a single unit.

### About this task

For more information see [Workflow job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_workflow_job_templates "A workflow job template links together a sequence of disparate resources that tracks the full set of jobs that were part of the release process as a single unit.") .

### Procedure

 Create a workflow template on automation controller by creating a workflow template custom resource:

```
apiVersion: tower.ansible.com/v1alpha1
kind: WorkflowTemplate
metadata:
  name: workflowtemplate-sample
spec:
  connection_secret: aap-access
  name: ExampleTowerWorkflow
  description: Example Workflow Template
  organization: Default
  inventory: Demo Inventory
  workflow_nodes:
  - identifier: node101
    unified_job_template:
      name: Demo Job Template
      inventory:
        organization:
          name: Default
      type: job_template
  - identifier: node102
    unified_job_template:
      name: Demo Job Template
      inventory:
        organization:
          name: Default
      type: job_template
```

## Create an automation controller inventory custom resource

By using an inventory file, Ansible Automation Platform can manage a large number of hosts with a single command.

### About this task

Inventories also help you use Ansible Automation Platform more efficiently by reducing the number of command line options you have to specify. For more information see [Inventories](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_inventories "Ansible Automation Platform works against a list of managed nodes or hosts in your infrastructure that are logically organized, using an inventory file. The installer inventory can specify your installation scenario and describe host deployments to Ansible.") .

### Procedure

 Create an inventory on automation controller by creating an inventory custom resource:

```
metadata:
  name: inventory-new
spec:
  connection_secret: aap-access
  description: my new inventory
  name: newinventory
  organization: Default
  state: present
  instance_groups:
    - default
  variables:
    string: "string_value"
    bool: true
    number: 1
    list:
      - item1: true
      - item2: "1"
    object:
      string: "string_value"
      number: 2
```

## Create an automation controller credential custom resource

Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.

### About this task

SSH and AWS are the most commonly used credentials. For a full list of supported credentials see[Credential types](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_credential_types "Ansible Automation Platform supports a number of credential types.") .

For help with defining values you can refer to the [OpenAPI (Swagger) file for Red Hat Ansible Automation Platform API](https://access.redhat.com/login?redirectTo=https%3A%2F%2Faccess.redhat.com%2Fsolutions%2F7050627) KCS article.

Note:

You can use `https://<aap-instance>/api/controller/v2/credential_types/` to view the list of credential types on your instance. To get the full list use the following `curl` command:

```
export AAP_TOKEN="your-oauth2-token"
export AAP_URL="https://your-aap-controller.example.com"

curl -s -H "Authorization: Bearer $AAP_TOKEN" "$AAP_URL/api/controller/v2/credential_types/" | jq -r '.results[].name'
```

### Procedure

 Create an AWS or SSH credential on automation controller by creating a credential custom resource:

- SSH credential:

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleCredential
metadata:
  name: ssh-cred
spec:
  name: ssh-cred
  organization: Default
  connection_secret: aap-access
  description: "SSH credential"
  type: "Machine"
  ssh_username: "cat"
  ssh_secret: my-ssh-secret
  runner_pull_policy: IfNotPresent
```

- AWS credential:

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleCredential
metadata:
  name: aws-cred
spec:
  name: aws-access
  organization: Default
  connection_secret: aap-access
  description: "This is a test credential"
  type: "Amazon Web Services"
  username_secret: aws-secret
  password_secret: aws-secret
  runner_pull_policy: IfNotPresent
```
