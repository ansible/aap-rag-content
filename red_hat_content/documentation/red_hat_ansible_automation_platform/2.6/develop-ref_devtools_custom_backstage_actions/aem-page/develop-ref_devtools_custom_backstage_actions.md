+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_devtools_custom_backstage_actions"
template = "docs/aem-title.html"
title = "Custom Backstage actions - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_devtools_custom_backstage_actions/aem-page/develop-ref_devtools_custom_backstage_actions.html"
last_crumb = "Custom Backstage actions"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Custom Backstage actions"
oversized = "false"
page_slug = "develop-ref_devtools_custom_backstage_actions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_devtools_custom_backstage_actions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_devtools_custom_backstage_actions/toc/toc.json"
type = "aem-page"
+++

# Custom Backstage actions

The following actions enable you to manage Ansible Automation Platform resources within a software template workflow.

## `rhaap:create-project`

Create an Ansible Automation Platform project that links to a source control repository containing Ansible content.

 **Input parameters**

| Parameter            | Type        | Required | Description                                                                                   |
| -------------------- | ----------- | -------- | --------------------------------------------------------------------------------------------- |
| <br> `token`         | <br>string  | <br>Yes  | <br>OAuth2 token for Ansible Automation Platform authentication.                              |
| <br> `deleteIfExist` | <br>boolean | <br>No   | <br>If `true`, the action deletes the project if it already exists before creating a new one. |
| <br> `values`        | <br>object  | <br>Yes  | <br>The project configuration object. See the "values" Object Structure table.                |


 **“values” Object Structure**

| Field                     | Type        | Required | Description                                                                                                   |
| ------------------------- | ----------- | -------- | ------------------------------------------------------------------------------------------------------------- |
| <br> `projectName`        | <br>string  | <br>Yes  | <br>Name of the project.                                                                                      |
| <br> `projectDescription` | <br>string  | <br>No   | <br>Description of the project.                                                                               |
| <br> `organization`       | <br>object  | <br>Yes  | <br>Organization object with `id` (number, required) and `name` (string, optional).                           |
| <br> `credentials`        | <br>object  | <br>No   | <br>Credential object with `id` (number, required), `name` (string, optional), and `kind` (string, optional). |
| <br> `scmUrl`             | <br>string  | <br>Yes  | <br>Source control URL (for example, GitHub/GitLab repository URL).                                           |
| <br> `scmBranch`          | <br>string  | <br>No   | <br>Source control branch, tag, or commit.                                                                    |
| <br> `scmUpdateOnLaunch`  | <br>boolean | <br>No   | <br>If `true`, updates the project revision before each job run.                                              |


 **Output parameters**

| Parameter                  | Type       | Description                                          |
| -------------------------- | ---------- | ---------------------------------------------------- |
| <br> `project`             | <br>object | <br>Created project details.                         |
| <br> `project.id`          | <br>number | <br>Project ID in Ansible Automation Platform (AAP). |
| <br> `project.name`        | <br>string | <br>Project name.                                    |
| <br> `project.description` | <br>string | <br>Project description.                             |
| <br> `project.url`         | <br>string | <br>Ansible Automation Platform URL for the project. |


 **Example**

```
steps:
  - id: create-aap-project
    name: Create AAP Project
    action: rhaap:create-project
    input:
      token: ${{ parameters.AAP_TOKEN }}
      deleteIfExist: true
      values:
        projectName: ${{ parameters.projectName }}
        organization: ${{ parameters.organization }}
        scmUrl: https://github.com/my-org/ansible-playbooks
        scmBranch: main
        scmUpdateOnLaunch: true
        credentials: GitHub Token
```

## `rhaap:create-execution-environment`

Create an execution environment in Ansible Automation Platform that defines the container image used to run Ansible jobs.

 **Input parameters**

| Parameter            | Type        | Required | Description                                                                       |
| -------------------- | ----------- | -------- | --------------------------------------------------------------------------------- |
| <br> `token`         | <br>string  | <br>Yes  | <br>OAuth2 token for Ansible Automation Platform authentication.                  |
| <br> `deleteIfExist` | <br>boolean | <br>No   | <br>If `true`, the action deletes the execution environment if it already exists. |
| <br> `values`        | <br>object  | <br>Yes  | <br>The execution environment configuration object.                               |


 **“values” Object Structure**

| Field                         | Type       | Required | Description                                                                                                          |
| ----------------------------- | ---------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
| <br> `environmentName`        | <br>string | <br>Yes  | <br>Name of the execution environment.                                                                               |
| <br> `environmentDescription` | <br>string | <br>No   | <br>Description of the execution environment.                                                                        |
| <br> `organization`           | <br>object | <br>Yes  | <br>Organization object with required `id` (number) and optional `name` (string).                                    |
| <br> `image`                  | <br>string | <br>Yes  | <br>Full image location, including registry, image name, and tag (for example, `quay.io/ansible/creator-ee:latest`). |
| <br> `pull`                   | <br>string | <br>No   | <br>Image pull policy: `always`, `missing`, or `never`. Default is `missing`.                                        |


 **Output parameters**

| Parameter                               | Type       | Description                                                              |
| --------------------------------------- | ---------- | ------------------------------------------------------------------------ |
| <br> `executionEnvironment`             | <br>object | <br>Created execution environment details.                               |
| <br> `executionEnvironment.id`          | <br>number | <br>Execution environment ID.                                            |
| <br> `executionEnvironment.name`        | <br>string | <br>Execution environment name.                                          |
| <br> `executionEnvironment.description` | <br>string | <br>Execution environment description.                                   |
| <br> `executionEnvironment.url`         | <br>string | <br>Ansible Automation Platform (AAP) URL for the execution environment. |


 **Example**

```
steps:
  - id: create-ee
    name: Create Execution Environment
    action: rhaap:create-execution-environment
    input:
      token: ${{ parameters.AAP_TOKEN }}
      deleteIfExist: false
      values:
        environmentName: Custom EE
        environmentDescription: Execution environment with custom collections
        organization: ${{ parameters.organization }}
        image: quay.io/ansible/creator-ee:v0.16.0
        pull: missing
```

## `rhaap:create-job-template`

Create a job template in Ansible Automation Platform that defines a reusable configuration for running Ansible playbooks.

 **Input parameters**

| Parameter            | Type        | Required | Description                                                              |
| -------------------- | ----------- | -------- | ------------------------------------------------------------------------ |
| <br> `token`         | <br>string  | <br>Yes  | <br>OAuth2 token for Ansible Automation Platform authentication.         |
| <br> `deleteIfExist` | <br>boolean | <br>No   | <br>If `true`, the action deletes the job template if it already exists. |
| <br> `values`        | <br>object  | <br>Yes  | <br>The job template configuration object.                               |


 **“values” Object Structure**

| Field                       | Type       | Required | Description                                                                                |
| --------------------------- | ---------- | -------- | ------------------------------------------------------------------------------------------ |
| <br> `templateName`         | <br>string | <br>Yes  | <br>Name of the job template.                                                              |
| <br> `templateDescription`  | <br>string | <br>No   | <br>Description of the job template.                                                       |
| <br> `project`              | <br>object | <br>Yes  | <br>Project object with required `id` (number) and optional `name` (string).               |
| <br> `organization`         | <br>object | <br>No   | <br>Organization object with `id` (number, required) and `name` (string, optional).        |
| <br> `jobInventory`         | <br>object | <br>Yes  | <br>Inventory object with required `id` (number) and optional `name` (string).             |
| <br> `playbook`             | <br>string | <br>Yes  | <br>Path to the playbook file to execute.                                                  |
| <br> `templateDescription`  | <br>string | <br>No   | <br>Description of the job template.                                                       |
| <br> `scmType`              | <br>string | <br>No   | <br>Source control type (for example, `Github` or `Gitlab`).                               |
| <br> `executionEnvironment` | <br>object | <br>No   | <br>Execution environment object with required `id` (number) and optional `name` (string). |
| <br> `extraVariables`       | <br>object | <br>No   | <br>Extra variables to pass to the playbook (key-value pairs).                             |


 **Output parameters**

| Parameter                   | Type       | Description                                                     |
| --------------------------- | ---------- | --------------------------------------------------------------- |
| <br> `template`             | <br>object | <br>Created job template details.                               |
| <br> `template.id`          | <br>number | <br>Job template ID.                                            |
| <br> `template.name`        | <br>string | <br>Job template name.                                          |
| <br> `template.description` | <br>string | <br>Job template description.                                   |
| <br> `template.url`         | <br>string | <br>Ansible Automation Platform (AAP) URL for the job template. |


 **Example**

```
steps:
  - id: create-job-template
    name: Create Job Template
    action: rhaap:create-job-template
    input:
      token: ${{ parameters.AAP_TOKEN }}
      deleteIfExist: true
      values:
        templateName: Deploy Application
        templateDescription: Deploys the application to production
        project: ${{ steps['create-aap-project'].output.project }}
        organization: ${{ parameters.organization }}
        jobInventory: ${{ parameters.jobInventory }}
        playbook: deploy.yml
        executionEnvironment: ${{ steps['create-ee'].output.executionEnvironment }}
        extraVariables:
          app_version: 1.0.0
          environment: production
```

## `rhaap:launch-job-template`

Launch an existing job template in Ansible Automation Platform.

 **Input parameters**

| Parameter     | Type       | Required | Description                                                      |
| ------------- | ---------- | -------- | ---------------------------------------------------------------- |
| <br> `token`  | <br>string | <br>Yes  | <br>OAuth2 token for Ansible Automation Platform authentication. |
| <br> `values` | <br>object | <br>Yes  | <br>The job launch configuration object.                         |


 **“values” Object Structure**

| Field                       | Type        | Required | Description                                                                |
| --------------------------- | ----------- | -------- | -------------------------------------------------------------------------- |
| <br> `template`             | <br>string  | <br>Yes  | <br>Job template name to launch.                                           |
| <br> `inventory`            | <br>object  | <br>No   | <br>Override inventory with `id` (number) and `name` (string).             |
| <br> `credentials`          | <br>array   | <br>No   | <br>Array of credential objects to use.                                    |
| <br> `extraVariables`       | <br>object  | <br>No   | <br>Extra variables to pass to the job (key-value pairs).                  |
| <br> `limit`                | <br>string  | <br>No   | <br>Host pattern to constrain which hosts the job runs against.            |
| <br> `jobType`              | <br>string  | <br>No   | <br>Job type: `run` or `check`.                                            |
| <br> `executionEnvironment` | <br>object  | <br>No   | <br>Override execution environment with `id` (number) and `name` (string). |
| <br> `verbosity`            | <br>object  | <br>No   | <br>Verbosity level object with `id` and `name`.                           |
| <br> `forks`                | <br>number  | <br>No   | <br>Number of parallel processes (default: `5`).                           |
| <br> `jobSliceCount`        | <br>number  | <br>No   | <br>Divide the job into N slices.                                          |
| <br> `timeout`              | <br>number  | <br>No   | <br>Job timeout in seconds (`0` = no timeout).                             |
| <br> `diffMode`             | <br>boolean | <br>No   | <br>Enable diff mode to show changes.                                      |
| <br> `jobTags`              | <br>string  | <br>No   | <br>Comma-separated tags to run only specific tasks.                       |
| <br> `skipTags`             | <br>string  | <br>No   | <br>Comma-separated tags to skip specific tasks.                           |


 **Output parameters**

| Parameter          | Type       | Description                                            |
| ------------------ | ---------- | ------------------------------------------------------ |
| <br> `data`        | <br>object | <br>Job execution details.                             |
| <br> `data.id`     | <br>number | <br>Job ID.                                            |
| <br> `data.status` | <br>string | <br>Job status.                                        |
| <br> `data.url`    | <br>string | <br>Ansible Automation Platform (AAP) URL for the job. |


 **Example**

```
steps:
  - id: launch-job
    name: Launch Job Template
    action: rhaap:launch-job-template
    input:
      token: ${{ parameters.AAP_TOKEN }}
      values:
        template: Deploy Application
        inventory: ${{ parameters.jobInventory }}
        credentials: ${{ parameters.credentials }}
        extraVariables:
          app_version: v1.0.1
          deploy_env: production
        jobType: run
        verbosity: Normal
        diffMode: true
        timeout: 3600
```

## Example with all backstage actions present

The following example displays how you can use multiple actions together.

```
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: ansible-complete-setup
  title: Complete Ansible Setup
  description: Creates an Ansible project, execution environment, job template, and launches it
spec:
  owner: platform-team
  type: service

  parameters:
    - title: Project Information
      required:
        - projectName
        - repoUrl
      properties:
        projectName:
          title: Project Name
          type: string
          description: Name of the Ansible project
        repoUrl:
          title: Repository URL
          type: string
          description: Git repository URL containing Ansible content

    - title: AAP Configuration
      required:
        - organization
        - jobInventory
        - credentials
      properties:
        organization:
          title: Organization
          type: string
          description: AAP Organization name
          default: 1-org
          ui:field: hidden  # To hide this field in the UI
        jobInventory:
          title: Inventory name
          type: string
          description: AAP Inventory name
          resource: inventories
          ui:field: AAPResourcePicker
          default: my-inventory
        credentials:
          title: Credentials
          description: Select SCM credential for Private repositories
          resource: credentials
          ui:field: AAPResourcePicker
          default: my-machine-credential
  steps:
    # Step 1: Create AAP Project
    - id: create-project
      name: Create AAP Project
      action: rhaap:create-project
      input:
        token: ${{ parameters.AAP_TOKEN }}
        deleteIfExist: true
        values:
          projectName: ${{ parameters.projectName }}
          organization: ${{ parameters.organization }}
          scmUrl: ${{ parameters.repoUrl }}
          scmBranch: main
          scmUpdateOnLaunch: true

    # Step 2: Create Execution Environment
    - id: create-ee
      name: Create Execution Environment
      action: rhaap:create-execution-environment
      input:
        token: ${{ parameters.AAP_TOKEN }}
        values:
          environmentName: ${{ parameters.projectName }}-ee
          organization: ${{ parameters.organization }}
          image: quay.io/ansible/creator-ee:latest
          pull: missing

    # Step 3: Create Job Template
    - id: create-template
      name: Create Job Template
      action: rhaap:create-job-template
      input:
        token: ${{ parameters.AAP_TOKEN }}
        values:
          templateName: ${{ parameters.projectName }}-deploy
          templateDescription: Deployment job template
          project: ${{ steps['create-project'].output.project }}
          organization: ${{ parameters.organization }}
          jobInventory: ${{ parameters.jobInventory }}
          playbook: site.yml
          executionEnvironment: ${{ steps['create-ee'].output.executionEnvironment }}

    # Step 4: Launch the Job
    - id: launch-job
      name: Launch Job
      action: rhaap:launch-job-template
      input:
        token: ${{ parameters.AAP_TOKEN }}
        values:
          template: ${{ parameters.projectName }}-deploy
          inventory: ${{ parameters.jobInventory }}
          credentials: ${{ parameters.credentials }}
          jobType: run
          extraVariables:
            created_by: backstage
            timestamp: ${{ '' | now }}

  output:
    links:
      - title: AAP Project
        url: ${{ steps['create-project'].output.project.url }}
      - title: Job Template
        url: ${{ steps['create-template'].output.template.url }}
      - title: Job Execution
        url: ${{ steps['launch-job'].output.data.url }}
```

## rhaap:clean-up

Remove resources created during a software template execution from Ansible Automation Platform. Use this action as a cleanup step to delete projects, execution environments, or job templates.

### Input parameters

| Parameter | Type   | Required | Description                                                  |
| --------- | ------ | -------- | ------------------------------------------------------------ |
| `token`   | string | Yes      | OAuth2 token for Ansible Automation Platform authentication. |
| `values`  | object | Yes      | Object specifying which resources to remove.                 |

### values object structure

| Field                  | Type   | Required | Description                                                                    |
| ---------------------- | ------ | -------- | ------------------------------------------------------------------------------ |
| `project`              | object | No       | Project to delete. Include `projectName` and `organization`.                   |
| `executionEnvironment` | object | No       | Execution environment to delete. Include `environmentName` and `organization`. |
| `template`             | object | No       | Job template to delete. Include `templateName` and `organization`.             |

### Output parameters

| Parameter | Type   | Description                                         |
| --------- | ------ | --------------------------------------------------- |
| `cleanUp` | string | Confirmation message indicating successful cleanup. |

### Example

```yaml
steps:
  - id: cleanup
    name: Clean Up Resources
    action: rhaap:clean-up
    input:
      token: ${{ parameters.AAP_TOKEN }}
      values:
        project:
          projectName: ${{ steps['create-project'].output.data.name }}
          organization: ${{ parameters.organization | resourceFilter('name') }}
        template:
          templateName: ${{ steps['create-template'].output.data.name }}
          organization: ${{ parameters.organization | resourceFilter('name') }}
```
