# 3. Working with templates
## 3.2. Understanding auto-generated templates
### 3.2.2. Auto-generated template example

The following example shows a template that self-service automation portal auto-generates from an existing Ansible Automation Platform Job Template. Every field in the generated YAML maps directly to an Ansible Automation Platform artifact:

- The Ansible Automation Platform Job Template name and description become `metadata` fields.
- Each **Prompt on Launch** option becomes an `AAPResourcePicker` field.
- Each Ansible Automation Platform Survey question becomes a standard form field.
- The `steps` section launches the original Ansible Automation Platform Job Template using the `rhaap:launch-job-template` action.

apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
# Namespace is hardcoded to "default"
namespace: default
# AAP artifact: Job Template name → lowercase with hyphens
name: deploy-application
# AAP artifact: Job Template name → title (copied directly)
title: Deploy Application
# AAP artifact: Job Template description → description (copied directly)
description: Deploy application to target environment
# AAP artifact: Job Template labels → tags (lowercase)
tags:
- automation
- aap
# AAP artifact: Job Template URL → annotations
annotations:
backstage.io/techdocs-ref: url:https://aap.example.com/#/templates/job_template/42
backstage.io/source-location: url:https://aap.example.com/#/templates/job_template/42

spec:
type: service

parameters:
- title: "Please enter the following details"
required:
- token
- inventory
- app_name
properties:
# Always present: OAuth token for AAP authentication (hidden from user)
token:
title: Token
type: string
description: Oauth2 token
ui:field: AAPTokenField
ui:widget: hidden
ui:backstage:
review:
show: false
ui:options:
disabled: true
hidden: true

# AAP artifact: "Prompt on Launch" → Inventory (users select by name; self-service portal resolves to AAP ID)
inventory:
title: Inventory
description: Please enter the inventory you want to use the services on
resource: inventories
ui:field: AAPResourcePicker
default: Production Servers

# AAP artifact: Survey question → "Application Name" (variable, title, type, default from survey spec)
app_name:
title: Application Name
description: Name of the application to deploy
type: string
default: my-app

steps:
- id: launch-job
# AAP artifact: Job Template name used as the step name
name: Deploy Application
action: rhaap:launch-job-template
input:
token: ${{ parameters.token }}
values:
# AAP artifact: Job Template name identifies which template to launch
template: Deploy Application
# "Prompt on Launch" values passed as launch parameters
inventory: ${{ parameters.inventory }}
# Survey answers passed as extra variables to AAP
extraVariables:
app_name: ${{ parameters.app_name }}

output:
text:
- title: Deploy Application template executed successfully
content: |
**Job ID:** ${{ steps['launch-job'].output.data.id }}
**Job status:** ${{ steps['launch-job'].output.data.status }}

The following table maps each generated field to its Ansible Automation Platform source:

**Table 3.1. Field mapping**

| Ansible Automation Platform source | Ansible Automation Platform value | Generated field | Transformation |
| --- | --- | --- | --- |
| <br>  N/A | <br> `default` | <br> `metadata.namespace` | <br>  Hardcoded to `default`. |
| <br>  Job Template → Name | <br>  Deploy Application | <br> `metadata.name` | <br>  Lowercase with hyphens. |
| <br>  Job Template → Name | <br>  Deploy Application | <br> `metadata.title` | <br>  Copied directly. |
| <br>  Job Template → Description | <br>  Deploy application to target environment | <br> `metadata.description` | <br>  Copied directly. |
| <br>  Job Template → Labels | <br> `automation`, `aap` | <br> `metadata.tags` | <br>  Lowercase, special characters replaced with hyphens. |
| <br>  Always present | <br>  OAuth2 token | <br> `parameters.token` | <br>  Auto-populated and hidden from user. |
| <br>  Prompt on Launch → Inventory | <br>  Production Servers | <br> `parameters.inventory` | <br> `AAPResourcePicker`; user selects by name, resolved to Ansible Automation Platform ID at launch. |
| <br>  Survey → Question 1 | <br>  app_name (text, required, default: "my-app") | <br> `parameters.app_name` | <br>  Variable, title, type, and default copied from Survey spec. |
| <br>  Job Template → Name | <br>  Deploy Application | <br> `input.values.template` | <br>  Identifies which Ansible Automation Platform Job Template to launch. |
| <br>  Prompt on Launch value | <br> `${{ parameters.inventory }}` | <br> `input.values.inventory` | <br>  Name resolved to Ansible Automation Platform ID at launch. |
| <br>  Survey answers | <br> `${{ parameters.app_name }}` | <br> `input.values.extraVariables` | <br>  Passed as `extra_vars` to the Ansible Automation Platform Job. |

