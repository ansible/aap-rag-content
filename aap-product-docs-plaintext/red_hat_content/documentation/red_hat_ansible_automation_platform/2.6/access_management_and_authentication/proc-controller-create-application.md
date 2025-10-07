# 3. Configuring access to external applications with token-based authentication
## 3.1. Manage OAuth applications
### 3.1.2. Creating a new application




When integrating an external web application with Ansible Automation Platform, the web application might need to create OAuth2 tokens on behalf of users of the web application.

Creating an application with the Authorization Code grant type is the preferred way to do this for the following reasons:

- External applications can obtain a token for users, using their credentials.
- Compartmentalized tokens issued for a particular application, enables those tokens to be easily managed. For example, revoking all tokens associated with that application.


**Procedure**

1. From the navigation panel, selectAccess Management→OAuth Applications.
1. ClickCreate OAuth application. The **Create Application** page opens.
1. Enter the following details:


1. ClickCreate OAuth application, or clickCancelto abandon your changes.

The **Client ID** and **Client Secret** display in a window. This will be the only time the client secret will be shown.

Note
The **Client Secret** is only created when the **Client type** is set to **Confidential** .




1. Click the copy icon and save the client ID and client secret to integrate an external application with Ansible Automation Platform.


