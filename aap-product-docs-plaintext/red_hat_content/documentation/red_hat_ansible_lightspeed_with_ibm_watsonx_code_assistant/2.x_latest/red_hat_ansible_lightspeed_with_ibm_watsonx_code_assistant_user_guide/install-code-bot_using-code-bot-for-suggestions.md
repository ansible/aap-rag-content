# 6. Installing and configuring the Ansible code bot
## 6.1. Installing the Ansible code bot




Install the Ansible code bot to get code recommendations for your repositories, and then log in to the Ansible code bot dashboard to monitor and manage your repository scans.

**Procedure**

1. Log in to GitHub by using the account associated with your organization.
1. Go to the [Ansible code bot](https://github.com/apps/ansible-code-bot) GitHub app.
1. Select the Ansible repositories that you want the app to access:


-  **All repositories** : Provides access to read the metadata of all repositories.
-  **Only select repositories** : Provides access to read the metadata of only the repositories that you select.

1. Optional: If you selected **Only select repositories** in the previous step, select the repositories that you want the Ansible code bot to access from the **Select repositories** list.
1. Click **Install & Authorize** . A message is displayed that specifies the following permissions are granted automatically to the bot during installation:


- Read access to metadata
- Read and write access to code and pull requests

1. When prompted, log in to your Red Hat Single Sign-On account as an organization administrator.
1. Log in to the Ansible code bot dashboard:


1. On the **Authorize Ansible code bot** page, verify your account and repository permissions.
1. Click **Authorize Ansible** .

From the **Authorize Ansible code bot** page, the following actions occur:


- Ansible code bot verifies that you are a part of an organization that has an active subscription to Red Hat Ansible Automation Platform.
- GitHub requests read permissions to access the repositories associated with your account.




On successful authorization, you are logged in to Ansible code bot dashboard. The dashboard displays all your repositories that have the Ansible code bot installed along with their scan status.

