# 2. Ansible Automation Platform containerized installation
## 2.6. Configuring the inventory file
### 2.6.3. Setting registry_username and registry_password




When using the `registry_username` and `registry_password` variables for an online non-bundled installation, you need to create a new registry service account.

Registry service accounts are named tokens that can be used in environments where credentials will be shared, such as deployment systems.

**Procedure**

1. Go to [https://access.redhat.com/terms-based-registry/accounts](https://access.redhat.com/terms-based-registry/accounts) .
1. On the **Registry Service Accounts** page clickNew Service Account.
1. Enter a name for the account using only the allowed characters.
1. Optionally enter a description for the account.
1. ClickCreate.
1. Find the created account in the list by searching for your name in the search field.
1. Click the name of the account that you created.
1. Alternatively, if you know the name of your token, you can go directly to the page by entering the URL:


```
https://access.redhat.com/terms-based-registry/token/&lt;name-of-your-token&gt;
```


1. A **token** page opens, displaying a generated username (different from the account name) and a token.


1. If no token is displayed, clickRegenerate Token. You can also click this to generate a new username and token.

1. Copy the username (for example "1234567|testuser") and use it to set the variable `    registry_username` .
1. Copy the token and use it to set the variable `    registry_password` .


