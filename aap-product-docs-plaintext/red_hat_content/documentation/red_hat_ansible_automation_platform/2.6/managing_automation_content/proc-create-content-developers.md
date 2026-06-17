# 2. Managing collections in automation hub
## 2.1. Managing namespaces
### 2.1.1. Creating a content development team

Create a new team in Ansible Automation Platform to support content curation and development in your organization. This team can contribute internally-developed collections for publication in private automation hub.

To help content developers create a namespace and upload their internally developed collections to private automation hub, you must first create a team and assign the required permissions.

**Prerequisites**

- You have administrative permissions in Ansible Automation Platform and can create teams.

**Procedure**

1. Log in to Ansible Automation Platform.
2. From the navigation panel, select Access Management → Teams and click Create team.
3. Enter **Content Engineering** as a **Name** for the team.
4. Select an **Organization** for the team.
5. Click Create team. The team Details page opens.
6. Select the **Roles** tab and then select the **Automation Content** tab.
7. Click Add roles.
8. Select **Namespace** from the **Resource type** list and click Next.
9. Select the namespaces that will receive the new roles and click Next.
10. Select the roles to apply to the selected namespaces and click Next.
11. Review your selections and click Finish.
12. Click Close to complete the process.

**Next steps**

The new team is created with the permissions that you assigned. You can now add users to the team in the **Users** tab. See [Assigning users to a team](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-gw-team-add-user) for further steps.

**Additional resources**

- [Teams](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#assembly-controller-teams_gw-manage-rbac)

