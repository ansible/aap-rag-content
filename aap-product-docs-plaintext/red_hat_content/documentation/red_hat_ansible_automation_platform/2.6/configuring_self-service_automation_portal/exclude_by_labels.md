# 3. Ansible Automation Platform synchronization configuration examples
## 3.4. Exclude by labels




To prevent templates from syncing into Portal with specific labels, use the `excludeLabels` parameter in your template configuration or search query.

You must format excluded labels as an array (for example, `excludeLabels: ["test", "deprecated"]` ).

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
excludeLabels:
- "test"
- "example"
schedule:
frequency: { minutes: 60 }
timeout: { minutes: 15 }
```

