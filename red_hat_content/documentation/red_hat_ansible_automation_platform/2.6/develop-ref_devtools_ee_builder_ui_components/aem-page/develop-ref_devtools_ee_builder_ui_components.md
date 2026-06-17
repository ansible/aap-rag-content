+++
title = "EE Builder custom UI components - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_devtools_ee_builder_ui_components"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_devtools_ee_builder_ui_components/aem-page/develop-ref_devtools_ee_builder_ui_components.html"
last_crumb = "EE Builder custom UI components"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "EE Builder custom UI components"
oversized = "false"
page_slug = "develop-ref_devtools_ee_builder_ui_components"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_devtools_ee_builder_ui_components"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_devtools_ee_builder_ui_components/toc/toc.json"
type = "aem-page"
+++

# EE Builder custom UI components

Custom UI components are available for use in Backstage Software Templates to provide specialized form fields for creating and configuring execution environment definitions.

To use a component in your template, set the `ui:field` property on a parameter:

```yaml
parameters:
  myField:
    type: string
    ui:field: BaseImagePicker
```

## BaseImagePicker

Displays a selection of pre-configured base container images for execution environment definitions. Includes an option to specify a custom image.

| Property    | Description                                                             |
| ----------- | ----------------------------------------------------------------------- |
| `ui:field`  | `BaseImagePicker`                                                       |
| `enum`      | Array of base image references, plus `custom` for a custom image entry. |
| `enumNames` | Display labels for each base image option.                              |


**Example:**

```yaml
baseImage:
  title: Base image
  type: string
  ui:field: BaseImagePicker
  enum:
    - registry.redhat.io/ansible-automation-platform/ee-minimal-rhel9:2.18
    - custom
  enumNames:
    - Red Hat Ansible Minimal EE - Ansible Core 2.18 (RHEL 9)
    - Custom Image
```

## CollectionsPicker

Provides an interactive interface for selecting Ansible collections to include in an execution environment. Supports searching and adding collections from private automation hub, Galaxy, and SCM repositories. Includes version selection and source management.

| Property   | Description                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------- |
| `ui:field` | `CollectionsPicker`                                                                          |
| `type`     | `array` (returns an array of collection objects with `name`, `version`, and `source` fields) |

## PackagesPicker

Enables adding Python packages or system packages to an execution environment definition. Supports direct entry and bulk addition through comma-separated values.

| Property   | Description                                        |
| ---------- | -------------------------------------------------- |
| `ui:field` | `PackagesPicker`                                   |
| `type`     | `array` (returns an array of package name strings) |

## FileUploadPicker

Provides a file upload interface for importing requirements files, such as `requirements.txt` for Python packages or `bindep.txt` for system packages. The file content is parsed and merged with manually entered values.

| Property   | Description                                     |
| ---------- | ----------------------------------------------- |
| `ui:field` | `FileUploadPicker`                              |
| `type`     | `string` (returns the file content as a string) |

## EEFileNamePicker

A text input field for specifying the execution environment definition name. Validates the name against existing EE definitions in the catalog to prevent duplicates and enforces naming conventions.

| Property   | Description        |
| ---------- | ------------------ |
| `ui:field` | `EEFileNamePicker` |
| `type`     | `string`           |

## EETagsPicker

Provides an interface for adding discovery tags to an execution environment definition. Tags help users find and categorize EE definitions in the catalog.

| Property   | Description                               |
| ---------- | ----------------------------------------- |
| `ui:field` | `EETagsPicker`                            |
| `type`     | `array` (returns an array of tag strings) |

## MCPServersPicker

Displays available Model Context Protocol (MCP) servers as selectable cards. Users can select which MCP servers to integrate with their execution environment.

| Property            | Description                                                          |
| ------------------- | -------------------------------------------------------------------- |
| `ui:field`          | `MCPServersPicker`                                                   |
| `type`              | `array` (returns an array of selected MCP server identifier strings) |
| `schema.items.enum` | Array of available MCP server identifiers.                           |

## ScmSelector

Provides a source control management (SCM) provider selector with built-in authentication. Users select a configured GitHub or GitLab instance, then authenticate through the SCM provider's OAuth flow. The component validates credentials and displays connection status.

| Property                                       | Description                                                                                                   |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `ui:field`                                     | `ScmSelector`                                                                                                 |
| `type`                                         | `string` (returns the selected SCM provider identifier)                                                       |
| `ui:options.providers`                         | Array of provider configuration objects with `label`, `provider` (`github` or `gitlab`), and optional `host`. |
| `ui:options.requestUserCredentials.secretsKey` | Key used to store the authenticated SCM token in template secrets.                                            |

## AdditionalBuildStepsPicker

Provides an interface for specifying custom build steps to include in the execution environment build process. Supports multiple build phases with command entry.

| Property   | Description                                                                            |
| ---------- | -------------------------------------------------------------------------------------- |
| `ui:field` | `AdditionalBuildStepsPicker`                                                           |
| `type`     | `array` (returns an array of build step objects with `stepType` and `commands` fields) |


**Available build step phases:**

| Phase             | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| `prepend_base`    | Commands to run before base image dependencies are installed. |
| `append_base`     | Commands to run after base image dependencies are installed.  |
| `prepend_galaxy`  | Commands to run before Galaxy collections are installed.      |
| `append_galaxy`   | Commands to run after Galaxy collections are installed.       |
| `prepend_builder` | Commands to run before builder dependencies are installed.    |
| `append_builder`  | Commands to run after builder dependencies are installed.     |
| `prepend_final`   | Commands to run before the final image stage.                 |
| `append_final`    | Commands to run after the final image stage.                  |
