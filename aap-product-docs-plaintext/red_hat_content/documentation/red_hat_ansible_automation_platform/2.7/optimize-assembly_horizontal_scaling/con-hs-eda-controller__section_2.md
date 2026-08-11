# Horizontally scale in Event-Driven Ansible
## Horizontal scaling in Event-Driven Ansible controller
### Inventory file updates for containerized installations

The following example shows how you can set up an inventory file for horizontal scaling of Event-Driven Ansible controller on Red Hat Enterprise Linux VMs using the host group name `[automationeda]` and the node type variable `eda_type`:

```
[automationeda]
3.88.116.111 routable_hostname=automationeda-api.example.com eda_type=api

# event-stream node
3.88.116.112 routable_hostname=automationeda-event-stream.example.com eda_type=event-stream

# worker node
3.88.116.113 routable_hostname=automationeda-worker.example.com eda_type=worker
```

