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






**Verification**

After the Ansible code bot is installed, it automatically scans the selected repositories that are in Jinja format. When the scanning is complete, the code bot generates an initial PR for each repository; the initial PR also contains the scan schedule configured to run weekly.


Perform the following tasks:

1. Review the initial PR for the suggested changes, and merge the PR.

After you merge the initial PR, the configured scan schedule is triggered, and the subsequent repository scans are performed weekly.

Note
If you do not merge the initial PR, the weekly scan schedule is not triggered and the Ansible code bot dashboard displays the repositories without any associated scan history.



The following illustration is an example of an initial PR being created:

![Ansible code bot settings](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/7d2a7878be12d37483bd485419467f7a/code-bot-initial-pr.png)



1. Optional: If required, you can [manually scan your repositories](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#manually-scan-repo_using-code-bot-for-suggestions) or [change the scan schedule to a daily or monthly cadence](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#configure-repo-scan_using-code-bot-for-suggestions) .
1. Modify scanned repositories by [adding repositories or removing existing repositories from being scanned](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#add-remove-repo-from-scans_using-code-bot-for-suggestions) .


**Additional resources**

-  [Troubleshooting Ansible code bot errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#ref-troubleshooting-code-bot_troubleshooting-lightspeed)


