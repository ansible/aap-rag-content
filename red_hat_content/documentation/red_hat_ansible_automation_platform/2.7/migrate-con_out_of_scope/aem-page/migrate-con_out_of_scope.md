+++
template = "docs/aem-title.html"
title = "Out of scope - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-con_out_of_scope"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-con_out_of_scope/", "Out of scope"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-con_out_of_scope/aem-page/migrate-con_out_of_scope.html"
last_crumb = "Out of scope"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Out of scope"
oversized = "false"
page_slug = "migrate-con_out_of_scope"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/migrate-con_out_of_scope"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-con_out_of_scope/toc/toc.json"
type = "aem-page"
+++

# Out of scope

Understand which Ansible Automation Platform components and configurations require manual re-creation in the target environment and are not covered by the migration process.

Migration covers core Ansible Automation Platform components. Some components and configurations are out of scope and require manual re-creation in the target environment:

- Event-Driven Ansible: Manually recreate configuration and content for Event-Driven Ansible in the target environment.
- Instance groups: Manually recreate instance group configurations after migration.
- Hub content: Manually re-import or reconfigure content hosted in automation hub.
- Custom Certificate Authority (CA) for receptor mesh: Manually reconfigure custom CA configurations for receptor mesh.
- Disconnected environments: The migration process does not cover disconnected environments.
- Execution environments (other than the default one): Manually rebuild or re-import custom execution environments.


Manually re-create, import, or configure these items in the target environment.
