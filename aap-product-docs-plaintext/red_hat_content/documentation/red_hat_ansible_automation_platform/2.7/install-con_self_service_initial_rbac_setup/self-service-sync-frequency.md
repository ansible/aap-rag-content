# Set up initial RBAC rules in Ansible automation portal
## Adjust synchronization frequency between Ansible Automation Platform and Ansible automation portal

The Helm chart defines how frequently users, teams and organization configuration information is synchronized from Ansible Automation Platform to Ansible automation portal.

### About this task

The frequency is set by the `catalog.providers.rhaap.schedule.frequency` key. By default, the synchronization occurs hourly.

### Procedure

To adjust the synchronization frequency, edit the value for the `catalog.providers.rhaap.schedule.frequency` key in the Helm chart.

```
catalog:
...
providers:
rhaap:
'{{- include "catalog.providers.env" . }}':
schedule:
frequency: {minutes: 60}
timeout: {seconds: 30}
```


Note:

Increasing the synchronization frequency generates extra traffic.

Bear this in mind when deciding the frequency, particularly if you have a large number of users.
