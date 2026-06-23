# Understanding Ansible Automation Platform synchronization
## Ansible Automation Platform synchronization configuration examples
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

