+++
title = "Event streams database user for external databases - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-event_streams_database_user_for_external_databases"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-plan_infrastructure_requirements_for_event_persistence_in_rulebook_activations/", "Plan infrastructure requirements for Event-Driven Ansible"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-event_streams_database_user_for_external_databases/aem-page/plan-event_streams_database_user_for_external_databases.html"
last_crumb = "Event streams database user for external databases"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Event streams database user for external databases"
oversized = "false"
page_slug = "plan-event_streams_database_user_for_external_databases"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-event_streams_database_user_for_external_databases"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-event_streams_database_user_for_external_databases/toc/toc.json"
type = "aem-page"
+++

# Event streams database user for external databases

If you use an external PostgreSQL database for Event-Driven Ansible, you must create a dedicated database user for event stream operations before installing or upgrading Ansible Automation Platform.

Event-Driven Ansible event streams require a dedicated PostgreSQL database user (`eda_event_stream`) for event stream operations. If you use a database managed by the Ansible Automation Platform installer or Operator, this user is created automatically. If you use an external database, you must create this user before installing or upgrading.

The `eda_event_stream` user requires only `CONNECT` privileges. Event streams use the database connection for pub-sub messaging only, with no read or write operations performed on the database. For more information, see the following related concepts and tasks.
