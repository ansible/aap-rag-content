# Organize rulebooks for event-driven automation

Projects are a logical collection of rulebooks. They must be a git repository and located in the path defined for Event-Driven Ansible content in Ansible collections: `/extensions/eda/rulebooks` at the root of the project.

Important:

Event-Driven Ansible controller uses PostgreSQL for data storage and background task workers via the `dispatcherd `service. When the workers are unavailable, you will not be able to create or sync projects, or enable rulebook activations.

## Set up a new project

Set up a project to connect Event-Driven Ansible controller to a Git repository, enabling it to pull, sync, and manage the rulebooks used by your automation.

### Before you begin

- You are logged in to the Ansible Automation Platform Dashboard as a Content Consumer.
- You have set up a credential, if necessary. For more information, see the [Setting up credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_eda_set_up_credential#eda-set-up-credential "Create a credential to securely store sensitive data (like tokens and passwords) required for rulebook activations to connect to source plugins or private registries.") section.
- You have an existing repository containing rulebooks.

### Procedure

1.  Log in to the Ansible Automation Platform Dashboard.
2.  Navigate to **Automation Decisions> (and then)Projects**.
3.  Click Create project.
4.  Insert the following:


Name
Enter project name.

Description
This field is optional.

Organization
Enter your organization’s name or select Default from the list.

Source control type
Git is the only source control type available for use. This field is optional.

Source control URL
Enter Git, SSH, or HTTP[S] protocol address of a repository, such as GitHub or GitLab. This required field is editable. See [Editing a project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_projects#eda-editing-a-project "Edit project details (like the source repository URL or credential) to manage where Event-Driven Ansible fetches its rulebooks from and how it authenticates.") to view details of how editing this field impacts rulebook activations.

Note:
This field accepts SSH private key or private key phrase. To enable the use of these private keys, your project URL must begin with `git@`.

Proxy
This is used to access HTTP or HTTPS servers. This field is optional and editable. See [Editing a project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_projects#eda-editing-a-project "Edit project details (like the source repository URL or credential) to manage where Event-Driven Ansible fetches its rulebooks from and how it authenticates.") to view details of how editing this field impacts rulebook activations.

Source control branch/tag/commit
This is the branch to checkout. In addition to branches, you can input tags, commit hashes, and arbitrary refs. Some commit hashes and refs may not be available unless you also provide a custom refspec. This field is optional and editable. See [Editing a project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_projects#eda-editing-a-project "Edit project details (like the source repository URL or credential) to manage where Event-Driven Ansible fetches its rulebooks from and how it authenticates.") to view details of how editing this field impacts rulebook activations.

Source control refspec
A refspec to fetch (passed to the Ansible git module). This parameter allows access to references via the branch field not otherwise available. This field is optional and editable. See [Editing a project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_projects#eda-editing-a-project "Edit project details (like the source repository URL or credential) to manage where Event-Driven Ansible fetches its rulebooks from and how it authenticates.") to view details of how editing this field impacts rulebook activations.

Source control credential
This is an optional credential used to authenticate with the provided Source control URL.

Content signature validation credential
Enable content signing to verify that the content has remained secure when a project is synced. If the content has been tampered with, the job will not run. This field is optional.

Options
- **Update revision on launch** - This checkbox is optional. Enabling it updates the project prior to starting or restarting a rulebook activation. For more information on how this option impacts your rulebook activations, see [Update revision on launch for projects](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_projects#GUID-a3765204-d569-4016-9af9-adcbcb4f13eb "The Update revision on launch option automatically syncs projects with source control. This ensures rulebook activations run the most current content, eliminating manual updates and the risk of outdated execution."). When you select this option, the Option Details section is displayed with the following field:
* **Cache Timeout** - This is the time in seconds to consider a project as current. During job runs and callbacks, the task system will evaluate the timestamp of the latest project update. If it is older than your Cache Timeout, it is not considered current, and a new project update is performed. For more information, see [Cache Timeout in Event-Driven Ansible project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_projects#GUID-cdc75060-9922-4d8e-9eb0-55bd38440abb "The cache timeout setting controls how long Event-Driven Ansible controller reuses a previous project synchronization result before performing a new sync operation.").
- **Verify SSL** - The Verify SSL option is enabled by default. Enabling this option verifies the SSL with HTTPS when the project is imported. Note:
You can disable this option if you have a local repository that uses self-signed certificates.

5.  Select Create project.

### Results

Your project is now created and can be managed in the **Projects** page.

After saving the new project, the project’s details page is displayed. From there or the **Projects** list view, you can edit or delete it.

## Projects list view

The Projects list view provides a quick dashboard to verify rulebook sync status, track content via the Git hash, and manage repository access.

Note:

If a rulebook changes in source control, you can re-sync a project by selecting the sync icon next to the project from the **Projects** list view. The **Git hash** updates represent the latest commit on that repository. An activation must be restarted or recreated if you want to use the updated project.

## Edit a project

Edit project details (like the source repository URL or credential) to manage where Event-Driven Ansible fetches its rulebooks from and how it authenticates.

### Procedure

1.  From the **Projects** list view, select the More Actions icon **⋮** next to the desired project. The Edit page is displayed.
2.  Edit the desired fields. Important:
When you update a project’s **Source control URL**, **Source control branch/tag/commit**, or **Source control refspec**, Event-Driven Ansible automatically triggers a project resync. This process updates the rulebooks available within Event-Driven Ansible controller and can significantly impact existing rulebook activations:

- **Rulebook Content Updates**: Running activations continue to use old content when a rulebook’s content changes. To apply the newer content, you must restart the affected rulebook activation. If the rulebook content you update is attached to an activation that uses event streams, you must re-attach the event stream to that activation after the updates are applied and then, restart the activation.
- **New Rulebooks**: Any new rulebook added to the repository becomes available in the database after the sync.
- **Deleted Rulebooks**: A removed rulebook is deleted from the database upon sync. Its associated activations, however, continue to run and can be restarted. Review and update any activations detached from their source rulebook.

3.  Select Save project.

## Delete a project

Use the platform gateway interface to delete a project that is no longer required from Event-Driven Ansible controller.

### Before you begin

1. A project is not currently linked to any rulebook activation.

### About this task

Note:

You cannot delete a project if it is still being used by a rulebook activation.

### Procedure

1.  To delete a project, complete one of the following:

- From the **Projects** list view, select the checkbox next to the desired project, and click the More Actions icon **⋮** from the page menu.
- From the **Projects** list view, click the More Actions icon **⋮** next to the desired project.

2.  Select Delete project.
3.  In the **Permanently delete projects** window, select Yes, I confirm that I want to delete this project.
4.  Select Delete project.

## Update revision on launch for projects

The **Update revision on launch** option automatically syncs projects with source control. This ensures rulebook activations run the most current content, eliminating manual updates and the risk of outdated execution.

Selecting automatic synchronization can ensure the following benefits:

- Rulebook activations that use the latest code from source control
- Reduction in manual intervention and potential for human error
- Consistent behavior with automation controller project management
- Prevention of production delays caused by manual sync requirements

When you enable project synchronization, Event-Driven Ansible controller completes the following tasks:

1. Checks the remote source control repository for updates
2. Synchronizes the project to the current revision
3. Updates cached rulebooks, roles, and collections
4. Launches or restarts the rulebook activation with updated content


Important:

Event-Driven Ansible controller uses PostgreSQL for data storage and background task workers via the `dispatcherd` service. When the workers are unavailable, you will not be able to create or sync projects, or enable rulebook activations.

### Cache Timeout in Event-Driven Ansible projects

The cache timeout setting controls how long Event-Driven Ansible controller reuses a previous project synchronization result before performing a new sync operation.

Use cache timeout when:

- Multiple rulebook activations use the same project
- Activations launch or restart in rapid succession
- You want to avoid redundant synchronization operations
- Source control repository has rate limiting or performance constraints

When you configure cache timeout, the following occurs:

1. Synchronization request fetches content from source control
2. Result is cached for the specified timeout duration
3. Subsequent synchronization requests within the timeout period use cached content
4. After timeout expires, next synchronization request fetches fresh content

## Project and rulebook activation settings interdependencies

Project and activation settings are interdependent. The Update revision on launch and Auto-restart on project update configurations combine to determine auto-restart behaviors and trigger specific user confirmation prompts.

*Table 1. Project and rulebook activation settings interdependencies*

| **Triggered by**                         | **Project State**                          | **Activation State**                          | **Resulting Behavior**                                                                                                                                             |
| ---------------------------------------- | ------------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Rulebook activation started or restarted | Enabled (Update revision on launch **ON**) | Enabled or Disabled                           | A message informs you that the project is configured to update on restart, which might impact other activations sharing this project. You must confirm to proceed. |
| Rulebook activation started or restarted | Disabled (Update revision on launch OFF)   | Enabledor Disabled                            | A standard message is displayed for the user to confirm they want to restart the rulebook activation.                                                              |
| Project synced                           | Enabled or Disabled                        | Enabled (Auto-restart on project update ON)   | A message informs you that the associated rulebook activation is configured to restart when this project syncs. You must confirm the sync.                         |
| Project synced                           | Enabled or Disabled                        | Disabled (Auto-restart on project update OFF) | A standard message is displayed for the user to confirm they want to sync the project.                                                                             |
