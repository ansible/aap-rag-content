# 4. Preparing the containerized Ansible Automation Platform installation
## 4.7. Setting registry_username and registry_password

Create a new registry service account on the Red Hat Customer Portal to generate a named token and username. Use these credentials to set the `registry_username` and `registry_password` variables, which are essential for supporting online non-bundled installations in environments where credentials must be shared, such as deployment systems.

**Procedure**

1. Go to <https://access.redhat.com/terms-based-registry/accounts>.

2. On the **Registry Service Accounts** page click New Service Account.

3. Enter a name for the account using only the allowed characters.

4. Optionally enter a description for the account.

5. Click Create.

6. Find the created account in the list by searching for your name in the search field.

7. Click the name of the account that you created.

8. Alternatively, if you know the name of your token, you can go directly to the page by entering the URL:

https://access.redhat.com/terms-based-registry/token/<name-of-your-token>

9. A **token** page opens, displaying a generated username (different from the account name) and a token.


1. If no token is displayed, click Regenerate Token. You can also click this to generate a new username and token.

10. Copy the username (for example "1234567|testuser") and use it to set the variable `registry_username`.

11. Copy the token and use it to set the variable `registry_password`.

