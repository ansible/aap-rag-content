# Organize rulebooks for event-driven automation
## Set up a new project
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

