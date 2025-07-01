# 5. Migrating Red Hat Ansible Automation Platform to Red Hat Ansible Automation Platform Operator
## 5.4. Post migration cleanup
### 5.4.1. Deleting Instance Groups post migration




You can use the following procedure to delete any unnecessary instance groups after you have successfully migrated.

Note
If you did not create an administrator password during migration, one was automatically created for you. To locate this password, go to your project, selectWorkloads→Secretsand open controller-admin-password. From there you can copy the password and paste it into the Red Hat Ansible Automation Platform password field.



**Procedure**

1. Log in to Red Hat Ansible Automation Platform as the administrator with the password you created during migration.
1. SelectAutomation Execution→Infrastructure→Instance Groups.
1. Select all Instance Groups except `    controlplane` and `    default` .
1. ClickDelete.


