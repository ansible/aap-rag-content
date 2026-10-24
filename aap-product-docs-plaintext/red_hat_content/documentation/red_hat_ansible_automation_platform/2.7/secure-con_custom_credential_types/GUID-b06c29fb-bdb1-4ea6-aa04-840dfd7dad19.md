# Create custom credentials for Event-Driven Ansible
## Create a new credential type

Build a reusable credential type template to enforce consistent input fields and authentication mechanisms for custom integrations across your organization.placeholder

### Procedure

1. From the navigation panel, select Automation Decisions> (and then)Infrastructure> (and then)Credential Types.
2. In the Credential Types view, click Create credential type.
3. Insert the following:


Name
Insert the name of your custom credential.

Description
This field is optional.

4. In the **Input configuration** field, specify an input schema that defines a set of ordered fields for that type. The format can be in YAML or JSON:
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

5. In the **Injector Configuration** field, enter environment variables or extra variables that specify the values a credential type can inject. The format can be in YAML or JSON (see examples in the previous step).

The following configuration in JSON format shows each field and how they are used:

```
{
"extra_vars": {
"some_extra_var": "{{ username }}:{{ password }}"
}
}
```

6. Click Create credential type. Your newly created credential type is displayed in the list of credential types.

7. Click the Edit ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png) icon to modify the credential type options.

