+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_config_ref"
title = "Ansible Automation Platform synchronization configuration reference - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_config_ref/aem-page/install-ref_portal_aap_sync_config_ref.html"
last_crumb = "Ansible Automation Platform synchronization configuration reference"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Ansible Automation Platform synchronization configuration reference"
oversized = "false"
page_slug = "install-ref_portal_aap_sync_config_ref"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_config_ref"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_config_ref/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform synchronization configuration reference

Definitions for all required and optional configuration parameters for the Ansible Automation Platform synchronization feature, including data types, filter options, and label normalization logic.

## Required synchronization settings

These parameters must be included in the `catalog.providers.rhaap` section of your Helm values file to enable identity synchronization.

| Option                                   | Type     | Requirement      | Default | Description                                                                                                                                     |
| ---------------------------------------- | -------- | ---------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `orgs`                                   | `string` | Must be provided | -       | The Ansible Automation Platform Organization to synchronize from. The configuration supports only one Ansible Automation Platform Organization. |
| `sync.orgsUsersTeams.schedule.frequency` | `object` | Must be provided | -       | Defines how often the identity data (Organization, Users, and Teams) synchronization runs (for example,`{ minutes: 60 }`).                      |
| `sync.orgsUsersTeams.schedule.timeout`   | `object` | Must be provided | -       | The maximum duration for identity synchronization before a timeout error occurs (for example,`{ minutes: 15 }`).                                |

## Optional Job Template synchronization settings

These parameters apply specifically to Job Template synchronization. If synchronization is enabled, the schedule and timeout settings must be provided.

| Option                                 | Type      | Requirement                                  | Default | Description                                                                                                                          |
| -------------------------------------- | --------- | -------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `sync.jobTemplates.enabled`            | `boolean` | Must be provided                             | `true`  | Set to`true` to enable Job Template synchronization, or`false` to disable it.                                                        |
| `sync.jobTemplates.surveyEnabled`      | `boolean` | Optional                                     | -       | Filters Job Templates based on whether an Ansible Automation Platform Survey is enabled. See the Filter Options section for details. |
| `sync.jobTemplates.labels`             | `array`   | Optional                                     | `[]`    | Filters Job Templates based on specific Ansible Automation Platform Labels. See the Filter Options section for details.              |
| `sync.jobTemplates.schedule.frequency` | `object`  | Must be provided if template sync is enabled | -       | Defines how often the Job Template synchronization runs (for example,`{ minutes: 60 }`).                                             |
| `sync.jobTemplates.schedule.timeout`   | `object`  | Must be provided if template sync is enabled | -       | The maximum duration for Job Template synchronization before a timeout error occurs (for example,`{ minutes: 15 }`).                 |

## Filter options

The following filter options apply only to Job Template synchronization.

The `surveyEnabled` filter accepts one of the following values:

- Omitted: Sync all Job Templates, regardless of their Ansible Automation Platform Survey status.
- `true`: Sync only Job Templates that have Ansible Automation Platform Surveys enabled.
- `false`: Sync only Job Templates that do not have Ansible Automation Platform Surveys enabled.

The `labels` filter accepts an array of strings:

- `[]` (empty array) or omitted: Sync all Job Templates, regardless of associated Ansible Automation Platform Labels.
- `["label1", "label2"]`: Sync only Job Templates that have any of the specified Ansible Automation Platform Labels (OR logic).
- Label matching is case-insensitive.

## Ansible Automation Platform label normalization

Before filtering is applied, Ansible Automation Platform Labels are normalized by applying the following transformations:

- Convert the label to lowercase (for example, "CaC" becomes "cac")
- Replace invalid characters
- Collapse multiple hyphens into a single hyphen (for example, "app--dev" becomes "app-dev")
- Remove leading and trailing hyphens (for example, "--tag--" becomes "tag")
