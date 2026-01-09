# 2. Getting started as a platform administrator
## 2.4. Manage user access with role-based access control




Role-based access control (RBAC) restricts user access based on the user’s role within the organization they are assigned to in Ansible Automation Platform. The roles in RBAC refer to the levels of access that users have to Ansible Automation Platform components and resources.

Use RBAC to control what users can do with the components of Ansible Automation Platform at a broad or granular level. You can choose whether the user is a system administrator or normal user, and align roles and access permissions with their positions within the organization.

You can define roles with multiple permissions that can then be assigned to resources, teams, and users. The permissions that make up a role govern what the assigned role allows. Permissions are allocated with only the access needed for a user to perform the tasks appropriate for their role.

The following procedures show how to get started with RBAC by creating a team, and a user to assign to the team. For the complete workflow related to using RBAC to manage access, see the Access management and authentication guide, particularly the sections on [Managing access with role-based access control](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access) and [Roles](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/assembly-gw-roles) .

Important
When managing users, teams, and organizations, use the Unified UI or the platform gateway API to ensure real-time synchronization across all platform components, including Event-Driven Ansible controller. If you use the legacy automation controller API, changes can take up to 15 minutes to propagate to Event-Driven Ansible controller, which can result in authentication errors for new users or teams.



