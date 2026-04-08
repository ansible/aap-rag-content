# 5. Using custom actions and UI components in Backstage Software Templates
## 5.3. Custom backstage actions




The following actions enable you to manage Ansible Automation Platform resources within a software template workflow.

### 5.3.1. `rhaap:create-project`




Create an Ansible Automation Platform project that links to a source control repository containing Ansible content.

**Input parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
|  `token` | string | Yes | OAuth2 token for Ansible Automation Platform authentication. |
|  `deleteIfExist` | boolean | No | If `true` , the action deletes the project if it already exists before creating a new one. |
|  `values` | object | Yes | The project configuration object. See the "values" Object Structure table. |


**“values” Object Structure**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
|  `projectName` | string | Yes | Name of the project. |
|  `projectDescription` | string | No | Description of the project. |
|  `organization` | object | Yes | Organization object with `id` (number, required) and `name` (string, optional). |
|  `credentials` | object | No | Credential object with `id` (number, required), `name` (string, optional), and `kind` (string, optional). |
|  `scmUrl` | string | Yes | Source control URL (for example, GitHub/GitLab repository URL). |
|  `scmBranch` | string | No | Source control branch, tag, or commit. |
|  `scmUpdateOnLaunch` | boolean | No | If `true` , updates the project revision before each job run. |


**Output parameters**

| Parameter | Type | Description |
| --- | --- | --- |
|  `project` | object | Created project details. |
|  `project.id` | number | Project ID in Ansible Automation Platform (AAP). |
|  `project.name` | string | Project name. |
|  `project.description` | string | Project description. |
|  `project.url` | string | Ansible Automation Platform URL for the project. |


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

### 5.3.2. `rhaap:create-execution-environment`




Create an execution environment in Ansible Automation Platform that defines the container image used to run Ansible jobs.

**Input parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
|  `token` | string | Yes | OAuth2 token for Ansible Automation Platform authentication. |
|  `deleteIfExist` | boolean | No | If `true` , the action deletes the execution environment if it already exists. |
|  `values` | object | Yes | The execution environment configuration object. |


**“values” Object Structure**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
|  `environmentName` | string | Yes | Name of the execution environment. |
|  `environmentDescription` | string | No | Description of the execution environment. |
|  `organization` | object | Yes | Organization object with required `id` (number) and optional `name` (string). |
|  `image` | string | Yes | Full image location, including registry, image name, and tag (for example, `quay.io/ansible/creator-ee:latest` ). |
|  `pull` | string | No | Image pull policy: `always` , `missing` , or `never` . Default is `missing` . |


**Output parameters**

| Parameter | Type | Description |
| --- | --- | --- |
|  `executionEnvironment` | object | Created execution environment details. |
|  `executionEnvironment.id` | number | Execution environment ID. |
|  `executionEnvironment.name` | string | Execution environment name. |
|  `executionEnvironment.description` | string | Execution environment description. |
|  `executionEnvironment.url` | string | Ansible Automation Platform (AAP) URL for the execution environment. |


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

### 5.3.3. `rhaap:create-job-template`




Create a job template in Ansible Automation Platform that defines a reusable configuration for running Ansible playbooks.

**Input parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
|  `token` | string | Yes | OAuth2 token for Ansible Automation Platform authentication. |
|  `deleteIfExist` | boolean | No | If `true` , the action deletes the job template if it already exists. |
|  `values` | object | Yes | The job template configuration object. |


**“values” Object Structure**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
|  `templateName` | string | Yes | Name of the job template. |
|  `templateDescription` | string | No | Description of the job template. |
|  `project` | object | Yes | Project object with required `id` (number) and optional `name` (string). |
|  `organization` | object | No | Organization object with `id` (number, required) and `name` (string, optional). |
|  `jobInventory` | object | Yes | Inventory object with required `id` (number) and optional `name` (string). |
|  `playbook` | string | Yes | Path to the playbook file to execute. |
|  `templateDescription` | string | No | Description of the job template. |
|  `scmType` | string | No | Source control type (for example, `Github` or `Gitlab` ). |
|  `executionEnvironment` | object | No | Execution environment object with required `id` (number) and optional `name` (string). |
|  `extraVariables` | object | No | Extra variables to pass to the playbook (key-value pairs). |


**Output parameters**

| Parameter | Type | Description |
| --- | --- | --- |
|  `template` | object | Created job template details. |
|  `template.id` | number | Job template ID. |
|  `template.name` | string | Job template name. |
|  `template.description` | string | Job template description. |
|  `template.url` | string | Ansible Automation Platform (AAP) URL for the job template. |


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

### 5.3.4. `rhaap:launch-job-template`




Launch an existing job template in Ansible Automation Platform.

**Input parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
|  `token` | string | Yes | OAuth2 token for Ansible Automation Platform authentication. |
|  `values` | object | Yes | The job launch configuration object. |


**“values” Object Structure**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
|  `template` | string | Yes | Job template name to launch. |
|  `inventory` | object | No | Override inventory with `id` (number) and `name` (string). |
|  `credentials` | array | No | Array of credential objects to use. |
|  `extraVariables` | object | No | Extra variables to pass to the job (key-value pairs). |
|  `limit` | string | No | Host pattern to constrain which hosts the job runs against. |
|  `jobType` | string | No | Job type: `run` or `check` . |
|  `executionEnvironment` | object | No | Override execution environment with `id` (number) and `name` (string). |
|  `verbosity` | object | No | Verbosity level object with `id` and `name` . |
|  `forks` | number | No | Number of parallel processes (default: `5` ). |
|  `jobSliceCount` | number | No | Divide the job into N slices. |
|  `timeout` | number | No | Job timeout in seconds ( `0` = no timeout). |
|  `diffMode` | boolean | No | Enable diff mode to show changes. |
|  `jobTags` | string | No | Comma-separated tags to run only specific tasks. |
|  `skipTags` | string | No | Comma-separated tags to skip specific tasks. |


**Output parameters**

| Parameter | Type | Description |
| --- | --- | --- |
|  `data` | object | Job execution details. |
|  `data.id` | number | Job ID. |
|  `data.status` | string | Job status. |
|  `data.url` | string | Ansible Automation Platform (AAP) URL for the job. |


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

### 5.3.5. Example with all backstage actions present




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

## 5.4. Custom UI components and filters




The **Ansible Backstage Plugins** provide custom UI components that enhance the software template experience by integrating directly with Ansible Automation Platform resource selection and authentication.

### 5.4.1. `AAPTokenField`




The `AAPTokenField` is a secure authentication field used in backstage scaffolder templates. It automatically fetches and stores an Ansible Automation Platform OAuth2 token, which is then available for all rhaap:* actions, enabling seamless authentication.

**AAPTokenField Properties**

The following table details the field’s properties for use in a template’s properties section.

| Property | Type | Description |
| --- | --- | --- |
|  `title` | string | The label displayed in the UI (for example, "AAP Token"). Defaults to "AAP Token". |
|  `description` | string | A short help text displayed below the input field. |
|  `ui:field` | string | Must be set to `AAPTokenField` . This setting instructs Backstage to render a custom react component instead of a default input field. |
|  `ui:backstage.review.show` | boolean | If `true` , this field appears in the **Review** step before scaffolding executes. The default value is `true` . |


**Authentication flow and token management**

All `rhaap:*` actions require an OAuth2 token for authenticating with Ansible Automation Platform. The field manages the token through the following process:

- Token Source: The token is automatically obtained from the Ansible Automation Platform OAuth2 authentication provider.
- Storage: The token is stored securely in Backstage secrets or fetched through the `    @ansible/backstage-plugin-auth-backend-module-rhaap-provider` .
- Usage: The token is passed to each action using the `    token` input parameter.


When the RHAAP auth provider is used, the token is injected automatically and can be referenced in the workflow steps as shown:

```
- id: create-project
action: rhaap:create-project
input:
token: ${{ parameters.AAP_TOKEN }}
# ... other inputs
```

**Example**

The following example shows how to declare and reference the AAPTokenField within a backstage template. Note that `ui:widget: hidden` and `ui:backstage: review: show: false` are used to ensure the token is not exposed in the UI.

```
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
name: my-AAP-template
title: Example AAP Template
spec:
parameters:
- title: Authentication
properties:
token:
title: AAP Authentication Token
type: string
description: Oauth2 token
ui:field: AAPTokenField
ui:widget: hidden
ui:backstage:
review:
show: false
steps:
- id: launch-job
name: Launch AAP Job Template
action: rhaap:launch-job-template
input:
token: ${{ parameters.token }}
...
```

**Error and validation handling**

All `rhaap:*` actions include built-in validation and user-friendly error reporting:

- Validation: If the token is missing or invalid, the action throws the error: "`Authorization token not provided`."
- Error Messages: Actions catch API client errors, extracting and surfacing meaningful messages without exposing stack traces.
- Workflow Safety: If a step fails due to authentication, subsequent steps are automatically skipped, ensuring a safe and predictable workflow.


### 5.4.2. `AAPResourcePicker`




The `AAPResourcePicker` is a dynamic field for backstage scaffolder templates. It fetches and displays a list of Ansible Automation Platform resources (such as inventories, organizations, or credentials) directly from the Ansible Automation Platform API, allowing users to select a resource for their automation workflow.

**AAPResourcePicker Properties**

The following table details the essential properties for configuring the resource picker in a template’s `properties` section.

| Property | Type | Description |
| --- | --- | --- |
|  `title` | string | The label displayed in the UI (for example, "Inventory"). |
|  `description` | string | A short help text shown below the field. |
|  `ui:field` | string | Must be set to `AAPResourcePicker` . |
|  `resource` | string | The specific Ansible Automation Platform (AAP) resource type to fetch and display (for example, `inventories` , `credentials` , or `organizations` ). |
|  `idKey` | string | The property name used to retrieve the resource ID (default:“id”). |
|  `nameKey` | string | The property name used to display the resource name in the list (default:“name”). |
|  `type` | string | Set to“array”for a multi-select field; omit this property for a single-select field. |


**Example**

The following example demonstrates how to use the `AAPResourcePicker` to create a single-select field for choosing an **Inventory** .

```
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
name: my-AAP-template
title: Example AAP Template
spec:
parameters:
- title: Authentication
properties:
jobInventory:
title: Inventory
description: Select inventory
resource: inventories
ui:field: AAPResourcePicker
default: DemoInventory
```

### 5.4.3. Custom filters




The plugins provide custom filters to extract specific properties from resource objects, which is essential for passing data between backstage steps.

| Filter | Purpose | Example Usage |
| --- | --- | --- |
|  `resourceFilter` | Extracts a single, specific property from a resource object. | `$!{{ parameters.organization |
| resourceFilter('name') }}` |  `multiResourceFilter` | Extracts a specific property from multiple resource objects (when the input is an array). |


## 5.5. Standard UI widgets




Standard UI widgets provide enhanced components for user forms to capture various types of input.

### 5.5.1. Textarea widget




The `textarea` widget renders a multi-line text input field for capturing long-form user input such as descriptions or configuration content.

```
properties:
description:
type: string
title: Description
ui:widget: textarea
ui:options:
rows: 5
placeholder: "Enter description..."
```

### 5.5.2. Select widget




The `select` widget displays a dropdown menu that enables users to choose a single value from a predefined list of options.

```
properties:
environment:
type: string
title: Environment
enum: ['dev', 'staging', 'prod']
ui:widget: select
default: 'dev'
```

### 5.5.3. Checkboxes widgets




The `checkboxes` widget renders a group of checkboxes, enabling the selection of multiple options from a list. The original plural "Checkboxes Widgets" is corrected to the singular form for style consistency.

```
properties:
features:
type: array
title: Base Images
items:
type: string
enum: ['baseImage1', 'baseImage2', 'baseImage3']
ui:widget: checkboxes
uniqueItems: true
```

### 5.5.4. Hidden widget




The `hidden` widget holds a fixed or prefilled value that is not visible to the user but is included in the submitted data. Use this widget for passing non-user-editable data, such as authentication tokens.

```
kind: Template
metadata:
name: my-AAP-template
title: Example AAP Template
spec:
parameters:
- title: Authentication
properties:
token:
title: AAP Authentication Token
type: string
description: Oauth2 token
ui:field: AAPTokenField
ui:widget: hidden
ui:backstage:
review:
show: false
steps:
- id: launch-job
name: Launch AAP Job Template
action: rhaap:launch-job-templat
input:
token: ${{ parameters.token }}
...
```

# Chapter 6. Creating execution environment definitions in self-service automation portal




Create custom execution environment (EE) definitions through Self Service Automation Portal using the EE Builder.

Note
Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/) .



## 6.1. Enabling the Execution Environment Builder in self-service automation portal




An administrator must enable the EE definition files feature in the configuration to display it in the left navigation panel.

To enable the EE definition files feature, you must modify the `enabled` key in your Helm chart configuration.

**Procedure**

1. Open the configuration file for your Helm chart.
1. Navigate to the `    default.main-menu-items` section.
1. Set the value of the `    enabled` key under the `    default.ee` configuration block to `    true` .

Note
Setting `    enabled: true` enables the EE definition files feature for all users.



**Example**

The final configuration must look like the following example:


```
default.main-menu-items:      menuItems:        default.mycatalog:          title: Templates          icon: home          to: /self-service/catalog          priority: 120        default.myitem:          title: History          icon: category          to: /self-service/create/tasks          priority: 110        default.ee:          enabled: false
```




## 6.2. Planning and reference for execution environment definitions




Understand how to successfully plan and configure your custom execution environment (EE) definition. Review the available options for base images, automation presets, and dependency requirements before you start the creation process to ensure your EE supports your organization’s automation content.

### 6.2.1. Execution Environment (EE) definition




The components and configurations for defining your EE are organized into two main categories: **Pre-defined templates** (presets) and **custom components** .

### 6.2.2. Pre-defined EE templates




Pre-defined EE templates are pre-configured templates designed to accelerate environment setup for common use cases. They already include specific base images, collections, and dependencies tailored for their respective domain.

| Preset | Description | Key considerations and use cases |
| --- | --- | --- |
| Start from scratch | A template which acts as a generic blank slate to start creating custom EEs from. | Use this preset when you require complete control over the base image and dependencies to build a highly customized or minimized EE. |
| Networking Automation | A template optimized for environments focused on network device interaction and network-specific content. | Use this preset when your automation primarily interacts with switches, routers, firewalls, and other network infrastructure. |
| Cloud Automation | A template optimized for environments focused on deploying and managing cloud resources (such as AWS or Microsoft). | Use this preset when your automation targets provisioning, configuration, and management of cloud services. |


### 6.2.3. Disabling pre-built templates




For environments where these pre-built templates are not needed or conflict with organizational standards, they can be disabled in the Helm chart configuration.

**Procedure**

- You can disable pre-built templates by commenting them out in the Helm chart configuration. The following is an example of all three pre-built templates commented out:


```
catalog:      locations:        # Local templates        - type: file          target: ../../examples/entities.yaml            # The following Ansible pre-built templates are disabled:        # - type: url        #   target: https://github.com/ansible/ansible-rhdh-templates/blob/main/templates/ee-start-from-scratch.yaml        # - type: url        #   target: https://github.com/ansible/ansible-rhdh-templates/blob/main/templates/ee-network-automation.yaml        # - type: url        #   target: https://github.com/ansible/ansible-rhdh-templates/blob/main/templates/ee-cloud-automation.yaml
```




### 6.2.4. Components for custom EE definitions




When creating a custom EE, you define the core underlying elements that dictate the environment’s capabilities, security, and dependencies. These components are used to define the custom EE, and are also utilized internally by the pre-defined presets.

| Component or setting | Description | Key considerations and examples |
| --- | --- | --- |
| Base images | The foundation layer of your EE, pre-configured with a specific operating system and toolset.

By default, the following base images are available in all 3 pre-defined templates:

- Red Hat Ansible Minimal EE - Ansible Core 2.18 (RHEL 8)
- Red Hat Ansible Minimal EE - Ansible Core 2.18 (RHEL 9)
- Red Hat Ansible Minimal EE - Ansible Core 2.16 (RHEL 8)
- Red Hat Ansible Minimal EE - Ansible Core 2.16 (RHEL 9) | Select a base image that aligns with your organization’s security and Python compatibility needs. Popular base images are optimized for minimal overhead or specific compliance requirements.

If you are providing a custom image, it must include `ansible-core` and `ansible-runner` .

Select a base image that aligns with your organization’s security and Python compatibility needs. |
| Collections | Specifies the Ansible Collections and Python libraries required by your automation content. | Ensure all necessary content is included from the documentation’s list. You can add collections manually or upload a `requirements.yml` file.

When collections overlap, the system merges the contents. If duplicates occur:

- If a version is not specified, the system prioritizes the collection using the most recent version available.
- If versions are explicitly specified for both collections, the system defaults to using the most recent version. |
| Python requirements | Defines the minimum Python version and any extra Python packages required for this execution environment. | Must reflect the version compatibility used across your organization for running automation reliably.

Avoid repeating Python requirements already specified as a dependency by the selected collections (for example, in their respective `requirements.txt` files). |
| System packages | Operating system (OS) libraries and packages required by the Python packages or collections. | Defines the extra OS libraries and packages required by the Python packages or collections listed in the EE.

Examples: `git` , `gcc` , `python3-devel` . These are necessary for compiling Python packages during the build process.

This list supplements, and must not repeat, any base OS dependencies already managed by your environment’s build system. |
| Additional build steps | Additional build steps are custom shell commands injected directly into the container runtime instruction file. | Use additional build steps to perform actions like installing private certificates or configuring environment variables not covered by standard package installation. |


## 6.3. Integrating Model Context Protocol (MCP) servers through the EE Builder




The EE Builder supports the optional integration of a Model Context Protocol (MCP) server. MCP servers are an advanced feature used to expose automation actions to AI assistants or other cognitive services.

If you select an MCP server, the EE Builder automatically handles the necessary configuration files and dependencies. This portal feature generates execution environment definition files for building an execution environment with your selected MCP servers.

The EE Builder currently supports the following MCP servers:

- Git Hub
- AWS


- AWS CCAPI
- AWS CDK
- AWS IAM
- AWS Core

- Azure


## 6.4. Creating EE definitions in Self-service automation portal using the EE Builder




You can use the Execution Environment (EE) Builder in the self-service automation portal to create custom EE definitions through a guided workflow.

**Prerequisites**

- You have installed the self-service automation portal.
- You have the EE Builder feature enabled.
- You have reviewed the [Planning and reference for EE definitions section](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_self-service_automation_portal/self-service-create-ee-definitions_aap-self-service-using#self-service-planning-reference-ee-definitions_self-service-create-ee-definitions) .


**Procedure**

1. Log into the self-service automation portal and select **EE definition files** from the lefthand navigation pane.
1. If this is your first time creating an EE definition file, click **Create Execution Environment definition file** , otherwise select the **Create** tab.
1. Click **Start** on your preferred template.
1. Select your preferred base image and click **Next** .

Note
Red Hat recommends using the **Red Hat Minimal EE** base. If selecting **Custom Image** , it is important you fully understand what the contents of your base image are. For example, a base image without Ansible core or Ansible runner will fail to build.




1. Select a collection from **Add popular Collections** or **Add Collection Manually** and click **Next** .


1. Optional: To add additional Python or System requirements, select **Specify additional python requirements and system packages** , and then click **Add packages manually** or **Choose File** .

1. Select your desired MCP servers and click **Next** .
1. Optional: In the **Additional Build Steps** section, you can specify custom build instructions that will be executed at specific steps during the build process:


1. Select **Add build Step** .
1. Select a step from the **Step type** drop-down list.
1. Input a command you want to run at that step. You can provide a string of commands by giving each command a new line.
1. Click **Next** .

1. In the **Generate and publish** section:


1. Fill in the following mandatory fields:


-  **EE File name**
-  **Description**
-  **Select source control provider**
-  **SCM repository organization name or username**
-  **Repository name**

1. Ensure the `        execution-environment` tag is applied. Click the plus (+) icon to add additional tags if required.
1. Ensure **Publish to a Git repository** is selected. If unselected, your EE will be provided as a download after the build process.
1. If the **Repository name** you provided does not already exist, select **Create new repository** . If it does exist and you check the box, a pull request will be created instead.
1. Click **Next** .

1. Confirm your details are correct and click **Create** . This begins the scaffolding process.
1. After the scaffolding is complete, click **Getting started** for next steps on how to build your EE definition.


**Verification**

Verify the creation and deployment of the EE definition file using one of the following methods:


1. In the self-service automation portal:


1. Click **View details in catalog** or **Download EE files** (downloads the generated files as a `        .tar` file).
1. Alternatively, select **EE definition files** in the left-hand navigation pane. The new file appears in the **Execution Environment definition files** box.

1. In the repository:


1. Click **GitHub repository** or **Gitlab repository** to confirm the files were scaffolded into your repository.



**Additional resources**

-  [Creating and using execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/creating_and_using_execution_environments/index)


## 6.5. Importing your custom EE definition




The EE definition workflow generates a reusable Backstage software template, named `&lt;ee-name&gt;-template.yaml` . This template includes the specified default configurations when you select **Publish to a Git repository** during the creation of your custom EE definition.

The template is also generated for non-SCM based publishings.

You can import this template into the self-service automation portal to make the default configuration available to others.

**Prerequisites**

- You have installed the self-service automation portal.
- You have the EE Builder feature enabled.
- You have a custom EE definition hosted in a repository.


**Procedure**

1. Go to the repository where your `    &lt;ee-name&gt;-template.yaml` is stored and open it.
1. Copy the URL of the **template.yaml** page.
1. Log into the self-service automation portal and select **EE definition files** from the lefthand navigation pane.
1. Click **Create** > **Add Template** .
1. Paste the template URL into the **Select URL** field and click **Analyze** .
1. Click **Import** .


**Verification**

To verify your template was added successfully, go to **EE definition files** > **Create** . Here you should see your newly created custom template.


## 6.6. Managing your EE files




Download your Execution Environment (EE) file to create a local backup. Copy an existing EE to use it as a template for a new, similar environment. Delete an EE to remove obsolete or unwanted definitions.

**Prerequisites**

- You have created an EE definition through the EE Builder.


**Procedure**

1. Log into the self-service automation portal and select **EE definition files** from the lefthand navigation pane.
1. Under the **Name** column, select the EE you want to take action on:


- To download your EE definition, click **Download EE files** .
- To delete your EE definition, click the![vertical dots](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_self-service_automation_portal-en-US/images/9a84eef17d4d9ae3eeb64f4b04afbbf7/actions.png)
icon and then select **Unregister entity** .
- To copy your EE definition:


- Click the![vertical dots](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_self-service_automation_portal-en-US/images/9a84eef17d4d9ae3eeb64f4b04afbbf7/actions.png)
icon and then select **Copy entity URL** .
- Select **EE definition files** from the lefthand navigation pane.
- Click **Create** and then **Add template** .
- Paste your entity URL into the **Select URL** field and click **Analyze** .
- Click **Import** . The new template now appears in the Execution Environment definition files page.




# Chapter 7. Providing feedback in self-service automation portal




Self-service automation portal provides a feedback form where you can suggest new features and content, as well as provide general feedback.

Note
The feedback form is disabled by default. If the **Feedback** button is not visible in the console, your administrator must enable it in the portal configuration.



1. Click **Feedback** in the self-service automation portal console to display the feedback form.

![Self-service automation portal feedback form](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_self-service_automation_portal-en-US/images/b6a52e77499334e9950b4b0c1c3ba861/rhdh-feedback-form.png)



1. Enter the feedback you want to provide.
1. Tick the **I understand that feedback is shared with Red Hat** checkbox.
1. Click **Submit** .


Note
To ensure that Red Hat receives your feedback, exclude your self-service automation portal URL in any browser ad blockers or privacy tools.




<span id="idm140678648781360"></span>
# Legal Notice

Copyright© Red Hat.
Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.
TheOpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.
All other trademarks are the property of their respective owners.





