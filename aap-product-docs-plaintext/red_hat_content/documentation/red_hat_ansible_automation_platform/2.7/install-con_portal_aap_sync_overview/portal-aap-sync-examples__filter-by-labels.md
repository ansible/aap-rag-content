# Understanding Ansible Automation Platform synchronization
## Ansible Automation Platform synchronization configuration examples
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

