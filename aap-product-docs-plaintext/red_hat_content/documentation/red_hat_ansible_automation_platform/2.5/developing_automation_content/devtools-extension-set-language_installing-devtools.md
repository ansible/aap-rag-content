# 3. Installing Ansible development tools
## 3.1. Requirements
### 3.1.6. Associating the Ansible language to YAML files




The Ansible VS Code extension works only when the language associated with a file is set to Ansible. The extension provides features that help create Ansible playbooks, such as auto-completion, hover, and diagnostics.

The Ansible VS Code extension automatically associates the Ansible language with some files. The procedures below describe how to set the language for files that are not recognized as Ansible files.

**Manually associating the Ansible language to YAML files**

The following procedure describes how to manually assign the Ansible language to a YAML file that is open in VS Code.


1. Open or create a YAML file in VS Code.
1. Hover the cursor over the language identified in the status bar at the bottom of the VS Code window to open the **Select Language Mode** list.
1. Select **Ansible** in the list.

The language shown in the status bar at the bottom of the VS Code window for the file is changed to Ansible.




**Adding persistent file association for the Ansible language to `settings.json` **

Alternatively, you can add file association for the Ansible language in your `settings.json` file.


1. Open the `    settings.json` file:


1. ClickView→Command Paletteto open the command palette.
1. Enter `        Workspace settings` in the search box and select **Open Workspace Settings (JSON)** .

1. Add the following code to `    settings.json` .


```
{      ...          "files.associations": {        "*plays.yml": "ansible",        "*init.yml": "yaml",      }    }
```




### 3.1.7. Installing and configuring the `Dev Containers` extension




If you are installing the containerized version of Ansible development tools, you must install the [Microsoft Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code.

1. Open VS Code.
1. Click the **Extensions** (![Extensions](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/417ed5315a44493c6a44ae5c12dc6fab/vscode-extensions-icon.png)
) icon in the Activity Bar, or clickView→Extensions, to display the **Extensions** view.
1. In the search field in the **Extensions** view, type `    Dev Containers` .
1. Select the Dev Containers extension from Microsoft and clickInstall.


If you are using Podman or Podman Desktop as your containerization platform, you must modify the default settings in the `Dev Containers` extension.

1. Replace docker with podman in the `    Dev Containers` extension settings:


1. In VS Code, open the settings editor.
1. Search for `        @ext:ms-vscode-remote.remote-containers` .

Alternatively, click the **Extensions** icon in the activity bar and click the gear icon for the `        Dev Containers` extension.



1. Set `    Dev &gt; Containers:Docker Path` to `    podman` .
1. Set `    Dev &gt; Containers:Docker Compose Path` to `    podman-compose` .


## 3.2. Installing Ansible development tools on a container inside VS Code




The Dev Containers VS Code extension requires a `.devcontainer` file to store settings for your dev containers. You must use the Ansible extension to scaffold a config file for your dev container, and reopen your directory in a container in VS Code.

**Prerequisites**

- You have installed a containerization platform, for example Podman, Podman Desktop, Docker, or Docker Desktop.
- You have a Red Hat login and you have logged in to the Red Hat registry at `    registry.redhat.io` . For information about logging in to `    registry.redhat.io` , see [Authenticating with the Red Hat container registry](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/developing_automation_content/index#devtools-setup-registry-redhat-io_installing-devtools) .
- You have installed VS Code.
- You have installed the Ansible extension in VS Code.
- You have installed the [Microsoft Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code.
- If you are installing Ansible development tools on Windows, launch VS Code and connect to the WSL machine:


1. Click the `        Remote` (![Remote](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/706517b6299d38221f473c0bce4863e1/vscode-remote-icon.png)
) icon.
1. In the dropdown menu that appears, select the option to connect to the WSL machine.



**Procedure**

1. In VS Code, navigate to your project directory.
1. Click the Ansible icon in the VS Code activity bar to open the Ansible extension.
1. In the **Ansible Development Tools** section of the Ansible extension, scroll down to the **ADD** option and select **Devcontainer** .
1. In the **Create a devcontainer** page, select the **Downstream** container image from the **Container image** options.

This action adds `    devcontainer.json` files for both Podman and Docker in a `    .devcontainer` directory.


1. Reopen or reload the project directory:


- If VS Code detects that your directory contains a `        devcontainer.json` file, the following notification appears:

![Reopen in container](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/396c911927f946c71508d085befd3e04/devtools-reopen-in-container.png)


Click **Reopen in Container** .


- If the notification does not appear, click the `        Remote` (![Remote](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/706517b6299d38221f473c0bce4863e1/vscode-remote-icon.png)
) icon. In the dropdown menu that appears, select **Reopen in Container** .

1. Select the dev container for Podman or Docker according to the containerization platform you are using.

The **Remote ()** status in the VS Code Status bar displays `    opening Remote` and a notification indicates the progress in opening the container.




**Verification**

When the directory reopens in a container, the **Remote ()** status displays `Dev Container: ansible-dev-container` .


Note
The base image for the container is a Universal Base Image Minimal (UBI Minimal) image that uses `microdnf` as a package manager. The `dnf` and `yum` package managers are not available in the container.

For information about using `microdnf` in containers based on UBI Minimal images, see [Adding software in a minimal UBI container](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/assembly_adding-software-to-a-ubi-container_building-running-and-managing-containers#proc_adding-software-in-a-minimal-ubi-container_assembly_adding-software-to-a-ubi-container) in the Red Hat Enterprise Linux _Building, running, and managing containers_ guide.



## 3.3. Installing Ansible development tools from a package on RHEL




Ansible development tools are bundled in the Ansible Automation Platform RPM (Red Hat Package Manager) package. Refer to the _ [RPM installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation) _ documentation for information on installing Ansible Automation Platform.

**Prerequisites**

- You have installed RHEL 8 or RHEL 9.

Note
RPM installation is not supported on RHEL 10.




- You have registered your system with Red Hat Subscription Manager.
- You have installed a containerization platform, for example Podman or Docker.


**Procedure**

1. Run the following command to check whether Simple Content Access (SCA) is enabled:


```
$ sudo subscription-manager status
```

If Simple Content Access is enabled, the output contains the following message:


```
Content Access Mode is set to Simple Content Access.
```


1. If Simple Content Access is not enabled, attach the Red Hat Ansible Automation Platform SKU:


```
$ sudo subscription-manager attach --pool=&lt;sku-pool-id&gt;
```



1. Install Ansible development tools with the following command:


```
$ sudo dnf install --enablerepo=ansible-automation-platform-2.5-for-rhel-8-x86_64-rpms ansible-dev-tools
```


```
$ sudo dnf install --enablerepo=ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms ansible-dev-tools
```




**Verification:**

Verify that the Ansible development tools components have been installed:


```
$ rpm -aq | grep ansible
```

The output displays the Ansible packages that are installed:

```
ansible-sign-0.1.1-2.el9ap.noarch
ansible-creator-24.4.1-1.el9ap.noarch
python3.11-ansible-runner-2.4.0-0.1.20240412.git764790f.el9ap.noarch
ansible-runner-2.4.0-0.1.20240412.git764790f.el9ap.noarch
ansible-builder-3.1.0-0.2.20240413.git167ed5c.el9ap.noarch
ansible-dev-environment-24.1.0-2.el9ap.noarch
ansible-core-2.16.6-0.1.20240413.gite636132.el9ap.noarch
python3.11-ansible-compat-4.1.11-2.el9ap.noarch
python3.11-pytest-ansible-24.1.2-1.el9ap.noarch
ansible-lint-6.14.3-4.el9ap.noarch
ansible-navigator-3.4.1-2.el9ap.noarch
python3.11-tox-ansible-24.2.0-1.el9ap.noarch
ansible-dev-tools-2.5-2.el9ap.noarch
```

On successful installation, you can view the help documentation for ansible-creator:

```
$ ansible-creator --help

usage: ansible-creator [-h] [--version] command ...

The fastest way to generate all your ansible content.

Positional arguments:
command
add           Add resources to an existing Ansible project.
init          Initialize a new Ansible project.

Options:
--version      Print ansible-creator version and exit.
-h     --help  Show this help message and exit
```

# Chapter 4. Creating a playbook project




## 4.1. Scaffolding a playbook project




The following steps describe the process for scaffolding a new playbook project with the Ansible VS Code extension.

1. Prerequisites


- You have installed Ansible development tools.
- You have installed and opened the Ansible VS Code extension.
- You have identified a directory where you want to save the project.



**Procedure**

1. Open VS Code.
1. Click the Ansible icon in the VS Code activity bar to open the Ansible extension.
1. Select **Get started** in the **Ansible content creator** section.

The **Ansible content creator** tab opens.


1. In the **Create** section, click **Ansible playbook project** .

The **Create Ansible project** tab opens.


1. In the form in the **Create Ansible project** tab, enter the following:


-  **Destination directory** : Enter the path to the directory where you want to scaffold your new playbook project.

Note
If you enter an existing directory name, the scaffolding process overwrites the contents of that directory. The scaffold process only allows you to use an existing directory if you enable the `        Force` option.




- If you are using the containerized version of Ansible Dev tools, the destination directory path is relative to the container, not a path in your local system. To discover the current directory name in the container, run the `            pwd` command in a terminal in VS Code. If the current directory in the container is `            workspaces` , enter `            workspaces/&lt;destination_directory_name&gt;` .
- If you are using a locally installed version of Ansible Dev tools, enter the full path to the directory, for example `            /user/&lt;username&gt;/projects/&lt;destination_directory_name&gt;` .

-  **SCM organization and SCM project** : Enter a name for the directory and subdirectory where you can store roles that you create for your playbooks.

1. Enter a name for the directory where you want to scaffold your new playbook project.


**Verification**

After the project directory has been created, the following message appears in the **Logs** pane of the **Create Ansible Project** tab. In this example, the destination directory name is `destination_directory_name` .


```
------------------ ansible-creator logs ------------------
Note: ansible project created at /Users/username/test_project
```

The following directories and files are created in your project directory:

```
$ tree -a -L 5 .
├── .devcontainer
│&nbsp;&nbsp; ├── devcontainer.json
│&nbsp;&nbsp; ├── docker
│&nbsp;&nbsp; │&nbsp;&nbsp; └── devcontainer.json
│&nbsp;&nbsp; └── podman
│&nbsp;&nbsp;     └── devcontainer.json
├── .gitignore
├── README.md
├── ansible-navigator.yml
├── ansible.cfg
├── collections
│&nbsp;&nbsp; ├── ansible_collections
│&nbsp;&nbsp; │&nbsp;&nbsp; └── scm_organization_name
│&nbsp;&nbsp; │&nbsp;&nbsp;     └── scm_project_name
│&nbsp;&nbsp; └── requirements.yml
├── devfile.yaml
├── inventory
│&nbsp;&nbsp; ├── group_vars
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── all.yml
│&nbsp;&nbsp; │&nbsp;&nbsp; └── web_servers.yml
│&nbsp;&nbsp; ├── host_vars
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── server1.yml
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── server2.yml
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── server3.yml
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── switch1.yml
│&nbsp;&nbsp; │&nbsp;&nbsp; └── switch2.yml
│&nbsp;&nbsp; └── hosts.yml
├── linux_playbook.yml
├── network_playbook.yml
└── site.yml
```

# Chapter 5. Writing and running a playbook with Ansible development tools




## 5.1. Setting up the Ansible configuration file for your playbook project




When you scaffolded your playbook project, an Ansible configuration file, `ansible.cfg` , was added to the root directory of your project.

If you have configured a default Ansible configuration file in `/etc/ansible/ansible.cfg` , copy any settings that you want to reuse in your project from your default Ansible configuration file to the `ansible.cfg` file in your project’s root directory.

To learn more about the Ansible configuration file, see [Ansible Configuration Settings](https://docs.ansible.com/ansible/latest/reference_appendices/config.html) in the Ansible documentation.

## 5.2. Writing your first playbook




Ansible development tools help you to create and run playbooks in VS Code.

**Prerequisites**

- You have installed and opened the Ansible VS Code extension.
- You have opened a terminal in VS Code.
- You have installed `    ansible-devtools` .


**Procedure**

1. Create a new .yml file in VS Code for your playbook, for example `    example_playbook.yml` . Put it in the same directory level as the example `    site.yml` file.
1. Add the following example code into the playbook file and save the file. The playbook consists of a single play that executes a `    ping` to your local machine.


```
---    - name: My first play      hosts: localhost      tasks:        - name: Ping my hosts          ansible.builtin.ping:
```

`    Ansible-lint` runs in the background and displays errors in the **Problems** tab of the terminal. There are no errors in this playbook:

![Ansible-lint showing no errors in a playbook](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/6481d621aaf9e19180ca0fa03cff54ea/ansible-lint-no-errors.png)



1. If you want to add new content to the playbook, use the following rules:


- Every playbook file must finish with a blank line.
- Trailing spaces at the end of lines are not allowed.
- Every playbook and every play require an identifier (name).

1. Save your playbook file.


## 5.3. Inspecting your playbook




The Ansible VS Code extension provides inline help, syntax highlighting, and assists you with indentation in `.yml` files.

1. Open a playbook in VS Code.
1. Hover your mouse over a keyword or a module name: the Ansible extension provides documentation:

![Ansible-lint showing no errors in a playbook](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/e134cf2cc46c309472833e581fef773f/ansible-lint-keyword-help.png)



1. If you begin to type the name of a module, for example `    ansible.builtin.ping` , the extension provides a list of suggestions.

Select one of the suggestions to autocomplete the line.

![Ansible-lint showing no errors in a playbook](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/ce331f515e980027fbd1ecd8000a82cf/ansible-lint-module-completion.png)





## 5.4. Debugging your playbook




Learn how to use VS Code to identify and understand error messages in playbooks.

1. The following playbook contains multiple errors. Copy and paste it into a new file in VS Code.


```
- name:      hosts: localhost      tasks:       - name:         ansible.builtin.ping:
```

The errors are indicated with a wavy underline in VS Code.


1. Hover your mouse over an error to view the details:

![Popup message explaining a playbook error](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/afc6eabd5cb29b92ae87af7528c73ca2/ansible-lint-errors.png)



1. Playbook files that contain errors are indicated with a number in the **Explorer** pane.
1. Select the **Problems** tab of the VS Code terminal to view a list of the errors.

![Playbook errors shown in Problems tab and explorer list](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/c7bd61a7d56db99093cb1390f508e5d0/ansible-lint-errors-explorer.png)


`    $[0].tasks[0].name None is not of type 'string'` indicates that the playbook does not have a label.




## 5.5. Running your playbook




The Ansible VS Code extension provides two options to run your playbook:

-  `    ansible-playbook` runs the playbook on your local machine using Ansible Core.
-  `    ansible-navigator` runs the playbook in an execution environment in the same manner that Ansible Automation Platform runs an automation job. You specify the base image for the execution environment in the Ansible extension settings.


### 5.5.1. Running your playbook with `ansible-playbook`




**Procedure**

- To run a playbook, right-click the playbook name in the **Explorer** pane, then selectRun Ansible Playbook via→Run playbook via `    ansible-playbook` .

![Run playbook via ansible-playbook](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/73a0c743e4f7c0f2a2f8073956b2fed4/ansible-playbook-run.png)





The output is displayed in the **Terminal** tab of the VS Code terminal. The `ok=2` and `failed=0` messages indicate that the playbook ran successfully.

![Success message for ansible-playbook execution](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/f7c82c475842a919188ec2aa473d5b0f/ansible-playbook-success.png)


### 5.5.2. Running your playbook with `ansible-navigator`




**Prerequisites**

- In the Ansible extension settings, enable the use of an execution environment in **Ansible Execution Environment > Enabled** .
- Enter the path or URL for the execution environment image in **Ansible > Execution Environment: Image** .


**Procedure**

1. To run a playbook, right-click the playbook name in the Explorer pane, then selectRun Ansible Playbook via→Run playbook via ansible-navigator run.

The output is displayed in the **Terminal** tab of the VS Code terminal. The **Successful** status indicates that the playbook ran successfully.

![Output for ansible-navigator execution](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/bbf860d1eec56d58648bfec6da63551f/devtools-extension-navigator-output.png)



1. Enter the number next to a play to step into the play results. The example playbook only contains one play. Enter `    0` to view the status of the tasks executed in the play.

![Tasks in ansible-navigator output](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/7cf0a79f0236bfcc6bdb9e9bd00c9cf5/devtools-extension-navigator-tasks.png)


Type the number next to a task to review the task results.




For more information on running playbooks with automation content navigator, see [Executing a playbook from automation content navigator](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_content_navigator/assembly-execute-playbooks-navigator_ansible-navigator#proc-execute-playbook-tui_execute-playbooks-navigator) in the _Using content navigator_ Guide.

### 5.5.3. Working with execution environments




You can view the automation execution environments provided by Red Hat in the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/search?searchType=containers&build_categories_list=Automation%20execution%20environment&p=1) .

Click on an execution environment for information on how to download it.

1. Log in to `    registry.redhat.io` if you have not already done so.

Note
If you are running Ansible development tools on a container inside VS Code and you want to pull execution environments or the `    devcontainer` to use as an execution environment, you must log in to `    registry.redhat.io` from a terminal prompt within the `    devcontainer` inside VS Code.




1. Using the information in the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/search?searchType=containers&build_categories_list=Automation%20execution%20environment&p=1) , download the execution environment you need.

For example, to download the minimal RHEL 8 base image, run the following command:


```
$ podman pull registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel9
```




You can build and create custom execution environments with `ansible-builder` . For more information about working with execution environments locally, see [Creating and using execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments) .

After customizing your execution environment, you can push your new image to the container registry in automation hub. See [Publishing an automation execution environment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments/index#assembly-publishing-exec-env) in the _Creating and using execution environments_ documentation.

## 5.6. Testing your playbooks




To test your playbooks in your project, run them in a non-production environment such as a lab setup or a virtual machine.

Automation content navigator ( `ansible-navigator` ) is a text-based user interface (TUI) for developing and troubleshooting Ansible content with execution environments.

Running a playbook using `ansible-navigator` generates verbose output that you can inspect to check whether the playbook is running the way you expected. You can specify the execution environment that you want to run your playbooks on, so that your tests replicate the production setup on Ansible Automation Platform:

- To run a playbook on an execution environment, run the following command from the terminal in VS Code:


```
$ ansible-navigator run &lt;playbook_name.yml&gt; -eei &lt;execution_environment_name&gt;
```

For example, to execute a playbook called `    site.yml` on the Ansible Automation Platform RHEL 9 minimum execution environment, run the following command from the terminal in VS Code.


```
ansible-navigator run site.yml --eei ee-minimal-rhel8
```




The output is displayed in the terminal. You can inspect the results and step into each play and task that was executed.

For more information about running playbooks, refer to [Running Ansible playbooks with automation content navigator](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_content_navigator/assembly-execute-playbooks-navigator_ansible-navigator) in the _Using content navigator_ guide.

# Chapter 6. Publishing and running your playbooks in Ansible Automation Platform




The following procedures describe how to deploy your new playbooks in your instance of Ansible Automation Platform so that you can use them to run automation jobs.

## 6.1. Saving your project in SCM




Save your playbook project as a repository in your source control management system, for example GitHub.

**Procedure**

1. Initialize your project directory as a git repository.
1. Push your project up to a source control system such as GitHub.


## 6.2. Running your playbook in Ansible Automation Platform




To run your playbook in Ansible Automation Platform, you must create a project in automation controller for the repository where you stored your playbook project. You can then create a job template for each playbook from the project.

**Procedure**

1. In a browser, log in to automation controller.
1. Configure a Source Control credential type for your source control system if necessary. See the [Creating new credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#controller-create-credential) section of _Using automation execution_ for more details. [https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#controller-create-credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#controller-create-credential)
1. In automation controller, create a project for the GitHub repository where you stored your playbook project. Refer to the [Projects](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-projects) chapter of _Using automation execution_ .
1. Create a job template that uses a playbook from the project that you created. Refer to the [Job Templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-job-templates) chapter of _Using automation execution_ .
1. Run your playbook from automation controller by launching the job template. Refer to the [Launching a job template](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-job-templates#controller-launch-job-template) section of _Using automation execution_ .


# Chapter 7. Developing collections




Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. Red Hat provides Ansible Content Collections on Ansible automation hub that contain both Red Hat Ansible Certified Content and Ansible validated content.

If you have installed private automation hub, you can create collections for your organization and push them to private automation hub so that you can use them in job templates in Ansible Automation Platform. You can use collections to package and distribute plug-ins. These plug-ins are written in Python.

You can also create collections to package and distribute Ansible roles, which are expressed in YAML. You can also include playbooks and custom plug-ins that are required for these roles in the collection. Typically, collections of roles are distributed for use within your organization.

# Chapter 8. Creating a collection for distributing roles




An Ansible role is a self-contained unit of Ansible automation content that groups related tasks and associated variables, files, handlers, and other assets in a defined directory structure.

You can run Ansible roles in one or more plays, and reuse them across playbooks. Invoking roles instead of tasks simplifies playbooks. You can migrate existing standalone roles into collections, and push them to private automation hub to share them with other users in your organization. Distributing roles in this way is a typical way to use collections.

With Ansible collections, you can store and distribute multiple roles in a single unit of reusable automation. Inside a collection, you can share custom plug-ins across all roles in the collection instead of duplicating them in each role.

You must move roles into collections if you want to use them in Ansible Automation Platform.

You can add existing standalone roles to a collection, or add new roles to it. Push the collection to source control and configure credentials for the repository in Ansible Automation Platform.

## 8.1. Planning your collection




Organize smaller bundles of curated automation into separate collections for specific functions, rather than creating one big general collection for all of your roles.

For example, you could store roles that manage the networking for an internal system called `myapp` in a `company_namespace.myapp_network` collection, and store roles that manage and deploy networking in AWS in a collection called `company_namespace.aws_net` .

## 8.2. Prerequisites




- You have installed VS Code and the Ansible extension.
- You have installed the Microsoft Dev Containers extension in {VS Code.
- You have installed Ansible development tools.
- You have installed a containerization platform, for example Podman, Podman Desktop, Docker, or Docker Desktop.
- You have a Red Hat account and you can log in to the Red Hat container registry at `    registry.redhat.io` . For information about logging in to `    registry.redhat.io` , see [Authenticating with the Red Hat container registry](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/developing_automation_content/index#devtools-setup-registry-redhat-io_installing-devtools) .


## 8.3. Scaffolding a collection for your roles




You can scaffold a collection for your roles from the Ansible extension in VS Code.

**Procedure**

1. Open VS Code.
1. Navigate to the directory where you want to create your roles collection.
1. Click the Ansible icon in the VS Code activity bar to open the Ansible extension.
1. Select **Get started** in the **Ansible content creator** section.

The **Ansible content creator** tab opens.


1. In the **Create** section, click **Ansible collection project** .

The **Create new Ansible project** tab opens.


1. In the form in the **Create Ansible project** tab, enter the following:


-  **Namespace** : Enter a name for your namespace, for example `        company_namespace` .
-  **Collection** : Enter a name for your collection, for example, `        myapp_network` .
-  **Init path** : Enter the path to the directory where you want to scaffold your new collection.

If you enter an existing directory name, the scaffolding process overwrites the contents of that directory. The scaffold process only allows you to use an existing directory if you enable the Force option.


- If you are using the containerized version of Ansible development tools, the destination directory path is relative to the container, not a path in your local system. To discover the current directory name in the container, run the pwd command in a terminal in VS Code. If the current directory in the container is `            workspaces` , enter `            workspaces/&lt;current_project&gt;/collections` .
- If you are using a locally installed version of Ansible Dev tools, enter the full path to the directory, for example `            /user/&lt;username&gt;/path/to/&lt;collection_directory&gt;` .


1. ClickCreate.


**Verification**

The following message appears in the **Logs** pane of the **Create Ansible collection** tab.


```
--------------------- ansible-creator logs ---------------------

Note: collection company_namespace.myapp_network created at /path/to/collections/directory
```

The following directories and files are created in your `collections/` directory:

```
├── .devcontainer
├── .github
├── .gitignore
├── .isort.cfg
├── .pre-commit-config.yaml
├── .prettierignore
├── .vscode
├── CHANGELOG.rst
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING
├── LICENSE
├── MAINTAINERS
├── README.md
├── changelogs
├── devfile.yaml
├── docs
├── extensions
├── galaxy.yml
├── meta
├── plugins
├── pyproject.toml
├── requirements.txt
├── roles
├── test-requirements.txt
├── tests
└── tox-ansible.ini
```

## 8.4. Migrating existing roles to your collection




The directory for a standalone role has the following structure. Your role might not contain all of these directories.

```
my_role
├── README.md
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── tasks
│   └── main.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
└── main.yml
```

An Ansible role has a defined directory structure with seven main standard directories. Each role must must include at least one of these directories. You can omit any directories the role does not use. Each directory contains a `main.yml` file.

**Procedure**

1. If necessary, rename the directory that contains your role to reflect its content, for example, `    acl_config` or `    tacacs` .

Roles in collections cannot have hyphens in their names. Use the underscore character ( `    _` ) instead.


1. Copy the roles directories from your standalone role into the `    roles/` directory in your collection.

For example, in a collection called `    myapp_network` , add your roles to the `    myapp_network/roles/` directory.


1. Copy any plug-ins from your standalone roles into the `    plugins directory/` for your new collection. The collection directory structure resembles the following.


```
company_namespace    └── myapp_network        ├── ...        ├── galaxy.yml        ├── docs        ├── extensions        ├── meta        ├── plugins        ├── roles        │   ├── acl_config        │   │   ├── README.md        │   │   ├── defaults        │   │   ├── files        │   │   ├── handlers        │   │   ├── meta        │   │   ├── tasks        │   │   ├── templates        │   │   ├── tests        │   │   └── vars        │   └── tacacs        │       ├── README.md        │       ├── default        │       ├── files        │       ├── handlers        │       ├── meta        │       ├── tasks        │       ├── templates        │       ├── tests        │       └── vars        │   ├── run        ├── ...        ├── tests        └── vars
```

The `    run` role is a default role directory that is created when you scaffold the collection.


1. Update your playbooks to use the fully qualified collection name (FQDN) for your new roles in your collection.


Not every standalone role will seamlessly integrate into your collection without modification of the code. For example, if a third-party standalone role from Galaxy that contains a plug-in uses the `module_utils/` directory, then the plug-in itself has import statements.

## 8.5. Creating a new role in your collection




**Procedure**

1. To create a new role, copy the default `    run` role directory that was scaffolded when you created the collection.
1. Define the tasks that you want your role to perform in the `    tasks/main.yml` file. If you are creating a role to reuse tasks in an existing playbook, copy the content in the tasks block of your playbook YAML file. Remove the whitespace to the left of the tasks. Use `    ansible-lint` in VS Code to check your YAML code.
1. If your role depends on another role, add the dependency in the `    meta/main.yml` file.


## 8.6. Adding documentation for your roles collection




It is important to provide documentation for your roles and roles collection, so that other users understand what your roles do and how to use them.

1. To add documentation for a role, navigate to the role directory.
1. Open the `    README.md` file in an editor. This file was added in the role directory when you scaffolded your collection directory.
1. Provide the following information in the `    README.md` files for every role in your collection:


- Role description: A brief summary of what the role does
- Requirements: List the collections, libraries, and required installations
- Dependencies
- Role variables: Provide the following information about the variables your role uses.


- Description
- Defaults
- Example values
- Required variables

- Example playbook: Show an example of a playbook that uses your role. Use comments in the playbook to help users understand where to set variables.

The `        README.md` file in [controller_configuration.ad_hoc_command_cancel](https://github.com/redhat-cop/controller_configuration/tree/devel/roles/ad_hoc_command_cancel) is an example of a role with standard documentation.



1. To add documentation for your roles collection, navigate to the collection directory.
1. In the `    README.md` file for your collection, provide the following information:


- Collection description: Describe what the collection does.
- Requirements: List required collections.
- List the roles as a component of the collection.
- Using the collection: Describe how to run the components of the collection.
- Add a troubleshooting section.
- Versioning: Describe the release cycle of your collection.



## 8.7. Publishing your collection in private automation hub




1. Prerequisite


- Package your collection into a tarball. Format your collection file name as follows:



`&lt;my_namespace-my_collection-x.y.z.tar.gz&gt;`

For example, `company_namespace-myapp_network-1.0.0.tar.gz`

**Procedure**

1. Create a namespace for your collection in private automation hub. See [Creating a namespace](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-collections-hub#proc-create-namespace) in the _Managing automation content_ guide.
1. Optional: Add information to your namespace. See [Adding additional information and resources to a namespace](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-collections-hub#proc-edit-namespace) in the _Managing automation content_ guide.
1. Upload your roles collections tarballs to your namespace. See [Uploading collections to your namespaces](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-collections-hub#proc-uploading-collections) in the _Managing automation content_ guide.
1. Approve your collection for internal publication. See [Uploading collections to your namespaces](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-collections-hub#proc-approve-collection) in the _Managing automation content_ guide.


### 8.7.1. Using your collection in projects in Red Hat Ansible Automation Platform




To use your collection in automation controller, you must add your collection to an execution environment and push it to private automation hub.

The following procedure describes the workflow to add a collection to an execution environment. Refer to [Customizing an existing automation executions environment image](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments/assembly-publishing-exec-env#proc-customize-ee-image) in the _Creating and using execution environments_ guide for the commands to execute these steps.

1. You can pull an execution environment base image from automation hub, or you can add your collection to your own custom execution environment.
1. Add the collections that you want to include in the execution environment.
1. Build the new execution environment.
1. Verify that the collections are in the execution environment.
1. Tag the image and push it to private automation hub.
1. Pull your new image into your automation controller instance.
1. The playbooks that use the roles in your collection must use the fully qualified domain name (FQDN) for the roles.



<span id="idm139845121530144"></span>
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





