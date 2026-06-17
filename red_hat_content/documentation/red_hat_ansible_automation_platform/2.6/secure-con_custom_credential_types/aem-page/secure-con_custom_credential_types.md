+++
title = "Create custom credentials for Event-Driven Ansible - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_custom_credential_types"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials/", "Configure credentials for Event-Driven Ansible"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_custom_credential_types/aem-page/secure-con_custom_credential_types.html"
last_crumb = "Create custom credentials for Event-Driven Ansible"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Create custom credentials for Event-Driven Ansible"
oversized = "false"
page_slug = "secure-con_custom_credential_types"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-con_custom_credential_types"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_custom_credential_types/toc/toc.json"
type = "aem-page"
+++

# Create custom credentials for Event-Driven Ansible

Create custom credential types (via JSON/YAML) to define unique security fields and logic, enabling support for proprietary event sources or specialized authentication.

Each credential type displays its own unique configurations in the **Input Configuration** and the **Injector Configuration** fields, if applicable. Both YAML and JSON formats are supported in the configuration fields.

Custom credentials support Ansible extra variables as a means of injecting their authentication information.

You can attach one or more cloud, vault, and Red Hat Ansible Automation Platform credential types to a rulebook activation.

 Note:

- When creating a new credential type, you must avoid collisions in the `extra_vars`.
- Extra variable names must not start with **EDA_** because they are reserved.
- You must have System administrator (superuser) permissions to be able to create and edit a credential type and to be able to view the **Injector configuration** field.

When you customize your own credential types, they display on the Credential Types page along with a list of built-in credential types.

## Input configuration

You can configure the input fields and define which parameters are required when a user creates a credential of this custom type.

The Input configuration has two attributes:

- fields - a collection of properties for a credential type.
- required - a list of required fields.


Fields can have multiple properties, depending on the credential type you select.

*Table 1. Input Configuration Field Properties*

| Fields         | Description                                                                    | Mandatory (Y/N)           |
| -------------- | ------------------------------------------------------------------------------ | ------------------------- |
| <br>id         | <br>Unique id of the field; must be a string type and stores the variable name | <br>Yes                   |
| <br>type       | <br>Can be string or boolean type                                              | <br>No, default is string |
| <br>label      | <br>Used by the UI when rendering the UI element                               | <br>Yes                   |
| <br>secret     | <br>Will be encrypted                                                          | <br>No, default false     |
| <br>multiline  | <br>If the field contains data from a file the multiline can be set to True    | <br>No, default false     |
| <br>help\_text | <br>The help text associated with this field                                   | <br>No                    |

## Injector configuration

You can use Injector configuration to safely transform and map credential data from input fields so that it can be correctly exposed and consumed by `ansible-rulebook` at runtime.

Event-Driven Ansible supports the following types of injectors:

- Environment variables (`env`) - Used in source plugins for the underlying package or shared library.
- Ansible extra variables (`extra_vars`) - Used for substitution in the rulebook conditions, actions or source plugin parameters.
- File-based templating (`file`) - Used to create file contents from the credential inputs such as certificates and keys, which might be required by source plugins. File injectors provide a way to deliver these certificates and keys to ansible-rulebook at runtime without having to store them in decision environments. As a result, ansible-rulebook creates temporary files and the file names can be accessed using `eda.filename` variables, which are automatically created for you after the files have been created (for instance, "{{eda.filename.my_cert}}”).


 Important:

When creating `extra_vars` in rulebook activations and credential type injectors, avoid using `eda` or `ansible` as key names since that conflicts with internal usage and might cause failure in both rulebook activations and credential type creation.

Injectors enable you to adjust the fields so that they can be injected into a rulebook as one of the above-mentioned injector types, which cannot have duplicate keys at the top level. If you have two sources in a rulebook that both require parameters such as username and password, the injectors, along with the rulebook, help you adapt the arguments for each source.

## Creating a new credential type

Define a custom credential type by using a YAML or JSON schema. Defining these custom types helps ensure that authentication information is securely injected into automation workflows.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Credentials.
2.  In the **Credential Types** view, click Create credential type.
3.  Enter the appropriate details in the **Name** and **Description** field.  Note:
      When creating a new credential type, do not use reserved variable names that start with `ANSIBLE_` for the **INPUT** and **INJECTOR** names and IDs, as they are invalid for custom credential types.

4.  In the **Input configuration** field, specify an input schema that defines a set of ordered fields for that type. The format can be in YAML or JSON:
       **YAML**

```
fields:
  - type: string
    id: username
    label: Username
  - type: string
    id: password
    label: Password
    secret: true
required:
  - username
  - password
```
    View more YAML examples at the [YAML page](https://yaml.org/spec/1.2.2/).

     **JSON**

```
{
"fields": [
  {
  "type": "string",
  "id": "username",
  "label": "Username"
  },
  {
  "secret": true,
  "type": "string",
  "id": "password",
  "label": "Password"
   }
  ],
 "required": ["username", "password"]
}
```
    View more JSON examples at [The JSON website](https://www.json.org/json-en.html).

    The following configuration in JSON format shows each field and how they are used:

```
{
  "fields": [{
    "id": "api_token",    # required - a unique name used to reference the field value

    "label": "API Token", # required - a unique label for the field

    "help_text": "User-facing short text describing the field.",

    "type": ("string" | "boolean")   # defaults to 'string'

    "choices": ["A", "B", "C"]   # (only applicable to `type=string`)

    "format": "ssh_private_key"  # optional, can be used to enforce data format validity
                                 for SSH private key data (only applicable to `type=string`)

    "secret": true,       # if true, the field value will be encrypted

    "multiline": false    # if true, the field should be rendered as multi-line for input entry
                          # (only applicable to `type=string`)
},{
    # field 2...
},{
    # field 3...
}],

    "required": ["api_token"]   # optional; one or more fields can be marked as required
},
```
    When `type=string`, fields can optionally specify multiple choice options:

```
{
  "fields": [{
      "id": "api_token",    # required - a unique name used to reference the field value
      "label": "API Token", # required - a unique label for the field
      "type": "string",
      "choices": ["A", "B", "C"]
  }]
},
```

5.  In the **Injector configuration** field, enter environment variables or extra variables that specify the values a credential type can inject. The format can be in YAML or JSON (see examples in the previous step). The following configuration in JSON format shows each field and how they are used:

```
{
  "file": {
      "template": "[mycloud]\ntoken={{ api_token }}"
  },
  "env": {
      "THIRD_PARTY_CLOUD_API_TOKEN": "{{ api_token }}"
  },
  "extra_vars": {
      "some_extra_var": "{{ username }}:{{ password }}"
  }
}
```
    Credential Types can also generate temporary files to support `.ini` files or certificate or key data:

```
{
  "file": {
      "template": "[mycloud]\ntoken={{ api_token }}"
  },
  "env": {
      "MY_CLOUD_INI_FILE": "{{ tower.filename }}"
  }
}
```
    In this example, automation controller writes a temporary file that has:

```
[mycloud]\ntoken=SOME_TOKEN_VALUE
```
    The absolute file path to the generated file is stored in an environment variable named `MY_CLOUD_INI_FILE`.

    The following is an example of referencing many files in a custom credential template:

     **Inputs**

```
{
  "fields": [{
    "id": "cert",
    "label": "Certificate",
    "type": "string"
  },{
    "id": "key",
    "label": "Key",
    "type": "string"
  }]
}
```
     **Injectors**

```
{
  "file": {
    "template.cert_file": "[mycert]\n{{ cert }}",
    "template.key_file": "[mykey]\n{{ key }}"
},
"env": {
    "MY_CERT_INI_FILE": "{{ tower.filename.cert_file }}",
    "MY_KEY_INI_FILE": "{{ tower.filename.key_file }}"
}
}
```

6.  Click Create credential type. Your newly created credential type is displayed on the list of credential types:

     ![New credential type](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/credential-types-new-listed.png)

7.  Click the Edit ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png) icon to modify the credential type options.  Note:
      In the **Edit** screen, you can modify the details or delete the credential. If the **Delete** option is disabled, this means that the credential type is being used by a credential, and you must delete the credential type from all the credentials that use it before you can delete it.

### Results

- Verify that the newly created credential type can be selected from the **Credential Type** selection window when creating a new credential:


 ![Verify new credential type](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/credential-types-new-listed-verify.png)

## Event-Driven Ansible Rule Engine credential type

The Event-Driven Ansible Rule Engine credential type configures database connections for event persistence. If deployed during installation, the installer automatically creates a default credential so event persistence functions immediately.

You can create your own *custom* Rule Engine credential only if your environment requires the following:

- **External database** - Use this to point to an external PostgreSQL instance if you did *not* deploy the built-in event persistence database.
- **Encryption required** - Use this to configure encryption keys for sensitive event data. The default Rule Engine credential does not support encryption.

The Event-Driven Ansible Rule Engine credential type includes the following fields:

**Database connection settings**
The host, port, database name, and user credentials necessary for authentication with the PostgreSQL instance assigned to event persistence.

**Encryption settings**
The specific encryption keys that provide security for sensitive event data stored within the database.

### Create an Event-Driven Ansible Rule Engine credential

Create a custom Event-Driven Ansible Rule Engine credential to connect to external PostgreSQL databases or to enable encryption for sensitive event data.

#### Before you begin

- You are logged in to Event-Driven Ansible controller as an administrator
- If using an external database, you have:
  * A PostgreSQL database instance configured for event persistence
  * Database connection details (host, port, database name)
  * Database credentials (username, password)

#### Procedure

1.  Log in to the Ansible Automation Platform Dashboard.
2.  From the navigation panel, select Automation Decisions> (and then)Infrastructure> (and then)Credentials.
3.  Click Create credential.
4.  Insert the following:
  

Name
Enter a name for the credential (for example, “External Event Persistence Database” or “Encrypted Event Persistence”)

Description
This field is optional.

Organization
Select an organization from the list. If you have not created custom organizations, select **Default**.

Credential type
Select Event-Driven Ansible Rule Engine.

5.  Configure the database connection fields:
  

Postgres DB Host
Enter the hostname or IP address of your PostgreSQL database.

Postgres DB Port
Enter the database port (default: `5432`).

Postgres DB Name
Enter the database name for event persistence.

Postgres DB User
Enter the database username.

Postgres DB Password
Enter the database password.

6. **Optional:** Configure encryption settings:
  

Primary Encryption Secret
Used to derive AES keys for database encryption. For key rotations, enter your new secret here and re-enter your previous secret into the Secondary Encryption Secret field to maintain access to historical events. Must be at least 12 characters.  Important:
  Only the derived key is stored in our system. You must remember your original secret. If lost, an Activation reset is required.

Secondary Encryption Secret
This field is used during key rotation to maintain access to legacy data. When updating your Primary Encryption Secret, you must manually re-enter your previous secret here. This allows the system to decrypt historical records while using the new string for future events. If left blank, the system assumes no rotation has occurred. Must be at least 12 characters.  Important:
  Configure encryption keys if your events contain sensitive information such as passwords, API tokens, or personally identifiable information (PII). The default Rule Engine credential does not support encryption.

7.  Click Save.

### Assign your new Event-Driven Ansible Rule Engine credential type to rulebook activations

Assign your custom Rule Engine credential to a rulebook activation to enable external database connectivity or data encryption. This ensures your automation uses specific security and storage configurations to persist event history effectively.

#### Procedure

1.  Log in to Ansible Automation Platform.
2.  Navigate to the Automation Decisions> (and then)Rulebook Activations
3.  Click Enable event persistence in the activation options.
4.  In the Rule Engine credential field, select your custom credential.
5.  Save your rulebook activation.

#### Results

Matched events from this activation will be stored in the database specified by your Rule Engine credential.

#### What to do next

After configuring event persistence with your Rule Engine credential:

1. Start a rulebook activation.
2. Verify that events are being stored by performing the following actions:
  1. Check the activation logs for database connection success messages.
  2. Verify events appear in the Rule Audit (unless **Skip audit events is enabled**).
  3. Restart the activation and confirming event processing resumes without data loss.
