+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_auto_generated_template_example"
title = "Auto-generated template example - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_auto_generated_template_example/aem-page/develop-ref_auto_generated_template_example.html"
last_crumb = "Auto-generated template example"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Auto-generated template example"
oversized = "false"
page_slug = "develop-ref_auto_generated_template_example"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_auto_generated_template_example"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_auto_generated_template_example/toc/toc.json"
type = "aem-page"
+++

# Auto-generated template example

The following example shows a template that Ansible automation portal auto-generates from an existing Ansible Automation Platform Job Template.

Every field in the generated YAML maps directly to an Ansible Automation Platform artifact:

- The Ansible Automation Platform Job Template name and description become `metadata` fields.
- Each **Prompt on Launch** option becomes an `AAPResourcePicker` field.
- Each Ansible Automation Platform Survey question becomes a standard form field.
- The `steps` section launches the original Ansible Automation Platform Job Template using the `rhaap:launch-job-template` action.

```
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  # Namespace is hardcoded to "default"
  namespace: default
  # AAP artifact: Job Template name -> lowercase with hyphens
  name: deploy-application
  # AAP artifact: Job Template name -> title (copied directly)
  title: Deploy Application
  # AAP artifact: Job Template description -> description (copied directly)
  description: Deploy application to target environment
  # AAP artifact: Job Template labels -> tags (lowercase)
  tags:
    - automation
    - aap
  # AAP artifact: Job Template URL -> annotations
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

        # AAP artifact: "Prompt on Launch" -> Inventory
        inventory:
          title: Inventory
          description: Please enter the inventory you want to use the services on
          resource: inventories
          ui:field: AAPResourcePicker
          default: Production Servers

        # AAP artifact: Survey question -> "Application Name"
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
```

## Field mapping

The following table maps each generated field to its Ansible Automation Platform source:

| Ansible Automation Platform source | Ansible Automation Platform value             | Generated field               | Transformation                                                                                   |
| ---------------------------------- | --------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------ |
| N/A                                | `default`                                     | `metadata.namespace`          | Hardcoded to `default`.                                                                          |
| Job Template > Name                | Deploy Application                            | `metadata.name`               | Lowercase with hyphens.                                                                          |
| Job Template > Name                | Deploy Application                            | `metadata.title`              | Copied directly.                                                                                 |
| Job Template > Description         | Deploy application to target environment      | `metadata.description`        | Copied directly.                                                                                 |
| Job Template > Labels              | `automation`, `aap`                           | `metadata.tags`               | Lowercase, special characters replaced with hyphens.                                             |
| Always present                     | OAuth2 token                                  | `parameters.token`            | Auto-populated and hidden from user.                                                             |
| Prompt on Launch > Inventory       | Production Servers                            | `parameters.inventory`        | `AAPResourcePicker`; user selects by name, resolved to Ansible Automation Platform ID at launch. |
| Survey > Question 1                | app\_name (text, required, default: "my-app") | `parameters.app_name`         | Variable, title, type, and default copied from Survey spec.                                      |
| Job Template > Name                | Deploy Application                            | `input.values.template`       | Identifies which Ansible Automation Platform Job Template to launch.                             |
| Prompt on Launch value             | `${{ parameters.inventory }}`                 | `input.values.inventory`      | Name resolved to Ansible Automation Platform ID at launch.                                       |
| Survey answers                     | `${{ parameters.app_name }}`                  | `input.values.extraVariables` | Passed as `extra_vars` to the Ansible Automation Platform Job.                                   |
