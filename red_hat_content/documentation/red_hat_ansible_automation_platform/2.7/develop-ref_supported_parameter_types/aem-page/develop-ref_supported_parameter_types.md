+++
title = "Supported parameter types - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_supported_parameter_types"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_supported_parameter_types/aem-page/develop-ref_supported_parameter_types.html"
last_crumb = "Supported parameter types"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Supported parameter types"
oversized = "false"
page_slug = "develop-ref_supported_parameter_types"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_supported_parameter_types"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_supported_parameter_types/toc/toc.json"
type = "aem-page"
+++

# Supported parameter types

Templates support standard Backstage parameter types and widgets. Ansible automation portal adds Ansible Automation Platform-specific field types for resource selection and authentication.

Templates support standard Backstage parameter types (`string`, `number`, `integer`, `boolean`, `array`) and widgets (`textarea`, `select`, `checkboxes`, `hidden`). For a complete reference of standard types and widgets, see the [Backstage Software Templates documentation](https://backstage.io/docs/features/software-templates/input-examples).

Ansible automation portal adds the following Ansible Automation Platform-specific field types:

| Type                                          | Widget                                                      | Description                                                           | Example use case                            |
| --------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------- |
| `ui:field: AAPTokenField`                     | Hidden token field                                          | OAuth2 authentication token, auto-populated and hidden from the user. | Always present in auto-generated templates. |
| `resource` + `ui:field: AAPResourcePicker`    | Ansible Automation Platform resource picker (single-select) | Select one Ansible Automation Platform resource by name.              | Inventory, organization.                    |
| `type: array` + `ui:field: AAPResourcePicker` | Ansible Automation Platform resource picker (multi-select)  | Select multiple Ansible Automation Platform resources by name.        | Credentials.                                |


These Ansible Automation Platform-specific fields are documented in detail in [AAP resource picker fields](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_aap_resource_picker_fields "Use ui:field: AAPResourcePicker to let users select Ansible Automation Platform resources by name. Ansible automation portal queries the Ansible Automation Platform API and displays available resources in a picker.").
