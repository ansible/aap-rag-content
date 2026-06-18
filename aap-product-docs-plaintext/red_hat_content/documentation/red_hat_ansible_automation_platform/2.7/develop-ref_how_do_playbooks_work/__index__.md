# How do Ansible Playbooks work

Ansible Playbooks are lists of tasks that run automatically for your specified inventory or groups of hosts. One or more Ansible tasks can be combined to make a play, that is, an ordered grouping of tasks mapped to specific hosts.

Tasks are executed in the order in which they are written.

A playbook can include one or more plays.

A playbook is composed of one or more `plays` in an ordered list.

The terms `playbook` and `play` are sports analogies.

Each play executes part of the overall goal of the playbook, running one or more tasks.

Each task calls an Ansible module.

Playbook
A list of plays that define the order in which Ansible performs operations, from top to bottom, to achieve an overall goal.

Play
An ordered list of tasks that maps to managed nodes in an inventory.

Task
A reference to a single module that defines the operations that Ansible performs.

Roles
Roles are a way to make code in playbooks reusable by putting the functionality into "libraries" that can then be used in any playbook as needed.

Module
A unit of code or binary that Ansible runs on managed nodes.

Ansible modules are grouped in collections with a *Fully Qualified Collection Name* (FQCN) for each module. Tasks are executed by modules, each of which performs a specific task in a playbook. A module contains metadata that determines when and where a task is executed, and which user executes it. There are thousands of Ansible modules that perform all kinds of IT tasks, such as:

- Cloud management
- User management
- Networking
- Security
- Configuration management
- Communication


![Structure of a typical playbook](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/playbook.png)

## How do I use Ansible Playbooks

Ansible Playbooks are files containing a series of instructions that define the required state of a system or application. They are written in YAML, a human-readable data serialization format, and used to automate IT tasks such as configuration management, application deployment, and orchestration.

You can use YAML to create playbooks without having to learn a complicated coding language.

There are two ways of using Ansible Playbooks:

- From the *command line interface* (CLI)
- Using Red Hat Ansible Automation Platform’s push-button deployments.

### From the CLI

After installing the open source Ansible project or Red Hat Ansible Automation Platform by using

```
$ sudo dnf install ansible
```
in the Red Hat Enterprise Linux CLI, you can use the `ansible-playbook` command to run Ansible Playbooks.

### From within the platform

The Red Hat Ansible Automation Platform user interface offers push-button Ansible Playbook deployments that can be used as part of larger jobs or job templates. These deployments come with additional safeguards that are particularly helpful to users who are newer to IT automation, or those without as much experience working in the CLI.

## Start automating with Ansible

Get started with Ansible by creating an automation project, building an inventory, and creating a `Hello World` playbook.

### Before you begin

- The Ansible package must be installed.
- A text editor must be available to create and edit files.

### Procedure

Create a project folder on your filesystem.

```
mkdir ansible_quickstart
cd ansible_quickstart
```
Using a single directory structure makes it easier to add to source control, and reuse and share automation content.
