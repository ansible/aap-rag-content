# AAP resource picker fields

Use `ui:field: AAPResourcePicker` to let users select Ansible Automation Platform resources by name. Ansible automation portal queries the Ansible Automation Platform API and displays available resources in a picker.

Set the `resource` property to specify the Ansible Automation Platform resource type.

The following table lists supported `resource` values:

| `resource` value | Ansible Automation Platform resource type | Selection mode               |
| ---------------- | ----------------------------------------- | ---------------------------- |
| `inventories`    | Inventories                               | Single-select                |
| `credentials`    | Credentials                               | Multi-select (`type: array`) |
| `organizations`  | Organizations                             | Single-select                |

## Single-select example (inventory)

```
inventory:
title: Inventory
description: Select target inventory.
resource: inventories
ui:field: AAPResourcePicker
default: Production Servers
```

## Multi-select example (credentials)

```
credentials:
title: Credentials
description: Select credentials for accessing the target hosts.
type: array
resource: credentials
ui:field: AAPResourcePicker
default:
- SSH Key
- AWS Credentials
```
