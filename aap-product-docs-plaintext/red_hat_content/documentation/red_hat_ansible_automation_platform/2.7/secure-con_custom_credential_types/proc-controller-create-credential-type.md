# Create custom credentials for Event-Driven Ansible
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

![New credential type](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/credential-types-new-listed.png)

7.  Click the Edit ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png) icon to modify the credential type options.  Note:
In the **Edit** screen, you can modify the details or delete the credential. If the **Delete** option is disabled, this means that the credential type is being used by a credential, and you must delete the credential type from all the credentials that use it before you can delete it.

### Results

- Verify that the newly created credential type can be selected from the **Credential Type** selection window when creating a new credential:


![Verify new credential type](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/credential-types-new-listed-verify.png)

