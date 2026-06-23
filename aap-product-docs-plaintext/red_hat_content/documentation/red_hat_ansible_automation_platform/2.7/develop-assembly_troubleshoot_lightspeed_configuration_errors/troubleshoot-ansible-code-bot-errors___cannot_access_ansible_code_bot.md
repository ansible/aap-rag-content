# Troubleshoot Red Hat Ansible Lightspeed configuration errors
## Troubleshoot Ansible code bot errors
### Cannot access Ansible code bot

After you install Ansible code bot and attempt to log in, you receive the following error message:

`Your organization does not have a valid Red Hat Ansible Lightspeed subscription`

After you install Ansible code bot, you are redirected to a page that shows an active subscription status, as shown in the following image:

*Figure 1. Ansible code bot login screen with an active subscription*

![Ansible code bot login screen with an active subscription](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/code-bot-login-screen.png)

If the login screen displays an inactive subscription status, Ansible code bot does not scan your Git repositories. The error occurs because your organization does not have a valid Ansible Automation Platform subscription. To resolve this error, ensure that you are part of an organization that has a valid Red Hat Ansible Automation Platform subscription.

