# Understanding Ansible Automation Platform synchronization
## Ansible Automation Platform synchronization configuration examples
### Filter by survey status

Synchronize identity data, but filter Job Templates to include only those that have Ansible Automation Platform Surveys enabled.

To sync Job Templates without Ansible Automation Platform Surveys, set `surveyEnabled:` to `false`.

```yaml
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
surveyEnabled: true
schedule:
frequency: { minutes: 60 }
timeout: { minutes: 15 }
```

