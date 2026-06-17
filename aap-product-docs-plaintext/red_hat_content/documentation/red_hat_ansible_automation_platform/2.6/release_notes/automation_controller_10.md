# 9. Patch releases
## 9.6. Ansible Automation Platform patch release December 10, 2025
### 9.6.5. Automation controller

#### 9.6.5.1. Features

- Receptor collection version bumped to 2.0.8, which is compatible with Red Hat Enterprise Linux 10.(AAP-58421)
- Added `x-ai-description` to controller schema to provide AI friendly description of each endpoint.(AAP-59819)

#### 9.6.5.2. Bug Fixes

- Fixed an issue where project update failed with no output, and project deletions failed. Automation controller now uses the force flag when syncing a project which has **Allow branch override** enabled.(AAP-58533)
- In this update, users attempting to install a software package on an unsupported architecture may encounter issues due to incorrect data in reminders. This has been resolved.(AAP-59728)
- Fixed an issue where the project update failed with no output and project deletions also failed.(AAP-58533)
- Fixed an issue where the OpenAPI specification for the Automation controller was incomplete, impeding MCP server integration development. This limited the seamless MCP server integration with the Ansible Automation Platform. The Automation controller’s REST API is now complete and accessible.(AAP-53640)

