# 3. Configuring access to external applications with token-based authentication
## 3.1. Manage OAuth applications
### 3.1.2. Creating a new application

When integrating an external web application with Ansible Automation Platform, the web application might need to create OAuth2 tokens on behalf of users of the web application.

Creating an application with the Authorization Code grant type is the preferred way to do this for the following reasons:

- External applications can obtain a token for users, using their credentials.
- Compartmentalized tokens issued for a particular application, enables those tokens to be easily managed. For example, revoking all tokens associated with that application.

**Procedure**

1. From the navigation panel, select Access Management → OAuth Applications.

2. Click Create OAuth application. The **Create Application** page opens.

3. Enter the following details:



Name
(required) Enter a name for the application you want to create.

URL
(optional) Enter the URL of the external application. This link is added to the navigation panel for easy access. This setting is currently offered as a Technology Preview only.

Description
(optional) Include a short description for your application.

Organization
(required) Select an organization with which this application is associated.

Authorization grant type
(required) Select one of the grant types to use for the user to get tokens for this application. For more information, see [Application functions](#ref-gw-application-functions "3.1.1.1.&nbsp;Application functions") for more information about grant types.

Client Type
(required) Select the level of security of the client device.

Redirect URIS
Provide a list of allowed URIs, separated by spaces. You need this if you specified the grant type to be **Authorization code**.

4. Click Create OAuth application, or click Cancel to abandon your changes.

The **Client ID** and **Client Secret** display in a window. This will be the only time the client secret will be shown.


Note
The **Client Secret** is only created when the **Client type** is set to **Confidential**.

5. Click the copy icon and save the client ID and client secret to integrate an external application with Ansible Automation Platform.

