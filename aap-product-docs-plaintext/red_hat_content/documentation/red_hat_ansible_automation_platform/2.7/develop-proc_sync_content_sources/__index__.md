# Synchronize content sources

Sync content from your configured Git repositories and private automation hub to keep the Ansible automation portal catalog current.

## Before you begin

- You have configured content sources. See [Configure collection discovery sources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery "Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog.").
- You have configured authentication. See [Configure a GitHub App for content discovery](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder "Create and install a GitHub App so that execution environment builder can scan your organization's repositories for Ansible collections.") or [Set up GitLab integration](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_gitlab_ee_builder "Configure GitLab content discovery and OAuth so that execution environment builder can scan GitLab groups for Ansible collections and save definition files.").
- You have applied configuration changes. See [Apply configuration changes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes "Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.").
- As an AAP administrator, you have access to automation portal.

## About this task

After syncing, discovered collections and EE definitions become available for users to browse and use in execution environment builder.

## Procedure

1.  Navigate to the **Collections** page.
2.  Click **Sync Now** in the top-right corner.
3.  In the modal, select the content sources you want to sync.
You can sync selectively by provider, host, or organization rather than syncing all sources at once.

Note:
Synchronization time depends on the number of collections and metadata in your configured repositories. Large repositories can take significantly longer. To reduce sync time, configure your private automation hub to sync only the collections your teams need.

4.  Click **Sync Selected**.

Note:
A toast notification confirms which sources are syncing. The **Sync Now** button is disabled during the operation and re-enabled when all selected sources finish.

## Results

- Navigate to **Collections** and verify that collections from your synced sources appear.
- Navigate to **Execution Environments** and verify that EE definitions from synced repositories appear in the catalog.

## What to do next

**Automatic synchronization**

Content sources sync automatically based on the schedule configured in [Configure collection discovery sources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery "Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog."). The `schedule.frequency` parameter controls how often each source is scanned for changes.

To adjust the sync frequency, modify the schedule values in your content source configuration and apply the updated Helm chart. See [Apply configuration changes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes "Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.").
