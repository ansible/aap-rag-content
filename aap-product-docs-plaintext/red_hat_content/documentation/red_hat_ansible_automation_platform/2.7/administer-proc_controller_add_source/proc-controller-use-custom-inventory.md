# Add a source to an inventory
## Source an inventory from a custom inventory plugin

This describes how to use the `servicenow.itsm` collection inventory plugin to sync inventory on Ansible Automation Platform.

### Procedure

1.  Create and sync a project using a Source Control Git repository that includes the following files:


```
>> requirements.yml
---
collections: - name: servicenow.itsm

>> inventories/myinventory.now.yml
# Create a file following the example below. It must have a configuration file extension ending in either "now.yml" or "now.yaml".
plugin: servicenow.itsm.now
query:
- os: = Linux Red Hat
- os: = Windows XP
keyed_groups:
- key: os
prefix: os
```
Note:
Refer to the official [Ansible documentation](https://console.redhat.com/ansible/automation-hub/repo/published/servicenow/itsm/content/inventory/now/) for detailed guidance on using and configuring the `servicenow.itsm.now` plugin.

2.  Create an inventory by setting the source to **Sourced from a Project**, selecting the new project, and choose `/(project root)` in the inventory file section.
3.  Synchronize the source in the inventory.

