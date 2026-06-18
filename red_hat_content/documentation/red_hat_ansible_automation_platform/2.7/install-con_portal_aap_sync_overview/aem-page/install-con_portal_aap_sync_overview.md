+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_portal_aap_sync_overview"
template = "docs/aem-title.html"
title = "Understanding Ansible Automation Platform synchronization - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_about/", "Install Ansible automation portal (OpenShift Container Platform only)"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_portal_aap_sync_overview/aem-page/install-con_portal_aap_sync_overview.html"
last_crumb = "Understanding Ansible Automation Platform synchronization"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Understanding Ansible Automation Platform synchronization"
oversized = "false"
page_slug = "install-con_portal_aap_sync_overview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-con_portal_aap_sync_overview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_portal_aap_sync_overview/toc/toc.json"
type = "aem-page"
+++

# Understanding Ansible Automation Platform synchronization

The synchronization feature imports your Organization, Users, Teams, and Job Templates from Ansible Automation Platform into Ansible automation portal, making these entities securely discoverable and accessible to portal users.

## Overview

Ansible automation portal synchronizes two types of data from Ansible Automation Platform:

- Organization, Users, and Teams: Identity and organizational structure data
- Job Templates: Executable automation templates


Both synchronizations run on a scheduled basis and can be manually triggered by Ansible Automation Platform Administrators in the portal UI.

## How it works

1. Ansible automation portal connects to your Ansible Automation Platform instance using configured credentials.
2. Ansible automation portal fetches data based on the configured Ansible Automation Platform Organization and filter criteria.
3. Ansible automation portal converts Ansible Automation Platform entities into portal entities and displays them in the UI.
4. Synchronization runs on a configurable schedule (for example, every 60 minutes).
5. Users access and launch resources based on their existing Ansible Automation Platform permissions.

## Ansible Automation Platform synchronization configuration reference

Definitions for all required and optional configuration parameters for the Ansible Automation Platform synchronization feature, including data types, filter options, and label normalization logic.

### Required synchronization settings

These parameters must be included in the `catalog.providers.rhaap` section of your Helm values file to enable identity synchronization.

| Option                                   | Type     | Requirement      | Default | Description                                                                                                                                     |
| ---------------------------------------- | -------- | ---------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `orgs`                                   | `string` | Must be provided | -       | The Ansible Automation Platform Organization to synchronize from. The configuration supports only one Ansible Automation Platform Organization. |
| `sync.orgsUsersTeams.schedule.frequency` | `object` | Must be provided | -       | Defines how often the identity data (Organization, Users, and Teams) synchronization runs (for example, `{ minutes: 60 }`).                     |
| `sync.orgsUsersTeams.schedule.timeout`   | `object` | Must be provided | -       | The maximum duration for identity synchronization before a timeout error occurs (for example, `{ minutes: 15 }`).                               |

### Optional Job Template synchronization settings

These parameters apply specifically to Job Template synchronization. If synchronization is enabled, the schedule and timeout settings must be provided.

| Option                                 | Type      | Requirement                                  | Default | Description                                                                                                                          |
| -------------------------------------- | --------- | -------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `sync.jobTemplates.enabled`            | `boolean` | Must be provided                             | `true`  | Set to `true` to enable Job Template synchronization, or `false` to disable it.                                                      |
| `sync.jobTemplates.surveyEnabled`      | `boolean` | Optional                                     | -       | Filters Job Templates based on whether an Ansible Automation Platform Survey is enabled. See the Filter Options section for details. |
| `sync.jobTemplates.labels`             | `array`   | Optional                                     | `[]`    | Filters Job Templates based on specific Ansible Automation Platform Labels. See the Filter Options section for details.              |
| `sync.jobTemplates.schedule.frequency` | `object`  | Must be provided if template sync is enabled | -       | Defines how often the Job Template synchronization runs (for example, `{ minutes: 60 }`).                                            |
| `sync.jobTemplates.schedule.timeout`   | `object`  | Must be provided if template sync is enabled | -       | The maximum duration for Job Template synchronization before a timeout error occurs (for example, `{ minutes: 15 }`).                |

### Filter options

The following filter options apply only to Job Template synchronization.

The `surveyEnabled` filter accepts one of the following values:

- Omitted: Sync all Job Templates, regardless of their Ansible Automation Platform Survey status.
- `true`: Sync only Job Templates that have Ansible Automation Platform Surveys enabled.
- `false`: Sync only Job Templates that do not have Ansible Automation Platform Surveys enabled.


The `labels` filter accepts an array of strings:

- `[]` (empty array) or omitted: Sync all Job Templates, regardless of associated Ansible Automation Platform Labels.
- `["label1", "label2"]`: Sync only Job Templates that have any of the specified Ansible Automation Platform Labels (OR logic).
- Label matching is case-insensitive.

### Ansible Automation Platform label normalization

Before filtering is applied, Ansible Automation Platform Labels are normalized by applying the following transformations:

- Convert the label to lowercase (for example, "CaC" becomes "cac")
- Replace invalid characters
- Collapse multiple hyphens into a single hyphen (for example, "app--dev" becomes "app-dev")
- Remove leading and trailing hyphens (for example, "--tag--" becomes "tag")

## Ansible Automation Platform synchronization configuration examples

Complete, tested YAML blocks for common synchronization scenarios, such as minimal setup, filtered synchronization, and production configurations. Use these examples to implement and validate settings in your Helm values file.

### Minimal configuration

Synchronizes the Organization, Users, Teams, and Job Templates using the default 60-minute frequency and 15-minute timeout.

```yaml
catalog:
  providers:
    rhaap:
      '{{- include "catalog.providers.env" . }}':
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
```

### Filter by survey status

Synchronize identity data, but filter Job Templates to include only those that have Ansible Automation Platform Surveys enabled.

To sync Job Templates without Ansible Automation Platform Surveys, set `surveyEnabled:` to `false`.

```yaml
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            surveyEnabled: true
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
```

### Filter by labels

Synchronize Job Templates that match any of the specified Ansible Automation Platform Labels: `portal`, `self-service`, or `production`. The configuration uses OR logic for labels.

```yaml
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            labels:
              - portal
              - self-service
              - production
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
```

### Exclude by labels

To prevent templates with specific labels from syncing into the portal, use the `excludeLabels` parameter in your template configuration or search query.

You must format excluded labels as an array (for example, `excludeLabels: ["test", "deprecated"]`).

```yaml
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            labels:
              - portal
              - self-service
              - production
            excludeLabels:
              - "test"
              - "example"
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
```

### Combine filters for production

Combine survey status and label filters:

```yaml
catalog:
  providers:
    rhaap:
      production:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            surveyEnabled: true
            labels:
              - portal
              - self-service
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
```
This configuration syncs:

- All Users and Teams from the "Default" organization
- Job Templates that belong to "Default" organization AND have Ansible Automation Platform Surveys enabled AND have Ansible Automation Platform Labels "portal" OR "self-service"

### Custom sync frequencies

Fast synchronization (development):

```yaml
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 5 }
              timeout: { seconds: 30 }
          jobTemplates:
            enabled: true
            schedule:
              frequency: { minutes: 5 }
              timeout: { seconds: 30 }
```
Standard synchronization:

```yaml
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
```
Slow synchronization:

```yaml
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { hours: 4 }
              timeout: { minutes: 30 }
          jobTemplates:
            enabled: true
            schedule:
              frequency: { hours: 4 }
              timeout: { minutes: 30 }
```

### Different frequencies for identity and templates

Sync identity data less frequently than Job Templates:

```yaml
catalog:
  providers:
    rhaap:
      production:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { hours: 4 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            schedule:
              frequency: { minutes: 30 }
              timeout: { minutes: 10 }
```

### Disable Job Template sync

Set `enabled: false` to temporarily disable Job Template synchronization while maintaining identity sync.

```yaml
catalog:
  providers:
    rhaap:
      development:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: false
            schedule:
              frequency: { minutes: 60 }
              timeout: { minutes: 15 }
```

### Production configuration example

Complete production configuration with filters:

```yaml
catalog:
  providers:
    rhaap:
      production:
        orgs: Default
        sync:
          orgsUsersTeams:
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
          jobTemplates:
            enabled: true
            surveyEnabled: true
            labels:
              - production
              - self-service
            schedule:
              frequency: { hours: 1 }
              timeout: { minutes: 15 }
```

## Manually triggering synchronization

Ansible Automation Platform administrators can manually trigger synchronization from the Ansible automation portal UI instead of waiting for the next scheduled sync.

### Procedure

1.  Log in to Ansible automation portal as an Ansible Automation Platform Administrator.
2.  Navigate to the Synchronization management page.
3.  Click Manual sync for Organization or Job Templates.
4.  Monitor the sync progress in the UI.

### Results

The synchronization is listed as Successful on the Synchronization management page.

## Troubleshooting Ansible Automation Platform synchronization

Review common issues, symptoms, and solutions if synchronization between Ansible Automation Platform and Ansible automation portal does not function as expected.

### No Job Templates appearing in portal

**Issue:** Expected Job Templates are missing from the portal interface.

**Solutions:**

- Verify the `surveyEnabled` setting in your Helm values file matches the status of your Job Templates.
- Confirm the `labels` filter includes the correct, approved Ansible Automation Platform Label names.
- Try temporarily removing filters to confirm if the Job Templates appear without restrictions.
- Verify the Ansible Automation Platform Organization name spelling is exact (it is case-sensitive).
- Check Ansible Automation Platform connectivity and the configured token permissions.

### No Users or Teams appearing in portal

**Issue:** Expected users or teams are missing from the portal interface.

**Solutions:**

- Check Ansible Automation Platform connectivity and the configured token permissions.
- Verify the Ansible Automation Platform Organization name matches exactly.
- Review the configured synchronization schedule and check system logs.
- Ensure users have the proper organization or team memberships within Ansible Automation Platform.

### Slow synchronization

**Issue:** Synchronization takes too long to complete or times out.

**Symptoms:**

- Timeouts during synchronization.
- Timeout errors appear in the logs.


**Solutions:**

- Increase the `timeout` value in the synchronization schedule.
- Reduce the synchronization `frequency` (sync less often).
- Add more specific filters to the Job Templates configuration to reduce the overall count of entities processed.
- For large organizations, increase the `timeout` specifically for the identity sync (`orgsUsersTeams`).

### Wrong Ansible Automation Platform organization

**Issue:** The portal displays unexpected Job Templates, users, or teams.

**Symptoms:**

- Expected Job Templates do not appear.
- Incorrect templates appear.
- Users or teams are missing, or the wrong ones are present.


**Solutions:**

- Verify the Ansible Automation Platform Organization name spelling is exact (it is case-sensitive).
- Check the organization names in Ansible Automation Platform itself.
- Ensure the configured organization exists in Ansible Automation Platform.
