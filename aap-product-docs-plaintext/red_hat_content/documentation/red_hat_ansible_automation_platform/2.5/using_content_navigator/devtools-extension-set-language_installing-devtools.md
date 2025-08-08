# 2. Installing Ansible development tools
## 2.1. Requirements
### 2.1.6. Associating the Ansible language to YAML files




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




### 2.1.7. Installing and configuring the `Dev Containers` extension




If you are installing the containerized version of Ansible development tools, you must install the [Microsoft Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code.

1. Open VS Code.
1. Click the **Extensions** (![Extensions](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/417ed5315a44493c6a44ae5c12dc6fab/vscode-extensions-icon.png)
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


## 2.2. Installing Ansible development tools on a container inside VS Code




The Dev Containers VS Code extension requires a `.devcontainer` file to store settings for your dev containers. You must use the Ansible extension to scaffold a config file for your dev container, and reopen your directory in a container in VS Code.

**Prerequisites**

- You have installed a containerization platform, for example Podman, Podman Desktop, Docker, or Docker Desktop.
- You have a Red Hat login and you have logged in to the Red Hat registry at `    registry.redhat.io` . For information about logging in to `    registry.redhat.io` , see [Authenticating with the Red Hat container registry](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_content_navigator/index#devtools-setup-registry-redhat-io_installing-devtools) .
- You have installed VS Code.
- You have installed the Ansible extension in VS Code.
- You have installed the [Microsoft Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code.
- If you are installing Ansible development tools on Windows, launch VS Code and connect to the WSL machine:


1. Click the `        Remote` (![Remote](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/706517b6299d38221f473c0bce4863e1/vscode-remote-icon.png)
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

![Reopen in container](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/396c911927f946c71508d085befd3e04/devtools-reopen-in-container.png)


Click **Reopen in Container** .


- If the notification does not appear, click the `        Remote` (![Remote](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/706517b6299d38221f473c0bce4863e1/vscode-remote-icon.png)
) icon. In the dropdown menu that appears, select **Reopen in Container** .

1. Select the dev container for Podman or Docker according to the containerization platform you are using.

The **Remote ()** status in the VS Code Status bar displays `    opening Remote` and a notification indicates the progress in opening the container.




**Verification**

When the directory reopens in a container, the **Remote ()** status displays `Dev Container: ansible-dev-container` .


Note
The base image for the container is a Universal Base Image Minimal (UBI Minimal) image that uses `microdnf` as a package manager. The `dnf` and `yum` package managers are not available in the container.

For information about using `microdnf` in containers based on UBI Minimal images, see [Adding software in a minimal UBI container](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/assembly_adding-software-to-a-ubi-container_building-running-and-managing-containers#proc_adding-software-in-a-minimal-ubi-container_assembly_adding-software-to-a-ubi-container) in the Red Hat Enterprise Linux _Building, running, and managing containers_ guide.



## 2.3. Installing Ansible development tools from a package on RHEL




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

# Chapter 3. Reviewing automation execution environments with automation content navigator




As a content developer, you can review your automation execution environment with automation content navigator and display the packages and collections included in the automation execution environments. Automation content navigator runs a playbook to extract and display the results.

## 3.1. Reviewing automation execution environments from automation content navigator




You can review your automation execution environments with the automation content navigator text-based user interface.

**Prerequisites**

- Automation execution environments


**Procedure**

1. Review the automation execution environments included in your automation content navigator configuration.


```
$ ansible-navigator images
```

![List of automation execution environments](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/90e4e02d453e60534c4b15909c8f67d3/navigator-images-list.png)



1. Type the number of the automation execution environment you want to delve into for more details.

![Automation execution environment details](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/843fc84551c92a30484d2056db1c9716/navigator-image-details.png)


You can review the packages and versions of each installed automation execution environment and the Ansible version any included collections.


1. Optional: pass in the automation execution environment that you want to use. This becomes the primary and is the automation execution environment that automation content navigator uses.


```
$ ansible-navigator images --eei registry.example.com/example-enterprise-ee:latest
```




**Verification**

- Review the automation execution environment output.

![Automation execution environment output](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/843fc84551c92a30484d2056db1c9716/navigator-image-details.png)





# Chapter 4. Reviewing inventories with automation content navigator




As a content creator, you can review your Ansible inventory with automation content navigator and interactively delve into the groups and hosts.

## 4.1. Reviewing inventory from automation content navigator




You can review Ansible inventories with the automation content navigator text-based user interface in interactive mode and delve into groups and hosts for more details.

**Prerequisites**

- A valid inventory file or an inventory plugin.


**Procedure**

1. Start automation content navigator.


```
$ ansible-navigator
```

Optional: type `    ansible-navigator inventory -i simple_inventory.yml` from the command line to view the inventory.


1. Review the inventory.


```
:inventory -i simple_inventory.yml           TITLE            DESCRIPTION    0│Browse groups    Explore each inventory group and group members members    1│Browse hosts     Explore the inventory with a list of all hosts
```


1. Type `    0` to brows the groups.


```
NAME               TAXONOMY                      TYPE    0│general            all                           group    1│nodes              all                           group    2│ungrouped          all                           group
```

The `    TAXONOMY` field details the hierarchy of groups the selected group or node belongs to.


1. Type the number corresponding to the group you want to delve into.


```
NAME              TAXONOMY                        TYPE    0│node-0            all▸nodes                       host    1│node-1            all▸nodes                       host    2│node-2            all▸nodes                       host
```


1. Type the number corresponding to the host you want to delve into, or type `    :&lt;number&gt;` for numbers greater than 9.


```
[node-1]    0│---    1│ansible_host: node-1.example.com    2│inventory_hostname: node-1
```




**Verification**

- Review the inventory output.


```
TITLE            DESCRIPTION    0│Browse groups   Explore each inventory group and group members members    1│Browse hosts    Explore the inventory with a list of all hosts
```




**Additional resources**

-  [ansible-inventory](https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html) .
-  [How to build your inventory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html) .


# Chapter 5. Browsing collections with automation content navigator




As a content creator, you can browse your Ansible collections with automation content navigator and interactively delve into each collection developed locally or within Automation execution environments.

## 5.1. Automation content navigator collections display




Automation content navigator displays information about your collections with the following details for each collection:

![Automation content navigator collections display](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/df264a85627b2f482122c5d3dc0c07cf/navigator-collections-shadow.png)


## 5.2. Browsing collections from automation content navigator




You can browse Ansible collections with the automation content navigator text-based user interface in interactive mode and delve into each collection. automation content navigator shows collections within the current project directory and those available in the automation execution environments

**Prerequisites**

- A locally accessible collection or installed automation execution environments.


**Procedure**

1. Start automation content navigator


```
$ ansible-navigator
```


1. Browse the collection. Alternately, you can type `    ansible-navigator collections` to directly browse the collections.


```
$ :collections
```

![A list of Ansible collections shown in the automation content navigator](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/a7b4611efdde018154c3717444581117/navigator-collection-list.png)



1. Type the number of the collection you want to explore.


```
:4
```

![A collection shown in the automation content navigator](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/11c84eb67977b58176f1ce30a5aa168e/navigator-plugin-list.png)



1. Type the number corresponding to the module you want to delve into.


```
ANSIBLE.UTILS.IP_ADDRESS: Test if something in an IP address     0│---     1│additional_information: {}     2│collection_info:     3│  authors:     4│  - Ansible Community     5│  dependencies: {}     6│  description: Ansible Collection with utilities to ease the management, manipulation,     7│    and validation of data within a playbook     8│  documentation: null     9│  homepage: null    10│  issues: null    11│  license: []    12│  license_file: LICENSE    13│  name: ansible.utils    14│  namespace: ansible    15│  path:/usr/share/ansible/collections/ansible_collections/ansible/utils/    16│  readme: README.md    &lt;... output truncated...&gt;
```


1. Optional: jump to the documentation examples for this module.


```
:{{ examples }}        0│    1│    2│#### Simple examples    3│    4│- name: Check if 10.1.1.1 is a valid IP address    5│  ansible.builtin.set_fact:    6│    data: "{{ '10.1.1.1' is ansible.utils.ip_address }}"    7│    8│# TASK [Check if 10.1.1.1 is a valid IP address] *********************    9│# ok: [localhost] =&gt; {    10│#     "ansible_facts": {    11│#         "data": true    12│#     },    13│#     "changed": false    14│# }    15│
```


1. Optional: open the example in your editor to copy it into a playbook.


```
:open
```

![Documentation example shown in the editing tool](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/3405ec63edee7bec61c21f0bc6ba5e57/navigator-vscode-example.png)





**Verification**

- Browse the collection list.

![Collection list](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/a7b4611efdde018154c3717444581117/navigator-collection-list.png)





## 5.3. Review documentation from automation content navigator




You can review Ansible documentation for collections and plugins with the automation content navigator text-based user interface in interactive mode. automation content navigator shows collections within the current project directory and those available in the automation execution environments

**Prerequisites**

- A locally accessible collection or installed automation execution environments.


**Procedure**

1. Start automation content navigator


```
$ ansible-navigator
```


1. Review the module you are interested in. Alternately, you can type `    ansible-navigator doc` to access the documentation.


```
:doc ansible.utils.ip_address
```


```
ANSIBLE.UTILS.IP_ADDRESS: Test if something in an IP address     0│---     1│additional_information: {}     2│collection_info:     3│  authors:     4│  - Ansible Community     5│  dependencies: {}     6│  description: Ansible Collection with utilities to ease the management, manipulation,     7│    and validation of data within a playbook     8│  documentation: null     9│  homepage: null    10│  issues: null    11│  license: []    12│  license_file: LICENSE    13│  name: ansible.utils    14│  namespace: ansible    15│  path:/usr/share/ansible/collections/ansible_collections/ansible/utils/    16│  readme: README.md    &lt;... output truncated...&gt;
```


1. Jump to the documentation examples for this module.


```
:{{ examples }}        0│    1│    2│#### Simple examples    3│    4│- name: Check if 10.1.1.1 is a valid IP address    5│  ansible.builtin.set_fact:    6│    data: "{{ '10.1.1.1' is ansible.utils.ip_address }}"    7│    8│# TASK [Check if 10.1.1.1 is a valid IP address] *********************    9│# ok: [localhost] =&gt; {    10│#     "ansible_facts": {    11│#         "data": true    12│#     },    13│#     "changed": false    14│# }    15│
```


1. Optional: open the example in your editor to copy it into a playbook.


```
:open
```

![Documentation example in editor](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/3405ec63edee7bec61c21f0bc6ba5e57/navigator-vscode-example.png)


See [Automation content navigator general settings](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_content_navigator/index#ref-navigator-general-settings_settings-navigator) for details on how to set up your editor.




**Additional resources**

-  [Collection index](https://docs.ansible.com/ansible/latest/collections/index.html)
-  [Using Ansible collections](https://docs.ansible.com/ansible/latest/collections_guide/index.html)
-  [Building Ansible inventories](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html)


# Chapter 6. Running Ansible playbooks with automation content navigator




As a content creator, you can execute your Ansible playbooks with automation content navigator and interactively delve into the results of each play and task to verify or troubleshoot the playbook. You can also execute your Ansible playbooks inside an execution environment and without an execution environment to compare and troubleshoot any problems.

## 6.1. Executing a playbook from automation content navigator




You can run Ansible playbooks with the automation content navigator text-based user interface to follow the execution of the tasks and delve into the results of each task.

**Prerequisites**

- A playbook.
- A valid inventory file if not using `    localhost` or an inventory plugin.


**Procedure**

1. Start automation content navigator


```
$ ansible-navigator
```


1. Run the playbook.


```
$ :run
```


1. Optional: type `    ansible-navigator run simple-playbook.yml -i inventory.yml` to run the playbook.
1. Verify or add the inventory and any other command line parameters.


```
INVENTORY OR PLAYBOOK NOT FOUND, PLEASE CONFIRM THE FOLLOWING    ─────────────────────────────────────────────────────────────────────────       Path to playbook: /home/ansible-navigator_demo/simple_playbook.yml       Inventory source: /home/ansible-navigator-demo/inventory.yml      Additional command line parameters: Please provide a value (optional)    ──────────────────────────────────────────────────────────────────────────                                                               Submit Cancel
```


1. Tab to `    Submit` and hit Enter. You should see the tasks executing.

![Executing playbook tasks](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/a3706c3ec1968a9904cfe1698883df98/navigator-play-list.png)



1. Type the number next to a play to step into the play results, or type `    :&lt;number&gt;` for numbers above 9.

![Task list](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/7dc3cc85136b2385479f478dfec6a029/navigator-task-list.png)


Notice failed tasks show up in red if you have colors enabled for automation content navigator.


1. Type the number next to a task to review the task results, or type `    :&lt;number&gt;` for numbers above 9.

![Failed task results](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/0d794db8521c4137d71804bd6c91da52/navigator-task-output-failed.png)



1. Optional: type `    :doc` bring up the documentation for the module or plugin used in the task to aid in troubleshooting.


```
ANSIBLE.BUILTIN.PACKAGE_FACTS (MODULE)      0│---      1│doc:      2│  author:      3│  - Matthew Jones (@matburt)      4│  - Brian Coca (@bcoca)      5│  - Adam Miller (@maxamillion)      6│  collection: ansible.builtin      7│  description:      8│  - Return information about installed packages as facts.    &lt;... output omitted ...&gt;     11│  module: package_facts     12│  notes:     13│  - Supports C(check_mode).     14│  options:     15│    manager:     16│      choices:     17│      - auto     18│      - rpm     19│      - apt     20│      - portage     21│      - pkg     22│      - pacman        &lt;... output truncated ...&gt;
```




**Additional resources**

-  [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html)
-  [Ansible playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html)


## 6.2. Reviewing playbook results with an automation content navigator artifact file




Automation content navigator saves the results of the playbook run in a JSON artifact file. You can use this file to share the playbook results with someone else, save it for security or compliance reasons, or review and troubleshoot later. You only need the artifact file to review the playbook run. You do not need access to the playbook itself or inventory access.

**Prerequisites**

- A automation content navigator artifact JSON file from a playbook run.


**Procedure**

- Start automation content navigator with the artifact file.


```
$ ansible-navigator replay simple_playbook_artifact.json
```


1. Review the playbook results that match when the playbook ran.

![Playbook results](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/4f50de6511503aed4d7729dafafad134/navigator-artifact-replay.png)






You can now type the number next to the plays and tasks to step into each to review the results, as you would after executing the playbook.

**Additional resources**

-  [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html)
-  [Ansible playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html)


# Chapter 7. Reviewing your Ansible configuration with automation content navigator




As a content creator, you can review your Ansible configuration with automation content navigator and interactively delve into settings.

## 7.1. Reviewing your Ansible configuration from automation content navigator




You can review your Ansible configuration with the automation content navigator text-based user interface in interactive mode and delve into the settings. Automation content navigator pulls in the results from an accessible Ansible configuration file, or returns the defaults if no configuration file is present.

**Prerequisites**

- You have authenticated to the Red Hat registry if you need to access additional automation execution environments. See [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication) for details.


**Procedure**

1. Start automation content navigator


```
$ ansible-navigator
```

Optional: type `    ansible-navigator config` from the command line to access the Ansible configuration settings.


1. Review the Ansible configuration.


```
:config
```

![Ansible configuration](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/060e3e3a6b8d3acd2dbfa26e0a789d44/navigator-ansible-config.png)


Some values reflect settings from within the automation execution environments needed for the automation execution environments to function. These display as non-default settings you cannot set in your Ansible configuration file.


1. Type the number corresponding to the setting you want to delve into, or type `    :&lt;number&gt;` for numbers greater than 9.


```
ANSIBLE COW ACCEPTLIST (current: ['bud-frogs', 'bunny', 'cheese']) (default:     0│---     1│current:     2│- bud-frogs     3│- bunny     4│- cheese     5│default:     6│- bud-frogs     7│- bunny     8│- cheese     9│- daemon
```




The output shows the current `setting` as well as the `default` . Note the `source` in this example is `env` since the setting comes from the automation execution environments.

**Verification**

- Review the configuration output.

![Configuration output](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/060e3e3a6b8d3acd2dbfa26e0a789d44/navigator-ansible-config.png)





**Additional resources**

-  [ansible-config](https://docs.ansible.com/ansible/latest/cli/ansible-config.html) .
-  [Introduction to Ansible configuration](https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html) .


# Chapter 8. Automation content navigator configuration settings




As a content creator, you can configure automation content navigator to suit your development environment.

## 8.1. Creating an automation content navigator settings file




You can alter the default automation content navigator settings through:

- The command line
- Within a settings file
- As an environment variable


Automation content navigator checks for a settings file in the following order and uses the first match:

-  `    ANSIBLE_NAVIGATOR_CONFIG` - The settings file path environment variable if set.
-  `    ./ansible-navigator.&lt;ext&gt;` - The settings file within the current project directory, with no dot in the file name.
-  `    \~/.ansible-navigator.&lt;ext&gt;` - Your home directory, with a dot in the file name.


Consider the following when you create an automation content navigator settings file:

- The settings file can be in `    JSON` or `    YAML` format.
- For settings in `    JSON` format, the extension must be `    .json` .
- For settings in `    YAML` format, the extension must be `    .yml` or `    .yaml` .
- The project and home directories can only contain one settings file each.
- If automation content navigator finds more than one settings file in either directory, it results in an error.


You can copy the example settings file below into one of those paths to start your `ansible-navigator` settings file.

```
---
ansible-navigator:
#   ansible:
#     config: /tmp/ansible.cfg
#     cmdline: "--forks 15"
#     inventories:
#     - /tmp/test_inventory.yml
#     playbook: /tmp/test_playbook.yml
#   ansible-runner:
#     artifact-dir: /tmp/test1
#     rotate-artifacts-count: 10
#     timeout: 300
#   app: run
#   collection-doc-cache-path: /tmp/cache.db
#   color:
#     enable: False
#     osc4: False
#   editor:
#     command: vim_from_setting
#     console: False
#   documentation:
#     plugin:
#       name: shell
#       type: become
#   execution-environment:
#     container-engine: podman
#     enabled: False
#     environment-variables:
#       pass:
#         - ONE
#         - TWO
#         - THREE
#       set:
#         KEY1: VALUE1
#         KEY2: VALUE2
#         KEY3: VALUE3
#     image: test_image:latest
#     pull-policy: never
#     volume-mounts:
#     - src: "/test1"
#       dest: "/test1"
#       label: "Z"
#   help-config: True
#   help-doc: True
#   help-inventory: True
#   help-playbook: False
#   inventory-columns:
#     - ansible_network_os
#     - ansible_network_cli_ssh_type
#     - ansible_connection
logging:
#     append: False
level: critical
#     file: /tmp/log.txt
#   mode: stdout
#   playbook-artifact:
#     enable: True
#     replay: /tmp/test_artifact.json
#     save-as: /tmp/test_artifact.json
```

## 8.2. Automation content navigator general settings




The following table describes each general parameter and setting options for automation content navigator.


<span id="idm140640043334784"></span>
**Table 8.1. Automation content navigator general parameters settings**

| Parameter | Description | Setting options |
| --- | --- | --- |
| ansible-runner-artifact-dir | The directory path to store artifacts generated by ansible-runner. |  **Default:** No default value set

**CLI:**  `--rad` or `--ansible-runner-artifact-dir`

**ENV:**  `ANSIBLE_NAVIGATOR_ANSIBLE_RUNNER_ARTIFACT_DIR`

**Settings file:**

```
ansible-navigator:
ansible-runner:
artifact-dir:
``` |
| ansible-runner-rotate-artifacts-count | Keep ansible-runner artifact directories, for last n runs. If set to 0, artifact directories are not deleted. |  **Default:** No default value set

**CLI:**  `--rac` or `--ansible-runner-rotate-artifacts-count`

**ENV:**  `ANSIBLE_NAVIGATOR_ANSIBLE_RUNNER_ROTATE_ARTIFACTS_COUNT`

**Settings file:**

```
ansible-navigator:
ansible-runner:
rotate-artifacts-count:
``` |
| ansible-runner-timeout | The timeout value after which `ansible-runner` force stops the execution. |  **Default:** No default value set

**CLI:**  `--rt` or `--ansible-runner-timeout`

**ENV:**  `ANSIBLE_NAVIGATOR_ANSIBLE_RUNNER_TIMEOUT`

**Settings file:**

```
ansible-navigator:
ansible-runner:
timeout:
``` |
| app | Entry point for automation content navigator. |  **Choices** : `collections` , `config` , `doc` , `images` , `inventory` , `replay` , `run` or `welcome`

**Default** : `welcome`

**CLI example** : `ansible-navigator collections`

**ENV** : `ANSIBLE_NAVIGATOR_APP`

**Settings file:**

```
ansible-navigator:
app:
``` |
| cmdline | Extra parameters passed to the corresponding command. |  **Default** : No default value

**CLI** : positional

**ENV** : `ANSIBLE_NAVIGATOR_CMDLINE`

**Settings file:**

```
ansible-navigator:
ansible:
cmdline:
``` |
| collection-doc-cache-path | The path to the collection doc cache. |  **Default** : `$HOME/.cache/ansible-navigator/collection_doc_cache.db`

**CLI** : `--cdcp` or `--collection-doc-cache-path`

**ENV** : `ANSIBLE_NAVIGATOR_COLLECTION_DOC_CACHE_PATH`

**Settings file:**

```
ansible-navigator:
collection-doc-cache-path:
``` |
| container-engine | Specify the container engine ( `auto` = `podman` then `docker` ). |  **Choices:**  `auto` , `podman` or `docker`

**Default:**  `auto`

**CLI:**  `--ce` or `--container-engine`

**ENV:**  `ANSIBLE_NAVIGATOR_CONTAINER_ENGINE`

**Settings file:**

```
ansible-navigator:
execution-environment:
container-engine:
``` |
| display-color | Enable the use of color in the display. |  **Choices:**  `True` or `False`

**Default:**  `True`

**CLI:**  `--dc` or `--display-color`

**ENV:**  `NO_COLOR`

**Settings file:**

```
ansible-navigator:
color:
enable:
``` |
| editor-command | Specify the editor used by automation content navigator | Default:* vi +{line_number} {filename}

**CLI:**  `--ecmd` or `--editor-command`

**ENV:**  `ANSIBLE_NAVIGATOR_EDITOR_COMMAND`

**Settings file:**

```
ansible-navigator:
editor:
command:
``` |
| editor-console | Specify if the editor is console based. |  **Choices:**  `True` or `False`

**Default:**  `True`

**CLI:**  `--econ` or `--editor-console`

**ENV:**  `ANSIBLE_NAVIGATOR_EDITOR_CONSOLE`

**Settings file:**

```
ansible-navigator:
editor:
console:
``` |
| execution-environment | Enable or disable the use of an automation execution environment. |  **Choices:**  `True` or `False`

**Default:**  `True`

**CLI:**  `--ee` or `--execution-environment`

**ENV:** * `ANSIBLE_NAVIGATOR_EXECUTION_ENVIRONMENT`

**Settings file:**

```
ansible-navigator:
execution-environment:
enabled:
``` |
| execution-environment-image | Specify the name of the automation execution environment image. |  **Default:**  `quay.io/ansible/ansible-runner:devel`

**CLI:**  `--eei` or `--execution-environment-image`

**ENV:**  `ANSIBLE_NAVIGATOR_EXECUTION_ENVIRONMENT_IMAGE`

**Settings file:**

```
ansible-navigator:
execution-environment:
image:
``` |
| execution-environment-volume-mounts | Specify volume to be bind mounted within an automation execution environment ( `--eev /home/user/test:/home/user/test:Z` ) |  **Default:** No default value set

**CLI:**  `--eev` or `--execution-environment-volume-mounts`

**ENV:**  `ANSIBLE_NAVIGATOR_EXECUTION_ENVIRONMENT_VOLUME_MOUNTS`

**Settings file:**

```
ansible-navigator:
execution-environment:
volume-mounts:
``` |
| log-append | Specify if log messages should be appended to an existing log file, otherwise a new log file is created per session. |  **Choices:**  `True` or `False`

**Default:** True

**CLI:**  `--la` or `--log-append`

**ENV:**  `ANSIBLE_NAVIGATOR_LOG_APPEND`

**Settings file:**

```
ansible-navigator:
logging:
append:
``` |
| log-file | Specify the full path for the automation content navigator log file. |  **Default:**  `$PWD/ansible-navigator.log`

**CLI:**  `--lf` or `--log-file`

**ENV:**  `ANSIBLE_NAVIGATOR_LOG_FILE`

**Settings file:**

```
ansible-navigator:
logging:
file:
``` |
| log-level | Specify the automation content navigator log level. |  **Choices:**  `debug` , `info` , `warning` , `error` or `critical`

**Default:**  `warning`

**CLI:**  `--ll` or `--log-level`

**ENV:**  `ANSIBLE_NAVIGATOR_LOG_LEVEL`

**Settings file:**

```
ansible-navigator:
logging:
level:
``` |
| mode | Specify the user-interface mode. |  **Choices:**  `stdout` or `interactive`

**Default:**  `interactive`

**CLI:**  `-m` or `--mode`

**ENV:**  `ANSIBLE_NAVIGATOR_MODE`

**Settings file:**

```
ansible-navigator:
mode:
``` |
| osc4 | Enable or disable terminal color changing support with OSC 4. |  **Choices:**  `True` or `False`

**Default:**  `True`

**CLI:**  `--osc4` or `--osc4`

**ENV:**  `ANSIBLE_NAVIGATOR_OSC4`

**Settings file:**

```
ansible-navigator:
color:
osc4:
``` |
| pass-environment-variable | Specify an exiting environment variable to be passed through to and set within the automation execution environment ( `--penv MY_VAR` ) |  **Default:** No default value set

**CLI:**  `--penv` or `--pass-environment-variable`

**ENV:**  `ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES`

**Settings file:**

```
ansible-navigator:
execution-environment:
environment-variables:
pass:
``` |
| pull-policy | Specify the image pull policy.

`always` - Always pull the image

`missing` - Pull if not locally available

`never` - Never pull the image

`tag` - If the image tag is `latest` always pull the image, otherwise pull if not locally available |  **Choices:**  `always` , `missing` , `never` , or `tag`

**Default:**  `tag`

**CLI:**  `--pp` or `--pull-policy`

**ENV:**  `ANSIBLE_NAVIGATOR_PULL_POLICY`

**Settings file:**

```
ansible-navigator:
execution-environment:
pull-policy:
``` |
| set-environment-variable | Specify an environment variable and a value to be set within the automation execution environment `(--senv MY_VAR=42` ) |  **Default:** No default value set

**CLI:**  `--senv` or `--set-environment-variable`

**ENV:**  `ANSIBLE_NAVIGATOR_SET_ENVIRONMENT_VARIABLES`

**Settings file:**

```
ansible-navigator:
execution-environment:
environment-variables:
set:
``` |




## 8.3. Automation content navigator `config` subcommand settings




The following table describes each parameter and setting options for the automation content navigator `config` subcommand.


<span id="idm140640040295472"></span>
**Table 8.2. Automation content navigator `config` subcommand parameters settings**

| Parameter | Description | Setting options |
| --- | --- | --- |
| config | Specify the path to the Ansible configuration file. |  **Default:** No default value set

**CLI:**  `-c` or `--config`

**ENV:**  `ANSIBLE_CONFIG`

**Settings file:**

```
ansible-navigator:
ansible:
config:
path:
``` |
| help-config | Help options for the `ansible-config` command in `stdout` mode. |  **Choices:** * `True` or `False`

**Default:**  `False`

**CLI:**  `--hc` or `--help-config`

**ENV:**  `ANSIBLE_NAVIGATOR_HELP_CONFIG`

**Settings file:**

```
ansible-navigator:
help-config:
``` |




## 8.4. automation content navigator `doc` subcommand settings




The following table describes each parameter and setting options for the automation content navigator `doc` subcommand.


<span id="idm140640038325504"></span>
**Table 8.3. automation content navigator `doc` subcommand parameters settings**

| Parameter | Description | Setting options |
| --- | --- | --- |
| help-doc | Help options for the `ansible-doc` command in `stdout` mode. |  **Choices:**  `True` or `False`

**Default:**  `False`

**CLI:**  `--hd` or `--help-doc`

**ENV:**  `ANSIBLE_NAVIGATOR_HELP_DOC`

**Settings file:**

```
ansible-navigator:
help-doc:
``` |
| plugin-name | Specify the plugin name. |  **Default:** No default value set

**CLI:** positional

**ENV:**  `ANSIBLE_NAVIGATOR_PLUGIN_NAME`

**Settings file:**

```
ansible-navigator:
documentation:
plugin:
name:
``` |
| plugin-type | Specify the plugin type. |  **Choices:**  `become` , `cache` , `callback` , `cliconf` , `connection` , `httpapi` , `inventory` , `lookup` , `module` , `netconf` , `shell` , `strategy` , or `vars`

**Default:**  `module`

**CLI:**  `-t` or `----type`

**ENV:**  `ANSIBLE_NAVIGATOR_PLUGIN_TYPE`

**Settings file:**

```
ansible-navigator:
documentation:
plugin:
type:
``` |




## 8.5. Automation content navigator `inventory` subcommand settings




The following table describes each parameter and setting options for the automation content navigator `inventory` subcommand.


<span id="idm140640041092176"></span>
**Table 8.4. Automation content navigator `inventory` subcommand parameters settings**

| Parameter | Description | Setting options |
| --- | --- | --- |
| help-inventory | Help options for the `ansible-inventory` command in `stdout` mode. |  **Choices:**  `True` or `False`

**Default:**  `False`

**CLI:**  `--hi` or `--help-inventory`

**ENV:**  `ANSIBLE_NAVIGATOR_INVENTORY_DOC`

**Settings file:**

```
ansible-navigator:
help-inventory:
``` |
| inventory | Specify an inventory file path or comma separated host list. |  **Default:** no default value set

**CLI:**  `--i` or `--inventory`

**ENV:**  `ANSIBLE_NAVIGATOR_INVENTORIES`

**Settings file:**

```
ansible-navigator:
inventories:
``` |
| inventory-column | Specify a host attribute to show in the inventory view. |  **Default:** No default value set

**CLI:**  `--ic` or `--inventory-column`

**ENV:** * `ANSIBLE_NAVIGATOR_INVENTORY_COLUMNS`  **Settings file:**

```
ansible-navigator:
inventory-columns:
``` |




## 8.6. Automation content navigator `replay` subcommand settings




The following table describes each parameter and setting options for the automation content navigator `replay` subcommand.


<span id="idm140640041980464"></span>
**Table 8.5. Automation content navigator `replay` subcommand parameters settings**

| Parameter | Description | Setting options |
| --- | --- | --- |
| playbook-artifact-replay | Specify the path for the playbook artifact to replay. |  **Default:** No default value set

**CLI:** positional

**ENV:**  `ANSIBLE_NAVIGATOR_PLAYBOOK_ARTIFACT_REPLAY`

**Settings file:**

```
ansible-navigator:
playbook-artifact:
replay:
``` |




## 8.7. Automation content navigator `run` subcommand settings




The following table describes each parameter and setting options for the automation content navigator `run` subcommand.


<span id="idm140640038777744"></span>
**Table 8.6. Automation content navigator `run` subcommand parameters settings**

| Parameter | Description | Setting options |
| --- | --- | --- |
| playbook-artifact-replay | Specify the path for the playbook artifact to replay. |  **Default:** No default value set

**CLI:** positional

**ENV:**  `ANSIBLE_NAVIGATOR_PLAYBOOK_ARTIFACT_REPLAY`

**Settings file:**

```
ansible-navigator:
playbook-artifact:
replay:
``` |
| help-playbook | Help options for the `ansible-playbook` command in `stdout` mode. |  **Choices:**  `True` or `False`

**Default:**  `False`

**CLI:**  `--hp` or `--help-playbook`

**ENV:**  `ANSIBLE_NAVIGATOR_HELP_PLAYBOOK`

**Settings file:**

```
ansible-navigator:
help-playbook:
``` |
| inventory | Specify an inventory file path or comma separated host list. |  **Default:** no default value set

**CLI:**  `--i` or `--inventory`

**ENV:**  `ANSIBLE_NAVIGATOR_INVENTORIES`

**Settings file:**

```
ansible-navigator:
inventories:
``` |
| inventory-column | Specify a host attribute to show in the inventory view. |  **Default:** No default value set

**CLI:**  `--ic` or `--inventory-column`

**ENV:** * `ANSIBLE_NAVIGATOR_INVENTORY_COLUMNS`  **Settings file:**

```
ansible-navigator:
inventory-columns:
``` |
| playbook | Specify the playbook name. |  **Default:** No default value set

**CLI:** positional

**ENV:**  `ANSIBLE_NAVIGATOR_PLAYBOOK`

**Settings file:** *

```
ansible-navigator:
ansible:
playbook:
``` |
| playbook-artifact-enable | Enable or disable the creation of artifacts for completed playbooks. Note: not compatible with `--mode stdout` when playbooks require user input. |  **Choices:**  `True` or `False`

**Default:**  `True`

**CLI:**  `--pae` or `--playbook-artifact-enable`  **ENV:**  `ANSIBLE_NAVIGATOR_PLAYBOOK_ARTIFACT_ENABLE`  **Settings file:**

```
ansible-navigator:
playbook-artifact:
enable:
``` |
| playbook-artifact-save-as | Specify the name for artifacts created from completed playbooks. |  **Default:**  `{playbook_dir}/{playbook_name}-artifact-{ts_utc}.json`

**CLI:**  `--pas` or `--playbook-artifact-save-as`

**ENV:**  `ANSIBLE_NAVIGATOR_PLAYBOOK_ARTIFACT_SAVE_AS`

**Settings file:**

```
ansible-navigator:
playbook-artifact:
save-as:
``` |




# Chapter 9. Troubleshooting Ansible content with automation content navigator




As a content creator, you can troubleshoot your Ansible content (collections, automation execution environments, and playbooks) with automation content navigator and interactively troubleshoot the playbook. You can also compare results inside or outside an automation execution environment and troubleshoot any problems.

## 9.1. Reviewing playbook results with an automation content navigator artifact file




Automation content navigator saves the results of the playbook run in a JSON artifact file. You can use this file to share the playbook results with someone else, save it for security or compliance reasons, or review and troubleshoot later. You only need the artifact file to review the playbook run. You do not need access to the playbook itself or inventory access.

**Prerequisites**

- A automation content navigator artifact JSON file from a playbook run.


**Procedure**

- Start automation content navigator with the artifact file.


```
$ ansible-navigator replay simple_playbook_artifact.json
```


1. Review the playbook results that match when the playbook ran.

![Playbook results](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/4f50de6511503aed4d7729dafafad134/navigator-artifact-replay.png)






You can now type the number next to the plays and tasks to step into each to review the results, as you would after executing the playbook.

**Additional resources**

-  [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html)
-  [Ansible playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html)


## 9.2. Frequently asked questions about automation content navigator




Use the following automation content navigator FAQ to help you troubleshoot problems in your environment.


<span id="idm140640046669104"></span>
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





