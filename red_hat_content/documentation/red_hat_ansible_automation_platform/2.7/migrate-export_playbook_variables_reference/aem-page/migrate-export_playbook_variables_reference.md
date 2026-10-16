+++
template = "docs/aem-title.html"
title = "Export playbook variables reference - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-export_playbook_variables_reference"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-assembly_source_environment/", "Prepare and export data from the source environment"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-export_playbook_variables_reference/aem-page/migrate-export_playbook_variables_reference.html"
last_crumb = "Export playbook variables reference"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Export playbook variables reference"
oversized = "false"
page_slug = "migrate-export_playbook_variables_reference"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/migrate-export_playbook_variables_reference"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-export_playbook_variables_reference/toc/toc.json"
type = "aem-page"
+++

# Export playbook variables reference

Use these variables to configure the `artifact_export` playbook. Set them in your inventory file under `[all:vars]` or pass them with `-e` when running the playbook.

| Variable             | Required | Default                   | Description                                                                                                                                                                                              |
| -------------------- | -------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aap_platform`       | Yes      | None                      | Platform type. Set to`rpm` for RPM-based deployments. Accepted values:`rpm`,`containerized`,`operator`.                                                                                                  |
| `artifact_dir`       | No       | Current working directory | Directory on the control node where the artifact is written. Created if it does not exist.                                                                                                               |
| `export_hub_content` | No       | `true`                    | Set to`false` to skip Pulp content export. The automation hub database is still exported when this is set to`false`. After import, automation content must be re-synced from your configured remote registries. |
| `postgresql_db_type` | No       | `managed`                 | Set to`external` if your deployment uses a PostgreSQL instance not managed by the installer.                                                                                                             |
