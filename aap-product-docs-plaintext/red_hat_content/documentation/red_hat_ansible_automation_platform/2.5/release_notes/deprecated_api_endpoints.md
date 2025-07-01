# 4. Deprecated features
## 4.1. Deprecated API endpoints




API endpoints that will be removed in a future release either because their functionality is being removed or superseded with other capabilities. For example, with the platform moving to a centralized authentication system in the platform gateway, the existing authorization APIs in the automation controller and automation hub are being deprecated for future releases as all authentication operations should occur in the platform gateway.

| Component | Endpoint | Capability |
| --- | --- | --- |
| Automation controller |  `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/o</span></strong></span>` | Token authentication is moving to the platform gateway. |
| Automation hub |  `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/login/keycloak</span></strong></span>` | Moving to the platform gateway. |
| Automation hub |  `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v3/auth/token</span></strong></span>` | Token authentication used for pulling collections will migrate to the platform gateway tokens. |
| Automation controller |  `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/organizations</span></strong></span>` | Moving to the platform gateway. |
| Automation controller |  `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/teams</span></strong></span>` | Moving to the platform gateway. |
| Automation controller |  `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/users</span></strong></span>` | Moving to the platform gateway. |
| Automation controller |  `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/roles</span></strong></span>` | Controller-specific role definitions are moving to `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/controller/v2/role_definitions</span></strong></span>` . |
| Automation controller | The following roles lists:

-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/teams/{id}/roles/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/users/{id}/roles/</span></strong></span>` | Controller-specific resource permissions are moving to `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/controller/v2/role_user_assignments</span></strong></span>` and `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/controller/v2/role_team_assignments</span></strong></span>` . |
| Automation controller | The following object roles lists:

-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/credentials/{id}/object_roles/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/instance_groups/{id}/object_roles/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/inventories/{id}/object_roles/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/job_templates/{id}/object_roles/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/organizations/{id}/object_roles/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/projects/{id}/object_roles/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/teams/{id}/object_roles/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/workflow_job_templates/{id}/object_roles/</span></strong></span>` | Controller-specific resource permissions are moving to `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/controller/v2/role_user_assignments</span></strong></span>` and `<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/controller/v2/role_team_assignments</span></strong></span>` . |
| Automation controller | The following resource access lists:

-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/credentials/{id}/access_list/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/instance_groups/{id}/access_list/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/inventories/{id}/access_list/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/job_templates/{id}/access_list/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/organizations/{id}/access_list/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/projects/{id}/access_list/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/teams/{id}/access_list/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/users/{id}/access_list/</span></strong></span>`
-  `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">/api/v2/workflow_job_templates/{id}/access_list/</span></strong></span>` | No replacements yet. |


