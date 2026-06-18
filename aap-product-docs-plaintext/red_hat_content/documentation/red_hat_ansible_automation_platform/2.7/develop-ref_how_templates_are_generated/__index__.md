# How templates are generated

When synchronization runs, Ansible automation portal reads Ansible Automation Platform Job Template configurations and generates corresponding templates.

## Metadata mapping

The following table shows how Ansible Automation Platform Job Template properties are mapped to template metadata fields:

| Ansible Automation Platform Job Template property | Generated template field | Transformation                                                   |
| ------------------------------------------------- | ------------------------ | ---------------------------------------------------------------- |
| Name                                              | `metadata.name`          | Converted to lowercase with hyphens                              |
| Name                                              | `metadata.title`         | Copied directly                                                  |
| Description                                       | `metadata.description`   | Copied directly                                                  |
| Labels                                            | `metadata.tags`          | Converted to lowercase, special characters replaced with hyphens |
| N/A                                               | `metadata.namespace`     | Hardcoded to `default`                                           |

## Parameter mapping

The following table shows how Ansible Automation Platform Job Template sources are mapped to template parameters:

| Ansible Automation Platform Job Template source | Generated template parameter type                                    |
| ----------------------------------------------- | -------------------------------------------------------------------- |
| Survey questions                                | Standard form fields (`type: string`, `enum`, `ui:widget`)           |
| "Prompt on Launch" options                      | `AAPResourcePicker` fields for Ansible Automation Platform resources |

## Field order

Ansible automation portal generates form fields from two sources in the Ansible Automation Platform Job Template configuration. Fields appear in the following order:

1. **OAuth token (hidden):** Auto-populated with the user's authentication token. This field is always present and always hidden.
2. **"Prompt on Launch" fields:** Each enabled "Prompt on Launch" option becomes an `AAPResourcePicker` field. Users select Ansible Automation Platform resources by name (Inventories, Credentials, Execution Environments). Ansible automation portal resolves names to Ansible Automation Platform internal IDs at launch time.
3. **Survey questions:** Each survey question becomes a form field with the matching input type (`text`, `dropdown`, `password`, `textarea`, `integer`, `float`, `multiplechoice`, `multiselect`).

## Defaults and required fields

- Survey question defaults and required/optional settings are preserved from the Ansible Automation Platform Job Template Survey.
- "Prompt on Launch" fields use the current Ansible Automation Platform Job Template settings for defaults and required/optional status.
- Ansible Automation Platform resource picker fields display resource names, not internal IDs.
