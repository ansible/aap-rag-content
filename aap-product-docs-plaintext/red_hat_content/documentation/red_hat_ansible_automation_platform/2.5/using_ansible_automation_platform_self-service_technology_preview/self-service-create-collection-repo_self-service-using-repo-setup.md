# 3. Setting up repositories for collections
## 3.2. Creating a repository for a collection




1. Locate the `    .tar` file for the collection.
1. Create a new directory to store the unpacked files.
1. Run the following command to unpack the `    .tar` file:


```
$ tar -xvf &lt;collection-name&gt;.tar.gz – directory &lt;collection_directory&gt;
```


1. Navigate to the extracted collection directory and initialize it as a Git repository:


```
$ cd &lt;collection_directory&gt;    $ git init
```


1. Edit the collection if you wish to modify the template.

The Ansible template definitions are stored in the `    extensions/patterns/` directory of the repository.


1. Push the repository to your SCM.


- See [Adding a local repository to GitHub using Git](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git) in the GitHub documentation.
- See [Create a project with git push](https://docs.gitlab.com/topics/git/project) in the Gitlab documentation.



## 3.3. Creating a repository for `ansible-pattern-loader`




To use one of the pre-loaded tiles in self-service technology preview, you must create a repository in GitHub or Gitlab for the [ansible-pattern-loader](https://github.com/ansible/ansible-pattern-loader) repository.

1. Clone the repository:


```
$ git clone git@github.com:ansible/ansible-pattern-loader.git
```


1. Push the repository to your SCM.


- See [Adding a local repository to GitHub using Git](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git) in the GitHub documentation.
- See [Create a project with git push](https://docs.gitlab.com/topics/git/project) in the Gitlab documentation.



# Chapter 4. Configuring source control credentials for private repositories




To work with private repositories, you must add your GitHub or Gitlab personal access tokens to Ansible Automation Platform as a source control credential.

Note
Ensure that the Ansible Automation Platform users and teams assigned to the Ansible Automation Platform objects, such as source control credentials, are part of the Ansible Automation Platform Organization configured to sync to the self-service technology preview. See _ [Installing Ansible Automation Platform self-service technology preview](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/installing_ansible_automation_platform_self-service_technology_preview) _ for more information.



## 4.1. Adding Source Control Credentials for GitHub or Gitlab in Ansible Automation Platform




**Prerequisite**

Ensure that the user who needs access to the repository has the appropriate permissions.


**Procedure**

1. Sign in to Ansible Automation Platform as an administrator.
1. Navigate toAutomation Execution→Infrastructure→Credentials.
1. On the **Credentials** page, clickCreate credential.
1. Add the following details:


-  **Name** : Credential name.
-  **Organization** : The name of the organization with which the credential is associated. The default is **Default** .

Note
Credentials in Ansible Automation Platform are always created under a specific organization.




-  **Credential type** : Source Control.
-  **Username** : Your Github username or the Gitlab group name under which the repository is hosted.

Note
Self-service technology preview does not support creating or modifying Gitlab repositories under personal user accounts. You must use a Gitlab Group instead.







## 4.2. Sharing credential access with uses and teams in Ansible Automation Platform




You can grant users access to credentials based on their team membership. When you add a user as a member of a team, they inherit access to the credentials assigned to that team.

1. In a browser, navigate to your Ansible Automation Platform instance.
1. Navigate toAutomation Execution→Infrastructure→Credentials.
1. On the **Credentials** page, clickCreate credential.
1. Open the credential you created for Gitlab or GitHub.
1. Select users or teams from the same organization:


- Select the **Team Access** tab if you want to provide access to the credential for a team.
- Select the **User Access** tab if you want to provide access to the credential for a user.

1. ClickAdd roles.
1. Click the checkbox beside the team or user you want to share the credentials with, and clickNext.
1. Select the roles you want applied to the team or user and clickNext.
1. Review the settings and clickFinish.

The **Add roles** dialog indicates whether the role assignments were successfully applied.


1. You can remove access to a role for a team by selecting the **Remove role** icon next to the team. This launches a confirmation dialog, asking you to confirm the removal.


# Chapter 5. Working with templates




## 5.1. Adding a template




This procedure describes how to add a tile to the **Templates** view of your self-service technology preview instance.

**Prerequisite**

You have created repositories in your SCM for the templates that you want to use.


**Procedure**

1. In a browser, navigate to your self-service technology preview instance and sign in with your Ansible Automation Platform credentials.
1. Navigate to the **Templates** Page.
1. Click **Add template** .
1. Enter a valid Github URL for the template that you want to add.
1. Click **Analyze** to fetch the template.
1. After the template has been fetched, review the list of what will be imported and added to the catalog.
1. Click **Import** .


**Verification**

After the import is complete, return to the **Templates** page to view the newly created template. You can now launch your template.


## 5.2. Launching a template




This procedure describes how to launch a template from a tile in the **Templates** view of your self-service technology preview instance.

**Procedure**

1. In a browser, navigate to your self-service technology preview instance and sign in with your Ansible Automation Platform credentials.
1. Navigate to the **Templates** page. The templates you have set up are displayed as tiles on the page.
1. In the template that you want to launch, click **Start** .

A description of the template is displayed.


1. Click **Launch** to begin configuring the parameters for running the template.
1. Fill out the required fields.
1. Click **Next** .
1. Review the entered information.
1. Click **Create** to launch the template.
1. The progress for the template execution is displayed.


**Verification**

To view the log for the template execution, click **Show logs** .


# Chapter 6. Working with RBAC




## 6.1. Setting up RBAC




RBAC is set up in the Helm chart with the `admin` user set as the RBAC administrator ( `rbac_admin` ).

This procedure describes how to create a role in self-service technology preview that allows only a selected team to view and execute particular templates.

**Prerequisites**

- As the admin user in your Ansible Automation Platform instance, you have created a user, for example `    example-user` .

See [Creating a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#proc-controller-creating-a-user) in the _Access management and authentication_ guide.


- You have added this user as a member of a team, for example `    example-team` .

See [Adding users to a team](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#proc-gw-team-add-user) in the _Access management and authentication_ guide.




**Procedure**

1. In a browser, log in to your self-service technology preview instance as the Ansible Automation Platform `    admin` user.
1. In the navigation panel, selectAdministration→RBAC.
1. In the **RBAC** view, click **Create** .

The **Create Role** view appears.


1. Enter a name for the role.
1. Select the user or group that you want to allow to use the role.
1. In the **Add Permission policies** section, select the plug-ins that you want to enable for the role.
1. Select **Permission** in the list of plug-ins to configure the fine-grained permission policies for the role.

1. Click **Next** .
1. Review the settings that you have selected for the role.
1. Click **Create** to create the role.


## 6.2. Verifying RBAC




This procedure describes how to verify that the role you set up is working correctly.

1. Verify that users with permissions can use a template:


1. Log in to self-service technology preview as a user who is a member of a team that has been enabled to use a role.
1. Verify that RBAC is applied and that the user can use the templates that you enabled for the role.

1. Log out of self-service technology preview.
1. Verify that users without permissions can not see or use a template:


1. Log in to self-service technology preview as a user who is not a member of the new team that has been enabled to use the role.
1. Verify that RBAC is applied and that the user cannot use the templates that you enabled for the role.

1. Log out of self-service technology preview.


# Chapter 7. Deregistering templates




## 7.1. Deregistering dynamically added templates




Dynamically added templates are templates that you have added using **Add Template** in the self-service technology preview console.

1. In a browser, navigate to the self-service technology preview instance.
1. Click the catalog template name to navigate to the **Template detail** view. The navigation bar contains the **Unregister Template** option.
1. Click **Unregister Template** .
1. In the dialog, confirm that you want to deregister the template.
1. Click **Delete Entity** to unregister the template.


**Verification**

In a browser, navigate to the **Templates** view for your self-service technology preview instance. Verify that the templates have been deleted.


## 7.2. Deregistering pre-installed templates




Self-service technology preview comes preloaded with example templates to help you get started. To remove the preloaded templates from the **Templates** page, you must edit the Helm chart for your Self-service installation.

1. In a browser, navigate to your OpenShift project for Ansible Self-service.
1. Select the **Topology** view.
1. Open the Helm chart for your deployment.
1. Locate the `    catalog.locations` section of the Helm chart:


```
locations:           - type: file           target: /software-templates/seed.yaml           rules:             - allow: [Template]
```


1. Comment out the `    type` , `    target` , and `    rules` keys of `    catalog.locations` by adding a `    #` character:


```
locations:           # - type: file           # target: /software-templates/seed.yaml           # rules:           #   - allow: [Template]
```


1. Click **Create** to re-launch the deployment.


**Verification**

In a browser, navigate to the **Templates** view for your self-service technology preview instance. Verify that the templates have been deleted.


# Chapter 8. Providing feedback in self-service technology preview




Self-service technology preview provides a feedback form where you can suggest new features and content, as well as provide general feedback.

1. Click **Feedback** in the self-service technology preview console to display the feedback form.

![Self-service technology preview feedback form](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/b6a52e77499334e9950b4b0c1c3ba861/rhdh-feedback-form.png)



1. Enter the feedback you want to provide.
1. Tick the **I understand that feedback is shared with Red Hat** checkbox.
1. Click **Submit** .


Note
To ensure that Red Hat receives your feedback, exclude your self-service technology preview URL in any browser ad blockers or privacy tools.




<span id="idm140460209550192"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





