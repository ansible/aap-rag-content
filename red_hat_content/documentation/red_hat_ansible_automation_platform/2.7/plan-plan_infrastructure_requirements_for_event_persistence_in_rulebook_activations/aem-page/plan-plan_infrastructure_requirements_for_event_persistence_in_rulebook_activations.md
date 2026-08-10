+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-plan_infrastructure_requirements_for_event_persistence_in_rulebook_activations"
template = "docs/aem-title.html"
title = "Plan infrastructure requirements for event persistence - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-plan_infrastructure_requirements_for_event_persistence_in_rulebook_activations/", "Plan infrastructure requirements for event persistence"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-plan_infrastructure_requirements_for_event_persistence_in_rulebook_activations/aem-page/plan-plan_infrastructure_requirements_for_event_persistence_in_rulebook_activations.html"
last_crumb = "Plan infrastructure requirements for event persistence"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Plan infrastructure requirements for event persistence"
oversized = "false"
page_slug = "plan-plan_infrastructure_requirements_for_event_persistence_in_rulebook_activations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-plan_infrastructure_requirements_for_event_persistence_in_rulebook_activations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-plan_infrastructure_requirements_for_event_persistence_in_rulebook_activations/toc/toc.json"
type = "aem-page"
+++

# Plan infrastructure requirements for event persistence

If you want to use event persistence in your rulebook activations, you must plan for the required infrastructure before installing Ansible Automation Platform. Event persistence requires a dedicated database and a Rule Engine credential that you configure during the planning and installation phases.

By default, events processed by rulebook activations are not persisted. When you enable event persistence, Event-Driven Ansible stores event data in a dedicated database so you can review and audit the events that triggered your automation rules. Because the event persistence database is deployed during installation, you must decide whether to use this feature before you begin the installation process. If you enable event persistence after installation, additional configuration steps are required. The following topics describe what event persistence provides, and the credential setup it requires so that you can factor these requirements into your deployment planning.
