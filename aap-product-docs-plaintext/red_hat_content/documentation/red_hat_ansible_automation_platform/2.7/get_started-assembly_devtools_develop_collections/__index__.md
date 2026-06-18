# Package and distribute automation content with collections

Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. Red Hat provides Ansible Content Collections on Ansible automation hub that contain both Red Hat Ansible Certified Content and Ansible validated content.

If you have installed private automation hub, you can create collections for your organization and push them to private automation hub so that you can use them in job templates in Ansible Automation Platform. You can use collections to package and distribute plug-ins. These plug-ins are written in Python.

You can also create collections to package and distribute Ansible roles, which are expressed in YAML. You can also include playbooks and custom plug-ins that are required for these roles in the collection. Typically, collections of roles are distributed for use within your organization.

## Publish to a collection

You can configure your projects to be uploaded to Git, or to the source control manager of your choice.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects.
2.  Locate or create the project that you want to publish to your source control manager.
3.  In the project **Details** tab, select **Edit project**.
4.  Select **Git** from the **Source Control Type** drop-down menu.
5.  Enter the appropriate details into the following fields:
1.  **Source Control URL** - see an example in the tooltip.
2.  Optional: **Source control branch/tag/commit**: Enter the SCM branch, tags, commit hashes, arbitrary refs, or revision number (if applicable) from the source control to checkout. Some commit hashes and references might not be available unless you also provide a custom refspec in the next field. If left blank, the default is `HEAD`, which is the last checked out branch, tag, or commit for this project.
3.  **Source Control Refspec** - This field is an option specific to Git source control and only advanced users familiar and comfortable with Git should specify which references to download from the remote repository. For more information, see [Job branch overriding](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_controller_job_branch_overriding#controller-job-branch-overriding "In automation controller, you can configure projects to allow job templates to override the branch, tag, or reference used for source control.").
4.  **Source Control Credential** - If authentication is required, select the appropriate source control credential.
6.  Optional: **Options** - select the launch behavior, if applicable:
1.  **Clean** - Removes any local modifications before performing an update.
2.  **Delete** - Deletes the local repository in its entirety before performing an update. Depending on the size of the repository this can significantly increase the amount of time required to complete an update.
3.  **Track submodules** - Tracks the latest commit. See the tooltip for more information.
4.  **Update Revision on Launch** - Updates the revision of the project to the current revision in the remote source control, and caches the roles directory from [Collections support](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_collections_support#ref-projects-collections-support "Automation controller supports project-specific Ansible collections in job runs."). Automation controller ensures that the local revision matches and that the roles and collections are up-to-date with the last update. In addition, to avoid job overflows if jobs are spawned faster than the project can synchronize, selecting this enables you to configure a cache timeout to cache previous project synchronizations for a given number of seconds.
5.  **Allow Branch Override** - Enables a job template or an inventory source that uses this project to start with a specified SCM branch or revision other than that of the project. For more information, see [Job branch overriding](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_controller_job_branch_overriding#controller-job-branch-overriding "In automation controller, you can configure projects to allow job templates to override the branch, tag, or reference used for source control.").
7.  Click Save to save your project.

## Upload a collection to automation hub

If you want to share a collection that you have created with the rest of the Ansible community, you can upload it to automation hub.

### Before you begin

- You have configured the `ansible-galaxy` client for automation hub.
- You have at least one namespace.
- You have run all content through `ansible-test sanity`

### About this task

Note:

Sharing a collection with the Ansible community requires getting the collection certified or validated by our Partner Engineering team. This action is available only to partner clients. For more about becoming a partner, see our [documentation on software certification](https://connect.redhat.com/en/partner-resources/software-certification-documentation).

You can upload your collection by using either the automation hub user interface or the `ansible-galaxy` client.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Namespaces.
2.  Within the My namespaces tab, locate and click into the namespace to which you want to upload a collection.
3.  Select the **Collections** tab, and then click Upload collection.
4.  In the New collection modal, click **Select file**. Locate the file on your system.
5.  Click Upload.
6.  Optional: you can also upload from the command line. Using the `ansible-galaxy` client, enter the following command:


```bash
$ ansible-galaxy collection publish path/to/my_namespace-my_collection-1.0.0.tar.gz --api-key=SECRET
```
