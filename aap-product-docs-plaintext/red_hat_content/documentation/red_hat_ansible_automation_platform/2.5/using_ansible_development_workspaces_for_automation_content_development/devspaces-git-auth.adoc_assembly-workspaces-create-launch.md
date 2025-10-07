# 3. Creating and launching an Ansible development workspace
## 3.1. Authentication
### 3.1.1. Configuring Git personal access token authentication




You must create a personal access token (PAT) in your Git source control manager (SCM), and add it to OpenShift Dev Spaces to enable access to your repositories from your Ansible development workspace.

**Procedure**

1. Create a personal access token in your Git SCM and save it.


- See [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) in the GitHub documentation.
- See [Personal access tokens](https://docs.gitlab.com/user/profile/personal_access_tokens) in the Gitlab documentation.

1. In a browser, navigate to the OpenShift Dev Spaces dashboard provided by your administrator, and log in.
1. Expand the dropdown menu under your login name and select **User Preferences** .
1. Select **Personal Access Tokens** .
1. Click **+Add Token** .
1. Complete the **Add Personal Access Token** form:


-  **Token Name** : Enter a name for your token
-  **Token** : Enter your personal access token for your Git repository.

1. Click **Add** to save the personal access token.


