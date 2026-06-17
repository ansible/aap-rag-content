# 9. Patch releases
## 9.4. Ansible Automation Platform patch release January 21, 2026
### 9.4.6. Event-Driven Ansible

#### 9.4.6.1. Features

- Added x-ai-description field to the activation PATCH method.(AAP-61969)
- With this update, activations in the "workers offline" status on the Event-Driven Ansible server are now protected from accidental deletion or disabling. This enhancement adds a warning banner to the User Interface (UI) for the "restart", "disable", and "delete" workflows, providing users with a clear warning before performing these actions. The feature also supports a force flag for the "disable" and "delete" operations, giving users the option to bypass the warning if necessary.(AAP-51378)

#### 9.4.6.2. Bug Fixes

- Fixed an issue where the IPv6 support in the Event-Driven Ansible operator configmaps was missing the extra listen **NGINX** directive. We added the required directive so the event streams pod now has **NGINX** bound to its IPv6 interface.(AAP-62001)

