# Create a custom resource for Resource Operator
## Create an automation controller inventory custom resource

By using an inventory file, Ansible Automation Platform can manage a large number of hosts with a single command.

### About this task

Inventories also help you use Ansible Automation Platform more efficiently by reducing the number of command line options you have to specify. For more information see [Inventories](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_inventories "Ansible Automation Platform works against a list of managed nodes or hosts in your infrastructure that are logically organized, using an inventory file. The installer inventory can specify your installation scenario and describe host deployments to Ansible.") .

### Procedure

Create an inventory on automation controller by creating an inventory custom resource:

```
metadata:
name: inventory-new
spec:
connection_secret: aap-access
description: my new inventory
name: newinventory
organization: Default
state: present
instance_groups:
- default
variables:
string: "string_value"
bool: true
number: 1
list:
- item1: true
- item2: "1"
object:
string: "string_value"
number: 2
```

