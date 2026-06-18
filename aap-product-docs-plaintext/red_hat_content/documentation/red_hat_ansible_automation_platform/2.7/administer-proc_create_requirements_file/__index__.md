# Create a requirements file

Use a requirements file to add collections to your automation hub.

## About this task

Requirements files are in YAML format and list the collections that you want to install in your automation hub. A standard `requirements.yml` file contains the following parameters:

- `name`: the name of the collection formatted as `<namespace>.<collection_name>`
- `version`: the collection version number

## Procedure

Create your requirements file.

In YAML format, collection information in your requirements file should contain the following information:

```bash
collections:
- name: namespace.collection_name
version: 1.0.0
```

## Example

Be sure to specify the collection version number, otherwise you will sync all collection versions. Syncing all versions can require more space than expected.

## What to do next

To sync the collections in your requirements file, follow the steps in [Synchronizing content collections](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_create_synclist "You can sync certified and validated collections in Ansible automation hub from console.redhat.com.").
