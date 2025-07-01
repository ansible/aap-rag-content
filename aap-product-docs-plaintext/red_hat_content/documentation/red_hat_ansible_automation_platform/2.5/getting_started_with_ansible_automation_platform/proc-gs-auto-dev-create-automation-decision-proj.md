# 3. Getting started as an automation developer
## 3.10. Creating an automation decision project




Like automation execution projects, automation decision projects are logical collections of automation decision content. You can use the project function to organize your automation decision content in a way that makes sense to you.

**Prerequisites**

- You have set up any neccessary credentials. For more information, see the [Setting up credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-credentials#eda-set-up-credential) section of the Using automation decisions guide.
- You have an existing repository containing rulebooks that are integrated with playbooks contained in a repository to be used by automation controller.


**Procedure**

1. From the navigation panel, select **Automation Decisions→Projects** .
1. ClickCreate project.
1. Enter the following information:


-  **Name** : Enter project name.
-  **Description** : This field is optional.
-  **Organization** : Select the organization associated with the project.
-  **Source control type** : Git is the only SCM type available for use.
-  **Proxy** : Proxy used to access HTTP or HTTPS servers.
-  **Source control branch/tag/commit** : Branch to checkout. Can also be tags, commit hashes, or arbitrary refs.
-  **Source control refspec** : A refspec to fetch. This parameter allows access to references through the branch field not otherwise available.
- Optional: **Source control credential** : The token needed to use the source control URL.
-  **Content signature validation credential** : Enables content signing to verify that the content has remained secure during project syncing. If the content is tampered with, the job will not run.
-  **Options** : Checking the box next to **Verify SSL** verifies the SSL with HTTPS when the project is imported.

1. ClickCreate project.


Your project is now created and can be managed in the **Projects** screen.

After saving the new project, the project’s details page is displayed. From there or the **Projects** list view, you can edit or delete it.

