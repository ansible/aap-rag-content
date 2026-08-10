+++
template = "docs/aem-title.html"
title = "How Ansible code bot handles duplicate pull requests - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/con_ansible_code_bot_duplicate_pr"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/con_ansible_code_bot_duplicate_pr/aem-page/con_ansible_code_bot_duplicate_pr.html"
last_crumb = "How Ansible code bot handles duplicate pull requests"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "How Ansible code bot handles duplicate pull requests"
oversized = "false"
page_slug = "con_ansible_code_bot_duplicate_pr"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/con_ansible_code_bot_duplicate_pr"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/con_ansible_code_bot_duplicate_pr/toc/toc.json"
type = "aem-page"
+++

# How Ansible code bot handles duplicate pull requests

This section outlines the conditional logic used by the Ansible code bot to manage repository scanning and pull request generation.

- If Ansible code bot has created a pull request on the latest commit default branch, it does not scan the repository. The bot skips scanning the repository because the pull request was committed on the latest default branch, and no new commit was made after that pull request.
- If there is an existing pull request that is not on the latest commit default branch, the Ansible code bot does a pull request difference to compare the changes in both branches. The following scenarios are possible:
  * **There is no difference in the existing and new scan results**: Ansible code bot does not push the scan results as a new pull request.
  * **There are differences found in the existing and the new scan results**: the Ansible code bot creates a new pull request. The newly-created pull request does not close the existing pull request, against which the pull request difference was noted. This behavior makes it easier for the repository administrator to review only the latest pull request created by the Ansible code bot, and the administrator can avoid reviewing the older pull requests created by the bot. If required, the administrator can close the older pull requests.
