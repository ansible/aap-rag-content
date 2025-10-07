# 3. Creating and launching an Ansible development workspace
## 3.3. Creating a devfile for an Ansible development workspace




To ensure your Ansible development workspace launches with the correct Ansible dev spaces image, you must add a `devfile` to your git repository. A `devfile` is a YAML file that defines the development environment for a project in Red Hat OpenShift Dev Spaces.

**Procedure**

1. In your Git repository for your Ansible development workspace, create a new file named `    devfile.yaml` .
1. Copy and paste the following sample code into the `    devfile.yaml` file:


```
---    # cspell: disable=devspaces    schemaVersion: 2.2.2    metadata:      name: ansible-devspaces-devfile    components:      - name: tooling-container        container:          image: registry.redhat.io/ansible-automation-platform-tech-preview/ansible-devspaces-rhel9:latest          memoryRequest: 256M          memoryLimit: 6Gi          cpuRequest: 250m          cpuLimit: 2000m          args: ["tail", "-f", "/dev/null"]          env:            - name: "ANSIBLE_COLLECTIONS_PATH"              value: "~/.ansible/collections:/usr/share/ansible/collections"            - name: KUBEDOCK_ENABLED              value: "true"    ...
```


1. Modify the image value to the name of your specific Ansible image.
1. Add the `    devfile.yaml` file to your Git repository and push the changes to your source control manager (SCM).


## 3.4. Creating a `.code-workspace` file for an Ansible development workspace




To configure VS Code extensions that are included in your Ansible development workspace, you must add a `.code-workspace` JSON file to your git repository.

**Procedure**

1. In your Git repository for your Ansible development workspace, create a new file named `    .code-workspace` .
1. Copy and paste the following sample code into the `    .code-workspace` file:


```
{    	"settings": {    		"ansible.lightspeed.suggestions.enabled": true,    		"ansible.lightspeed.enabled": true    	},    	"extensions": {    		"recommendations": [                            "redhat.ansible",                            "redhat.vscode-yaml",                            "redhat.vscode-openshift-connector",                            "eamodio.gitlens",    		]    	},    }
```


1. If you want to add extra extensions to your Ansible development workspace, add them in the `    extensions.recommendations` section of the file.
1. Add the `    .code-workspace` file to your Git repository and push the changes to your source control manager (SCM).


## 3.5. Launching an Ansible dev spaces workspace




**Prerequisites**

- Your administrator has provided a URL for a OpenShift Dev Spaces dashboard.
- You have prepared a git repository that contains the `    devfile.yaml` and `    .code-workspace` files that define the Ansible development workspace configuration.


**Procedure**

1. In a browser, navigate to the OpenShift Dev Spaces dashboard and log in.
1. Select **Create Workspace** in the navigation pane.
1. In the **Import from Git** field of the **Create Workspace** form, enter the URL for the Git repository that contains your `    devfile.yaml` and `    .code-workspace` files.
1. Click **Create & Open** .
1. OpenShift Dev Spaces displays the progress for the provisioning process of your Ansible development workspace.

![Workspace provisioning progress](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_Ansible_development_workspaces_for_automation_content_development-en-US/images/5c644184e7d5c0d6e09a9726c36a5309/devtools-workspaces-provisioning.png)


After the Ansible development workspace launches, a VS Code environment opens in your browser.


1. To open a terminal for executing commands and viewing `    ansible-lint` suggestions in VS Code, click the main menu icon in the **Activity** bar and selectTerminal→New Terminal.

For more information about working in a VS Code terminal, see [Getting started with the terminal](https://code.visualstudio.com/docs/terminal/getting-started) in the VS Code documentation.




# Chapter 4. Developing automation content in your workspace




The Ansible development tools are installed as part of the Ansible extension in the Ansible development workspace. You can use Ansible development tools to scaffold directories for automation content in your repository.

Using the Ansible extension ensures that best practices for directory structure are met. For more information about using the Ansible extension to develop automation content, refer to [Developing automation content](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/developing_automation_content) .

Red Hat recommends that you create only one collection per repository, so that each collection has a clear, specific purpose. This approach promotes reusability, as each collection is a self-contained unit of content. A one-to-one relationship between a collection and its repository also improves manageability by simplifying dependency management, maintenance, and release cycles.

## 4.1. Creating collections and playbooks in your Ansible development workspace




Use the Ansible extension in VS Code to use Ansible development tools to scaffold directories and files for your automation content. You can use Red Hat Ansible Lightspeed with IBM watsonx Code Assistant to help you write playbooks, and `ansible-lint` to debug them.

**Procedure**

1. In the OpenShift Dev Spaces dashboard. select the Ansible development workspace where you want to develop automation content.
1. In the **Activity** bar of VS Code, select the Ansible icon to open Ansible development tools.
1. Select **Connect** in the Ansible Lightspeed section to log in to Ansible Lightspeed.
1. Select an option in the **initialize** section of **Ansible Development tools** to scaffold files and directories for a collection project or a playbook project.


- For more information on creating a playbook project, see the [Scaffolding a playbook project](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/developing_automation_content/creating-playbook-project) chapter of the _Developing automation content_ guide.
- For more information on creating a roles collection project, see the [Scaffolding a collection project for your roles](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/developing_automation_content/devtools-create-roles-collection_develop-automation-content#devtools-scaffold-roles-collection_devtools-create-roles-collection) section of the _Developing automation content_ guide.

1. Select options in the **Add** section of Ansible development tools to add files for playbooks or roles to your project. Alternatively, you can use the options in the **Ansible Lightspeed** section to generate playbooks or roles.
1. Save your work:


1. Click the main menu icon in the **Activity** bar and selectTerminal→New Terminal.
1. Use `        git add` and `        git commit` commands to stage the changed files and commit your changes to the local repository in the workspace.
1. Use the `        git push` command to push your updates to your repository in your source control manager.



## 4.2. Editing and debugging automation content in your Ansible development workspace




You can continue your work in a previously created workspace. Workspaces that have been inactive for a set period might be paused to free up resources. The duration of inactivity before timeout is configured in OpenShift Dev Spaces by your administrator. A paused workspace automatically relaunches when you select it from the OpenShift Dev Spaces dashboard.

Ansible lint indicates errors in your playbooks.

**Procedure**

1. To display your previously created workspaces, select **Workspaces** in your OpenShift Dev Spaces dashboard.
1. Select **Open** next to the workspace that you want to use.
1. Select the **Explorer** icon in the **Activity** bar to open the file explorer, and open the file you want to edit.
1. While you are editing, the Ansible extension provides suggestions. Select a suggestion from the dropdown list to include it in your playbook.
1. To view documentation for a keyword or a module, hover your mouse over it.
1. Open the terminal in VS Code: click the main menu icon in the **Activity** bar and selectTerminal→New Terminal.
1. Select the **Problems** tab in the terminal to view issues that `    ansible-lint` has identified.

In the following example, one error is selected in the **Problems** tab, and the corresponding line in the playbook is highlighted.

![Playbook and ansible-lint messages](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_Ansible_development_workspaces_for_automation_content_development-en-US/images/23339de5f24a69f937c6efa62f92d09b/devspaces-errors-playbook.png)



1. When you have resolved the problems in your playbook, a message is displayed in the **Problems** tab of the terminal.


## 4.3. Executing playbooks in your Ansible development workspace




You can execute a playbook using the Ansible extension in VS Code.

**Procedure**

- To execute a playbook in your Ansible development workspace, right-click on a playbook name in the file explorer and selectRun ansible playbook via→Run ansible playbook via ansible playbook.


Note
You cannot use execution environments in Ansible development workspaces. Do not use `ansible-navigator` to execute playbooks.



## 4.4. Sharing your work




To share automation content with your colleagues, you can work from the same repository.

1. To contribute to a colleague’s project, request the URL for the Git repository that corresponds to your colleague’s Ansible development workspace.
1. Launch a workspace using the repository URL that your colleague shared.
1. Work within a new git branch and contribute to your colleague’s repository by creating a merge or pull request.


# Chapter 5. Ansible development workspaces management and teardown




You can delete Ansible development workspaces from OpenShift Dev Spaces. For more information on managing OpenShift Dev Spaces, see the Red Hat OpenShift Dev Spaces _ [Authentication guide](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.23/html-single/administration_guide/index) _ .

## 5.1. Deleting an Ansible development workspace




To delete the contents of an Ansible development workspace, you delete the workspace itself. This action removes all the pods, storage, and other resources associated with that specific workspace, effectively wiping its contents.

**Prerequisites**

- You know the name of the workspace you want to delete.


**Procedure**

1. Stop the Ansible development workspace that you want to delete.


- To stop the workspace in the Dev Spaces dashboard, select the workspace that you want to delete and selectactions→Stop Workspace.
- To stop the workspace using OpenShift `        oc` commands, follow the steps in [Stopping workspaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.22/html-single/user_guide/index#managing-workspaces-with-apis-stopping-workspaces) in the Red Hat OpenShift Dev Spaces _User Guide_ .

1. Delete the workspace:


- To delete the workspace from the Dev Spaces dashboard, select the workspace that you want to delete and selectactions→Delete Workspace.
- To delete a workspace using OpenShift `        oc` commands, follow the steps in [Removing workspaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.22/html-single/user_guide/index#managing-workspaces-with-apis-removing-workspaces) in the Red Hat OpenShift Dev Spaces _User Guide_ .



## 5.2. Uninstalling OpenShift Dev Spaces




- To uninstall OpenShift Dev Spaces, follow the steps in the [Uninstalling Dev Spaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.23/html/administration_guide/uninstalling-devspaces) chapter of the Red Hat OpenShift Dev Spaces _Administration Guide_ .


Note
Uninstalling Ansible dev spaces removes all Ansible dev spaces-related user data.




<span id="idm139764556326304"></span>
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





