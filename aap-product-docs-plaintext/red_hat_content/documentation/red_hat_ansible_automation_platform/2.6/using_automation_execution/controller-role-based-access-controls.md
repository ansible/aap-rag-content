# 9. Workflows in automation controller
## 9.4. Role-based access controls




To edit and delete a workflow job template, you must have the administrator role. To create a workflow job template, you must be an organization administrator or a system administrator. However, you can run a workflow job template that has job templates that you do not have permissions for. System administrators can create a blank workflow and then grant an `admin_role` to a low-level user, after which they can delegate more access and build the graph. You must have `execute` access to a job template to add it to a workflow job template.

You can also perform other tasks, such as making a duplicate copy or re-launching a workflow, depending on which permissions are granted to a user. You must have permissions to all the resources used in a workflow, such as job templates, before relaunching or making a copy.

For more information, see [Managing access with role based access control](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access) .

For more information about performing the tasks described, see [Workflow job templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-workflow-job-templates) .

