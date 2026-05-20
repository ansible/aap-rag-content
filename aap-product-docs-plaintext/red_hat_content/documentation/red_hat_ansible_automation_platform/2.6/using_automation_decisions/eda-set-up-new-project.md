# 4. Projects
## 4.1. Setting up a new project

Set up a project to connect Event-Driven Ansible controller to a Git repository, enabling it to pull, sync, and manage the rulebooks used by your automation.

**Prerequisites**

- You are logged in to the Ansible Automation Platform Dashboard as a Content Consumer.
- You have set up a credential, if necessary. For more information, see the [Setting up credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-credentials#eda-set-up-credential) section.
- You have an existing repository containing rulebooks.

**Procedure**

1. Log in to the Ansible Automation Platform Dashboard.

2. Navigate to **Automation Decisions → Projects**.

3. Click Create project.

4. Insert the following:



Name
Enter project name.

Description
This field is optional.

Source control type
Git is the only source control type available for use. This field is optional.

Source control URL
Enter Git, SSH, or HTTP[S] protocol address of a repository, such as GitHub or GitLab. This required field is editable. See [Editing a project](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-projects#eda-editing-a-project) to view details of how editing this field impacts rulebook activations.


Note
This field accepts SSH private key or private key phrase. To enable the use of these private keys, your project URL must begin with `git@`.

Proxy
This is used to access HTTP or HTTPS servers. This field is optional and editable. See [Editing a project](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-projects#eda-editing-a-project) to view details of how editing this field impacts rulebook activations.

Source control branch/tag/commit
This is the branch to checkout. In addition to branches, you can input tags, commit hashes, and arbitrary refs. Some commit hashes and refs may not be available unless you also provide a custom refspec. This field is optional and editable. See [Editing a project](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-projects#eda-editing-a-project) to view details of how editing this field impacts rulebook activations.

Source control refspec
A refspec to fetch (passed to the Ansible git module). This parameter allows access to references via the branch field not otherwise available. This field is optional and editable. See [Editing a project](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-projects#eda-editing-a-project) to view details of how editing this field impacts rulebook activations.

Source control credential
This is an optional credential used to authenticate with the provided Source control URL.

Content signature validation credential
Enable content signing to verify that the content has remained secure when a project is synced. If the content has been tampered with, the job will not run. This field is optional.

Options
The Verify SSL option is enabled by default. Enabling this option verifies the SSL with HTTPS when the project is imported.


Note
You can disable this option if you have a local repository that uses self-signed certificates.

5. Select Create project.

**Results**

Your project is now created and can be managed in the **Projects** page.

After saving the new project, the project’s details page is displayed. From there or the **Projects** list view, you can edit or delete it.

