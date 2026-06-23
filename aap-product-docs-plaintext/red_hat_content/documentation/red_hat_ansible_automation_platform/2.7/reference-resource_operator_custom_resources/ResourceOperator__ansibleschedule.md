# Resource Operator custom resources
## Resource Operator custom resources [tower.ansible.com/v1alpha1]
### AnsibleSchedule

Creates a schedule on the automation controller to run a job template at specified intervals.

| Field                  | Type   | Description                                                                                                                                  | Default        |
| ---------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `connection_secret`    | String | Name of the Kubernetes secret containing the platform gateway connection details. Required.                                                  | -              |
| `name`                 | String | Display name for the schedule.                                                                                                               | -              |
| `rrule`                | String | Recurrence rule in iCalendar RRULE format defining the schedule, for example `DTSTART:20210101T000000Z RRULE:FREQ=DAILY;INTERVAL=1;COUNT=1`. | -              |
| `unified_job_template` | String | Name of the job template or workflow to schedule.                                                                                            | -              |
| `runner_pull_policy`   | String | Image pull policy for the runner pod.                                                                                                        | `IfNotPresent` |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleSchedule
metadata:
name: schedule
spec:
connection_secret: aap-access
name: "Demo Schedule"
rrule: "DTSTART:20210101T000000Z RRULE:FREQ=DAILY;INTERVAL=1;COUNT=1"
unified_job_template: "Demo Job Template"
```

