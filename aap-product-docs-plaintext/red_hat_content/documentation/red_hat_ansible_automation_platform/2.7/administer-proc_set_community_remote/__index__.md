# Configure the private automation hub community remote

Configure the community remote so you can sync content from Ansible Galaxy.

## Before you begin

- You have a `requirements.yml` file that identifies those collections to synchronize from Ansible Galaxy as in the following example:     **Requirements.yml example**

```
collections:
# Install a collection from Ansible Galaxy.
- name: community.aws
version: 5.2.0
source: https://galaxy.ansible.com
```

## About this task

You can edit the **community** remote repository to synchronize chosen collections from Ansible Galaxy to your private automation hub. By default, your private automation hub community repository directs to `galaxy.ansible.com/api/`.

## Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Remotes.
3.  In the **Details** tab in the **Community** remote, click Edit remote.
4.  In the **YAML requirements** field, paste the contents of your `requirements.yml` file.
5.  Click Save remote.

## Results

You can now synchronize collections identified in your `requirements.yml` file from Ansible Galaxy to your private automation hub.

## What to do next

See [Synchronizing content collections](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_create_synclist "You can sync certified and validated collections in Ansible automation hub from console.redhat.com.")for syncing steps.
