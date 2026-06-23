# Troubleshoot Red Hat Ansible Lightspeed configuration errors
## Troubleshoot Ansible code bot errors
### Cannot scan your Git repository using Ansible code bot

If the Ansible code bot is not configured correctly, it does not scan your Git repositories or does not create pull requests.

To resolve Ansible code bot errors, ensure that:

- You have selected all the Git repositories that you want to scan.
- You have a `.yml` configuration file named `ansible-code-bot.yml` in your repository `.github` folder. For example, `.github/ansible-code-bot.yml`.


Run a manual scan on your git repositories by adding the **ansible-code-bot-scan** topic to your repository. For more information, see Manually scan your Git repositories.

If the Ansible code bot still cannot scan your Git repository, the following scenarios are possible:

- The Ansible code bot did not identify any ansible-lint violations in the Git repository.
- The Ansible code bot does not have permission to scan the Git repository.
- Your organization does not have a valid Red Hat Ansible Automation Platform subscription.

