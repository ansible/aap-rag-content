# Update the deployment URL

Complete the necessary post-installation configuration, including updating the OAuth application and setting up initial Role-Based Access Control (RBAC). You can then access and sign in to the portal.

## Add the deployment URL to the OAuth Application

When you set up your OAuth application in Ansible Automation Platform before deploying Ansible automation portal, you added placeholder text for the `Redirect URIs` value.

### About this task

You must update this value using the URL from the deployed application so that you can run automation on Ansible automation portal from Ansible automation portal.

### Procedure

1.  Determine the `Redirect URI` from your OpenShift deployment:
1.  Open the URL for the deployment from the OpenShift console to display the sign-in page for Ansible automation portal.
![Open URL from OpenShift web console](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/self-service-topology-get-url.png)
2.  Copy the URL for the sign-in page for Ansible automation portal.
3.  To determine the `Redirect URI` value, append `/api/auth/rhaap/handler/frame` to the end of the deployment URL. For example, if the URL for the deployment is `https://my-automation-portal-project.mycluster.com`, then the `Redirect URI` value is `https://my-automation-portal-project.mycluster.com/api/auth/rhaap/handler/frame`.

2.  Update the `Redirect URIs` field in the OAuth application in Ansible Automation Platform:
1.  In a browser, open your instance of Ansible Automation Platform.
2.  Navigate to Access Management> (and then)OAuth Applications.
3.  In the list view, click the OAuth application you created.
4.  Replace the placeholder text in the `Redirect URIs` field with the value you determined from your OpenShift deployment.
5.  Click `Save` to apply the changes.

## Sign in to Ansible automation portal

Log in to the deployed Ansible automation portal using your existing Ansible Automation Platform credentials. The portal uses these credentials for authentication.

### Before you begin

- You have configured an OAuth application in Ansible Automation Platform for Ansible automation portal.
- You have configured a user account in Ansible Automation Platform.

### Procedure

1.  In a browser, navigate to the URL for Ansible automation portal to open the sign-in page.
![Self-service sign-in page](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/self-service-sign-in-page.png)
2.  Click Sign In.
3.  The sign-in page for Ansible Automation Platform appears:
![Ansible Automation Platform sign-in page](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/rhaap-sign-in-page.png)
4.  Enter your Ansible Automation Platform credentials and click **Log in**.
5.  The Ansible automation portal web console opens.

If you are using custom or self-signed SSL certificates and when attempting to log in to Ansible automation portal, it displays the error:

`Login failed; caused by Error: Failed to send POST request: fetch failed`

This error indicates that Ansible automation portal cannot verify the SSL certificate from your Ansible Automation Platform instance.

To resolve this issue, configure Ansible automation portal to trust your custom CA certificate.

Note:

While you can disable SSL validation by setting `checkSSL: false` in the Helm chart configuration, this approach is not recommended for production environments as it reduces security. Instead, configure Ansible automation portal to trust your custom CA certificate.
