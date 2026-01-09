# 15. Supported Inventory plugin templates
## 15.7. OpenStack




The OpenStack inventory plugin integrates with OpenStack clouds to dynamically generate Ansible inventories based on the current state of the cloud resources.

```
expand_hostvars: true
fail_on_errors: true
inventory_hostname: uuid
plugin: openstack.cloud.openstack
```

