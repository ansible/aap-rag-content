+++
title = "Custom UI components and filters - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_custom_ui_components"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_custom_ui_components/aem-page/develop-ref_devtools_custom_ui_components.html"
last_crumb = "Custom UI components and filters"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Custom UI components and filters"
oversized = "false"
page_slug = "develop-ref_devtools_custom_ui_components"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_custom_ui_components"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_custom_ui_components/toc/toc.json"
type = "aem-page"
+++

# Custom UI components and filters

The **Ansible Backstage Plugins** provide custom UI components that enhance the software template experience by integrating directly with Ansible Automation Platform resource selection and authentication.

## `AAPTokenField`

The `AAPTokenField` is a secure authentication field used in backstage scaffolder templates. It automatically fetches and stores an Ansible Automation Platform OAuth2 token, which is then available for all rhaap:* actions, enabling seamless authentication.

 **AAPTokenField Properties**

The following table details the field's properties for use in a template's properties section.

| Property                        | Type        | Description                                                                                                                               |
| ------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `title`                    | <br>string  | <br>The label displayed in the UI (for example, "AAP Token"). Defaults to "AAP Token".                                                    |
| <br> `description`              | <br>string  | <br>A short help text displayed below the input field.                                                                                    |
| <br> `ui:field`                 | <br>string  | <br>Must be set to `AAPTokenField`. This setting instructs Backstage to render a custom react component instead of a default input field. |
| <br> `ui:backstage.review.show` | <br>boolean | <br>If `true`, this field appears in the **Review** step before scaffolding executes. The default value is `true`.                        |

 **Authentication flow and token management**

All `rhaap:*` actions require an OAuth2 token for authenticating with Ansible Automation Platform. The token is always stored in the Backstage secrets context as `aapToken` and referenced in template steps as `${{ secrets.aapToken }}`.

How the token reaches the secrets context depends on the deployment model:

- **Ansible automation portal (Create Task):** The portal automatically injects the token into `secrets.aapToken` when the user submits the form. You do not need to declare `AAPTokenField` in the template parameters — the token is handled transparently.
- **Ansible plug-ins for Red Hat Developer Hub:** The standard Backstage scaffolder does not auto-inject the token. You must include `AAPTokenField` in the template parameters to trigger the OAuth popup and populate `secrets.aapToken`.

Important:

Starting in Ansible Backstage Plugins v2.2.0, the portal no longer passes the OAuth token in template form values. Do not use `${{ parameters.token }}` in `rhaap:*` action steps — `AAPTokenField` stores a masked display value in form parameters. Always use `${{ secrets.aapToken }}` to access the real OAuth token.

When the RHAAP auth provider is used, the token is referenced in the workflow steps as shown:

```
- id: create-project
  action: rhaap:create-project
  input:
    token: ${{ secrets.aapToken }}
    # ... other inputs
```

 **Example**

The following example shows how to declare `AAPTokenField` for Ansible plug-ins for Red Hat Developer Hub deployments. For Ansible automation portal deployments, the authentication section is optional.

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
        token: ${{ secrets.aapToken }}
        ...
```

 **Error and validation handling**

All `rhaap:*` actions include built-in validation and user-friendly error reporting:

- Validation: If the token is missing or invalid, the action throws the error: "`Authorization token not provided`."
- Error Messages: Actions catch API client errors, extracting and surfacing meaningful messages without exposing stack traces.
- Workflow Safety: If a step fails due to authentication, subsequent steps are automatically skipped, ensuring a safe and predictable workflow.

## `AAPResourcePicker`

 `AAPResourcePicker` is a dynamic field for Backstage scaffolder templates. It fetches Ansible Automation Platform resources (like inventories or credentials) via the Ansible Automation Platform API, allowing users to select resources for their automation workflows.

 **AAPResourcePicker Properties**

The following table details the essential properties for configuring the resource picker in a template’s `properties` section.

| Property           | Type       | Description                                                                                                                                            |
| ------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br> `title`       | <br>string | <br>The label displayed in the UI (for example, "Inventory").                                                                                          |
| <br> `description` | <br>string | <br>A short help text shown below the field.                                                                                                           |
| <br> `ui:field`    | <br>string | <br>Must be set to `AAPResourcePicker`.                                                                                                                |
| <br> `resource`    | <br>string | <br>The specific Ansible Automation Platform (AAP) resource type to fetch and display (for example, `inventories`, `credentials`, or `organizations`). |
| <br> `idKey`       | <br>string | <br>The property name used to retrieve the resource ID (default: “id”).                                                                                |
| <br> `nameKey`     | <br>string | <br>The property name used to display the resource name in the list (default: “name”).                                                                 |
| <br> `type`        | <br>string | <br>Set to “array” for a multi-select field; omit this property for a single-select field.                                                             |

 **Example**

The following example demonstrates how to use the `AAPResourcePicker` to create a single-select field for choosing an **Inventory**.

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

## Custom filters

The plugins provide custom filters to extract specific properties from resource objects, which is essential for passing data between backstage steps.

| Filter                     | Purpose                                                                                       | Example Usage                                                        |
| -------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| <br> `resourceFilter`      | <br>Extracts a single, specific property from a resource object.                              | <br> `$!{{ parameters.organization | resourceFilter('name') }}`      |
| <br> `multiResourceFilter` | <br>Extracts a specific property from multiple resource objects (when the input is an array). | <br> `$!{{ parameters.organization | multiResourceFilter('name') }}` |
