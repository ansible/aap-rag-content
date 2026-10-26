+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_examples"
title = "Ansible Automation Platform synchronization configuration examples - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_examples/aem-page/install-ref_portal_aap_sync_examples.html"
last_crumb = "Ansible Automation Platform synchronization configuration examples"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Ansible Automation Platform synchronization configuration examples"
oversized = "false"
page_slug = "install-ref_portal_aap_sync_examples"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_examples"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_portal_aap_sync_examples/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform synchronization configuration examples

Complete, tested YAML blocks for common synchronization scenarios, such as minimal setup, filtered synchronization, and production configurations. Use these examples to implement and validate settings in your Helm values file.

## Minimal configuration

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

## Filter by survey status

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

## Filter by labels

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

## Exclude by labels

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

## Combine filters for production

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

## Custom sync frequencies

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

## Different frequencies for identity and templates

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

## Disable Job Template sync

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

## Production configuration example

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
