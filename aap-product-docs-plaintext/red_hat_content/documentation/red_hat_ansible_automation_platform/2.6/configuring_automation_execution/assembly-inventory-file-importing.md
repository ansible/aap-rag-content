# Chapter 5. Inventory File Importing




With automation controller you can select an inventory file from source control, rather than creating one from scratch.

The files are non-editable, and as inventories are updated at the source, the inventories within the projects are also updated accordingly, including the `group_vars` and `host_vars` files or directory associated with them. SCM types can consume both inventory files and scripts. Both inventory files and custom inventory types use scripts.

Imported hosts have a description of _imported_ by default. This can be overridden by setting the `_awx_description` variable on a given host. For example, if importing from a sourced `.ini` file, you can add the following host variables:

```
[main]
127.0.0.1 _awx_description="my host 1"
127.0.0.2 _awx_description="my host 2"
```

Similarly, group descriptions also default to _imported_ , but can also be overridden by `_awx_description` .

To use old inventory scripts in source control, see [Export old inventory scripts](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/controller-inventories#ref-controller-export-old-scripts) in _Using automation execution_ .

