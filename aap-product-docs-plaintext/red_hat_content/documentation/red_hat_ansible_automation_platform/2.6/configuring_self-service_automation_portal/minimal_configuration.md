# 3. Ansible Automation Platform synchronization configuration examples
## 3.1. Minimal configuration




Synchronizes all Organizations, Users, Teams, and Job Templates using the using the default 60-minute frequency and 15-minute timeout.

```
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

