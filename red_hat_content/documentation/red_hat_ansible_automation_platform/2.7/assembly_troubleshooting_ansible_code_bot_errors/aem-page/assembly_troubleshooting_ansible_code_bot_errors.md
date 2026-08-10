+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_troubleshooting_ansible_code_bot_errors"
template = "docs/aem-title.html"
title = "Troubleshoot Ansible code bot errors - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_troubleshooting_ansible_code_bot_errors/aem-page/assembly_troubleshooting_ansible_code_bot_errors.html"
last_crumb = "Troubleshoot Ansible code bot errors"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Troubleshoot Ansible code bot errors"
oversized = "false"
page_slug = "assembly_troubleshooting_ansible_code_bot_errors"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/assembly_troubleshooting_ansible_code_bot_errors"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_troubleshooting_ansible_code_bot_errors/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot Ansible code bot errors

This section provides information about errors when using the Ansible code bot and their workarounds.

## Cannot access Ansible code bot

After you install Ansible code bot and attempt to log in, you receive the following error message:

 `Your organization does not have a valid Red Hat Ansible Lightspeed subscription`

After you install Ansible code bot, you are redirected to a page that shows an active subscription status, as shown in the following image:

*Figure 1. Ansible code bot login screen with an active subscription*

![Ansible code bot login screen with an active subscription](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/code-bot-login-screen.png)

If the login screen displays an inactive subscription status, Ansible code bot does not scan your Git repositories. The error occurs because your organization does not have a valid Ansible Automation Platform subscription. To resolve this error, ensure that you are part of an organization that has a valid Red Hat Ansible Automation Platform subscription.

## Cannot scan your Git repository using Ansible code bot

If the Ansible code bot is not configured correctly, it does not scan your Git repositories or does not create pull requests.

To resolve Ansible code bot errors, ensure that:

- You have selected all the Git repositories that you want to scan.
- You have a `.yml` configuration file named `ansible-code-bot.yml` in your repository `.github` folder. For example, `.github/ansible-code-bot.yml`.

Run a manual scan on your git repositories by adding the **ansible-code-bot-scan** topic to your repository. For more information, see Manually scan your Git repositories.

If the Ansible code bot still cannot scan your Git repository, the following scenarios are possible:

- The Ansible code bot did not identify any ansible-lint violations in the Git repository.
- The Ansible code bot does not have permission to scan the Git repository.
- Your organization does not have a valid Red Hat Ansible Automation Platform subscription.

## Cannot create pull requests

You might encounter an error where the Ansible code bot cannot create pull requests after scanning your Git repositories.

To resolve this error, ensure that:

- You have verified that there are are no duplicate pull requests. For more information, see How Ansible code bot handles duplicate pull requests.
- You have deleted the branches after closing the pull requests created by the Ansible code bot. For more information, see Deleting a branch used for a pull request.
