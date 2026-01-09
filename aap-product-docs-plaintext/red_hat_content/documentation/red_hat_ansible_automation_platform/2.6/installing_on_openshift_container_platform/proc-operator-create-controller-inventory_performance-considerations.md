# 13. Ansible Automation Platform Resource Operator
## 13.5. Create custom resources for Resource Operator
### 13.5.7. Creating an automation controller inventory custom resource




By using an inventory file, Ansible Automation Platform can manage a large number of hosts with a single command.

Inventories also help you use Ansible Automation Platform more efficiently by reducing the number of command line options you have to specify. For more information see the [Inventories](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-inventories) section of the _Using automation execution_ guide.

**Procedure**

- Create an inventory on automation controller by creating an inventory custom resource:


```
metadata:      name: inventory-new    spec:      connection_secret: controller-access      description: my new inventory      name: newinventory      organization: Default      state: present      instance_groups:        - default      variables:        string: "string_value"        bool: true        number: 1        list:          - item1: true          - item2: "1"        object:          string: "string_value"          number: 2
```




