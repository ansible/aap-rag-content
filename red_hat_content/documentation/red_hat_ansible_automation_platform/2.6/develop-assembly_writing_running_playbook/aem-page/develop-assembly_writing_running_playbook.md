+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_writing_running_playbook"
template = "docs/aem-title.html"
title = "Write your first automation task using the VS Code extension - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_devtools_intro/", "Create, test, and deploy automation content with ansible-dev-tools"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_writing_running_playbook/aem-page/develop-assembly_writing_running_playbook.html"
last_crumb = "Write your first automation task using the VS Code extension"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Write your first automation task using the VS Code extension"
oversized = "false"
page_slug = "develop-assembly_writing_running_playbook"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_writing_running_playbook"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_writing_running_playbook/toc/toc.json"
type = "aem-page"
+++

# Write your first automation task using the VS Code extension

Learn how to write, inspect, debug, and run Ansible playbooks directly within VS Code using Ansible development tools.

## Set up the Ansible configuration file

When you scaffolded your playbook project, an Ansible configuration file, `ansible.cfg`, was added to the root directory of your project.

### Procedure

 If you have configured a default Ansible configuration file in `/etc/ansible/ansible.cfg`, copy any settings that you want to reuse in your project from your default Ansible configuration file to the `ansible.cfg` file in your project’s root directory.

To learn more about the Ansible configuration file, see [Reviewing your Ansible configuration with automation content navigator](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_execute_playbook_navigator#assembly-review-config-navigator "As a content creator, you can review your Ansible configuration with automation content navigator and interactively delve into settings.").

## Write your first playbook

Create your first Ansible playbook within VS Code using the Ansible extension. The tools available help ensure that your syntax is correct and ready to run.

### Before you begin

- You have installed and opened the Ansible VS Code extension.
- You have opened a terminal in VS Code.
- You have installed `ansible-devtools`.

### Procedure

1.  Create a new .yml file in VS Code for your playbook, for example `example_playbook.yml`. Put it in the same directory level as the example `site.yml` file.
2.  Add the following example code into the playbook file and save the file. The playbook consists of a single play that executes a `ping` to your local machine.

```
---
- name: My first play
  hosts: localhost
  tasks:
    - name: Ping my hosts
      ansible.builtin.ping:
```
    `Ansible-lint` runs in the background and displays errors in the **Problems** tab of the terminal. There are no errors in this playbook:


![Ansible-lint showing no errors in a playbook](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ansible-lint-no-errors.png)  

3.  If you want to add new content to the playbook, use the following rules:

  - Every playbook file must finish with a blank line.
  - Trailing spaces at the end of lines are not allowed.
  - Every playbook and every play require an identifier (name).

4.  Save your playbook file.

## Inspect your playbook

The Ansible VS Code extension provides inline help, syntax highlighting, and assists you with indentation in `.yml` files.

### Procedure

1.  Open a playbook in VS Code.
2.  Hover your mouse over a keyword or a module name: the Ansible extension provides documentation:  
![Ansible-lint showing no errors in a playbook](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ansible-lint-keyword-help.png)  
3.  If you begin to type the name of a module, for example `ansible.builtin.ping`, the extension provides a list of suggestions. Select one of the suggestions to autocomplete the line.


![Ansible-lint showing no errors in a playbook](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ansible-lint-module-completion.png)  

## Debug your playbook

Learn how to use VS Code to identify and understand error messages in playbooks.

### Procedure

1.  The following playbook contains multiple errors. Copy and paste it into a new file in VS Code.

```
- name:
  hosts: localhost
  tasks:
   - name:
     ansible.builtin.ping:
```
    The errors are indicated with a wavy underline in VS Code.

2.  Hover your mouse over an error to view the details:  
![Popup message explaining a playbook error](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ansible-lint-errors.png)  
3.  Playbook files that contain errors are indicated with a number in the **Explorer** pane.
4.  Select the **Problems** tab of the VS Code terminal to view a list of the errors.  
![Playbook errors shown in Problems tab and explorer list](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ansible-lint-errors-explorer.png)  
      `$[0].tasks[0].name None is not of type 'string'` indicates that the playbook does not have a label.
