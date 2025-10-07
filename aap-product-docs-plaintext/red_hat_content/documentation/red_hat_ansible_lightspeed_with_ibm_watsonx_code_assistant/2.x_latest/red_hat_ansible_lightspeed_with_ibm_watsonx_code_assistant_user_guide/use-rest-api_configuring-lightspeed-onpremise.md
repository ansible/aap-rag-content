# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 3.3.8. Using the Ansible Lightspeed REST API




As the platform administrator, you can configure and use the Ansible Lightspeed REST API to build a custom automation development and tooling workflow outside of VS Code. For information about the Ansible Lightspeed REST API, see [Ansible AI Connect. 1.0.0 (v1)](https://developers.redhat.com/api-catalog/api/ansible-lightspeed) in the API catalog.

Note
The Ansible Lightspeed REST API is available for Ansible Automation Platform 2.5 and later.



**Prerequisite**

- Ensure that you are using the Red Hat Ansible Automation Platform operator patch version 2.5-20250305.9 or later and Red Hat Ansible Lightspeed operator version 2.5.250225 or later.


**Procedure**

1. Select the platform user for whom you want to grant REST API access.

You can select an existing user or create a platform user in the Red Hat Ansible Automation Platform. For the procedure, see the [Creating a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_ansible_automation_platform/assembly-gs-platform-admin#proc-gs-platform-admin-create-user) section of _Getting started with Ansible Automation Platform_ .


1. Verify that you can log in to the Ansible Lightspeed portal for on-premise deployment ( `    https://&lt;lightspeed_route&gt;/` ) as the platform user you selected or created, and then log out.
1. Create a token for the platform user:


1. Log in to the Ansible Lightspeed portal for on-premise deployment ( `        https://&lt;lightspeed_route&gt;/admin` ) as an administrator by using the following credentials:


- Username: **admin**
- Password: The secret that is named as `            &lt;lightspeed-custom-resource-name&gt;-admin-password` in the Red Hat OpenShift Container Platform cluster namespace where Red Hat Ansible Lightspeed is deployed.

1. On the Django administration window, select **Users** from the Users area. A list of users is displayed.
1. Verify that the platform user is listed in the **Users** list.
1. From the Django Oauth toolkit area, selectAccess tokens→Add.
1. Provide the following information and click **Save** :


-  **User** : Use the magnifying glass icon to search and select the newly-created or existing user for whom you want to grant API access.
-  **Token** : Specify a token for the user. Copy this token for later use.
-  **Id token** : Select the token ID.
-  **Application** : Select **Ansible Lightspeed for VS Code** .
-  **Expires** : Select the date and time when you want the token to expire.
-  **Scope** : Specify the scope as **read write** .

An access token is created for the user.



1. Log out from the Ansible Lightspeed portal for on-premise deployment.

1. Make a direct call to the Ansible Lightspeed REST API by specifying the newly-created token in the authorization header:


```
curl -H "Authorization: Bearer &lt;token&gt;"    https://&lt;lightspeed_route&gt;/api/v1/me/
```




