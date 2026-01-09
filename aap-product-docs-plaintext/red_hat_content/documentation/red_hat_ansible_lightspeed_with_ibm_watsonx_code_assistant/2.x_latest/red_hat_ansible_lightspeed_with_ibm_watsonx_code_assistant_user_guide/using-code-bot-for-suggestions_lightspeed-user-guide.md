# Chapter 7. Installing and configuring the Ansible code bot




The Ansible code bot scans existing content collections, roles, and playbooks hosted in GitHub repositories, and proactively creates pull requests whenever best practices or quality improvement recommendations are available.

Ansible code bot scans your code repositories to recommend code quality improvements. It promotes Ansible best practices while avoiding common errors that can lead to bugs or make code harder to maintain. The bot automatically submits pull requests to the repository, which proactively alerts the repository owner to a recommended change to their content. You can configure Ansible code bot to scan your existing Git repositories (both public and private).

Note
Your organization must have an active subscription to Red Hat Ansible Automation Platform to use the Ansible code bot. However, IBM watsonx Code Assistant is not required to use the Ansible code bot.



After the Ansible code bot is installed, it automatically scans the selected repositories that are in Jinja format. Once the scanning is complete, the code bot generates an initial PR for each repository; the initial PR also contains the scan schedule configured to run weekly. You must review the initial PR for the suggested changes and merge the PR. Once the initial PR is merged, the scan schedule is triggered, and the subsequent repository scans are performed weekly. If required, you can change the scan schedule to a daily or monthly cadence.

You can access the Ansible code bot dashboard that displays all your repositories that have the bot installed along with their scan status. From the dashboard, you can start a manual scan, view the scan history, and view the repository. From GitHub, you can configure a schedule to scan your repository at regular intervals, and add or remove a repository from being scanned. For more information, see [Managing repository scans](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#manage-repo-scans_using-code-bot-for-suggestions) .

Important
Ansible code bot is supported on the following GitHub versions:

- GitHub.com
- GitHub Enterprise Cloud

Ansible code bot is not supported on GitHub Enterprise Server. For more information, see [GitHub’s plans](https://docs.github.com/en/enterprise-cloud@latest/get-started/learning-about-github/githubs-plans) in the GitHub documentation.






The following examples are code recommendations that the Ansible code bot can suggest:

- Available alternatives for deprecated legacy syntax or implementation patterns
- Module version changes and updates, such as:


- Adding any new required parameters
- Flagging deprecated parameters
- Removing unused parameters

- Applying YAML best practices
- Adding comment blocks
- Fixing casing issues in name fields


