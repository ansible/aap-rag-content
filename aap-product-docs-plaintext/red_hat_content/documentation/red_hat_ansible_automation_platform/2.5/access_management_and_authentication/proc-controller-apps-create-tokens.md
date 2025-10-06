# 3. Configuring access to external applications with token-based authentication
## 3.2. Adding tokens




You can view a list of users that have tokens to access an application by selecting the **Tokens** tab in the **OAuth Applications** details page.

Note
You can only create OAuth 2 Tokens for your own user, which means you can only configure or view tokens from your own user profile.



When authentication tokens have been configured, you can select the application to which the token is associated and the level of access that the token has.

**Procedure**

1. From the navigation panel, selectAccess Management→Users.
1. Select the username for your user profile to configure OAuth 2 tokens.
1. Select the **Tokens** tab.

When no tokens are present, the **Tokens** screen prompts you to add them.


1. ClickCreate tokento open the **Create Token** window.
1. Enter the following details:


1. ClickCreate token, or clickCancelto abandon your changes.

The Token information is displayed with **Token** and **Refresh Token** information, and the expiration date of the token. This will be the only time the token and refresh token will be shown. You can view the token association and token information from the list view.


1. Click the copy icon and save the token and refresh token for future use.


**Verification**

You can verify that the application now shows the user with the appropriate token using the Tokens tab on the Applications details page.


1. From the navigation panel, selectAccess Management→OAuth Applications.
1. Select the application you want to verify from the **Applications** list view.
1. Select the **Tokens** tab.

Your token should be displayed in the list of tokens associated with the application you chose.




**Additional resources**

-  [Token and session management](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#ref-controller-token-session-management)


