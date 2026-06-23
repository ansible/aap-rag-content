# Integrate third-party secret management systems
## Thycotic Secret Server

Thycotic Secret Server is a secrets management system that enables secure storage and retrieval of sensitive information such as passwords, API keys, and certificates.

Give the following metadata to configure your lookup When you select **Thycotic Secrets Server** as **Credential Type**:

- **Secret Server URL** (required): give the URL used for communicating with the Thycotic Secrets Server management system
- **Username** (required): specify the authenticated user for this service
- **Domain**: give the (application) user domain
- **Password** (required): give the password associated with the user

## Configuring a `GitHub App Installation Access Token Lookup`

Learn how to configure a `GitHub App Installation Access Token Lookup` credential in automation controller.

### About this task

With this plugin you can use a private GitHub App RSA key as a credential input source to pull access tokens from GitHub App installations. Platform gateway uses existing GitHub authorization from organizations' GitHub repositories.

For more information, see [Generating an installation access token for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app).

### Procedure

1.  Create a lookup credential that stores your secrets. For more information, see [Create new credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_create_credential "Learn how to create new credentials in Automation controller.").
2.  Select **GitHub App Installation Access Token Lookup** for **Credential type**, and enter the following attributes to properly configure your lookup:

- **GitHub App ID**: Enter the App ID provided by your instance of GitHub, this is what is used to authenticate.
- **GitHub App Installation ID**: Enter the ID of the application into your target organization where the access token is scoped. You must set it up to have access to your target repository.
- **RSA Private Key**: Enter the generated private key that your GitHub instance generated. You can get it from the GitHub App maintainer within GitHub. For more information, see [Managing private keys for GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps).

3.  Click Create credential to confirm and save the credential. The following is an example of a configured **GitHub App Installation Access Token Lookup** credential:

![GitHub App token lookup credential](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/credentials-create-github-app-lookup-credential.png)

4.  Create a target credential that searches for the lookup credential. To use your lookup in a private repository, select **Source Control** as your **Credential type**. Enter the following attributes to properly configure your target credential:

- **Username**: Enter the username `x-access-token`.

- **Password**: Click the ![Link](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftkey.png) icon for managing external credentials in the input field. You are prompted to set the input source to use to retrieve your secret information. This is the lookup credential that you have already created. ![Target credential secret info](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/credentials-github-app-target-secret-info.png)

5.  Enter an optional description for the metadata requested and click Finish.
6.  Click Create credential to confirm and save the credential.
7.  Verify both your lookup credential and your target credential are now available on the **Credentials** list view. To use the target credential in a project, create a project and enter the following information:

- **Name**: Enter the name for your project.

- **Organization**: Select the name of the organization from the drop-down menu..

- **Execution environment**: Optionally select an execution environment, if applicable.

- **Source control type**: If you are syncing with a private repository, select **Git** for your source control. The **Type Details** view opens for additional input. Enter the following information:

- **Source control URL**: Enter the URL of the private repository you want to access. The other related fields pertaining to **branch/tag/commit** and **refspec** are not relevant for use with a lookup credential.

- **Source control credential**: Select the target credential that you have already created. The following is an example of a configured target credential in a project:

![GitHub App project](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/project-create-git-github-app.png)

8.  Click Create project and the project sync automatically starts. The project **Details** tab displays the progress of the job:
![Project sync GitHub App](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/project-sync-github-app.png)

If your project sync fails, you might have to manually re-enter `<https://api.github.com>` in the **GitHub API endpoint URL** field from Step 2 and re-run your project sync.
