# Create a new application
## Associate tokens with applications

You can view a list of users that have tokens to access an application by selecting the **Tokens** tab in the **OAuth Applications** details page.

### About this task

Note:

You can only create OAuth 2 Tokens for your own user, which means you can only configure or view tokens from your own user profile.

When authentication tokens have been configured, you can select the application to which the token is associated and the level of access that the token has.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  Select the username for your user profile to configure OAuth 2 tokens.
3.  Select the **Tokens** tab. When no tokens are present, the **Tokens** screen prompts you to add them.

4.  Click Create token to open the **Create Token** window.
5.  Enter the following details:


Application
Enter the name of the application with which you want to associate your token. Alternatively, you can search for it by clicking Browse. This opens a separate window that enables you to choose from the available options. Select **Name** from the filter list to filter by name if the list is extensive.

Note:
To create a Personal Access Token (PAT) that is not linked to any application, leave the Application field blank.

Description
(optional) Provide a short description for your token.

Scope
(required) Specify the level of access you want this token to have. The scope of an OAuth 2 token can be set as one of the following:

- **Write**: Allows requests sent with this token to add, edit and delete resources in the system.
- **Read**: Limits actions to read only. Note that the write scope includes read scope.

6.  Click Create token, or click Cancel to abandon your changes. The Token information is displayed with **Token** and **Refresh Token** information, and the expiration date of the token. This will be the only time the token and refresh token will be shown. You can view the token association and token information from the list view.

7.  Click the copy icon and save the token and refresh token for future use.

### Results

You can verify that the application now shows the user with the appropriate token by using the **Tokens** tab on the Applications details page.

1. From the navigation panel, select Access Management> (and then)OAuth Applications.

2. Select the application you want to verify from the **Applications** list view.

3. Select the **Tokens** tab. Your token should be displayed in the list of tokens associated with the application you chose.

