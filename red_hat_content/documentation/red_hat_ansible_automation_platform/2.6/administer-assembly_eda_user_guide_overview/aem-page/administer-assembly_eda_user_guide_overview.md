+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_user_guide_overview"
title = "Trigger automation from events with Event-Driven Ansible - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_user_guide_overview/", "Trigger automation from events with Event-Driven Ansible"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_user_guide_overview/aem-page/administer-assembly_eda_user_guide_overview.html"
last_crumb = "Trigger automation from events with Event-Driven Ansible"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Trigger automation from events with Event-Driven Ansible"
oversized = "false"
page_slug = "administer-assembly_eda_user_guide_overview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_user_guide_overview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_user_guide_overview/toc/toc.json"
type = "aem-page"
+++

# Trigger automation from events with Event-Driven Ansible

Event-Driven Ansible is a highly scalable, flexible automation capability. It works with external event sources (like software vendors' monitoring tools) to identify IT events and automatically implement the defined changes or responses within a rulebook.

Learn how to configure and manage the end-to-end lifecycle of event-driven automation within the Red Hat Ansible Automation Platform. Event-Driven Ansible provides you the ability to perform the following actions:

- Manage projects for rulebook storage
- Build and restore decision environments for execution
- Define credentials for secure authentication
- Create event streams for centralized routing
- Manage rulebook activations to main persistent, scalable listeners that monitor infrastructure and trigger automated workflows in real time


Note:

- API documentation for Event-Driven Ansible controller is available through the platform gateway (for example, `https://<gateway-host>/api/eda/v1/docs`).
- To meet high availability demands, Event-Driven Ansible controller shares centralized Redis (REmote DIctionary Server) with the Ansible Automation Platform UI. When Redis is unavailable, you will not be able to create or sync projects, or enable rulebook activations.

Important:

In new installations of Ansible Automation Platform, using Event-Driven Ansible controller’s API to manage organizations, teams, or users requires an automated sync of up to 15 minutes to propagate changes to the rest of the Ansible Automation Platform components. To avoid potential errors and ensure immediate access, use the platform gateway API instead, or the unified UI.
