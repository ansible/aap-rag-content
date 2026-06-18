# Ansible components

Ansible Automation Platform comprises integrated components that orchestrate the end-to-end automation process. This modular architecture allows teams to build, share, and scale secure workflows across the entire enterprise.

Ansible Automation Platform is structured around three main components:

- Automation execution: where you can deploy, define, operate, scale, and delegate automation across your enterprise.
- Automation content: the central location for your Ansible content, which you can integrate into your automation environment.
- Automation decisions: where you can manage Event-Driven Ansible, an automation engine that listens to your system's even stream and reacts to events that you have specified with targeted automation tasks.

These components are united by the platform gateway, which includes an activity stream that captures changes to platform gateway resources, including the creation or modification of organizations, users, and service clusters, among others.

## Automation execution

At the heart of Ansible Automation Platform is a centralized control center for deploying, scaling, and delegating enterprise automation. From one location, you can run playbooks via a web UI, monitor dashboard activity, and use centralized logging to track job execution.

In the automation execution environment, you can use automation controller tasks to build job templates, which standardize how automation is deployed, initiated, and delegated, making it more reusable and consistent.

### Inventories

An inventory is a single file, usually in INI or YAML format, containing a list of hosts and groups that can be acted upon using Ansible commands and playbooks. You can use an inventory file to specify your installation scenario and describe host deployments to Ansible. You can also use an inventory file to organize managed nodes in centralized files that give Ansible with system information and network locations.

### Policy enforcement

Policy enforcement at automation runtime is a feature that uses encoded rules to define, manage, and enforce policies that govern how your users interact with your Ansible Automation Platform instance. Policy enforcement automates policy management, improving security, compliance, and efficiency. Policy enforcement points can be configured at the level of the inventory, job template, or organization. For more, see **Implementing policy enforcement** .

## Automation content

Automation hub is the central location for your Ansible Automation Platform content. In automation hub you can also find content collections that you can download and integrate into your automation environment. You can also create and upload your own content to distribute to your users.

An Ansible Content Collection is a ready-to-use toolkit for automation and can include multiple types of content, including roles, modules, playbooks, and plugins all in one place.

You can access automation hub in one of two ways:

- On the Red Hat-hosted Hybrid Cloud Console, where you can find Red Hat validated or certified content that you can sync to your platform environment.
- On a self-hosted, on-premise private automation hub, where you can curate content for your automation users and manage access to collections and execution environments.


Depending on the way you access automation hub, you may have access to different types of content collections.

There are two types of Red Hat Ansible content:

- Ansible Certified Content Collections, which Red Hat builds, supports, and maintains. Certified collections are included in your subscription to Red Hat Ansible Automation Platform and can be found in automation hub.
- Ansible validated content collections, which are customizable and therefore do not have a support guarantee, but have been tested in the Ansible Automation Platform environment.


### Ansible roles

Ansible roles allow you to create reusable automation content that helps teams to work more efficiently and avoid duplicating efforts. With roles, you can group together a broader range of existing automation content, like playbooks, configuration files, templates, tasks, and handlers to create customized automation content that can be reused and shared with others.

You can also make roles configurable by exposing variables that users can set when calling the role, allowing them to configure their system according to their organization’s requirements.

Roles are generally included in Ansible content collections.

### Ansible playbooks

Playbooks are YAML files that contain specific sets of human-readable instructions, or “plays,” that you send to run on a single target or groups of targets. Ansible playbooks are repeatable and reusable configuration management tools designed to deploy complex applications.

You can use playbooks to manage configurations of and deployments to remote machines to sequence multitiered rollouts involving rolling updates. Use playbooks to delegate actions to other hosts, interacting with monitoring servers and load balancers along the way.

Once written, you can use and re-use playbooks for automation across your enterprise. For example, if you need to run a task more than once, write a playbook and put it under source control. Then, you can use the playbook to push out new configuration or confirm the configuration of remote systems.

Ansible playbooks can declare configurations, orchestrate steps of any manually ordered process on many machines in a defined order, or start tasks synchronously or asynchronously.

You can also use Red Hat Ansible Lightspeed, Ansible’s generative AI service, to create and develop playbooks to fit your needs.

## Automation decisions

Red Hat Ansible Automation Platform includes Event-Driven Ansible, an automation engine that listens to your system’s event stream and reacts to events that you have specified with targeted automation tasks.

Managed through Event-Driven Ansible controller, Ansible rulebooks are the framework for automation decisions. Ansible rulebooks are collections of rulesets, which in turn consist of one or more sources, rules, and conditions. Rulebooks tell the system what events to flag and how to respond to them. From the Automation Decisions section of the platform user interface, you can use rulebooks to connect and listen to event sources, and define actions that are triggered in response to certain events.

## Automation mesh

Automation mesh is an overlay network intended to ease the distribution of automation across a collection of execution nodes using existing connectivity.

Execution nodes are where Ansible Playbooks are actually executed. A node runs an automation execution environment which, in turn, runs the Ansible Playbook.

Automation mesh creates peer-to-peer connections between these execution nodes, increasing the resiliency of your automation workloads to network latency and connection disruptions. This also permits more flexible architectures and provides rapid, independent scaling of control and execution capacity.

## Red Hat Ansible Lightspeed

Red Hat Ansible Lightspeed with IBM watsonx Code Assistant is a generative AI service for Ansible developers. It uses natural-language prompts and IBM watsonx models to provide best-practice code recommendations.

Red Hat Ansible Lightspeed with IBM watsonx Code Assistant helps automation teams learn, create, and maintain Red Hat Ansible Automation Platform content more efficiently.

## Product Notification Feed

As of July 2025, the Ansible Automation Platform RSS notification feed is available. This feed serves as a method for communicating various product updates and changes to customers.

Customers can subscribe to the notifications by visiting Ansible Automation Platform Product Notifications through an RSS feed reader. This feed is updated with events such as Ansible Automation Platform upgrades and system maintenance.

All Ansible Automation Platform customers can subscribe to this content. Messages include categorization tags to specify deployment types: managed, self-managed (on-premise), or a combination. Red Hat is developing a future enhancement to integrate this feature directly into the UI.

## Ansible development tools

Ansible development tools are an integrated and supported suite of capabilities that help IT practitioners at any skill level generate automation content faster than they might with manual coding.

Ansible development tools can help you create, test, and deploy automation content like playbooks, execution environments, and collections quickly and accurately using recommended practices.

## Ansible Automation Platform installation and configuration

Choose the appropriate installation methods to match your infrastructure and organizational requirements.

Depending on your organization’s needs, you can install Red Hat Ansible Automation Platform using one of the following methods, based on your environment:

-  [RPM installation](/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_platform_install_overview "The Red Hat Ansible Automation Platform installation program offers you flexibility, allowing you to install Ansible Automation Platform by using several supported installation scenarios.")
-  [Installing on OpenShift Container Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.")
-  [Cloud environments](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x)
-  [Containerized installation](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro "Containerized Ansible Automation Platform uses Podman to run the platform in containers on Red Hat Enterprise Linux host machines. With this installation method, you manage both the product and infrastructure lifecycle while taking advantage of containerized architecture.")

## Dashboard components

After you install Ansible Automation Platform on your system and log in for the first time, familiarize yourself with the platform dashboard.

Quick starts
Learn about Ansible automation functions with guided tutorials called quick starts. In the dashboard, you can access quick starts by selecting **Quick starts** from the navigation panel, and selecting a quick start tile. Click Start and complete the onscreen instructions. You can also filter quick starts by keyword and status.

Resource status
Indicates the status of your hosts, projects, and inventories. The status indicator links to your configured hosts, projects and inventories where you can search, filter, add and change these resources.

Job Activity
View a summary of your current job status. Filter the job status within a period of time or by job type, or click Go to jobs to view a complete list of jobs that are currently available.

Jobs
View recent jobs that have run, or click View all Jobs to view a complete list of jobs that are currently available, or create a new job.

Projects
View recently updated projects or click View all Projects to view a complete list of the projects that are currently available, or create a new project.

Inventories
View recently updated inventories or click View all Inventories to view a complete list of available inventories, or create a new inventory.

Rulebook Activations
View the list of recent rulebook activations and their status, display the complete list of rulebook activations that are currently available, or create a new rulebook activation.

Rule Audit
View recently fired rule audits, view rule audit records, and view rule audit data based on corresponding rulebook activation runs.

Decision Environments
View recently updated decision environments, or click View all Decision Environments to see a complete list of available inventories, or create a new decision environment.
