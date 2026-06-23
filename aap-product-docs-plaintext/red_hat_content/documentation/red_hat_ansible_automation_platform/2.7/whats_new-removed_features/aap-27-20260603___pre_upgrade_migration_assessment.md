# Removed features
## Pre-upgrade migration assessment

Before upgrading, review your environment for the following direct-access patterns, all of which require a migration plan:

| Area                  | What to Review                                                                                                                                  |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| User & Org Management | Any organization, team, or user management interfacing directly with automation controller or automation hub APIs or collections Authentication |
| Authentication        | Legacy users authenticating with basic auth directly to automation controller                                                                   |
| Tokens & OAuth        | Legacy Personal Access Tokens (PATs) or OAuth applications connecting directly to automation controller                                         |
| Image Management      | Any container registry processes managing images directly on private automation hub                                                             |
| Access Control        | RBAC configurations managed directly on individual components rather than through platform gateway                                              |
| Job Management        | Job template or job re-execution triggers to launch jobs directly to automation controller                                                      |
| Inventory Management  | Managing Inventory using automation controller to add, edit, or remove inventory groups or nodes                                                |
| Project Management    | Managing SCM projects using automation controller to add, edit, or remove projects.                                                             |
All of the above must be migrated to use the equivalent functionality provided by the platform gateway.

