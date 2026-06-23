# Install and configure the Ansible code bot
## Manually scan the repository from GitHub

You can manually scan your Git repositories from GitHub if you did not set up a scanning schedule for your Ansible code bot or if you do not want to wait for the next scheduled scan.

### About this task

If you manually scan your repository, and no pull request was created, it is likely so because a duplicate pull request already exists.

### Procedure

1.  In GitHub, go to the main page of the repository that you want to scan.
2.  To modify the repository settings, click the **Settings** icon beside the **About** area.
3.  In the **Topics** field, enter the keyword topic **ansible-code-bot-scan** to the repository. The following illustration shows the keyword topic for starting a manual scan:


![Ansible code bot settings](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/lightspeed-ansible-code-bot-manual-trigger-setting.png)

4.  Click **Save changes**. Based on the repository webhook event, Ansible code bot starts a manual scan of your repository. If the avoid duplicate pull requests condition is not met, then the manual scan results in a new pull request with all the necessary Ansible code bot recommendations.

