# Ansible Automation Platform 2.7 hotfix patch release September 25, 2026
## Platform Operator

- Fixed an issue where the gateway could intermittently return 503 errors on its internal health-check endpoint during periods of concurrent user activity. This was caused by an overly restrictive connection limit, which has now been removed. (AAP-93604)
