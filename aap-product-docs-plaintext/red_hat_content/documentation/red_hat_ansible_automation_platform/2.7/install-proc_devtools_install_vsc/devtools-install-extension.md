# Install and configure VS Code
## Install the VS Code Ansible extension

The Ansible extension adds language support for Ansible to VS Code. It incorporates Ansible development tools to facilitate creating and running automation content.

### About this task

For a full description of the Ansible extension, see the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.ansible).

### Procedure

1.  Open VS Code.
2.  Click the **Extensions** (![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/vscode-extensions-icon.png)) icon in the Activity Bar, or click View> (and then)Extensions, to display the **Extensions** view.
3.  In the search field in the **Extensions** view, type `Ansible Red Hat`.
4.  Select the Ansible extension and click Install.

### Results

When the language for a file is recognized as Ansible, the Ansible extension provides features such as auto-completion, hover, diagnostics, and goto. The language identified for a file is displayed in the Status bar at the bottom of the VS Code window.

The following files are assigned the Ansible language:

- YAML files in a `/playbooks` directory
- Files with the following double extension: `.ansible.yml` or `.ansible.yaml`
- Certain YAML names recognized by Ansible, for example `site.yml` or `site.yaml`
- YAML files whose filename contains "playbook": `playbook.yml` or `playbook.yaml`

If the extension does not identify the language for your playbook files as Ansible, follow the procedure in [Associating the Ansible language to YAML files](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_devtools_install "You have two options for installing Ansible development tools, so that you can choose the installation method that best suits your preferred operating system and development environment.").

