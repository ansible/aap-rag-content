+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_using_code_bot_for_suggestions"
title = "Install and configure the Ansible code bot - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_using_code_bot_for_suggestions/aem-page/assembly_using_code_bot_for_suggestions.html"
last_crumb = "Install and configure the Ansible code bot"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Install and configure the Ansible code bot"
oversized = "false"
page_slug = "assembly_using_code_bot_for_suggestions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/assembly_using_code_bot_for_suggestions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_using_code_bot_for_suggestions/toc/toc.json"
type = "aem-page"
+++

# Install and configure the Ansible code bot

Ansible code bot scans GitHub repositories (collections, roles, playbooks) and proactively creates pull requests with best practice or quality improvement recommendations.

Important:

The Ansible code bot was deprecated on October 1, 2025 and will be retired anytime after December 31, 2025. Red Hat is no longer actively maintaining or supporting the component.

Ansible code bot scans your code repositories to recommend code quality improvements. It promotes Ansible best practices while avoiding common errors that can lead to bugs or make code harder to maintain. The bot automatically submits pull requests to the repository, which proactively alerts the repository owner to a recommended change to their content. You can configure Ansible code bot to scan your existing Git repositories (both public and private). Your organization must have an active subscription to Red Hat Ansible Automation Platform to use the Ansible code bot. However, IBM watsonx Code Assistant is not required to use the Ansible code bot.

After the Ansible code bot is installed, it automatically scans the selected repositories that are in Jinja format. Once the scanning is complete, the code bot generates an initial PR for each repository; the initial PR also contains the scan schedule configured to run weekly. You must review the initial PR for the suggested changes and merge the PR. Once the initial PR is merged, the scan schedule is triggered, and the subsequent repository scans are performed weekly. If required, you can change the scan schedule to a daily or monthly cadence.

You can access the Ansible code bot dashboard that displays all your repositories that have the bot installed along with their scan status. From the dashboard, you can start a manual scan, view the scan history, and view the repository. From GitHub, you can configure a schedule to scan your repository at regular intervals, and add or remove a repository from being scanned.

Important:

Ansible code bot is supported on the following GitHub versions:

- GitHub.com

- GitHub Enterprise Cloud     Ansible code bot is not supported on GitHub Enterprise Server.

The following examples are code recommendations that the Ansible code bot can suggest:

- Available alternatives for deprecated legacy syntax or implementation patterns
- Module version changes and updates, such as:
  * Adding any new required parameters
  * Flagging deprecated parameters
  * Removing unused parameters
- Applying YAML best practices
- Adding comment blocks
- Fixing casing issues in name fields
