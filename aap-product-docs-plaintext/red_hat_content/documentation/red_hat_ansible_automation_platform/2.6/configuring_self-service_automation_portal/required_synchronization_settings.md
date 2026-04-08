# 2. Ansible Automation Platform synchronization configuration reference
## 2.1. Required synchronization settings




These parameters **must** be included in the `catalog.providers.rhaap` section of your Helm values file to enable identity synchronization.

| Option | Type | Requirement | Default | Description |
| --- | --- | --- | --- | --- |
|  `orgs` |  `string` |  **Must** be provided | - | The Ansible Automation Platform Organization to synchronize from. The configuration supports only one Ansible Automation Platform Organization. |
|  `sync.orgsUsersTeams.schedule.frequency` |  `object` |  **Must** be provided | - | Defines how often the identity data (Organizations, Users, and Teams) synchronization runs (for example, `{ minutes: 60 }` ). |
|  `sync.orgsUsersTeams.schedule.timeout` |  `object` |  **Must** be provided | - | The maximum duration for identity synchronization before a timeout error occurs (for example, `{ minutes: 15 }` ). |


