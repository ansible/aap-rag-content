# Understanding Ansible Automation Platform synchronization
## Ansible Automation Platform synchronization configuration examples
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

