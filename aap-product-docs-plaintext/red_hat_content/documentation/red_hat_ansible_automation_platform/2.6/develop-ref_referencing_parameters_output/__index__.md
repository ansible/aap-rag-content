# Reference parameters in output

You can reference any value the user entered in the `parameters` section by using the `${{ parameters.<field_name> }}` syntax.

The following table lists common parameter references:

| Reference                       | Description                                             | Example output                   |
| ------------------------------- | ------------------------------------------------------- | -------------------------------- |
| `${{ parameters.app_name }}`    | User-entered text field value                           | `my-app`                         |
| `${{ parameters.inventory }}`   | User-selected Ansible Automation Platform resource name | `Production Servers`             |
| `${{ parameters.credentials }}` | User-selected credentials (array)                       | `["SSH Key", "AWS Credentials"]` |
| `${{ parameters.environment }}` | User-selected enum value                                | `production`                     |

## Displaying user selections in the output

```
output:
text:
- title: Request submitted
content: |
Your request for **${{ parameters.app_name }}** has been submitted.

**Configuration:**
- Inventory: ${{ parameters.inventory }}
- Environment: ${{ parameters.environment }}
```
