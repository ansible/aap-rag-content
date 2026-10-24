# Create custom credentials for Event-Driven Ansible
## Input configuration

You can configure the input fields and define which parameters are required when a user creates a credential of this custom type.

The Input configuration has two attributes:

- fields - a collection of properties for a credential type.
- required - a list of required fields.

Fields can have multiple properties, depending on the credential type you select.

*Table 1. Input Configuration Field Properties*

| Fields     | Description                                                                | Mandatory (Y/N)       |
| ---------- | -------------------------------------------------------------------------- | --------------------- |
| id         | Unique id of the field; must be a string type and stores the variable name | Yes                   |
| type       | Can be string or boolean type                                              | No, default is string |
| label      | Used by the UI when rendering the UI element                               | Yes                   |
| secret     | Will be encrypted                                                          | No, default false     |
| multiline  | If the field contains data from a file the multiline can be set to True    | No, default false     |
| help\_text | The help text associated with this field                                   | No                    |

