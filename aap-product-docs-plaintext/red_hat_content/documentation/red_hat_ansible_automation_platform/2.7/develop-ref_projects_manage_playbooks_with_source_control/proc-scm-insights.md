# Configure playbooks to use source control management (SCM) systems
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
- **Update revision on launch** - Updates the revision of the project to the current revision in the remote source control, and caches the roles directory from [Ansible Galaxy support](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_manage_playbooks_with_source_control#ref-projects-galaxy-support "At the end of a project update, automation controller searches for the requirements.yml file in the roles directory, located at &lt;project-top-level-directory&gt;/roles/requirements.yml.") or [Collections support](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_collections_support#ref-projects-collections-support "Automation controller supports project-specific Ansible collections in job runs."). Automation controller ensures that the local revision matches, and that the roles and collections are up-to-date. If jobs are spawned faster than the project can synchronize, selecting this enables you to configure a Cache Timeout to cache previous project synchronizations for a certain number of seconds, to avoid job overflow.

7.  Click Save project.

