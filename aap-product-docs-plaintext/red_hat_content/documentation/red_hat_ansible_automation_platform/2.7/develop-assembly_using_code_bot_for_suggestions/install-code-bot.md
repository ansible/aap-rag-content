# Install and configure the Ansible code bot
## Install the Ansible code bot

Install the Ansible code bot to get code recommendations for your repositories, and then log in to the Ansible code bot dashboard to monitor and manage your repository scans.

### Procedure

1.  Log in to GitHub by using the account associated with your organization.
2.  Go to the [Ansible code bot](https://github.com/apps/ansible-code-bot) GitHub app.
3.  Select the Ansible repositories that you want the app to access:

- **All repositories**: Provides access to read the metadata of all repositories.
- **Only select repositories**: Provides access to read the metadata of only the repositories that you select.

4.  Optional: If you selected **Only select repositories** in the previous step, select the repositories that you want the Ansible code bot to access from the **Select repositories** list.
5.  Click **Install & Authorize**. A message is displayed that specifies the following permissions are granted automatically to the bot during installation:

- Read access to metadata
- Read and write access to code and pull requests

6.  When prompted, log in to your Red Hat Single Sign-On account as an organization administrator.
7.  Log in to the Ansible code bot dashboard:
1.  On the **Authorize Ansible code bot** page, verify your account and repository permissions.
2.  Click **Authorize Ansible**. From the **Authorize Ansible code bot** page, the following actions occur:

- Ansible code bot verifies that you are a part of an organization that has an active subscription to Red Hat Ansible Automation Platform.

- GitHub requests read permissions to access the repositories associated with your account. On successful authorization, you are logged in to Ansible code bot dashboard. The dashboard displays all your repositories that have the Ansible code bot installed along with their scan status.

### Results

After the Ansible code bot is installed, it automatically scans the selected repositories that are in Jinja format. When the scanning is complete, the code bot generates an initial PR for each repository; the initial PR also contains the scan schedule configured to run weekly.

Perform the following tasks:

1. Review the initial PR for the suggested changes, and merge the PR. After you merge the initial PR, the configured scan schedule is triggered, and the subsequent repository scans are performed weekly.

Note:
If you do not merge the initial PR, the weekly scan schedule is not triggered and the Ansible code bot dashboard displays the repositories without any associated scan history.

The following illustration is an example of an initial PR being created:


![Ansible code bot settings](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/code-bot-initial-pr.png)

2. Optional: If required, you can manually scan your repositories or change the scan schedule to a daily or monthly cadence.

3. Modify the scanned repositories.

