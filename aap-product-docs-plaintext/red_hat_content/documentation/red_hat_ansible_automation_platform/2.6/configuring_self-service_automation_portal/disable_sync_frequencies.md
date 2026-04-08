# 3. Ansible Automation Platform synchronization configuration examples
## 3.7. Disable sync frequencies




Sync identity data less frequently than Job Templates:

```
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

