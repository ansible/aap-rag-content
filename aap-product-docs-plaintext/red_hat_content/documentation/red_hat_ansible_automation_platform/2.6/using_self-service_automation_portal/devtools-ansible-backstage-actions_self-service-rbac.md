# 5. Using custom actions and UI components in Backstage Software Templates
## 5.3. Custom backstage actions

The following actions enable you to manage Ansible Automation Platform resources within a software template workflow.

### 5.3.1. `rhaap:create-project`

Create an Ansible Automation Platform project that links to a source control repository containing Ansible content.

**Input parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| <br> `token` | <br>  string | <br>  Yes | <br>  OAuth2 token for Ansible Automation Platform authentication. |
| <br> `deleteIfExist` | <br>  boolean | <br>  No | <br>  If `true`, the action deletes the project if it already exists before creating a new one. |
| <br> `values` | <br>  object | <br>  Yes | <br>  The project configuration object. See the "values" Object Structure table. |

**“values” Object Structure**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| <br> `projectName` | <br>  string | <br>  Yes | <br>  Name of the project. |
| <br> `projectDescription` | <br>  string | <br>  No | <br>  Description of the project. |
| <br> `organization` | <br>  object | <br>  Yes | <br>  Organization object with `id` (number, required) and `name` (string, optional). |
| <br> `credentials` | <br>  object | <br>  No | <br>  Credential object with `id` (number, required), `name` (string, optional), and `kind` (string, optional). |
| <br> `scmUrl` | <br>  string | <br>  Yes | <br>  Source control URL (for example, GitHub/GitLab repository URL). |
| <br> `scmBranch` | <br>  string | <br>  No | <br>  Source control branch, tag, or commit. |
| <br> `scmUpdateOnLaunch` | <br>  boolean | <br>  No | <br>  If `true`, updates the project revision before each job run. |

**Output parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| <br> `project` | <br>  object | <br>  Created project details. |
| <br> `project.id` | <br>  number | <br>  Project ID in Ansible Automation Platform (AAP). |
| <br> `project.name` | <br>  string | <br>  Project name. |
| <br> `project.description` | <br>  string | <br>  Project description. |
| <br> `project.url` | <br>  string | <br>  Ansible Automation Platform URL for the project. |

**Example**

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

### 5.3.2. `rhaap:create-execution-environment`

Create an execution environment in Ansible Automation Platform that defines the container image used to run Ansible jobs.

**Input parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| <br> `token` | <br>  string | <br>  Yes | <br>  OAuth2 token for Ansible Automation Platform authentication. |
| <br> `deleteIfExist` | <br>  boolean | <br>  No | <br>  If `true`, the action deletes the execution environment if it already exists. |
| <br> `values` | <br>  object | <br>  Yes | <br>  The execution environment configuration object. |

**“values” Object Structure**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| <br> `environmentName` | <br>  string | <br>  Yes | <br>  Name of the execution environment. |
| <br> `environmentDescription` | <br>  string | <br>  No | <br>  Description of the execution environment. |
| <br> `organization` | <br>  object | <br>  Yes | <br>  Organization object with required `id` (number) and optional `name` (string). |
| <br> `image` | <br>  string | <br>  Yes | <br>  Full image location, including registry, image name, and tag (for example, `quay.io/ansible/creator-ee:latest`). |
| <br> `pull` | <br>  string | <br>  No | <br>  Image pull policy: `always`, `missing`, or `never`. Default is `missing`. |

**Output parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| <br> `executionEnvironment` | <br>  object | <br>  Created execution environment details. |
| <br> `executionEnvironment.id` | <br>  number | <br>  Execution environment ID. |
| <br> `executionEnvironment.name` | <br>  string | <br>  Execution environment name. |
| <br> `executionEnvironment.description` | <br>  string | <br>  Execution environment description. |
| <br> `executionEnvironment.url` | <br>  string | <br>  Ansible Automation Platform (AAP) URL for the execution environment. |

**Example**

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

### 5.3.3. `rhaap:create-job-template`

Create a job template in Ansible Automation Platform that defines a reusable configuration for running Ansible playbooks.

**Input parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| <br> `token` | <br>  string | <br>  Yes | <br>  OAuth2 token for Ansible Automation Platform authentication. |
| <br> `deleteIfExist` | <br>  boolean | <br>  No | <br>  If `true`, the action deletes the job template if it already exists. |
| <br> `values` | <br>  object | <br>  Yes | <br>  The job template configuration object. |

**“values” Object Structure**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| <br> `templateName` | <br>  string | <br>  Yes | <br>  Name of the job template. |
| <br> `templateDescription` | <br>  string | <br>  No | <br>  Description of the job template. |
| <br> `project` | <br>  object | <br>  Yes | <br>  Project object with required `id` (number) and optional `name` (string). |
| <br> `organization` | <br>  object | <br>  No | <br>  Organization object with `id` (number, required) and `name` (string, optional). |
| <br> `jobInventory` | <br>  object | <br>  Yes | <br>  Inventory object with required `id` (number) and optional `name` (string). |
| <br> `playbook` | <br>  string | <br>  Yes | <br>  Path to the playbook file to execute. |
| <br> `templateDescription` | <br>  string | <br>  No | <br>  Description of the job template. |
| <br> `scmType` | <br>  string | <br>  No | <br>  Source control type (for example, `Github` or `Gitlab`). |
| <br> `executionEnvironment` | <br>  object | <br>  No | <br>  Execution environment object with required `id` (number) and optional `name` (string). |
| <br> `extraVariables` | <br>  object | <br>  No | <br>  Extra variables to pass to the playbook (key-value pairs). |

**Output parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| <br> `template` | <br>  object | <br>  Created job template details. |
| <br> `template.id` | <br>  number | <br>  Job template ID. |
| <br> `template.name` | <br>  string | <br>  Job template name. |
| <br> `template.description` | <br>  string | <br>  Job template description. |
| <br> `template.url` | <br>  string | <br>  Ansible Automation Platform (AAP) URL for the job template. |

**Example**

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

### 5.3.4. `rhaap:launch-job-template`

Launch an existing job template in Ansible Automation Platform.

**Input parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| <br> `token` | <br>  string | <br>  Yes | <br>  OAuth2 token for Ansible Automation Platform authentication. |
| <br> `values` | <br>  object | <br>  Yes | <br>  The job launch configuration object. |

**“values” Object Structure**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| <br> `template` | <br>  string | <br>  Yes | <br>  Job template name to launch. |
| <br> `inventory` | <br>  object | <br>  No | <br>  Override inventory with `id` (number) and `name` (string). |
| <br> `credentials` | <br>  array | <br>  No | <br>  Array of credential objects to use. |
| <br> `extraVariables` | <br>  object | <br>  No | <br>  Extra variables to pass to the job (key-value pairs). |
| <br> `limit` | <br>  string | <br>  No | <br>  Host pattern to constrain which hosts the job runs against. |
| <br> `jobType` | <br>  string | <br>  No | <br>  Job type: `run` or `check`. |
| <br> `executionEnvironment` | <br>  object | <br>  No | <br>  Override execution environment with `id` (number) and `name` (string). |
| <br> `verbosity` | <br>  object | <br>  No | <br>  Verbosity level object with `id` and `name`. |
| <br> `forks` | <br>  number | <br>  No | <br>  Number of parallel processes (default: `5`). |
| <br> `jobSliceCount` | <br>  number | <br>  No | <br>  Divide the job into N slices. |
| <br> `timeout` | <br>  number | <br>  No | <br>  Job timeout in seconds (`0` = no timeout). |
| <br> `diffMode` | <br>  boolean | <br>  No | <br>  Enable diff mode to show changes. |
| <br> `jobTags` | <br>  string | <br>  No | <br>  Comma-separated tags to run only specific tasks. |
| <br> `skipTags` | <br>  string | <br>  No | <br>  Comma-separated tags to skip specific tasks. |

**Output parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| <br> `data` | <br>  object | <br>  Job execution details. |
| <br> `data.id` | <br>  number | <br>  Job ID. |
| <br> `data.status` | <br>  string | <br>  Job status. |
| <br> `data.url` | <br>  string | <br>  Ansible Automation Platform (AAP) URL for the job. |

**Example**

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

### 5.3.5. Example with all backstage actions present

The following example displays how you can use multiple actions together.

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

## 5.4. Custom UI components and filters

The **Ansible Backstage Plugins** provide custom UI components that enhance the software template experience by integrating directly with Ansible Automation Platform resource selection and authentication.

### 5.4.1. `AAPTokenField`

The `AAPTokenField` is a secure authentication field used in backstage scaffolder templates. It automatically fetches and stores an Ansible Automation Platform OAuth2 token, which is then available for all rhaap:* actions, enabling seamless authentication.

**AAPTokenField Properties**

The following table details the field’s properties for use in a template’s properties section.

| Property | Type | Description |
| --- | --- | --- |
| <br> `title` | <br>  string | <br>  The label displayed in the UI (for example, "AAP Token"). Defaults to "AAP Token". |
| <br> `description` | <br>  string | <br>  A short help text displayed below the input field. |
| <br> `ui:field` | <br>  string | <br>  Must be set to `AAPTokenField`. This setting instructs Backstage to render a custom react component instead of a default input field. |
| <br> `ui:backstage.review.show` | <br>  boolean | <br>  If `true`, this field appears in the **Review** step before scaffolding executes. The default value is `true`. |

**Authentication flow and token management**

All `rhaap:*` actions require an OAuth2 token for authenticating with Ansible Automation Platform. The field manages the token through the following process:

- Token Source: The token is automatically obtained from the Ansible Automation Platform OAuth2 authentication provider.
- Storage: The token is stored securely in Backstage secrets or fetched through the `@ansible/backstage-plugin-auth-backend-module-rhaap-provider`.
- Usage: The token is passed to each action using the `token` input parameter.

When the RHAAP auth provider is used, the token is injected automatically and can be referenced in the workflow steps as shown:

- id: create-project
action: rhaap:create-project
input:
token: ${{ parameters.AAP_TOKEN }}
# ... other inputs

**Example**

The following example shows how to declare and reference the AAPTokenField within a backstage template. Note that `ui:widget: hidden` and `ui:backstage: review: show: false` are used to ensure the token is not exposed in the UI.

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
| <br> `title` | <br>  string | <br>  The label displayed in the UI (for example, "Inventory"). |
| <br> `description` | <br>  string | <br>  A short help text shown below the field. |
| <br> `ui:field` | <br>  string | <br>  Must be set to `AAPResourcePicker`. |
| <br> `resource` | <br>  string | <br>  The specific Ansible Automation Platform (AAP) resource type to fetch and display (for example, `inventories`, `credentials`, or `organizations`). |
| <br> `idKey` | <br>  string | <br>  The property name used to retrieve the resource ID (default: “id”). |
| <br> `nameKey` | <br>  string | <br>  The property name used to display the resource name in the list (default: “name”). |
| <br> `type` | <br>  string | <br>  Set to “array” for a multi-select field; omit this property for a single-select field. |

**Example**

The following example demonstrates how to use the `AAPResourcePicker` to create a single-select field for choosing an **Inventory**.

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

### 5.4.3. Custom filters

The plugins provide custom filters to extract specific properties from resource objects, which is essential for passing data between backstage steps.

| Filter | Purpose | Example Usage |
| --- | --- | --- |
| <br> `resourceFilter` | <br>  Extracts a single, specific property from a resource object. | <br>  `$!{{ parameters.organization |
| <br>  resourceFilter('name') }}` | <br> `multiResourceFilter` | <br>  Extracts a specific property from multiple resource objects (when the input is an array). |

## 5.5. Standard UI widgets

Standard UI widgets provide enhanced components for user forms to capture various types of input.

### 5.5.1. Textarea widget

The `textarea` widget renders a multi-line text input field for capturing long-form user input such as descriptions or configuration content.

properties:
description:
type: string
title: Description
ui:widget: textarea
ui:options:
rows: 5
placeholder: "Enter description..."

### 5.5.2. Select widget

The `select` widget displays a dropdown menu that enables users to choose a single value from a predefined list of options.

properties:
environment:
type: string
title: Environment
enum: ['dev', 'staging', 'prod']
ui:widget: select
default: 'dev'

### 5.5.3. Checkboxes widgets

The `checkboxes` widget renders a group of checkboxes, enabling the selection of multiple options from a list. The original plural "Checkboxes Widgets" is corrected to the singular form for style consistency.

properties:
features:
type: array
title: Base Images
items:
type: string
enum: ['baseImage1', 'baseImage2', 'baseImage3']
ui:widget: checkboxes
uniqueItems: true

### 5.5.4. Hidden widget

The `hidden` widget holds a fixed or prefilled value that is not visible to the user but is included in the submitted data. Use this widget for passing non-user-editable data, such as authentication tokens.

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

## 5.6. Parameter types and field options

The `parameters` section in a template defines the form fields that users complete before execution. Each property in `parameters.properties` renders as a form field. This section documents the available types, widgets, and validation options you can use when building custom templates.

### 5.6.1. Supported parameter types

Templates support standard Backstage parameter types (`string`, `number`, `integer`, `boolean`, `array`) and widgets (`textarea`, `select`, `checkboxes`, `hidden`). For a complete reference of standard types and widgets, see the [Backstage Software Templates documentation](https://backstage.io/docs/features/software-templates/input-examples).

self-service automation portal adds the following Ansible Automation Platform-specific field types:

**Table 5.1. Ansible Automation Platform-specific field types**

| Type | Widget | Description | Example use case |
| --- | --- | --- | --- |
| <br> `ui:field: AAPTokenField` | <br>  Hidden token field | <br>  OAuth2 authentication token, auto-populated and hidden from the user. | <br>  Always present in auto-generated templates. |
| <br> `resource` + `ui:field: AAPResourcePicker` | <br>  Ansible Automation Platform resource picker (single-select) | <br>  Select one Ansible Automation Platform resource by name. | <br>  Inventory, organization. |
| <br> `type: array` + `ui:field: AAPResourcePicker` | <br>  Ansible Automation Platform resource picker (multi-select) | <br>  Select multiple Ansible Automation Platform resources by name. | <br>  Credentials. |

These Ansible Automation Platform-specific fields are documented in detail in [AAP resource picker fields](#aap-resource-picker-fields_self-service-rbac "5.6.2.&nbsp;AAP resource picker fields").

### 5.6.2. AAP resource picker fields

Use `ui:field: AAPResourcePicker` to let users select Ansible Automation Platform resources by name. self-service automation portal queries the Ansible Automation Platform API and displays available resources in a picker. Set the `resource` property to specify the Ansible Automation Platform resource type.

The following table lists supported `resource` values:

**Table 5.2. Supported resource values**

| `resource` value | Ansible Automation Platform resource type | Selection mode |
| --- | --- | --- |
| <br> `inventories` | <br>  Inventories | <br>  Single-select |
| <br> `credentials` | <br>  Credentials | <br>  Multi-select (`type: array`) |
| <br> `organizations` | <br>  Organizations | <br>  Single-select |

#### 5.6.2.1. Single-select example (inventory)

inventory:
title: Inventory
description: Select target inventory.
resource: inventories
ui:field: AAPResourcePicker
default: Production Servers

#### 5.6.2.2. Multi-select example (credentials)

credentials:
title: Credentials
description: Select credentials for accessing the target hosts.
type: array
resource: credentials
ui:field: AAPResourcePicker
default:
- SSH Key
- AWS Credentials

## 5.7. Dynamic fields

Dynamic fields appear or disappear based on user selections. Use the `dependencies` keyword with `allOf` and `if`/`then` to define conditional field visibility. This lets you build forms where selecting a value in one field reveals additional fields relevant to that selection.

Dynamic fields are useful for:

- Showing advanced options only when the user enables them.
- Displaying different configuration fields based on a resource type or category selection.
- Requesting a reason or justification when the user selects a specific option.

### 5.7.1. Showing or hiding fields based on a toggle

Use a `boolean` toggle field to show or hide a group of additional fields.

In this example, selecting "Show advanced options" reveals one additional field. When the toggle is off, the field is hidden and not submitted.

parameters:
- title: Time server settings
required:
- ntpServers
properties:
ntpServers:
title: NTP servers
type: string
default: 0.rhel.pool.ntp.org, 1.rhel.pool.ntp.org
showAdvanced:
title: Show advanced options?
type: boolean
default: false
dependencies:
showAdvanced:
allOf:
- if:
properties:
showAdvanced:
const: true
then:
properties:
maxSyncDelay:
type: number
title: Max sync delay (ms)
default: 500

When `showAdvanced` is `true`, the form displays `maxSyncDelay`. When `showAdvanced` is `false`, the field is hidden.

### 5.7.2. Showing different fields based on a selection

Use an `enum` field with `dependencies` and `allOf` to display different configuration fields for each option.

In this example, selecting a database type reveals a version dropdown specific to that engine:

properties:
dbType:
title: Database type
type: string
enum:
- PostgreSQL
- MySQL
dependencies:
dbType:
allOf:
- if:
properties:
dbType:
const: PostgreSQL
then:
properties:
version:
type: number
enum: [13, 14, 15]
title: PostgreSQL version
default: 15
- if:
properties:
dbType:
const: MySQL
then:
properties:
version:
type: string
enum: ['5.7', '8.0']
title: MySQL version
default: '8.0'

Each `if`/`then` block in the `allOf` array matches one `enum` value. Selecting "PostgreSQL" shows the PostgreSQL version list; selecting "MySQL" replaces it with the MySQL version list.

### 5.7.3. Chaining multiple dynamic dependencies

You can define multiple `dependencies` in the same parameter step. Each dependency operates independently.

In this example, selecting "Yes" for the restart confirmation reveals a reason field, while enabling advanced options reveals additional technical fields:

dependencies:
showAdvanced:
allOf:
- if:
properties:
showAdvanced:
const: true
then:
properties:
maxSyncDelay:
type: number
title: Max sync delay (ms)
default: 500
serviceRestart:
allOf:
- if:
properties:
serviceRestart:
const: 'Yes'
then:
properties:
restartReason:
type: string
title: Reason for restart
description: Provide a reason for restarting the service.
default: Applying new configuration.
minLength: 10
errorMessage:
minLength: 'Provide a more detailed reason (at least 10 characters).'

Each key under `dependencies` corresponds to a property name in the same parameter step. When the user changes a field value, only the matching `if`/`then` branch is displayed.

## 5.8. Configuring the output section

The `output` section defines what users see after a template runs. You can display text messages, reference user input from `parameters`, show job execution data from `steps`, and provide external links.

The `output` section supports two types of content:

- **`text`:** Displays text blocks with titles and markdown content.
- **`links`:** Displays clickable buttons that open external URLs.

### 5.8.1. Output text

Use `output.text` to display information to the user after the template runs. Each text block has a `title` and `content` field. The `content` field supports markdown formatting.

output:
text:
- title: Request submitted
content: |
Your request has been submitted.

You can include multiple text blocks:

output:
text:
- title: Request submitted
content: |
Your deployment of **${{ parameters.app_name }}** has been submitted.

**Job ID:** ${{ steps['launch-job'].output.data.id }}
**Status:** ${{ steps['launch-job'].output.data.status }}

- title: Configuration summary
content: |
- Inventory: ${{ parameters.inventory }}
- Application: ${{ parameters.app_name }}

### 5.8.2. Output links

Use `output.links` to display clickable buttons. Each link has a `title` and `url` field. You can optionally set an `icon` field.

output:
links:
- title: Check Request Status
url: https://portal.example.com/requests/status
icon: help

You can reference step output data in link URLs:

output:
links:
- title: View job in Ansible Automation Platform
url: ${{ steps['launch-job'].output.data.url }}

You can include multiple links:

output:
links:
- title: View job in Ansible Automation Platform
url: ${{ steps['launch-job'].output.data.url }}
- title: RHEL documentation
url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/
icon: docs

### 5.8.3. Referencing parameters in output

You can reference any value the user entered in the `parameters` section by using the `${{ parameters.<field_name> }}` syntax.

The following table lists common parameter references:

**Table 5.3. Common parameter references**

| Reference | Description | Example output |
| --- | --- | --- |
| <br> `${{ parameters.app_name }}` | <br>  User-entered text field value | <br> `my-app` |
| <br> `${{ parameters.inventory }}` | <br>  User-selected Ansible Automation Platform resource name | <br> `Production Servers` |
| <br> `${{ parameters.credentials }}` | <br>  User-selected credentials (array) | <br> `["SSH Key", "AWS Credentials"]` |
| <br> `${{ parameters.environment }}` | <br>  User-selected enum value | <br> `production` |

#### 5.8.3.1. Example: Displaying user selections in the output

output:
text:
- title: Request submitted
content: |
Your request for **${{ parameters.app_name }}** has been submitted.

**Configuration:**
- Inventory: ${{ parameters.inventory }}
- Environment: ${{ parameters.environment }}

### 5.8.4. Referencing step output in output

After the `rhaap:launch-job-template` action runs, the step output includes job execution data. Reference this data using the `${{ steps['<step-id>'].output.data.<field> }}` syntax.

The `rhaap:launch-job-template` action returns the following output fields:

**Table 5.4. Output fields from rhaap:launch-job-template**

| Reference | Type | Description |
| --- | --- | --- |
| <br> `${{ steps['launch-job'].output.data.id }}` | <br>  number | <br>  Ansible Automation Platform Job ID. |
| <br> `${{ steps['launch-job'].output.data.status }}` | <br>  string | <br>  Ansible Automation Platform Job status (for example, `pending`, `running`, `successful`). |
| <br> `${{ steps['launch-job'].output.data.url }}` | <br>  string | <br>  Direct URL to the job in Ansible Automation Platform. |

#### 5.8.4.1. Example: Displaying job execution data in the output

output:
text:
- title: Job launched
content: |
**Job ID:** ${{ steps['launch-job'].output.data.id }}
**Status:** ${{ steps['launch-job'].output.data.status }}
links:
- title: View job in Ansible Automation Platform
url: ${{ steps['launch-job'].output.data.url }}

# Chapter 6. Providing feedback in self-service automation portal

Self-service automation portal provides a feedback form where you can suggest new features and content, as well as provide general feedback.

Note

The feedback form is disabled by default. If the **Feedback** button is not visible in the console, your administrator must enable it in the portal configuration.

1. Click **Feedback** in the self-service automation portal console to display the feedback form.


![Self-service automation portal feedback form](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_self-service_automation_portal-en-US/images/b6a52e77499334e9950b4b0c1c3ba861/rhdh-feedback-form.png)

2. Enter the feedback you want to provide.

3. Tick the **I understand that feedback is shared with Red Hat** checkbox.

4. Click **Submit**.

Note

To ensure that Red Hat receives your feedback, exclude your self-service automation portal URL in any browser ad blockers or privacy tools.

# Legal Notice

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
