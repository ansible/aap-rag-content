# 2. Ansible Automation Platform synchronization configuration reference
## 2.2. Optional Job Template synchronization settings




These parameters apply specifically to Job Template synchronization. If synchronization is enabled, the schedule and timeout settings **must** be provided.

| Option | Type | Requirement | Default | Description |
| --- | --- | --- | --- | --- |
|  `sync.jobTemplates.enabled` |  `boolean` |  **Must** be provided |  `true` | Set to `true` to enable Job Template synchronization, or `false` to disable it. |
|  `sync.jobTemplates.surveyEnabled` |  `boolean` | Optional | - | Filters Job Templates based on whether an Ansible Automation Platform Survey is enabled. See the **Filter Options** section for details. |
|  `sync.jobTemplates.labels` |  `array` | Optional |  `[]` | Filters Job Templates based on specific Ansible Automation Platform Labels. See the **Filter Options** section for details. |
|  `sync.jobTemplates.schedule.frequency` |  `object` |  **Must** be provided if template sync is enabled | - | Defines how often the Job Template synchronization runs (for example, `{ minutes: 60 }` ). |
|  `sync.jobTemplates.schedule.timeout` |  `object` |  **Must** be provided if template sync is enabled | - | The maximum duration for Job Template synchronization before a timeout error occurs (for example, `{ minutes: 15 }` ). |


