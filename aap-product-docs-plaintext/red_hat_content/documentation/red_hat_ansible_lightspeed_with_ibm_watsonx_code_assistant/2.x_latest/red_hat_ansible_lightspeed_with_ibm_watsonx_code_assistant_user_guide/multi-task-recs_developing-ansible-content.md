# 4. Developing Ansible content
## 4.3. Creating task recommendations
### 4.3.3. Creating multitask recommendations




You can request multitask code recommendations by entering a sequence of natural language task prompts in Ansible VS Code extension. In a YAML file, start your prompt with a pound symbol (#), and separate each prompt by using the ampersand symbol (&).

**Example of a multitask prompt**

```
# Install postgresql-server &amp; run postgresql-setup command
```


For better readability, you can split your multitask inline prompts over multiple lines. To achieve this, end your current line with an ampersand symbol (&) and start the next line with the hash symbol (#).

**Example of a multitask prompt split over multiple lines**

```
# Create a keypair called lightspeed-keypair &amp; create a vpc &amp; create vpc_id var &amp;
# create a security group that allows SSH &amp; create subnet with 10.0.1.0/24 cidr &amp;
# create an internet gateway &amp; create a route table
```


The Ansible Lightspeed service reads the text, interacts with the IBM watsonx Code Assistant model, and generates the code recommendations.

Note
While entering a multitask prompt, the Ansible VS Code extension might display a warning if you have long lines in your prompt based on your ansible-lint settings. This warning is a minor readability error and does not impact the quality of your code recommendation output. To resolve the error, you can either ignore it or fix it by splitting your multitask inline prompt over multiple lines.



**Prerequisites**

- You meet **one** of the following requirements:


- Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
- Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.

- You have [installed and configured the Ansible VS Code extension](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#con-configure-vs-code-extension_developing-ansible-content) .


**Procedure**

1. Log in to VS Code with your Red Hat account.
1. Create a new YAML file or use an existing YAML file.


- Create a YAML file:


1. SelectFile→New Text File.
1. From the lower right of the screen, click **Plain Text** , and in the language mode, select **Ansible** .
1. Save the file as a YAML file format extension ( `            .yml` or `            .yaml` ).

- Use an existing YAML file:


1. On the bottom right of the screen, click the existing language mode, and in the language mode settings, select **Ansible** .

Note
If you do not see the language mode section in your VS Code editor, from the Command Palette, selectConfigure Language Mode→Ansible.






1. Verify that you see an entry for **Lightspeed** on the status bar at the lower right of VS Code.

If **Ansible** is already selected as the desired language but the **Lightspeed** entry is not displayed, re-select **Ansible** as the language mode. The following illustration shows **Lightspeed** entry on the VS Code status bar.


<span id="idm139960285606528"></span>
**Figure 4.3. Ansible and Lightspeed set as selected language mode**

![Settings show Lightspeed as selected language mode](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/03ba1497281fc60846ce63163c57ecab/lightspeed-multitask-vs-code.png)





1. Optional: If you see an error message about missing Ansible lint, you can install the missing module or disable it. Perform any one of the following tasks:


- Install Ansible lint: For installation information, see the [Installing](https://ansible.readthedocs.io/projects/lint/installing/) section of the Ansible Lint documentation.
- Disable Ansible lint:


1. From the Activity bar, click the **Extensions** icon![Extensions](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/7d3e99e2c8c192205eee349f07f39c7e/extensions-icon-vscode.png)
.
1. From the **Installed** extensions list, select **Ansible** .
1. From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings** .
1. Clear the **Ansible › Validation › Lint: Enabled** checkbox.


1. Create a playbook or use an existing playbook.

For more information, see the [Getting started with playbooks](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_playbooks) guide.


1. In the playbook, provide the following information to request multitask code recommendations:


1. Start a new YAML file comment by entering a pound symbol (#) at the correct indentation.
1. Add a detailed natural language prompt in a sequence, separating each task by using the ampersand symbol (&).

**Example of a multitask prompt**


```
# Install postgresql-server &amp; run postgresql-setup command
```


For better readability, split your multitask inline prompts over multiple lines. To achieve this, end your current line with an ampersand symbol (&) and start the next line with the hash symbol (#).

**Example of a multitask prompt split over multiple lines**


```
# Create a keypair called lightspeed-keypair &amp; create a vpc &amp; create vpc_id var &amp;        # create a security group that allows SSH &amp; create subnet with 10.0.1.0/24 cidr &amp;        # create an internet gateway &amp; create a route table
```



1. Press **Enter** directly after the task description. Keep the cursor at the same location in your file, and wait for the code recommendation results to populate.

The Ansible Lightspeed service is engaged, and it starts generating code recommendations for multiple tasks.

Important
Ansible Lightspeed service takes around 5 seconds per task to populate the code recommendations. If you are using a multitask prompt, the Ansible Lightspeed service takes a bit longer (number of tasks times 5 seconds) to populate the results. Do not move your cursor or press any key while the code recommendation is being generated. If you change the cursor location or press any key, Ansible VS Code extension cancels the request and the Ansible Lightspeed service does not process your request.



When the Ansible Lightspeed service is engaged, a **Lightspeed** processing status indicator is displayed in the lower right of the screen to denote that your code recommendation is being generated.

![Lightspeed icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/ae185d20966a8759e445c12c5d3912a2/lightspeed-task-in-progress.png)




1. Optional: If multitask code recommendations are not being generated, log out of VS Code and log in again using your Red Hat account.
1. View your code recommendations and ensure that the recommendations match your task intent.

The following illustration shows the code recommendations generated by the Ansible Lightspeed service for the multitask prompt **Install postgresql-server & run postgresql-setup command** : :

![Lightspeed single task in progress](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/34748d9232c783fe1b70b31ab32da4e8/lightspeed-multitask-requests.png)



1. Accept or reject the code recommendations:


- To accept a code recommendation, press **Tab** .
- To reject a code recommendation, press **Esc** .

Note
If you reject a recommendation, you can modify the prompt and review the generated code recommendations once again to match your task intent.





1. On the **ANSIBLE: LIGHTSPEED TRAINING MATCHES** tab, view the content source matching results.

The following illustration shows the training matches found in existing Ansible Galaxy content for the task prompt multitask prompt **Install postgresql-server & run postgresql-setup command** :

![training matches in existing content](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/1f0180015e378772f9d8876be53e9a9c/lightspeed-multitask-content-matches.png)



1. Click **Save** to save the code recommendation changes in your Ansible YAML file.


**Additional resources**

-  [Troubleshooting Ansible Visual Studio Code extension errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#troubleshooting-vscode_troubleshooting-lightspeed)
-  [Troubleshooting Ansible code bot errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#troubleshooting-code-bot_troubleshooting-lightspeed)


