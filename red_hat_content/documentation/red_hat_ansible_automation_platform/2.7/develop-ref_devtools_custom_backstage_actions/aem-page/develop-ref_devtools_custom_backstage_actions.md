+++
template = "docs/aem-title.html"
title = "Custom Backstage actions - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_custom_backstage_actions"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_custom_backstage_actions/aem-page/develop-ref_devtools_custom_backstage_actions.html"
last_crumb = "Custom Backstage actions"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Custom Backstage actions"
oversized = "false"
page_slug = "develop-ref_devtools_custom_backstage_actions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_custom_backstage_actions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_custom_backstage_actions/toc/toc.json"
type = "aem-page"
+++

# Custom Backstage actions

The following actions enable you to manage Ansible Automation Platform resources within a software template workflow.

## `rhaap:create-project`

Create an Ansible Automation Platform project that links to a source control repository containing Ansible content.

 **Input parameters**

| Parameter       | Type    | Required | Description                                                                               |
| --------------- | ------- | -------- | ----------------------------------------------------------------------------------------- |
| `token`         | string  | Yes      | OAuth2 token for Ansible Automation Platform authentication.                              |
| `deleteIfExist` | boolean | No       | If `true`, the action deletes the project if it already exists before creating a new one. |
| `values`        | object  | Yes      | The project configuration object. See the "values" Object Structure table.                |

 **“values” Object Structure**

| Field                | Type    | Required | Description                                                                                               |
| -------------------- | ------- | -------- | --------------------------------------------------------------------------------------------------------- |
| `projectName`        | string  | Yes      | Name of the project.                                                                                      |
| `projectDescription` | string  | No       | Description of the project.                                                                               |
| `organization`       | object  | Yes      | Organization object with `id` (number, required) and `name` (string, optional).                           |
| `credentials`        | object  | No       | Credential object with `id` (number, required), `name` (string, optional), and `kind` (string, optional). |
| `scmUrl`             | string  | Yes      | Source control URL (for example, GitHub/GitLab repository URL).                                           |
| `scmBranch`          | string  | No       | Source control branch, tag, or commit.                                                                    |
| `scmUpdateOnLaunch`  | boolean | No       | If `true`, updates the project revision before each job run.                                              |

 **Output parameters**

| Parameter             | Type   | Description                                      |
| --------------------- | ------ | ------------------------------------------------ |
| `project`             | object | Created project details.                         |
| `project.id`          | number | Project ID in Ansible Automation Platform (AAP). |
| `project.name`        | string | Project name.                                    |
| `project.description` | string | Project description.                             |
| `project.url`         | string | Ansible Automation Platform URL for the project. |

 **Example**

```
steps:
  - id: create-aap-project
    name: Create AAP Project
    action: rhaap:create-project
    input:
      token: ${{ secrets.aapToken }}
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

| Parameter       | Type    | Required | Description                                                                   |
| --------------- | ------- | -------- | ----------------------------------------------------------------------------- |
| `token`         | string  | Yes      | OAuth2 token for Ansible Automation Platform authentication.                  |
| `deleteIfExist` | boolean | No       | If `true`, the action deletes the execution environment if it already exists. |
| `values`        | object  | Yes      | The execution environment configuration object.                               |

 **“values” Object Structure**

| Field                    | Type   | Required | Description                                                                                                      |
| ------------------------ | ------ | -------- | ---------------------------------------------------------------------------------------------------------------- |
| `environmentName`        | string | Yes      | Name of the execution environment.                                                                               |
| `environmentDescription` | string | No       | Description of the execution environment.                                                                        |
| `organization`           | object | Yes      | Organization object with required `id` (number) and optional `name` (string).                                    |
| `image`                  | string | Yes      | Full image location, including registry, image name, and tag (for example, `quay.io/ansible/creator-ee:latest`). |
| `pull`                   | string | No       | Image pull policy: `always`, `missing`, or `never`. Default is `missing`.                                        |

 **Output parameters**

| Parameter                          | Type   | Description                                                          |
| ---------------------------------- | ------ | -------------------------------------------------------------------- |
| `executionEnvironment`             | object | Created execution environment details.                               |
| `executionEnvironment.id`          | number | Execution environment ID.                                            |
| `executionEnvironment.name`        | string | Execution environment name.                                          |
| `executionEnvironment.description` | string | Execution environment description.                                   |
| `executionEnvironment.url`         | string | Ansible Automation Platform (AAP) URL for the execution environment. |

 **Example**

```
steps:
  - id: create-ee
    name: Create Execution Environment
    action: rhaap:create-execution-environment
    input:
      token: ${{ secrets.aapToken }}
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

| Parameter       | Type    | Required | Description                                                          |
| --------------- | ------- | -------- | -------------------------------------------------------------------- |
| `token`         | string  | Yes      | OAuth2 token for Ansible Automation Platform authentication.         |
| `deleteIfExist` | boolean | No       | If `true`, the action deletes the job template if it already exists. |
| `values`        | object  | Yes      | The job template configuration object.                               |

 **“values” Object Structure**

| Field                  | Type   | Required | Description                                                                            |
| ---------------------- | ------ | -------- | -------------------------------------------------------------------------------------- |
| `templateName`         | string | Yes      | Name of the job template.                                                              |
| `templateDescription`  | string | No       | Description of the job template.                                                       |
| `project`              | object | Yes      | Project object with required `id` (number) and optional `name` (string).               |
| `organization`         | object | No       | Organization object with `id` (number, required) and `name` (string, optional).        |
| `jobInventory`         | object | Yes      | Inventory object with required `id` (number) and optional `name` (string).             |
| `playbook`             | string | Yes      | Path to the playbook file to execute.                                                  |
| `templateDescription`  | string | No       | Description of the job template.                                                       |
| `scmType`              | string | No       | Source control type (for example, `Github` or `Gitlab`).                               |
| `executionEnvironment` | object | No       | Execution environment object with required `id` (number) and optional `name` (string). |
| `extraVariables`       | object | No       | Extra variables to pass to the playbook (key-value pairs).                             |

 **Output parameters**

| Parameter              | Type   | Description                                                 |
| ---------------------- | ------ | ----------------------------------------------------------- |
| `template`             | object | Created job template details.                               |
| `template.id`          | number | Job template ID.                                            |
| `template.name`        | string | Job template name.                                          |
| `template.description` | string | Job template description.                                   |
| `template.url`         | string | Ansible Automation Platform (AAP) URL for the job template. |

 **Example**

```
steps:
  - id: create-job-template
    name: Create Job Template
    action: rhaap:create-job-template
    input:
      token: ${{ secrets.aapToken }}
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

| Parameter | Type   | Required | Description                                                  |
| --------- | ------ | -------- | ------------------------------------------------------------ |
| `token`   | string | Yes      | OAuth2 token for Ansible Automation Platform authentication. |
| `values`  | object | Yes      | The job launch configuration object.                         |

 **“values” Object Structure**

| Field                  | Type    | Required | Description                                                            |
| ---------------------- | ------- | -------- | ---------------------------------------------------------------------- |
| `template`             | string  | Yes      | Job template name to launch.                                           |
| `inventory`            | object  | No       | Override inventory with `id` (number) and `name` (string).             |
| `credentials`          | array   | No       | Array of credential objects to use.                                    |
| `extraVariables`       | object  | No       | Extra variables to pass to the job (key-value pairs).                  |
| `limit`                | string  | No       | Host pattern to constrain which hosts the job runs against.            |
| `jobType`              | string  | No       | Job type: `run` or `check`.                                            |
| `executionEnvironment` | object  | No       | Override execution environment with `id` (number) and `name` (string). |
| `verbosity`            | object  | No       | Verbosity level object with `id` and `name`.                           |
| `forks`                | number  | No       | Number of parallel processes (default: `5`).                           |
| `jobSliceCount`        | number  | No       | Divide the job into N slices.                                          |
| `timeout`              | number  | No       | Job timeout in seconds (`0` = no timeout).                             |
| `diffMode`             | boolean | No       | Enable diff mode to show changes.                                      |
| `jobTags`              | string  | No       | Comma-separated tags to run only specific tasks.                       |
| `skipTags`             | string  | No       | Comma-separated tags to skip specific tasks.                           |

 **Output parameters**

| Parameter     | Type   | Description                                        |
| ------------- | ------ | -------------------------------------------------- |
| `data`        | object | Job execution details.                             |
| `data.id`     | number | Job ID.                                            |
| `data.status` | string | Job status.                                        |
| `data.url`    | string | Ansible Automation Platform (AAP) URL for the job. |

 **Example**

```
steps:
  - id: launch-job
    name: Launch Job Template
    action: rhaap:launch-job-template
    input:
      token: ${{ secrets.aapToken }}
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
        token: ${{ secrets.aapToken }}
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
        token: ${{ secrets.aapToken }}
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
        token: ${{ secrets.aapToken }}
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
        token: ${{ secrets.aapToken }}
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

| Field                  | Type   | Required | Description                                                                  |
| ---------------------- | ------ | -------- | ---------------------------------------------------------------------------- |
| `project`              | object | No       | Project to delete. Include`projectName` and`organization`.                   |
| `executionEnvironment` | object | No       | Execution environment to delete. Include`environmentName` and`organization`. |
| `template`             | object | No       | Job template to delete. Include`templateName` and`organization`.             |

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
      token: ${{ secrets.aapToken }}
      values:
        project:
          projectName: ${{ steps['create-project'].output.data.name }}
          organization: ${{ parameters.organization | resourceFilter('name') }}
        template:
          templateName: ${{ steps['create-template'].output.data.name }}
          organization: ${{ parameters.organization | resourceFilter('name') }}
```
