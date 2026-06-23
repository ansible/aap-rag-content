# Resource Operator custom resources
## Resource Operator custom resources [tower.ansible.com/v1alpha1]
### AnsibleInventory

Creates an inventory on the automation controller.

| Field               | Type   | Description                                                                                             | Default   |
| ------------------- | ------ | ------------------------------------------------------------------------------------------------------- | --------- |
| `connection_secret` | String | Name of the Kubernetes secret containing the platform gateway connection details. Required.             | -         |
| `name`              | String | Display name for the inventory.                                                                         | -         |
| `description`       | String | Description of the inventory.                                                                           | -         |
| `organization`      | String | Organization the inventory belongs to.                                                                  | -         |
| `state`             | String | Desired state of the inventory. Options: `present`, `absent`.                                           | `present` |
| `instance_groups`   | Array  | List of instance groups to associate with the inventory.                                                | -         |
| `variables`         | Object | Inventory variables as key-value pairs. Supports strings, booleans, numbers, lists, and nested objects. | -         |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleInventory
metadata:
name: inventory-new
spec:
connection_secret: aap-access
name: newinventory
organization: Default
state: present
variables:
env: production
region: us-east-1
```

