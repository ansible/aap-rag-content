# 2. Ansible Automation Platform synchronization configuration reference
## 2.2. Optional Job Template synchronization settings

These parameters apply specifically to Job Template synchronization. If synchronization is enabled, the schedule and timeout settings **must** be provided.

| Option | Type | Requirement | Default | Description |
| --- | --- | --- | --- | --- |
| <br> `sync.jobTemplates.enabled` | <br> `boolean` | <br> **Must** be provided | <br> `true` | <br>  Set to `true` to enable Job Template synchronization, or `false` to disable it. |
| <br> `sync.jobTemplates.surveyEnabled` | <br> `boolean` | <br>  Optional | <br>  - | <br>  Filters Job Templates based on whether an Ansible Automation Platform Survey is enabled. See the **Filter Options** section for details. |
| <br> `sync.jobTemplates.labels` | <br> `array` | <br>  Optional | <br> `[]` | <br>  Filters Job Templates based on specific Ansible Automation Platform Labels. See the **Filter Options** section for details. |
| <br> `sync.jobTemplates.schedule.frequency` | <br> `object` | <br> **Must** be provided if template sync is enabled | <br>  - | <br>  Defines how often the Job Template synchronization runs (for example, `{ minutes: 60 }`). |
| <br> `sync.jobTemplates.schedule.timeout` | <br> `object` | <br> **Must** be provided if template sync is enabled | <br>  - | <br>  The maximum duration for Job Template synchronization before a timeout error occurs (for example, `{ minutes: 15 }`). |

