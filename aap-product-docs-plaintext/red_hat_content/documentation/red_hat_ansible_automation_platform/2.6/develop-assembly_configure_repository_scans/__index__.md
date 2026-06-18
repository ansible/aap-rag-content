# Configure the Ansible code bot to scan your repository at regular intervals

After installing the Ansible code bot, it automatically scans the selected repositories that are in Jinja format. Once the scanning is complete, the code bot generates an initial PR for each repository; the initial PR also contains the scan schedule configured to run weekly.

You must review the initial PR for the suggested changes and merge the PR. Once the initial PR is merged, the scan schedule is triggered, and the subsequent repository scans are performed weekly. If required, you can change the scan schedule to a daily or monthly cadence.

Note:

If you do not merge the initial PR, the weekly scan schedule is not triggered and the Ansible code bot dashboard displays the repositories without any associated scan history. In such a scenario, you must manually create a configuration file `ansible-code-bot.yml` and specify your scan schedule within the file.

## How Ansible code bot handles duplicate pull requests

This section outlines the conditional logic used by the Ansible code bot to manage repository scanning and pull request generation.

- If Ansible code bot has created a pull request on the latest commit default branch, it does not scan the repository. The bot skips scanning the repository because the pull request was committed on the latest default branch, and no new commit was made after that pull request.
- If there is an existing pull request that is not on the latest commit default branch, the Ansible code bot does a pull request difference to compare the changes in both branches. The following scenarios are possible:
* **There is no difference in the existing and new scan results**: Ansible code bot does not push the scan results as a new pull request.
* **There are differences found in the existing and the new scan results**: the Ansible code bot creates a new pull request. The newly-created pull request does not close the existing pull request, against which the pull request difference was noted. This behavior makes it easier for the repository administrator to review only the latest pull request created by the Ansible code bot, and the administrator can avoid reviewing the older pull requests created by the bot. If required, the administrator can close the older pull requests.
