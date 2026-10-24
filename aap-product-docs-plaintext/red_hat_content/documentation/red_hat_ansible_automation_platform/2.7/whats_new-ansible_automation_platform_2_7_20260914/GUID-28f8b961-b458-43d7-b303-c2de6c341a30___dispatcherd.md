# Ansible Automation Platform 2.7 patch release September 14, 2026 (2.7-8)
## Automation Controller

- Fixed an issue where Automation Controller 4.8.1 resource synchronization created duplicate global `RoleUserAssignment` records, causing JWT authentication to fail with `MultipleObjectsReturned`; global role assignments are now deduplicated and uniqueness is enforced via a database constraint. (AAP-90593)

