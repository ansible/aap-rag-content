# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 3.3.9. Monitoring your Red Hat Ansible Lightspeed on-premise deployment




After the Red Hat Ansible Lightspeed on-premise deployment is successful, use the following procedure to monitor the metrics on an API endpoint `/metrics` .

**Procedure**

1. Create a **system auditor** user:


1. Create a user with a **system auditor** role in the Red Hat Ansible Automation Platform. For the procedure, see the [Creating a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_ansible_automation_platform/assembly-gs-platform-admin#proc-gs-platform-admin-create-user) section of _Getting started with Ansible Automation Platform_ .
1. Verify that you can log in to the Ansible Lightspeed portal for on-premise deployment ( `        https://&lt;lightspeed_route&gt;/` ) as the newly-created system auditor user, and then log out.

1. Create a token for the **system auditor** user:


1. Log in to the Ansible Lightspeed portal for on-premise deployment ( `        https://&lt;lightspeed_route&gt;/admin` ) as an administrator by using the following credentials:


- Username: **admin**
- Password: The secret that is named as `            &lt;lightspeed-custom-resource-name&gt;-admin-password` in the Red Hat OpenShift Container Platform cluster namespace where Red Hat Ansible Lightspeed is deployed.

1. On the Django administration window, select **Users** from the Users area. A list of users is displayed.
1. Verify that the user with the system auditor role is listed in the **Users** list.
1. From the Django Oauth toolkit area, selectAccess tokens→Add.
1. Provide the following information and click **Save** :


-  **User** : Use the magnifying glass icon to search and select the user with the system auditor role.
-  **Token** : Specify a token for the user. Copy this token for later use.
-  **Id token** : Select the token ID.
-  **Application** : Select **Ansible Lightspeed for VS Code** .
-  **Expires** : Select the date and time when you want the token to expire.
-  **Scope** : Specify the scope as **read write** .

An access token is created for the user with a system auditor role.



1. Log out from the Ansible Lightspeed portal for on-premise deployment.

1. Monitor your Red Hat Ansible Lightspeed on-premise deployment, by using the authorization token of the user with the system auditor role, to access the metrics endpoint `    https://&lt;lightspeed_route&gt;/metrics` .


