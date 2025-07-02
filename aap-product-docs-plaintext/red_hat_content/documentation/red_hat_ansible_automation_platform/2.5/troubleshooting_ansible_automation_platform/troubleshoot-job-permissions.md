# 6. Jobs
## 6.4. Issue - Jobs in private automation hub are failing with "denied: requested access to the resource is denied, unauthorized: Insufficient permissions" error message




Jobs are failing with the error message "denied: requested access to the resource is denied, unauthorized: Insufficient permissions" when using an execution environment in private automation hub.

This issue happens when your private automation hub is protected with a password or token and the registry credential is not assigned to the execution environment.

**Procedure**

1. Go to automation controller.
1. From the navigation panel, selectAdministration→Execution Environments.
1. Click the execution environment assigned to the job template that is failing.
1. ClickEdit.
1. Assign the appropriate **Registry credential** from your private automation hub to the execution environment.


**Additional resources**

- For information about creating new credentials in automation controller, see [Creating new credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#controller-create-credential) in _Using automation execution_ .


