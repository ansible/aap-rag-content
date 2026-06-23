# Create a new application

When integrating an external web application with Ansible Automation Platform, the web application might need to create OAuth2 tokens on behalf of users of the web application.

## About this task

Creating an application with the Authorization Code grant type is the preferred way to do this for the following reasons:

- External applications can obtain a token for users, using their credentials.
- Compartmentalized tokens issued for a particular application, enables those tokens to be easily managed. For example, revoking all tokens associated with that application.

## Procedure

1.  From the navigation panel, select Access Management> (and then)OAuth Applications.
2.  Click Create OAuth application. The **Create Application** page opens.
3.  Enter the following details:


Name
(required) Enter a name for the application you want to create.

URL
(optional) Enter the URL of the external application. This link is added to the navigation panel for easy access. This setting is currently offered as a Technology Preview only.

Description
(optional) Include a short description for your application.

Organization
(required) Select an organization with which this application is associated.

Authorization grant type
(required) Select one of the grant types to use for the user to get tokens for this application. For more information, see [Application functions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication#ref-gw-application-functions "Several OAuth 2 utilities are available for authorization, token refresh, and revoke. You can specify the following grant types when creating an application:") for more information about grant types.

Client Type
(required) Select the level of security of the client device.

Redirect URIS
Provide a list of allowed URIs, separated by spaces. You need this if you specified the grant type to be **Authorization code**.

4.  Click Create OAuth application, or click Cancel to abandon your changes. The **Client ID** and **Client Secret** display in a window. This will be the only time the client secret will be shown.

Note:
The **Client Secret** is only created when the **Client type** is set to **Confidential**.

5.  Click the copy icon and save the client ID and client secret to integrate an external application with Ansible Automation Platform.

