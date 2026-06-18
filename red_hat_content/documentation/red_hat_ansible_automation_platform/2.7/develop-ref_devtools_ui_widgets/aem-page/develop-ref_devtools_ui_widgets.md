+++
template = "docs/aem-title.html"
title = "Standard UI widgets - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_ui_widgets"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_ui_widgets/aem-page/develop-ref_devtools_ui_widgets.html"
last_crumb = "Standard UI widgets"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Standard UI widgets"
oversized = "false"
page_slug = "develop-ref_devtools_ui_widgets"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_ui_widgets"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_devtools_ui_widgets/toc/toc.json"
type = "aem-page"
+++

# Standard UI widgets

Standard UI widgets provide enhanced components for user forms to capture various types of input.

## Textarea widget

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

## Select widget

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

## Checkboxes widgets

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

## Hidden widget

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

## Standard UI widgets

Standard UI widgets provide enhanced components for user forms to capture various types of input.

### Textarea widget

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

### Select widget

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

### Checkboxes widgets

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

### Hidden widget

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

## Standard UI widgets

Standard UI widgets provide enhanced components for user forms to capture various types of input.

### Textarea widget

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

### Select widget

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

### Checkboxes widgets

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

### Hidden widget

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

## Standard UI widgets

Standard UI widgets provide enhanced components for user forms to capture various types of input.

### Textarea widget

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

### Select widget

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

### Checkboxes widgets

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

### Hidden widget

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

## Standard UI widgets

Standard UI widgets provide enhanced components for user forms to capture various types of input.

### Textarea widget

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

### Select widget

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

### Checkboxes widgets

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

### Hidden widget

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
