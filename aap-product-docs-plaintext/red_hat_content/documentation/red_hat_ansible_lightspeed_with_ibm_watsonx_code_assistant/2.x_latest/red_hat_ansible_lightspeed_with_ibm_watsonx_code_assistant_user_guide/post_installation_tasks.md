# 6. Installing and configuring the Ansible code bot
## 6.1. Installing the Ansible code bot
### 6.1.1. Post-installation tasks




After the Ansible code bot is installed, it automatically scans the selected repositories that are in Jinja format. When the scanning is complete, the code bot generates an initial PR for each repository; the initial PR also contains the scan schedule configured to run weekly.

**Procedure**

1. Review the initial PR for the suggested changes, and merge the PR.

After you merge the initial PR, the configured scan schedule is triggered, and the subsequent repository scans are performed weekly.

Note
If you do not merge the initial PR, the weekly scan schedule is not triggered and the Ansible code bot dashboard displays the repositories without any associated scan history.



The following illustration is an example of an initial PR being created:

![Ansible code bot settings](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/7d2a7878be12d37483bd485419467f7a/code-bot-initial-pr.png)



1. Optional: If required, you can [manually scan your repositories](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#manually-scan-repo_using-code-bot-for-suggestions) or [change the scan schedule to a daily or monthly cadence](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#configure-repo-scan_using-code-bot-for-suggestions) .
1. Modify scanned repositories by [adding repositories or removing existing repositories from being scanned](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#add-remove-repo-from-scans_using-code-bot-for-suggestions) .


**Additional resources**

-  [Troubleshooting Ansible code bot errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#troubleshooting-code-bot_troubleshooting-lightspeed)


