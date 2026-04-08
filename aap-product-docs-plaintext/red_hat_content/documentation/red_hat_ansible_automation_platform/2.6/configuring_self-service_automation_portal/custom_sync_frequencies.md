# 3. Ansible Automation Platform synchronization configuration examples
## 3.6. Custom sync frequencies




Fast synchronization (development):

```
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

```
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

```
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

