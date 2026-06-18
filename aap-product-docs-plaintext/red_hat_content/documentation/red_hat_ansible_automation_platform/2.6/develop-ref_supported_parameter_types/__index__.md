# Supported parameter types

Templates support standard Backstage parameter types and widgets. Ansible automation portal adds Ansible Automation Platform-specific field types for resource selection and authentication.

Templates support standard Backstage parameter types (`string`, `number`, `integer`, `boolean`, `array`) and widgets (`textarea`, `select`, `checkboxes`, `hidden`). For a complete reference of standard types and widgets, see the [Backstage Software Templates documentation](https://backstage.io/docs/features/software-templates/input-examples).

Ansible automation portal adds the following Ansible Automation Platform-specific field types:

| Type                                          | Widget                                                      | Description                                                           | Example use case                            |
| --------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------- |
| `ui:field: AAPTokenField`                     | Hidden token field                                          | OAuth2 authentication token, auto-populated and hidden from the user. | Always present in auto-generated templates. |
| `resource` + `ui:field: AAPResourcePicker`    | Ansible Automation Platform resource picker (single-select) | Select one Ansible Automation Platform resource by name.              | Inventory, organization.                    |
| `type: array` + `ui:field: AAPResourcePicker` | Ansible Automation Platform resource picker (multi-select)  | Select multiple Ansible Automation Platform resources by name.        | Credentials.                                |


These Ansible Automation Platform-specific fields are documented in detail in [AAP resource picker fields](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_aap_resource_picker_fields "Use ui:field: AAPResourcePicker to let users select Ansible Automation Platform resources by name. Ansible automation portal queries the Ansible Automation Platform API and displays available resources in a picker.").
