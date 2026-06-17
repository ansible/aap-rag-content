# 8. Troubleshooting
## 8.4. Troubleshooting Ansible code bot errors
### 8.4.3. Cannot create pull requests

You might encounter an error where the Ansible code bot cannot create pull requests after scanning your Git repositories.

To resolve this error, ensure that:

- You have verified that there are are no duplicate pull requests. For more information, see [How Ansible code bot handles duplicate pull requests](#ansible-code-bot-duplicate-pr_using-code-bot-for-suggestions "7.4.&nbsp;How Ansible code bot handles duplicate pull requests").
- You have deleted the branches after closing the pull requests created by the Ansible code bot. For more information, see [Deleting a branch used for a pull request](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request#deleting-a-branch-used-for-a-pull-request).

