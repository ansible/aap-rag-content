+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-event_persistence_in_rulebook_activations"
template = "docs/aem-title.html"
title = "Event persistence in rulebook activations - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-plan_infrastructure_requirements_for_event_persistence_in_rulebook_activations/", "Plan infrastructure requirements for event persistence"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-event_persistence_in_rulebook_activations/aem-page/plan-event_persistence_in_rulebook_activations.html"
last_crumb = "Event persistence in rulebook activations"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Event persistence in rulebook activations"
oversized = "false"
page_slug = "plan-event_persistence_in_rulebook_activations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-event_persistence_in_rulebook_activations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-event_persistence_in_rulebook_activations/toc/toc.json"
type = "aem-page"
+++

# Event persistence in rulebook activations

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
