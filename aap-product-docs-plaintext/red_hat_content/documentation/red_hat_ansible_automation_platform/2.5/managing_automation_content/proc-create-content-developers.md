# 2. Managing collections in automation hub
## 2.1. Using namespaces to manage collections in automation hub
### 2.1.1. Creating a new team for content curators




You can create a new team in Ansible Automation Platform designed to support content curation in your organization. This team can contribute internally-developed collections for publication in private automation hub.

To help content developers create a namespace and upload their internally developed collections to private automation hub, you must first create and edit a team and assign the required permissions.

**Prerequisites**

- You have administrative permissions in Ansible Automation Platform and can create teams.


**Procedure**

1. Log in to your Ansible Automation Platform.
1. From the navigation panel, selectAccess Management→Teamsand clickCreate team.
1. Enter **Content Engineering** as a **Name** for the team.
1. Select an **Organization** for the team.
1. ClickCreate team. You have created the new team and the team Details page opens.
1. Select the **Roles** tab and then select the **Automation Content** tab.
1. ClickAdd roles.
1. Select **Namespace** from the **Resource type** list and clickNext.
1. Select the namespaces that will receive the new roles and clickNext.
1. Select the roles to apply to the selected namespaces and clickNext.
1. Review your selections and clickFinish.
1. ClickCloseto complete the process.

The new team is created with the permissions that you assigned. You can then add users to the team.


1. Click the **Users** tab on the **Teams** page.
1. ClickAdd users.
1. Select users and clickAdd users.


For further instructions on managing access with teams, see [Teams](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#assembly-controller-teams_gw-manage-rbac) in the Access management and authentication guide.

