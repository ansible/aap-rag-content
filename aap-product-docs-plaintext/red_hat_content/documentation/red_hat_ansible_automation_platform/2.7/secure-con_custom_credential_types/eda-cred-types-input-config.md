# Create custom credentials for Event-Driven Ansible
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

