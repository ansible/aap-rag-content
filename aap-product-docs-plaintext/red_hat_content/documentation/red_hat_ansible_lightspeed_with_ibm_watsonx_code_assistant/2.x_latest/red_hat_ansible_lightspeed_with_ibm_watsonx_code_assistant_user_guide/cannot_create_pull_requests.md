# 7. Troubleshooting
## 7.4. Troubleshooting Ansible code bot errors
### 7.4.3. Cannot create pull requests




You might encounter an error where the Ansible code bot cannot create pull requests after scanning your Git repositories.

To resolve this error, ensure that:

- You have verified that there are are no duplicate pull requests. For more information, see [How Ansible code bot handles duplicate pull requests](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#ansible-code-bot-duplicate-pr) .
- You have deleted the branches after closing the pull requests created by the Ansible code bot. For more information, see [Deleting a branch used for a pull request](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request#deleting-a-branch-used-for-a-pull-request) .



<span id="idm139816010941632"></span>
