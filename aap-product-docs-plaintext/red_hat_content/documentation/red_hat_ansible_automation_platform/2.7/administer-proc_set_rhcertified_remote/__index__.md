# Configure the rh-certified remote repository

You can edit the **rh-certified** remote repository to synchronize collections from automation hub hosted on console.redhat.com to your private automation hub.

## Before you begin

- You have valid **Modify Ansible repo content** permissions.
- You have retrieved the Sync URL and API Token from the automation hub hosted service on console.redhat.com.
- You have configured access to port 443. This is required for synchronizing certified collections. For more information, see the automation hub table in the "Network ports and protocols" chapter of Planning your installation.

## About this task

By default, your private automation hub `rh-certified` repository includes the URL for the entire group of Ansible Certified Content Collections.

To use only those collections specified by your organization, a private automation hub administrator can upload manually-created requirements files from the `rh-certified` remote.

If you have collections `A`, `B`, and `C` in your requirements file, and a new collection `X` is added to console.redhat.com that you want to use, you must add `X` to your requirements file for private automation hub to synchronize it.

## Procedure

1.  Log in to your Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Remotes.
3.  In the **rh-certified** remote repository, click Edit remote.
4.  In the **URL** field, paste the **Sync URL**.
5.  In the **Token** field, paste the token you acquired from console.redhat.com.
6.  Click Save remote.

## Results

You can now synchronize collections from console.redhat.com to your private automation hub.

## What to do next

See [Synchronizing Ansible content collections in automation hub](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_create_synclist "You can sync certified and validated collections in Ansible automation hub from console.redhat.com.") for syncing steps.
