# 3. Ansible Automation Platform synchronization configuration examples
## 3.8. Disable Job Template sync




Set `enabled: false` to temporarily disable Job Template synchronization while maintaining identity sync.

```
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

