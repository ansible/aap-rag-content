# 3. Ansible Automation Platform synchronization configuration examples
## 3.5. Combine filters for production




Combine survey status and label filters:

```
catalog:
providers:
rhaap:
production:
orgs: Default
sync:
orgsUsersTeams:
schedule:
frequency: { hours: 1 }
timeout: { minutes: 15 }
jobTemplates:
enabled: true
surveyEnabled: true
labels:
- portal
- self-service
schedule:
frequency: { hours: 1 }
timeout: { minutes: 15 }
```

This configuration syncs:

- All Users, Teams, and Organizations from the "Default" organization
- Job Templates that belong to "Default" organization AND have Ansible Automation Platform Surveys enabled **AND** have Ansible Automation Platform Labels "portal" **OR** "self-service"


