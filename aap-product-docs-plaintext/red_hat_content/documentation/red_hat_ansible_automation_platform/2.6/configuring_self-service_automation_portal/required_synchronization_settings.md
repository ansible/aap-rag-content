# 2. Ansible Automation Platform synchronization configuration reference
## 2.1. Required synchronization settings

These parameters **must** be included in the `catalog.providers.rhaap` section of your Helm values file to enable identity synchronization.

| Option | Type | Requirement | Default | Description |
| --- | --- | --- | --- | --- |
| <br> `orgs` | <br> `string` | <br> **Must** be provided | <br>  - | <br>  The Ansible Automation Platform Organization to synchronize from. The configuration supports only one Ansible Automation Platform Organization. |
| <br> `sync.orgsUsersTeams.schedule.frequency` | <br> `object` | <br> **Must** be provided | <br>  - | <br>  Defines how often the identity data (Organization, Users, and Teams) synchronization runs (for example, `{ minutes: 60 }`). |
| <br> `sync.orgsUsersTeams.schedule.timeout` | <br> `object` | <br> **Must** be provided | <br>  - | <br>  The maximum duration for identity synchronization before a timeout error occurs (for example, `{ minutes: 15 }`). |

