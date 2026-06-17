# 3. Working with templates
## 3.2. Understanding auto-generated templates
### 3.2.3. How templates are generated

When synchronization runs, self-service automation portal reads Ansible Automation Platform Job Template configurations and generates corresponding templates. self-service automation portal maps Ansible Automation Platform Job Template properties to template fields as follows.

#### 3.2.3.1. Metadata mapping

The following table shows how Ansible Automation Platform Job Template properties are mapped to template metadata fields:

**Table 3.2. Metadata mapping**

| Ansible Automation Platform Job Template property | Generated template field | Transformation |
| --- | --- | --- |
| <br>  Name | <br> `metadata.name` | <br>  Converted to lowercase with hyphens |
| <br>  Name | <br> `metadata.title` | <br>  Copied directly |
| <br>  Description | <br> `metadata.description` | <br>  Copied directly |
| <br>  Labels | <br> `metadata.tags` | <br>  Converted to lowercase, special characters replaced with hyphens |
| <br>  N/A | <br> `metadata.namespace` | <br>  Hardcoded to `default` |

#### 3.2.3.2. Parameter mapping

The following table shows how Ansible Automation Platform Job Template sources are mapped to template parameters:

**Table 3.3. Parameter mapping**

| Ansible Automation Platform Job Template source | Generated template parameter type |
| --- | --- |
| <br>  Survey questions | <br>  Standard form fields (`type: string`, `enum`, `ui:widget`) |
| <br>  "Prompt on Launch" options | <br> `AAPResourcePicker` fields for Ansible Automation Platform resources |

#### 3.2.3.3. Field order

self-service automation portal generates form fields from two sources in the Ansible Automation Platform Job Template configuration. Fields appear in the following order:

1. **OAuth token (hidden):** Auto-populated with the user’s authentication token. This field is always present and always hidden.
2. **"Prompt on Launch" fields:** Each enabled "Prompt on Launch" option becomes an `AAPResourcePicker` field. Users select Ansible Automation Platform resources by name (Inventories, Credentials, Execution Environments). self-service automation portal resolves names to Ansible Automation Platform internal IDs at launch time.
3. **Survey questions:** Each survey question becomes a form field with the matching input type (`text`, `dropdown`, `password`, `textarea`, `integer`, `float`, `multiplechoice`, `multiselect`).

#### 3.2.3.4. Defaults and required fields

- Survey question defaults and required/optional settings are preserved from the Ansible Automation Platform Job Template Survey.
- "Prompt on Launch" fields use the current Ansible Automation Platform Job Template settings for defaults and required/optional status.
- Ansible Automation Platform resource picker fields display resource names, not internal IDs.

