# Ansible Automation Platform 2.7 patch release August 24, 2026 (2.7-6)
## Controller

- Fixed an issue where fixed an HTTP 500 error when assigning org-scoped roles (such as Organization JobTemplate Admin) to teams via POST /api/controller/v2/role_team_assignments/. The error was caused by a settings mismatch between Controller and Gateway for ANSIBLE_BASE_ALLOW_TEAM_ORG_MEMBER, which caused the Gateway to reject reverse-synced team role assignments containing the member_organization permission. Additionally, reverse-sync failures now log a warning instead of propagating as unhandled server errors. (AAP-85962)
- Fixed an issue where users with insufficient permissions were able to remove other users role assignments (AAP-86293)
- Fixed an issue where fixes an issue where unnecessary project syncs were triggered on multi node clusters (AAP-86621)
- Fixed an issue where fixed migration 0206_jobhostsummary_host_id_idx failing during 2.6→2.7 upgrade when the composite index had been created manually via awx-manage create_host_summary_index or raw SQL. The migration is now idempotent using CREATE INDEX IF NOT EXISTS. (AAP-87829)
- Fixed an issue where revert prior change that added member_organization permission to other organization-level controller roles. (AAP-88479)

