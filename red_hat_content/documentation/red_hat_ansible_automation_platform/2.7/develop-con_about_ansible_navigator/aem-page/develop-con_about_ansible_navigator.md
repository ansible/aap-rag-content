+++
template = "docs/aem-title.html"
title = "What is automation content navigator? - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_about_ansible_navigator"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_intro_navigator/", "Emulate a platform environment locally with automation content navigator"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-con_about_ansible_navigator/aem-page/develop-con_about_ansible_navigator.html"
last_crumb = "What is automation content navigator?"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "What is automation content navigator?"
oversized = "false"
page_slug = "develop-con_about_ansible_navigator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-con_about_ansible_navigator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-con_about_ansible_navigator/toc/toc.json"
type = "aem-page"
+++

# What is automation content navigator?

Automation content navigator is a command line, content-creator-focused tool with a text-based user interface. You can use automation content navigator to:

- Launch and watch jobs and playbooks.
- Share stored, completed playbook and job run artifacts in JSON format.
- Browse and introspect automation execution environments.
- Browse your file-based inventory.
- Render Ansible module documentation and extract examples you can use in your playbooks.
- View a detailed command output on the user interface.

## Automation content navigator modes

automation content navigator provides two operating modes to support your development needs: a command line interface for quick tasks and an interactive text-based interface for complex evaluation and troubleshooting.

stdout mode
Accepts most of the existing Ansible commands and extensions at the command line.

text-based user interface mode
Provides an interactive, text-based interface to the Ansible commands. Use this mode to evaluate content, run playbooks, and troubleshoot playbooks after they run using artifact files.

### stdout mode

Use the `-m stdout` subcommand with automation content navigator to use the familiar Ansible commands, such as `ansible-playbook` within automation execution environments or on your local development environment. You can use commands you are familiar with for quick tasks.

Automation content navigator also provides extensive help in this mode:

`--help`
Accessible from `ansible-navigator` command or from any subcommand, such as `ansible-navigator config --help`.

subcommand help
Accessible from the subcommand, for example `ansible-navigator config --help-config`. This help displays the details of all the parameters supported from the related Ansible command.

### Text-based user interface mode

The text-based user interface mode provides enhanced interaction with automation execution environments, collections, playbooks, and inventory. This mode is compatible with integrated development environments (IDE), such as Visual Studio Code.

![Text-based user interface mode](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-welcome.png)  

This mode includes a number of helpful user interface options:

colon commands
You can access all the automation content navigator commands with a colon, such as `:run` or `:collections`

navigating the text-based interface
The screen shows how to page up or down, scroll, escape to a prior screen or access `:help`.

output by line number
You can access any line number in the displayed output by preceding it with a colon, for example `:12`.

color-coded output
With colors enabled, automation content navigator displays items, such as deprecated modules, in red.

pagination and scrolling
You can page up or down, scroll, or escape by using the options displayed at the bottom of each automation content navigator screen.

You cannot switch between modes after automation content navigator is running.

This document uses the text-based user interface mode for most procedures.

### Automation content navigator modes

automation content navigator provides two operating modes to support your development needs: a command line interface for quick tasks and an interactive text-based interface for complex evaluation and troubleshooting.

stdout mode
Accepts most of the existing Ansible commands and extensions at the command line.

text-based user interface mode
Provides an interactive, text-based interface to the Ansible commands. Use this mode to evaluate content, run playbooks, and troubleshoot playbooks after they run using artifact files.

#### stdout mode

Use the `-m stdout` subcommand with automation content navigator to use the familiar Ansible commands, such as `ansible-playbook` within automation execution environments or on your local development environment. You can use commands you are familiar with for quick tasks.

Automation content navigator also provides extensive help in this mode:

`--help`
Accessible from `ansible-navigator` command or from any subcommand, such as `ansible-navigator config --help`.

subcommand help
Accessible from the subcommand, for example `ansible-navigator config --help-config`. This help displays the details of all the parameters supported from the related Ansible command.

#### Text-based user interface mode

The text-based user interface mode provides enhanced interaction with automation execution environments, collections, playbooks, and inventory. This mode is compatible with integrated development environments (IDE), such as Visual Studio Code.

![Text-based user interface mode](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-welcome.png)  

This mode includes a number of helpful user interface options:

colon commands
You can access all the automation content navigator commands with a colon, such as `:run` or `:collections`

navigating the text-based interface
The screen shows how to page up or down, scroll, escape to a prior screen or access `:help`.

output by line number
You can access any line number in the displayed output by preceding it with a colon, for example `:12`.

color-coded output
With colors enabled, automation content navigator displays items, such as deprecated modules, in red.

pagination and scrolling
You can page up or down, scroll, or escape by using the options displayed at the bottom of each automation content navigator screen.

You cannot switch between modes after automation content navigator is running.

This document uses the text-based user interface mode for most procedures.

### Automation content navigator modes

automation content navigator provides two operating modes to support your development needs: a command line interface for quick tasks and an interactive text-based interface for complex evaluation and troubleshooting.

stdout mode
Accepts most of the existing Ansible commands and extensions at the command line.

text-based user interface mode
Provides an interactive, text-based interface to the Ansible commands. Use this mode to evaluate content, run playbooks, and troubleshoot playbooks after they run using artifact files.

#### stdout mode

Use the `-m stdout` subcommand with automation content navigator to use the familiar Ansible commands, such as `ansible-playbook` within automation execution environments or on your local development environment. You can use commands you are familiar with for quick tasks.

Automation content navigator also provides extensive help in this mode:

`--help`
Accessible from `ansible-navigator` command or from any subcommand, such as `ansible-navigator config --help`.

subcommand help
Accessible from the subcommand, for example `ansible-navigator config --help-config`. This help displays the details of all the parameters supported from the related Ansible command.

#### Text-based user interface mode

The text-based user interface mode provides enhanced interaction with automation execution environments, collections, playbooks, and inventory. This mode is compatible with integrated development environments (IDE), such as Visual Studio Code.

![Text-based user interface mode](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-welcome.png)  

This mode includes a number of helpful user interface options:

colon commands
You can access all the automation content navigator commands with a colon, such as `:run` or `:collections`

navigating the text-based interface
The screen shows how to page up or down, scroll, escape to a prior screen or access `:help`.

output by line number
You can access any line number in the displayed output by preceding it with a colon, for example `:12`.

color-coded output
With colors enabled, automation content navigator displays items, such as deprecated modules, in red.

pagination and scrolling
You can page up or down, scroll, or escape by using the options displayed at the bottom of each automation content navigator screen.

You cannot switch between modes after automation content navigator is running.

This document uses the text-based user interface mode for most procedures.

### Automation content navigator commands

The automation content navigator commands run familiar Ansible CLI commands in `-m stdout` mode. You can use all the subcommands and options from the related Ansible CLI command. Use `ansible-navigator --help` for details.

**Automation content navigator commands**

| Command     | Description                                      | CLI example                            |
| ----------- | ------------------------------------------------ | -------------------------------------- |
| collections | Explore available collections                    | `ansible-navigator collections --help` |
| config      | Explore the current Ansible configuration        | `ansible-navigator config --help`      |
| doc         | Review documentation for a module or plugin      | `ansible-navigator doc --help`         |
| images      | Explore execution environment images             | `ansible-navigator images --help`      |
| inventory   | Explore an inventory                             | `ansible-navigator inventory --help`   |
| replay      | Explore a previous run using a playbook artifact | `ansible-navigator replay --help`      |
| run         | Run a playbook                                   | `ansible-navigator run --help`         |
| welcome     | Start at the welcome page                        | `ansible-navigator welcome --help`     |

### Relationship between Ansible and automation content navigator commands

The automation content navigator commands run familiar Ansible CLI commands in `-m stdout` mode. You can use all the subcommands and options available in the related Ansible CLI command. Use `ansible-navigator --help` for details.

**Comparison of automation content navigator and Ansible CLI commands**

| automation content navigator command | Ansible CLI command         |
| ------------------------------------ | --------------------------- |
| `ansible-navigator collections`      | `ansible-galaxy collection` |
| `ansible-navigator config`           | `ansible-config`            |
| `ansible-navigator doc`              | `ansible-doc`               |
| `ansible-navigator inventory`        | `ansible-inventory`         |
| `ansible-navigator run`              | `ansible-playbook`          |
