# 4. Configuring template RBAC and display logic
## 4.1. Role-based access control (RBAC)




The template type determines where you must configure user permissions.

-  **Auto-generated templates** : Permissions synchronize from Ansible Automation Platform. Users must have permissions on the underlying Ansible Automation Platform job template. For more information, see [Setting up initial RBAC rules in self-service automation portal](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_self-service_automation_portal/index#self-service-initial-rbac-setup_self-service-accessing-deployment) .
-  **Custom templates** : You must explicitly configure permissions within the self-service automation portal. Users must also have permission to run the associated job templates in Ansible Automation Platform. For more information see, [Setting up RBAC for custom self-service templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_self-service_automation_portal/index#self-service-set-up-rbac_self-service-rbac) .


