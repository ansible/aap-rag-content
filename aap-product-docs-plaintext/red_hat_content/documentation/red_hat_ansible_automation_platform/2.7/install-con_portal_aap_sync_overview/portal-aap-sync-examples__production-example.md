# Understanding Ansible Automation Platform synchronization
## Ansible Automation Platform synchronization configuration examples
### Production configuration example

Complete production configuration with filters:

```yaml
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

