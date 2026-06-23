# Configure playbooks to use source control management (SCM) systems
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
- **Source control refspec** - This field is an option specific to git source control and only advanced users familiar and comfortable with git should specify which references to download from the remote repository. For more information, see [Job branch overriding](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_controller_job_branch_overriding#controller-job-branch-overriding "In automation controller, you can configure projects to allow job templates to override the branch, tag, or reference used for source control.").
- **Source control credential** - If authentication is required, select the appropriate source control credential.

6.  Optional: **Options** - select the launch behavior, if applicable:

- **Clean** - Removes any local modifications before performing an update.
- **Delete** - Deletes the local repository in its entirety before performing an update. Depending on the size of the repository this can significantly increase the amount of time required to complete an update.
- **Track submodules** - Tracks the latest commit. There is more information in the tooltip ![tooltip](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/question-circle.png).
- **Update revision on launch** - Updates the revision of the project to the current revision in the remote source control, and caching the roles directory from [Ansible Galaxy support](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_manage_playbooks_with_source_control#ref-projects-galaxy-support "At the end of a project update, automation controller searches for the requirements.yml file in the roles directory, located at &lt;project-top-level-directory&gt;/roles/requirements.yml.") or [Collections support](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_collections_support#ref-projects-collections-support "Automation controller supports project-specific Ansible collections in job runs."). Automation controller ensures that the local revision matches and that the roles and collections are up-to-date with the last update. In addition, to avoid job overflows if jobs are spawned faster than the project can synchronize, selecting this enables you to configure a Cache Timeout to cache previous project synchronizations for a given number of seconds.
- **Allow branch override** - Enables a job template or an inventory source that uses this project to start with a specified SCM branch or revision other than that of the project. For more information, see [Job branch overriding](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_controller_job_branch_overriding#controller-job-branch-overriding "In automation controller, you can configure projects to allow job templates to override the branch, tag, or reference used for source control.").

7.  Click Save project.

