# Get started automating with playbooks

An Ansible Playbook is a blueprint for automation tasks, which are actions executed with limited manual effort across an inventory of solutions. Playbooks tell Ansible what to do on which devices.

A playbook automatically executes the same action across a specified inventory type, such as a set of routers, replacing manual repetitive work.

Playbooks are regularly used to automate IT infrastructure, such as operating systems, Kubernetes platforms, networks, security systems, and code repositories such as GitHub.

You can use playbooks to program applications, services, server nodes, and other devices, without the effort of creating everything from scratch. Playbooks, and the conditions, variables, and tasks within them, can be saved, shared, or reused indefinitely. This makes it easier for you to codify operational knowledge and ensure that the same actions are performed consistently.

## How do Ansible Playbooks work

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
