# Ansible Automation Platform patch release December 10, 2025
## Ansible Automation Platform Operator

Enhancements
- Event-Driven Ansible event-stream mTLS configuration has been added to the installer.(AAP-58343)
- Added `spec_overrides` field to the restore CR spec:
* Added support for overriding Controller-specific settings via `spec_overrides.controller`.
* Added support for overriding automation hub specific settings via `spec_overrides.hub`.
* Added support for overriding Event-Driven Ansible specific settings via `spec_overrides.eda`.
* Added support for overriding database-specific settings via `spec_overrides.database`.(AAP-60024)

Bug Fixes
- Fixed an issue with object storage secrets that were not included in the Automation Hub backup.(AAP-59610)
- Fixed the conditional failure for `AnsibleWorkflow` job launch when using the `AnsibleWorkflow` CR in Ansible Automation Platform 2.6.(AAP-59106)
- Fixed an issue where there was an OpenShift Container Platform resource runner python library dependency missing from the container image.(AAP-59032)
- Fixed a server error that could happen when assigning permissions via the `/api/eda/` or `/api/controller/` endpoints.(AAP-58622)

