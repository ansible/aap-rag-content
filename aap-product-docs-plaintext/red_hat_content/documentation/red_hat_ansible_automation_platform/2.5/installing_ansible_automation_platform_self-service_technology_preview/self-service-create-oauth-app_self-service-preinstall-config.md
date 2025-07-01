# 3. Pre-installation configuration
## 3.1. Creating an OAuth application




To use the Helm chart to deploy self-service technology preview, you must have set up an OAuth application on your Ansible Automation Platform instance. However, you cannot run automation on your Ansible Automation Platform instance until you have deployed your self-service technology preview Helm chart, because the OAuth configuration requires the URL for your deployment.

Create the OAuth Application on your Ansible Automation Platform instance, using a placeholder name for the deployment URL.

After deploying self-service technology preview, you must [replace the placeholder value with a URL derived from your deployment URL](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_ansible_automation_platform_self-service_technology_preview/index#self-service-add-deployment-url-oauth-app_self-service-accessing-deployment) in your OAuth application.

The steps below describe how to create an OAuth Application in the Ansible Automation Platform Platform console.

**Procedure**

1. Open your Ansible Automation Platform instance in a browser and log in.
1. Navigate toAccess Management→OAuth Applications.
1. Click **Create OAuth Application** .
1. Complete the fields in the form.


-  **Name** : Add a name for your application.
-  **Organization** : Choose the organization.
-  **Authorization grant type** : Choose `        Authorization code` .
-  **Client type** : choose `        Confidential` .
-  **Redirect URIs** : Add placeholder text for the deployment URL (for example `        https//:example.com` ).

![Create OAuth application](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/828fab2808e2881822da27c48fcaf96e/self-service-create-oauth-app.png)




1. Click **Create OAuth application** .

The **Application information** popup displays the `    clientId` and `    clientSecret` values.


1. Copy the `    clientId` and `    clientSecret` values and save them.

These values are used in an OpenShift secret for Ansible Automation Platform authentication.




