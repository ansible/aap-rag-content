# Create an OAuth application

To use the Helm chart to deploy Ansible automation portal, you must have set up an OAuth application on your Ansible Automation Platform instance.

## About this task

However, you cannot run automation on your Ansible Automation Platform instance until you have deployed your Ansible automation portal Helm chart, because the OAuth configuration requires the URL for your deployment.

Create the OAuth Application on your Ansible Automation Platform instance, using a placeholder name for the deployment URL.

After deploying Ansible automation portal, you must [replace the placeholder value with a URL derived from your deployment URL](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_accessing_deployment#self-service-add-deployment-url-oauth-app "When you set up your OAuth application in Ansible Automation Platform before deploying Ansible automation portal, you added placeholder text for the Redirect URIs value.") in your OAuth application.

The steps below describe how to create an OAuth Application in the Ansible Automation Platform Platform console.

## Procedure

1. Open your Ansible Automation Platform instance in a browser and log in.
2. Navigate to Access Management> (and then)OAuth Applications.
3. Click **Create OAuth Application**.
4. Complete the fields in the form.   - **Name**: Add a name for your application.
- **Organization**: Choose the organization.
- **Authorization grant type**: Choose `Authorization code`.
- **Client type**: choose `Confidential`.
- **Redirect URIs**: Add placeholder text for the deployment URL (for example `<https://example.com>`).
- **PKCE required**: When selected, this option requires clients to use PKCE during the authorization code flow. PKCE prevents authorization code interception attacks and is required by the OAuth 2.1 specification. Select this for any OAuth application whose clients support OAuth 2.1 or for applications which are needed to enforce this check. For example, select this option when creating an OAuth application to enable the MCP Server for Ansible Automation Platform.

*Figure 1. Create OAuth application*
![User interface for Create OAuth application in Ansible Automation Platform](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/create-oauth-application.png)

5. Click **Create OAuth application**. The **Application information** popup displays the `clientId` and `clientSecret` values.

6. Copy the `clientId` and `clientSecret` values and save them. These values are used in an OpenShift secret for Ansible Automation Platform authentication.

