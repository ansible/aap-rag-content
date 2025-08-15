# 3. Credential types
## 3.2. Creating a new credential type




You can create a credential type to use with a source plugin that you select based on the supported, default credential types. You can make your credential type available to a team or individuals.

**Procedure**

1. Log in to the Ansible Automation Platform Dashboard.
1. From the navigation panel, selectAutomation Decisions→Infrastructure→Credential Types.
1. ClickCreate credential type.
1. Insert the following:


1. In the **Input Configuration** field, specify an input schema that defines a set of ordered fields for that type. The format can be in YAML or JSON:

**YAML**


```
fields:      - type: string        id: username        label: Username      - type: string        id: password        label: Password        secret: true    required:      - username      - password
```

View more YAML examples at the [YAML page](https://yaml.org/spec/1.2.2/) .

**JSON**


```
{    "fields": [      {      "type": "string",      "id": "username",      "label": "Username"      },      {      "secret": true,      "type": "string",      "id": "password",      "label": "Password"       }      ],     "required": ["username", "password"]    }
```

View more JSON examples at [The JSON website](https://www.json.org/json-en.html) .


1. In the **Injector Configuration** field, enter environment variables or extra variables that specify the values a credential type can inject. The format can be in YAML or JSON (see examples in the previous step).

The following configuration in JSON format shows each field and how they are used:


```
{        "extra_vars": {          "some_extra_var": "{{ username }}:{{ password }}"      }    }
```


1. ClickCreate credential type.

Your newly created credential type is displayed in the list of credential types.


1. Click theEdit credential type![Edit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_decisions-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
icon to modify the credential type options.


**Verification**

- Verify that the newly created credential type can be selected from the **Credential Type** list when creating a new credential.


**Next steps**

- On the **Edit** page, you can modify the details or delete the credential.
- If the **Delete** option is disabled, this means that the credential type is being used by a credential, and you must delete the credential type from all the credentials that use it before you can delete it.


**Additional resources**

[Setting up credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-credentials#eda-set-up-credential) .


