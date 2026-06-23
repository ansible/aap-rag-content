# Understanding Ansible Automation Platform synchronization
## Ansible Automation Platform synchronization configuration examples
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

