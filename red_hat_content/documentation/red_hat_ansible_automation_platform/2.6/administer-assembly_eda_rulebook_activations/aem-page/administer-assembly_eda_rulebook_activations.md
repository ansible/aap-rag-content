+++
template = "docs/aem-title.html"
title = "Define rules that trigger automation from events - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_rulebook_activations"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_user_guide_overview/", "Trigger automation from events with Event-Driven Ansible"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_rulebook_activations/aem-page/administer-assembly_eda_rulebook_activations.html"
last_crumb = "Define rules that trigger automation from events"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Define rules that trigger automation from events"
oversized = "false"
page_slug = "administer-assembly_eda_rulebook_activations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_rulebook_activations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_rulebook_activations/toc/toc.json"
type = "aem-page"
+++

# Define rules that trigger automation from events

A rulebook is a set of conditional rules that Event-Driven Ansible uses to perform IT actions in an event-driven automation model. Rulebooks are the means that users tell Event-Driven Ansible which source to check for an event and when that event occurs what to do when certain conditions are met.

A rulebook specifies actions to be performed when a rule is triggered. A rule gets triggered when the events match the conditions for the rules. The following actions are currently supported:

- `run_playbook` (only supported with ansible-rulebook CLI)
-  `run_module`
-  `run_job_template`
-  `run_workflow_template`
-  `set_fact`
-  `post_event`
-  `retract_fact`
-  `print_event`
-  `shutdown`
-  `debug`
-  `none`


To view further details, see Ansible Actions.

A rulebook activation is a process running in the background defined by a decision environment executing a specific rulebook. You can set up your rulebook activation by following Set up a rulebook activation.

Warning:

Red Hat does not recommend the use of a non-supported source plugin with 1 postgres database. This can pose a potential risk to your use of Ansible Automation Platform.

Important:

To meet high availability demands, Event-Driven Ansible controller shares centralized Redis (REmote DIctionary Server) with the Ansible Automation Platform UI. When Redis is unavailable, the following functions will not be available:

- Creating an activation, if `is_enabled` is True
- Deleting an activation
- Enabling an activation, if not already enabled
- Disabling an activation, if not already disabled
- Restarting an activation

## Set up a rulebook activation

Create a rulebook activation to link a rulebook to a decision environment and event sources, initiating the event-driven automation process.

### Before you begin

- You are logged in to the Ansible Automation Platform Dashboard as a Content Consumer.
- You have set up a project.
- You have set up a decision environment.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  Navigate to the Automation Decisions> (and then)Rulebook Activations.
3.  Click Create rulebook activation.
4.  Insert the following:
  

Name
Insert the name.

Description
This field is optional.

Organization
Enter your organization name or select Default from the list.

Project
Projects are a logical collection of rulebooks. This field is optional.

Rulebook
Rulebooks are displayed according to the project selected.

Credential
Select 0 or more credentials for this rulebook activation. This field is optional.

  Note:

  - The credentials that display in this field are customized based on your rulebook activation and only include the following credential types: Vault, Red Hat Ansible Automation Platform, or any custom credential types that you have created. For more information about credentials, see [Credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials "You can use credentials to store secrets that can be used for authentication purposes with resources, such as decision environments, rulebook activations and projects for Event-Driven Ansible controller, and projects for automation controller.").
  - If you plan to use a Red Hat Ansible Automation Platform credential, you can *only* select 1 Red Hat Ansible Automation Platform credential type for a rulebook activation.

Decision environment
Decision environments are a container image to run Ansible rulebooks.

Restart policy
This is the policy that determines how an activation should restart after the container process running the source plugin ends.

  - Policies:
    1. **Always**: This restarts the rulebook activation immediately, regardless of whether it ends successfully or not, and occurs no more than 5 times.
    2. **Never**: This never restarts a rulebook activation when the container process ends.
    3. **On failure**: This restarts the rulebook activation after 60 seconds by default, only when the container process fails, and occurs no more than 5 times.

Log level
This field defines the severity and type of content in your logged events.

  - Levels:
    1. **Error**: Logs that contain error messages that are displayed in the **History** tab of an activation.
    2. **Info**: Logs that contain useful information about rulebook activations, such as a success or failure, triggered action names and their related action events, and errors.
    3. **Debug**: Logs that contain information that is only useful during the debug phase and might be of little value during production. This log level includes both error and log level data.

Service name
This defines a service name for Kubernetes to configure inbound connections if the activation exposes a port. This field is optional.

Rulebook activation enabled?
This automatically enables the rulebook activation to run.

Variables
The variables for the rulebook are in a JSON or YAML format. The content would be equivalent to the file passed through the `--vars` flag of ansible-rulebook command.

  Note:
      In the context of automation controller and Event-Driven Ansible controller, you can use both `extra_vars` and credentials to store a variety of information. However, credentials are the preferred method of storing sensitive information such as passwords or API keys because they offer better security and centralized management, whereas `extra_vars` are more suitable for passing dynamic, non-sensitive data.

Options
Check the **Skip audit events** option if you do not want to see your events in the Rule Audit.

5.  Click Create rulebook activation.

### Results

Your rulebook activation is now created and can be managed on the **Rulebook Activations** page.

After saving the new rulebook activation, the rulebook activation’s details page is displayed, with either a **Pending**, **Running**, or **Failed** status. From there or the **Rulebook Activations** list view, you can restart or delete it.

Note:

Occasionally, when a source plugin shuts down, it causes a rulebook to exit gracefully after a certain amount of time. When a rulebook activation shuts down, any tasks that are waiting to be performed will be canceled, and an info level message is sent to the activation log. For more information, see [Rulebooks](https://docs.ansible.com/projects/rulebook/en/latest/rulebooks.html#).

### What to do next

For all activations that have run, you can view the Details and History tabs to get more information about what happened.

## Rulebook activation list view

Use the **Rulebook Activations** list view to quickly monitor the operational status, event fire count, and restart frequency of all your deployed automation services.

If the **Status** is **Running**, it means that the rulebook activation is running in the background and executing the required actions according to the rules declared in the rulebook.

You can view more details by selecting the activation from the **Rulebook Activations** list view.

For all activations that have run, you can view the **Details** and **History** tabs to get more information about what happened.

### View activation output

View the activation output in the History tab to inspect the execution results, confirm successful automation runs, and diagnose runtime errors or task failures.

#### Procedure

1.  Select the **History** tab to access the list of all the activation instances. An activation instance represents a single execution of the activation.
2.  Then select the activation instance you want to view. The **Output** for the activation instance is displayed.

#### What to do next

To view events that came in and triggered an action, navigate to Automation Decisions> (and then)Rule Audit and follow instructions in the [Rule Audit](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-rule-audit) section.

### Auto-restart on project update for rulebook activations

When a project synchronizes and the rulebook content has changed in the source repository, you can configure the system to automatically restart the affected rulebook activation. This ensures that running activations always use the most current rulebook logic without manual intervention.

Without auto-restart, a project synchronization updates the rulebook files on disk but any currently running activations continue to use the previously loaded rulebook logic. This can lead to a mismatch between the rulebook definitions in your source repository and the logic that is actively processing events. Auto-restart eliminates this drift by ensuring that activations are automatically restarted with the updated rulebook content after a project sync.

The behavior of an auto-restart is determined by the combined state of the Update revision on launch setting in the project and the Auto-restart on project update setting in the activation. Because these features are interdependent, changing a project setting may trigger confirmation prompts to ensure you understand the impact on all associated rulebook activations. For more information on the interdependencies, see Project and rulebook activation settings interdependencies.

### Event persistence in rulebook activations

Event persistence stores incoming data from event sources in a dedicated database. After event persistence is enabled for an activation, the system retains matched events until the rule triggers, ensuring no data is lost before an action occurs.

Event persistence ensures continuity by retaining events during rulebook activation restarts. This feature requires a dedicated PostgreSQL database using one of the following options:

- **Built-in event persistence database** - Deployed automatically during Ansible Automation Platform installation, if selected. With this option, event persistence works out of the box with a default Event-Driven Ansible Rule Engine credential.
- **External database** - A PostgreSQL database instance you manage separately. This option requires creating a custom Rule Engine credential pointing to your external database. For more information on creating a custom Rule Engine, see the following **Related tasks**. For specific information on **persistence database requirements** (sizing, IOPs, and similar), refer to the deployment topology content in the following **Related concepts** and **Related reference**.


When event persistence is enabled for a rulebook activation:

1. Event-Driven Ansible receives events from the configured event source.
2. Each matched event is saved to the event persistence database.
3. Matched events are retained in the database until all conditions are met and an action is fired.
4. Processed events are then removed from the database.


Here are key factors to consider when choosing to enable event persistence:

- If your events contain sensitive information, you must create a custom Rule Engine credential with encryption keys to protect your event data. To create your own custom Event-Driven Ansible Rule engine credential, see the following related concept and tasks.
- The default Event-Driven Ansible Rule Engine credential does not support encryption of event data.
