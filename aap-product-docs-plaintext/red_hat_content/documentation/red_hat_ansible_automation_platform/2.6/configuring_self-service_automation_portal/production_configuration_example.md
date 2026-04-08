# 3. Ansible Automation Platform synchronization configuration examples
## 3.9. Production configuration example




Complete production configuration with filters:

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
- production
- self-service
schedule:
frequency: { hours: 1 }
timeout: { minutes: 15 }
```

