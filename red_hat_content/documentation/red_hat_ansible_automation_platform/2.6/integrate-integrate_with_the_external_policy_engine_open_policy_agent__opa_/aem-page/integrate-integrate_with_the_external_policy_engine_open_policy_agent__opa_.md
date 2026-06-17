+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-integrate_with_the_external_policy_engine_open_policy_agent__opa_"
template = "docs/aem-title.html"
title = "Integrate with the external policy engine Open Policy Agent (OPA) - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-integrate_with_the_external_policy_engine_open_policy_agent__opa_/", "Integrate with the external policy engine Open Policy Agent (OPA)"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-integrate_with_the_external_policy_engine_open_policy_agent__opa_/aem-page/integrate-integrate_with_the_external_policy_engine_open_policy_agent__opa_.html"
last_crumb = "Integrate with the external policy engine Open Policy Agent (OPA)"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Integrate with the external policy engine Open Policy Agent (OPA)"
oversized = "false"
page_slug = "integrate-integrate_with_the_external_policy_engine_open_policy_agent__opa_"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/integrate-integrate_with_the_external_policy_engine_open_policy_agent__opa_"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-integrate_with_the_external_policy_engine_open_policy_agent__opa_/toc/toc.json"
type = "aem-page"
+++

# Integrate with the external policy engine Open Policy Agent (OPA)

Integrating Ansible Automation Platform with Open Policy Agent (OPA) enforces policies at automation runtime. Use encoded rules to define, manage, and enforce how users interact with the platform. Automate policy management to improve security, compliance, and operational efficiency.

 Integrating with OPA helps you to:

- **Enforce policies at runtime**: Stop automation actions that violate organizational policies and provide users with clear information about policy violations before jobs run.
- **Centralize policy management**: Offload policy decisions to your OPA server and manage automation governance rules alongside organizational policies.
- **Improve compliance and security**: Apply policy rules to automation content at the organization, inventory, or job template level to ensure consistent governance.

## How Ansible Automation Platform supports OPA integration

When you trigger policy enforcement, policies are retrieved from your OPA server. These policies are applied to automation content before jobs run. If a violation is detected, the action stops and you receive information about the specific policy violation.

Associate policies with organizations, inventories, or job templates to control where policy enforcement occurs.
