# Horizontally scale in Event-Driven Ansible
## Horizontal scaling in Event-Driven Ansible controller
### Inventory file updates for RPM-based installations (VMs)

The following example shows how you can set up an inventory file for horizontal scaling of Event-Driven Ansible controller on Red Hat Enterprise Linux VMs using the host group name `[automationedacontroller]` and the node type variable `eda_node_type`:

```
[automationedacontroller]

3.88.116.111 routable_hostname=automationedacontroller-api.example.com eda_node_type=api

# worker node
3.88.116.112 routable_hostname=automationedacontroller-api.example.com eda_node_type=worker
```

