# 9. Ansible Automation Platform Resource Operator
## 9.3. Connecting Resource Operator to platform gateway




To connect Resource Operator with platform gateway you must create a Kubernetes secret with the connection information for your automation controller instance.

Note
You can only create OAuth 2 Tokens for your own user through the API or UI, which means you can only configure or view tokens from your own user profile.



**Procedure**

To create an OAuth2 token for your user in the platform gateway UI:


1. Log in to Red Hat OpenShift Container Platform.
1. In the navigation panel, selectAccess Management→Users.
1. Select the username you want to create a token for.
1. SelectTokens→Automation Execution
1. ClickCreate Token.
1. You can leave **Applications** empty. Add a description and select **Read** or **Write** for the **Scope** .


Note
Make sure you provide a valid user when creating tokens. Otherwise, you get an error message that you tried to issue the command without either specifying a user, or supplying a username that does not exist.



