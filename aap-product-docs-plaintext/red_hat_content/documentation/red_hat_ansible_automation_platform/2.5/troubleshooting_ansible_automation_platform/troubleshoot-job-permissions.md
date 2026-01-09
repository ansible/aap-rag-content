# 6. Jobs
## 6.4. Issue - Jobs failing with insufficient permissions error in private automation hub




Jobs are failing with the error message "denied: requested access to the resource is denied, unauthorized: Insufficient permissions". This happens when using an execution environment in private automation hub.

This issue occurs when you protect private automation hub with a password or token but do not assign the registry credential to the execution environment.

**Procedure**

1. Go to automation controller.
1. From the navigation panel, selectAdministration→Execution Environments.
1. Click the execution environment assigned to the job template that is failing.
1. ClickEdit.
1. Assign the appropriate **Registry credential** from your private automation hub to the execution environment.


**Additional resources**

-  [Creating new credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#controller-create-credential)


