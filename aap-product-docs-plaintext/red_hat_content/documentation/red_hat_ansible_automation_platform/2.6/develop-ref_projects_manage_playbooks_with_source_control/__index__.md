# Configure playbooks to use source control management (SCM) systems

Choose one of the following options when managing playbooks by using source control:

-  [SCM Types - Configuring playbooks to use Git and Subversion](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_projects_manage_playbooks_with_source_control#proc-scm-git-subversion "Configure automation controller projects to synchronize Ansible playbooks directly from Git and Subversion. Integrating with Source Control Management supports collaboration and helps ensure you always deploy the latest automation code.")
-  [SCM Type - Configuring playbooks to use Red Hat Lightspeed](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_projects_manage_playbooks_with_source_control#proc-scm-insights "Configure your projects to retrieve Ansible playbooks directly from Red Hat Lightspeed. Integrate with Red Hat Lightspeed to manage and deploy remediation playbooks identified through its analysis of your Red Hat Enterprise Linux environment.")
-  [SCM Type - Configuring playbooks to use a remote archive](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_projects_manage_playbooks_with_source_control#proc-scm-remote-archive "Playbooks that use a remote archive enable projects to be based on a build process that produces a versioned artifact, or release, containing all the requirements for that project in a single archive.")

## Configure playbooks to use Git and Subversion SCM types

Configure automation controller projects to synchronize Ansible playbooks directly from Git and Subversion. Integrating with Source Control Management supports collaboration and helps ensure you always deploy the latest automation code.

### About this task

By following these steps, you can ensure your environment always uses the latest version of your playbooks directly from your chosen SCM.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects.
2.  Click the project name you want to use.
3.  In the project **Details** tab, click Edit project.
4.  Select the appropriate option (Git or Subversion) from the **Source control type** menu.
5.  Enter the appropriate details into the following fields:

- **Source control URL** - See an example in the tooltip .
- Optional: **Source control branch/tag/commit**: Enter the SCM branch, tags, commit hashes, arbitrary refs, or revision number (if applicable) from the source control (Git or Subversion) to checkout. Some commit hashes and references might not be available unless you also give a custom refspec in the next field. If left blank, the default is `HEAD` which is the last checked out Branch, Tag, or Commit for this project.
- **Source control refspec** - This field is an option specific to git source control and only advanced users familiar and comfortable with git should specify which references to download from the remote repository. For more information, see [Job branch overriding](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-con_controller_job_branch_overriding#controller-job-branch-overriding "In automation controller, you can configure projects to allow job templates to override the branch, tag, or reference used for source control.").
- **Source control credential** - If authentication is required, select the appropriate source control credential.

6.  Optional: **Options** - select the launch behavior, if applicable:

- **Clean** - Removes any local modifications before performing an update.
- **Delete** - Deletes the local repository in its entirety before performing an update. Depending on the size of the repository this can significantly increase the amount of time required to complete an update.
- **Track submodules** - Tracks the latest commit. There is more information in the tooltip ![tooltip](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/question-circle.png).
- **Update revision on launch** - Updates the revision of the project to the current revision in the remote source control, and caching the roles directory from [Ansible Galaxy support](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_projects_manage_playbooks_with_source_control#ref-projects-galaxy-support "At the end of a project update, automation controller searches for the requirements.yml file in the roles directory, located at &lt;project-top-level-directory&gt;/roles/requirements.yml.") or [Collections support](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_projects_collections_support#ref-projects-collections-support "Automation controller supports project-specific Ansible collections in job runs."). Automation controller ensures that the local revision matches and that the roles and collections are up-to-date with the last update. In addition, to avoid job overflows if jobs are spawned faster than the project can synchronize, selecting this enables you to configure a Cache Timeout to cache previous project synchronizations for a given number of seconds.
- **Allow branch override** - Enables a job template or an inventory source that uses this project to start with a specified SCM branch or revision other than that of the project. For more information, see [Job branch overriding](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-con_controller_job_branch_overriding#controller-job-branch-overriding "In automation controller, you can configure projects to allow job templates to override the branch, tag, or reference used for source control.").

7.  Click Save project.

## Configure playbooks to use Red Hat Lightspeed

Configure your projects to retrieve Ansible playbooks directly from Red Hat Lightspeed. Integrate with Red Hat Lightspeed to manage and deploy remediation playbooks identified through its analysis of your Red Hat Enterprise Linux environment.

### About this task

This integration streamlines the process of addressing identified vulnerabilities and optimizing system configurations, ensuring your automation aligns with best practices and security recommendations.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects.
2.  Click the project name you want to use.
3.  In the project **Details** tab, click Edit project.
4.  Select **Red Hat Lightspeed** from the **Source Control Type** menu.
5.  In the **Red Hat Lightspeed credential** field, select the appropriate credential for use with Red Hat Lightspeed, as Red Hat Lightspeed requires a credential for authentication.
6.  Optional: In the **Options** field, select the launch behavior, if applicable:

- **Clean** - Removes any local modifications before performing an update.
- **Delete** - Deletes the local repository in its entirety before performing an update. Depending on the size of the repository this can significantly increase the amount of time required to complete an update.
- **Update revision on launch** - Updates the revision of the project to the current revision in the remote source control, and caches the roles directory from [Ansible Galaxy support](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_projects_manage_playbooks_with_source_control#ref-projects-galaxy-support "At the end of a project update, automation controller searches for the requirements.yml file in the roles directory, located at &lt;project-top-level-directory&gt;/roles/requirements.yml.") or [Collections support](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_projects_collections_support#ref-projects-collections-support "Automation controller supports project-specific Ansible collections in job runs."). Automation controller ensures that the local revision matches, and that the roles and collections are up-to-date. If jobs are spawned faster than the project can synchronize, selecting this enables you to configure a Cache Timeout to cache previous project synchronizations for a certain number of seconds, to avoid job overflow.

7.  Click Save project.

## Configure playbooks to use a remote archive

Playbooks that use a remote archive enable projects to be based on a build process that produces a versioned artifact, or release, containing all the requirements for that project in a single archive.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects.
2.  Click the project name you want to use.
3.  In the project **Details** tab, click Edit project.
4.  Select **Remote Archive** from the **Source control type** menu.
5.  Enter the appropriate details into the following fields:

- **Source control URL** - requires a URL to a remote archive, such as a *GitHub Release* or a build artifact stored in *Artifactory* and unpacks it into the project path for use.
- **Source control credential** - If authentication is required, select the appropriate source control credential.

6.  Optional: In the **Options** field, select the launch behavior, if applicable:

- **Clean** - Removes any local modifications before performing an update.
- **Delete** - Deletes the local repository in its entirety before performing an update. Depending on the size of the repository this can significantly increase the amount of time required to complete an update.
- **Update revision on launch** - Not recommended. This option updates the revision of the project to the current revision in the remote source control, and caches the roles directory from [Ansible Galaxy support](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_projects_manage_playbooks_with_source_control#ref-projects-galaxy-support "At the end of a project update, automation controller searches for the requirements.yml file in the roles directory, located at &lt;project-top-level-directory&gt;/roles/requirements.yml.") or [Collections support](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_projects_collections_support#ref-projects-collections-support "Automation controller supports project-specific Ansible collections in job runs.").
- **Allow branch override** - Not recommended. This option enables a job template that uses this project to launch with a specified SCM branch or revision other than that of the project’s.  Note:
Since this source control type is intended to support the concept of unchanging artifacts, it is advisable to disable Galaxy integration (for roles, at a minimum).

7.  Click Save project.

## Updating projects from source control

Regularly updating your projects ensures your Ansible Automation Platform environment is synchronized with the latest versions of playbooks, roles, and collections from your integrated SCM repositories.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects.
2.  Click the sync ![Sync](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/sync.png) icon next to the project that you want to update.  Note:
Immediately after adding a project setup to use source control, a sync starts that fetches the project details from the configured source control.

- Click the project’s status under the **Status** column for further information about the update process.

### Results

This brings you to the **Output** tab of the **Jobs** section.

## Reuse prebuilt automation by referencing roles

At the end of a project update, automation controller searches for the `requirements.yml` file in the `roles` directory, located at `<project-top-level-directory>/roles/requirements.yml`.

If this file is found, the following command automatically runs:

```
ansible-galaxy role install -r roles/requirements.yml -p <project-specific cache location>/requirements_roles -vvv
```
This file enables you to reference Ansible Galaxy roles or roles within other repositories which can be checked out in conjunction with your own project. The addition of Ansible Galaxy access eliminates the need to create git submodules to achieve this result. Given that SCM projects, along with roles or collections, are pulled into and executed from a private job environment, a `<private job directory>` specific to the project within `/tmp` is created by default.

The cache directory is a subdirectory inside the global projects folder. You can copy the content from the cache location to `<job private directory>/requirements_roles`.

By default, automation controller has a system-wide setting that enables you to dynamically download roles from the `roles/requirements.yml` file for SCM projects. You can turn off this setting in the **Job Settings** screen from the navigation panel Settings> (and then)Automation Execution> (and then)Job, by unchecking the **Enable Role Download** box.

Whenever a project synchronization runs, automation controller determines if the project source and any roles from Galaxy or Collections are out of date with the project. Project updates download the roles inside the update.

If jobs need to pick up a change made to an upstream role, updating the project ensures that this happens. A change to the role means that a new commit was pushed to the *provision-role* source control.

To make this change take effect in a job, you do not have to push a new commit to the *playbooks* repository. You must update the project, which downloads roles to a local cache.

For instance, say you have two git repositories in source control. The first one is *playbooks* and the project in automation controller points to this URL. The second one is *provision-role* and it is referenced by the `roles/requirements.yml` file inside of the *playbooks* git repository.

Jobs download the most recent roles before every job run. Roles and collections are locally cached for performance reasons. You must select **Update revision on launch** in the project **Options** to ensure that the upstream role is re-downloaded before each job run:

![update-on-launch](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/projects-scm-update-options-update-on-launch-checked.png)

The update happens much earlier in the process than the sync, so this identifies errors and details faster and in a more logical location.

If there are any directories that must be specifically exposed, you can specify those in the **Job Settings** screen from the navigation panel Settings> (and then)Automation Execution> (and then)Job, in **Paths to expose to isolated Jobs**. You can also update the following entry in the settings file:

```
AWX_ISOLATION_SHOW_PATHS = ['/list/of/', '/paths']
```


Note:

If your playbooks need to use keys or settings defined in `AWX_ISOLATION_SHOW_PATHS`, you must add `AWX_ISOLATION_SHOW_PATHS` to `/var/lib/awx/.ssh`.

If you made changes in the settings file, be sure to restart services with the `automation-controller-service restart` command after your changes have been saved.

In the UI, you can configure these settings in the **Jobs Settings** window.

![Configure jobs](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/configure-controller-jobs-path-to-expose.png)
