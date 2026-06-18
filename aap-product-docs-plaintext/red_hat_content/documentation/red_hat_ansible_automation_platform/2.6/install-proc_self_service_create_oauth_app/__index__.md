# Create an OAuth application

To use the Helm chart to deploy Ansible automation portal, you must have set up an OAuth application on your Ansible Automation Platform instance.

## About this task

However, you cannot run automation on your Ansible Automation Platform instance until you have deployed your Ansible automation portal Helm chart, because the OAuth configuration requires the URL for your deployment.

Create the OAuth Application on your Ansible Automation Platform instance, using a placeholder name for the deployment URL.

After deploying Ansible automation portal, you must [replace the placeholder value with a URL derived from your deployment URL](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_self_service_accessing_deployment#self-service-add-deployment-url-oauth-app "When you set up your OAuth application in Ansible Automation Platform before deploying Ansible automation portal, you added placeholder text for the Redirect URIs value.") in your OAuth application.

The steps below describe how to create an OAuth Application in the Ansible Automation Platform Platform console.

## Procedure

1.  Open your Ansible Automation Platform instance in a browser and log in.
2.  Navigate to Access Management> (and then)OAuth Applications.
3.  Click **Create OAuth Application**.
4.  Complete the fields in the form.   - **Name**: Add a name for your application.
- **Organization**: Choose the organization.
- **Authorization grant type**: Choose `Authorization code`.
- **Client type**: choose `Confidential`.
- **Redirect URIs**: Add placeholder text for the deployment URL (for example `<https://example.com>`).
![Create OAuth application](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/self-service-create-oauth-app.png)

5.  Click **Create OAuth application**. The **Application information** popup displays the `clientId` and `clientSecret` values.

6.  Copy the `clientId` and `clientSecret` values and save them. These values are used in an OpenShift secret for Ansible Automation Platform authentication.

## Enable Oauth token creation for external users

Ansible automation portal uses Ansible Automation Platform or authentication and as an OAuth provider.

### About this task

You must enable OAuth token creation in Ansible Automation Platform so that users can authenticate with the platform from Ansible automation portal.

Note:

Users who do not have permission to log in to Ansible Automation Platform cannot log in to Self-service portal, because Ansible Automation Platform provides the OAuth tokens. Therefore, a user who is removed from an external IdP (for example LDAP, SAML, Azure) can no longer log into Ansible Automation Platform or Ansible automation portal. This prevents potential external token issues. For more information, refer to the [Manage OAuth2 token creation for external users](/documentation/en-us/red_hat_ansible_automation_platform/2.6/configure-con_gw_manage_oauth2_external_users#gw-manage-oauth2-external-users "Configure your platform settings to enable OAuth2 token creation for external users. Allowing users authenticated via LDAP, SAML, or SSO to generate tokens prevents 403 Forbidden errors and helps ensure they maintain programmatic API access.") section of[Configure central authentication for Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication "Configure authentication methods such as LDAP or SAML to simplify the user login experience. Providing the correct connection details for your chosen identity provider helps ensure seamless and secure access to Ansible Automation Platform.").

### Procedure

1.  In a browser, log in to your Ansible Automation Platform instance as a user with admin privileges.
2.  In the navigation pane, select Settings> (and then)Platform gateway.
3.  Locate the **Allow external users to create OAuth2 tokens** setting.
4.  Enable **Allow external users to create OAuth2 tokens** if it is not already enabled:
1.  Click Edit platform gateway settings.
2.  Set **Allow external users to create OAuth2 tokens** to **Enabled**.
![Allow external users to create OAuth2 tokens setting](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/self-service-enable-external-oauth.png)
3.  Click Save platform gateway settings to save your updates and return to the **Platform gateway settings** page.
5.  In the **Platform gateway settings** page, verify that the **Allow external users to create OAuth2 tokens** setting is enabled.

## Generate an API token for Ansible Automation Platform authentication

You must create an API token in Ansible Automation Platform. The token is used in an OpenShift secret for Ansible Automation Platform authentication.

### Procedure

1.  Log in to your instance of Ansible Automation Platform as a user with Ansible Automation Platform administrator privileges.
2.  Navigate to Access Management> (and then)API Tokens to display the API Tokens page.
3.  Click Create API Token.
4.  Add a description and select your OAuth application.
5.  In the Scope menu, select `Write`.

![Create API Token dialog showing the Scope set to Write](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/self-service-generate-oauth-token.png)

6.  Click Create Token to generate the token.
7.  Save the new token.
The token is used in an OpenShift secret that is fetched by the Helm chart.
