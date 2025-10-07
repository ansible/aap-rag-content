# 11. Projects
## 11.1. Adding a new project
### 11.1.2. Managing playbooks using source control




Choose one of the following options when managing playbooks using source control:

-  [SCM Types - Configuring playbooks to use Git and Subversion](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-scm-git-subversion)
-  [SCM Type - Configuring playbooks to use Red Hat Insights](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-scm-insights)
-  [SCM Type - Configuring playbooks to use a remote archive](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-scm-remote-archive)


#### 11.1.2.1. SCM Types - Configuring playbooks to use Git and Subversion




Configure your projects to synchronize Ansible playbooks from Source Code Management (SCM) systems such as Git and Subversion. Integrating with SCM is a best practice for managing playbooks, as it provides version control, collaboration features, and a centralized repository for your automation code. By following these steps, you can ensure your environment always uses the latest version of your playbooks directly from your chosen SCM.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Projects.
1. Click the project name you want to use.
1. In the project **Details** tab, clickEdit project.
1. Select the appropriate option (Git or Subversion) from the **Source control type** menu.
1. Enter the appropriate details into the following fields:


-  **Source control URL** - See an example in the tooltip .
- Optional: **Source control branch/tag/commit** : Enter the SCM branch, tags, commit hashes, arbitrary refs, or revision number (if applicable) from the source control (Git or Subversion) to checkout. Some commit hashes and references might not be available unless you also give a custom refspec in the next field. If left blank, the default is `        HEAD` which is the last checked out Branch, Tag, or Commit for this project.
-  **Source control refspec** - This field is an option specific to git source control and only advanced users familiar and comfortable with git should specify which references to download from the remote repository. For more information, see [Job branch overriding](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-job-branch-overriding) .
-  **Source control credential** - If authentication is required, select the appropriate source control credential.

1. Optional: **Options** - select the launch behavior, if applicable:


-  **Clean** - Removes any local modifications before performing an update.
-  **Delete** - Deletes the local repository in its entirety before performing an update. Depending on the size of the repository this can significantly increase the amount of time required to complete an update.
-  **Track submodules** - Tracks the latest commit. There is more information in the tooltip![Tooltip](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/0c17081b1d1293156a760e9a6e06634a/question_circle.png)
.
-  **Update revision on launch** - Updates the revision of the project to the current revision in the remote source control, and caching the roles directory from [Ansible Galaxy support](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#ref-projects-galaxy-support) or [Collections support](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#ref-projects-collections-support) . Automation controller ensures that the local revision matches and that the roles and collections are up-to-date with the last update. In addition, to avoid job overflows if jobs are spawned faster than the project can synchronize, selecting this enables you to configure a Cache Timeout to cache previous project synchronizations for a given number of seconds.
-  **Allow branch override** - Enables a job template or an inventory source that uses this project to start with a specified SCM branch or revision other than that of the project. For more information, see [Job branch overriding](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-job-branch-overriding) .

1. ClickSave project.


#### 11.1.2.2. SCM Type - Configuring playbooks to use Red Hat Insights




Configure your projects to retrieve Ansible playbooks directly from Red Hat Insights. By integrating with Red Hat Insights, you can use it to manage and deploy remediation playbooks identified through its analysis of your Red Hat Enterprise Linux environment. This integration streamlines the process of addressing identified vulnerabilities and optimizing system configurations, ensuring your automation aligns with best practices and security recommendations.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Projects.
1. Click the project name you want to use.
1. In the project **Details** tab, clickEdit project.
1. Select **Red Hat Insights** from the **Source Control Type** menu.
1. In the **Insights credential** field, select the appropriate credential for use with Insights, as Red Hat Insights requires a credential for authentication.
1. Optional: In the **Options** field, select the launch behavior, if applicable:


-  **Clean** - Removes any local modifications before performing an update.
-  **Delete** - Deletes the local repository in its entirety before performing an update. Depending on the size of the repository this can significantly increase the amount of time required to complete an update.
-  **Update revision on launch** - Updates the revision of the project to the current revision in the remote source control, and caches the roles directory from [Ansible Galaxy support](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#ref-projects-galaxy-support) or [Collections support](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#ref-projects-collections-support) . Automation controller ensures that the local revision matches, and that the roles and collections are up-to-date. If jobs are spawned faster than the project can synchronize, selecting this enables you to configure a Cache Timeout to cache previous project synchronizations for a certain number of seconds, to avoid job overflow.

1. ClickSave project.


#### 11.1.2.3. SCM Type - Configuring playbooks to use a remote archive




Playbooks that use a remote archive enable projects to be based on a build process that produces a versioned artifact, or release, containing all the requirements for that project in a single archive.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Projects.
1. Click the project name you want to use.
1. In the project **Details** tab, clickEdit project.
1. Select **Remote Archive** from the **Source control type** menu.
1. Enter the appropriate details into the following fields:


-  **Source control URL** - requires a URL to a remote archive, such as a _GitHub Release_ or a build artifact stored in _Artifactory_ and unpacks it into the project path for use.
-  **Source control credential** - If authentication is required, select the appropriate source control credential.

1. Optional: In the **Options** field, select the launch behavior, if applicable:


-  **Clean** - Removes any local modifications before performing an update.
-  **Delete** - Deletes the local repository in its entirety before performing an update. Depending on the size of the repository this can significantly increase the amount of time required to complete an update.
-  **Update revision on launch** - Not recommended. This option updates the revision of the project to the current revision in the remote source control, and caches the roles directory from [Ansible Galaxy support](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#ref-projects-galaxy-support) or [Collections support](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#ref-projects-collections-support) .
-  **Allow branch override** - Not recommended. This option enables a job template that uses this project to launch with a specified SCM branch or revision other than that of the project’s.

Note
Since this source control type is intended to support the concept of unchanging artifacts, it is advisable to disable Galaxy integration (for roles, at a minimum).





1. ClickSave project.


