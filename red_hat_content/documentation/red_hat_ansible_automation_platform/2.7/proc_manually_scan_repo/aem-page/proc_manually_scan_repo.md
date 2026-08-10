+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/proc_manually_scan_repo"
title = "Manually scan the repository from the Ansible code bot dashboard - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/proc_manually_scan_repo/aem-page/proc_manually_scan_repo.html"
last_crumb = "Manually scan the repository from the Ansible code bot dashboard"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Manually scan the repository from the Ansible code bot dashboard"
oversized = "false"
page_slug = "proc_manually_scan_repo"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/proc_manually_scan_repo"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/proc_manually_scan_repo/toc/toc.json"
type = "aem-page"
+++

# Manually scan the repository from the Ansible code bot dashboard

You can manually scan your Git repositories if you did not set up a scanning schedule for your Ansible code bot or if you do not want to wait for the next scheduled scan.

## About this task

If you manually scan your repository, and no pull request was created, it is likely so because a duplicate pull request already exists.

## Procedure

1.  Log in to the [Ansible code bot dashboard](https://bot.ai.ansible.redhat.com/console). The **Repositories** list displays a list of repositories that you selected for scanning.

   Note:
      If you do not see your repository in the **Repositories** list, you can add it for scanning.

2.  To start a manual scan of your repository, click the **Ellipsis** icon (![Ellipsis icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ansible-code-bot-dashboard-kebab-icon.png)) beside the repository that you want to scan and select **Scan now**.
3.  Click **Refresh** to view the status of the scan job.
4.  To view more details about your repository scans, click the **Ellipsis** icon (![Ellipsis icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ansible-code-bot-dashboard-kebab-icon.png)) beside the repository and select **View scan history**. The repository’s scan history is displayed along with the scan start time, scan status, type of scan (scheduled or manual), link to the pull request if it was created, and the log message if the scan failed.

5.  To view your repository on GitHub, click the **Ellipsis** icon (![Ellipsis icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ansible-code-bot-dashboard-kebab-icon.png)) beside the repository and select **View repository**.
