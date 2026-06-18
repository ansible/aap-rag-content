+++
template = "docs/aem-title.html"
title = "Define events with rulebooks - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-con_gs_define_events_rulebooks"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-assembly_gs_auto_dev/", "Get started as an automation developer"]]
category = "Get started"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/get_started-con_gs_define_events_rulebooks/aem-page/get_started-con_gs_define_events_rulebooks.html"
last_crumb = "Define events with rulebooks"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Define events with rulebooks"
oversized = "false"
page_slug = "get_started-con_gs_define_events_rulebooks"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/get_started-con_gs_define_events_rulebooks"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/get_started-con_gs_define_events_rulebooks/toc/toc.json"
type = "aem-page"
+++

# Define events with rulebooks

An Ansible rulebook is a collection of rulesets that references one or more sources, rules, and conditions.

Rulebooks are to Event-Driven Ansible what playbooks are to Ansible Automation Platform as a whole. Like a playbook, a rulebook defines automation tasks for the platform, along with when they should be triggered.

## Rulebook actions

Rulebooks use an "if-this-then-that” logic that tells Event-Driven Ansible what actions to activate when a rule is triggered. Event-Driven Ansible listens to the controller event stream and, when an event triggers a rule, activates an automation action in response.

Rulebooks can trigger the following activations:

-  `run_job_template`
- `run_playbook` (only supported with ansible-rulebook CLI)
-  `debug`
-  `print_event`
-  `set_fact`
-  `post_event`
-  `retract_fact`
-  `shutdown`
