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

| Command         | Description                                          | CLI example                                 |
| --------------- | ---------------------------------------------------- | ------------------------------------------- |
| <br>collections | <br>Explore available collections                    | <br> `ansible-navigator collections --help` |
| <br>config      | <br>Explore the current Ansible configuration        | <br> `ansible-navigator config --help`      |
| <br>doc         | <br>Review documentation for a module or plugin      | <br> `ansible-navigator doc --help`         |
| <br>images      | <br>Explore execution environment images             | <br> `ansible-navigator images --help`      |
| <br>inventory   | <br>Explore an inventory                             | <br> `ansible-navigator inventory --help`   |
| <br>replay      | <br>Explore a previous run using a playbook artifact | <br> `ansible-navigator replay --help`      |
| <br>run         | <br>Run a playbook                                   | <br> `ansible-navigator run --help`         |
| <br>welcome     | <br>Start at the welcome page                        | <br> `ansible-navigator welcome --help`     |

### Relationship between Ansible and automation content navigator commands

The automation content navigator commands run familiar Ansible CLI commands in `-m stdout` mode. You can use all the subcommands and options available in the related Ansible CLI command. Use `ansible-navigator --help` for details.

**Comparison of automation content navigator and Ansible CLI commands**

| automation content navigator command | Ansible CLI command              |
| ------------------------------------ | -------------------------------- |
| <br> `ansible-navigator collections` | <br> `ansible-galaxy collection` |
| <br> `ansible-navigator config`      | <br> `ansible-config`            |
| <br> `ansible-navigator doc`         | <br> `ansible-doc`               |
| <br> `ansible-navigator inventory`   | <br> `ansible-inventory`         |
| <br> `ansible-navigator run`         | <br> `ansible-playbook`          |
