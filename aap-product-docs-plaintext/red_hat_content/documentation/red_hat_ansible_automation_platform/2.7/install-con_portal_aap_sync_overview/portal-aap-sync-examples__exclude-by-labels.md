# Understanding Ansible Automation Platform synchronization
## Ansible Automation Platform synchronization configuration examples
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

