# 3. Ansible Automation Platform synchronization configuration examples
## 3.3. Filter by labels




Synchronize Job Templates that match **ANY** of the specified Ansible Automation Platform Labels: `portal` , `self-service` , or `production` . The configuration uses **OR** logic for labels.

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
enabled: true
labels:
- portal
- self-service
- production
schedule:
frequency: { minutes: 60 }
timeout: { minutes: 15 }
```

