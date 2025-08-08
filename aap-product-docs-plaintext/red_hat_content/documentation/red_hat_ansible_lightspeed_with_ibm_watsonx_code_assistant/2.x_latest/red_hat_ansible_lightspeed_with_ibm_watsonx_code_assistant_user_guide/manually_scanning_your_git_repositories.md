# 6. Installing and configuring the Ansible code bot
## 6.3. Managing repository scans
### 6.3.1. Manually scanning your Git repositories




You can manually scan your Git repositories if you did not set up a scanning schedule for your Ansible code bot or if you do not want to wait for the next scheduled scan. If you manually scan your repository, and no pull request was created, it is likely so because a duplicate pull request already exists. You can scan your repository from both the Ansible code bot dashboard and GitHub.

#### 6.3.1.1. Manually scanning the repository from the Ansible code bot dashboard




You can manually scan your Git repositories if you did not set up a scanning schedule for your Ansible code bot or if you do not want to wait for the next scheduled scan.

**Procedure**

1. Log in to the [Ansible code bot dashboard](https://bot.ai.ansible.redhat.com/console) .

The **Repositories** list displays a list of repositories that you selected for scanning.

Note
If you do not see your repository in the **Repositories** list, you can add it for scanning. For more information, see [Adding or removing repositories from the Ansible code bot](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#add-remove-repo-from-scans_using-code-bot-for-suggestions) .




1. To start a manual scan of your repository, click the **Ellipsis** icon (![Ellipsis icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/fdb39922da186178fe9909a1a5cde1cc/ansible-code-bot-dashboard-kebab-icon.png)
) beside the repository that you want to scan and select **Scan now** .
1. Click **Refresh** to view the status of the scan job.
1. To view more details about your repository scans, click the **Ellipsis** icon (![Ellipsis icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/fdb39922da186178fe9909a1a5cde1cc/ansible-code-bot-dashboard-kebab-icon.png)
) beside the repository and select **View scan history** .

The repository’s scan history is displayed along with the scan start time, scan status, type of scan (scheduled or manual), link to the pull request if it was created, and the log message if the scan failed.


1. To view your repository on GitHub, click the **Ellipsis** icon (![Ellipsis icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/fdb39922da186178fe9909a1a5cde1cc/ansible-code-bot-dashboard-kebab-icon.png)
) beside the repository and select **View repository** .


#### 6.3.1.2. Manually scanning the repository from GitHub




You can manually scan your Git repositories from GitHub if you did not set up a scanning schedule for your Ansible code bot or if you do not want to wait for the next scheduled scan.

**Procedure**

1. In GitHub, go to the main page of the repository that you want to scan.
1. To modify the repository settings, click the **Settings** icon beside the **About** area.
1. In the **Topics** field, enter the keyword topic **ansible-code-bot-scan** to the repository.

The following illustration shows the keyword topic for starting a manual scan:

![Ansible code bot settings](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/1c089735ab28d4d5a1e3a8be24bed72b/lightspeed-ansible-code-bot-manual-trigger-setting.png)



1. Click **Save changes** .

Based on the repository webhook event, Ansible code bot starts a manual scan of your repository. If the avoid duplicate pull requests condition is not met, then the manual scan results in a new pull request with all the necessary Ansible code bot recommendations.




**Additional resources**

-  [Troubleshooting Ansible code bot errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#ref-troubleshooting-code-bot_troubleshooting-lightspeed)


