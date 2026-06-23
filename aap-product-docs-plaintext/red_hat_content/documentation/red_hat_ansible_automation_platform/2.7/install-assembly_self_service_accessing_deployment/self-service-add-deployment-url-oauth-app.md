# Update the deployment URL
## Add the deployment URL to the OAuth Application

When you set up your OAuth application in Ansible Automation Platform before deploying Ansible automation portal, you added placeholder text for the `Redirect URIs` value.

### About this task

You must update this value using the URL from the deployed application so that you can run automation on Ansible automation portal from Ansible automation portal.

### Procedure

1.  Determine the `Redirect URI` from your OpenShift deployment:
1.  Open the URL for the deployment from the OpenShift console to display the sign-in page for Ansible automation portal.
![Open URL from OpenShift web console](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-topology-get-url.png)
2.  Copy the URL for the sign-in page for Ansible automation portal.
3.  To determine the `Redirect URI` value, append `/api/auth/rhaap/handler/frame` to the end of the deployment URL. For example, if the URL for the deployment is `https://my-automation-portal-project.mycluster.com`, then the `Redirect URI` value is `https://my-automation-portal-project.mycluster.com/api/auth/rhaap/handler/frame`.

2.  Update the `Redirect URIs` field in the OAuth application in Ansible Automation Platform:
1.  In a browser, open your instance of Ansible Automation Platform.
2.  Navigate to Access Management> (and then)OAuth Applications.
3.  In the list view, click the OAuth application you created.
4.  Replace the placeholder text in the `Redirect URIs` field with the value you determined from your OpenShift deployment.
5.  Click `Save` to apply the changes.

