+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_using_code_bot_for_suggestions"
title = "Install and configure the Ansible code bot - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_using_code_bot_for_suggestions/aem-page/develop-assembly_using_code_bot_for_suggestions.html"
last_crumb = "Install and configure the Ansible code bot"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Install and configure the Ansible code bot"
oversized = "false"
page_slug = "develop-assembly_using_code_bot_for_suggestions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_using_code_bot_for_suggestions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_using_code_bot_for_suggestions/toc/toc.json"
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

## Install the Ansible code bot

Install the Ansible code bot to get code recommendations for your repositories, and then log in to the Ansible code bot dashboard to monitor and manage your repository scans.

### Procedure

1.  Log in to GitHub by using the account associated with your organization.
2.  Go to the [Ansible code bot](https://github.com/apps/ansible-code-bot) GitHub app.
3.  Select the Ansible repositories that you want the app to access:

  - **All repositories**: Provides access to read the metadata of all repositories.
  - **Only select repositories**: Provides access to read the metadata of only the repositories that you select.

4.  Optional: If you selected **Only select repositories** in the previous step, select the repositories that you want the Ansible code bot to access from the **Select repositories** list.
5.  Click **Install & Authorize**. A message is displayed that specifies the following permissions are granted automatically to the bot during installation:

  - Read access to metadata
  - Read and write access to code and pull requests

6.  When prompted, log in to your Red Hat Single Sign-On account as an organization administrator.
7.  Log in to the Ansible code bot dashboard:
  1.  On the **Authorize Ansible code bot** page, verify your account and repository permissions.
  2.  Click **Authorize Ansible**. From the **Authorize Ansible code bot** page, the following actions occur:

    - Ansible code bot verifies that you are a part of an organization that has an active subscription to Red Hat Ansible Automation Platform.

    - GitHub requests read permissions to access the repositories associated with your account. On successful authorization, you are logged in to Ansible code bot dashboard. The dashboard displays all your repositories that have the Ansible code bot installed along with their scan status.

### Results

After the Ansible code bot is installed, it automatically scans the selected repositories that are in Jinja format. When the scanning is complete, the code bot generates an initial PR for each repository; the initial PR also contains the scan schedule configured to run weekly.

Perform the following tasks:

1. Review the initial PR for the suggested changes, and merge the PR. After you merge the initial PR, the configured scan schedule is triggered, and the subsequent repository scans are performed weekly.

   Note:
      If you do not merge the initial PR, the weekly scan schedule is not triggered and the Ansible code bot dashboard displays the repositories without any associated scan history.

     The following illustration is an example of an initial PR being created:

  
![Ansible code bot settings](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/code-bot-initial-pr.png)  

2. Optional: If required, you can manually scan your repositories or change the scan schedule to a daily or monthly cadence.

3. Modify the scanned repositories.

## Uninstall the Ansible code bot

If you no longer want to use the Ansible code bot, you can uninstall it from GitHub. After the code bot is uninstalled, you can still access the Ansible code bot dashboard but you cannot see the repositories on the dashboard or scan your repositories.

### Procedure

1.  Log in to GitHub by using the account associated with your organization.
2.  In GitHub, click your profile photo > **Settings**.
3.  Under Integrations, click **Applications** > **Installed GitHub Apps**.
4.  Click **Configure** beside the Ansible code bot app.
5.  Under the **Danger zone** area, click **Uninstall**. The Ansible code bot app is uninstalled from your GitHub account.

## Manage repository scans

The Ansible code bot dashboard displays a list of your repositories where the code bot is installed, and indicates if the scan schedule is not set, or is set to manual or scheduled scan.

You can scan your Git repository by starting a manual scan, or configure a schedule to scan your repository at regular intervals. After the scan is completed, you can view the scan history. The scan history shows the start time, status, and type of scan. It also includes a link to the pull request if it was created, and the log message if the scan failed. You can also add new repositories for scanning or remove existing repositories from being scanned.

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

## Manually scan the repository from the Ansible code bot dashboard

You can manually scan your Git repositories if you did not set up a scanning schedule for your Ansible code bot or if you do not want to wait for the next scheduled scan.

### About this task

If you manually scan your repository, and no pull request was created, it is likely so because a duplicate pull request already exists.

### Procedure

1.  Log in to the [Ansible code bot dashboard](https://bot.ai.ansible.redhat.com/console). The **Repositories** list displays a list of repositories that you selected for scanning.

   Note:
      If you do not see your repository in the **Repositories** list, you can add it for scanning.

2.  To start a manual scan of your repository, click the **Ellipsis** icon (![Ellipsis icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ansible-code-bot-dashboard-kebab-icon.png)) beside the repository that you want to scan and select **Scan now**.
3.  Click **Refresh** to view the status of the scan job.
4.  To view more details about your repository scans, click the **Ellipsis** icon (![Ellipsis icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ansible-code-bot-dashboard-kebab-icon.png)) beside the repository and select **View scan history**. The repository’s scan history is displayed along with the scan start time, scan status, type of scan (scheduled or manual), link to the pull request if it was created, and the log message if the scan failed.

5.  To view your repository on GitHub, click the **Ellipsis** icon (![Ellipsis icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ansible-code-bot-dashboard-kebab-icon.png)) beside the repository and select **View repository**.
