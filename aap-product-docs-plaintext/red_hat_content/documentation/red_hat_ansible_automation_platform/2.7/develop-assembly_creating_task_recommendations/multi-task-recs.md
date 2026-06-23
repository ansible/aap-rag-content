# Create task recommendations
## Create multitask recommendations

You can request multitask code recommendations by entering a sequence of natural language task prompts in Ansible VS Code extension. In a YAML file, start your prompt with a pound symbol (#), and separate each prompt by using the ampersand symbol (&).

### Before you begin

- You meet **one** of the following requirements:
* Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
* Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.
- You have [installed and configured the Ansible VS Code extension](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension#installing-ansible-vscode-extension "Red Hat Ansible Lightspeed with IBM watsonx Code Assistant integrates with the Ansible Visual Studio (VS) Code extension. When enabled, the extension automatically collects recommendations, usage telemetry, and Ansible YAML file state through automated events.").

### About this task

**Example of a multitask prompt**

```
# Install postgresql-server & run postgresql-setup command
```
For better readability, you can split your multitask inline prompts over multiple lines. To achieve this, end your current line with an ampersand symbol (&) and start the next line with the hash symbol (#).

**Example of a multitask prompt split over multiple lines**

```
# Create a keypair called lightspeed-keypair & create a vpc & create vpc_id var &
# create a security group that allows SSH & create subnet with 10.0.1.0/24 cidr &
# create an internet gateway & create a route table
```
The Ansible Lightspeed service reads the text, interacts with the IBM watsonx Code Assistant model, and generates the code recommendations.

Note:

While entering a multitask prompt, the Ansible VS Code extension might display a warning if you have long lines in your prompt based on your ansible-lint settings. This warning is a minor readability error and does not impact the quality of your code recommendation output. To resolve the error, you can either ignore it or fix it by splitting your multitask inline prompt over multiple lines.

### Procedure

1.  Log in to VS Code with your Red Hat account.
2.  Create a new YAML file or use an existing YAML file.   - Create a YAML file:
1. Select File> (and then)New Text File.
2. From the lower right of the screen, click **Plain Text**, and in the language mode, select **Ansible**.
3. Save the file as a YAML file format extension (`.yml` or `.yaml`).
- Use an existing YAML file:
1. On the bottom right of the screen, click the existing language mode, and in the language mode settings, select **Ansible**.  Note:
If you do not see the language mode section in your VS Code editor, from the Command Palette, select Configure Language Mode> (and then)Ansible.

3.  Verify that you see an entry for **Lightspeed** on the status bar at the lower right of VS Code. If **Ansible** is already selected as the desired language but the **Lightspeed** entry is not displayed, re-select **Ansible** as the language mode. The following illustration shows **Lightspeed** entry on the VS Code status bar.

*Figure 2. Ansible and Lightspeed set as selected language mode*

![Settings show Lightspeed as selected language mode](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/lightspeed-multitask-vs-code.png)

4.  Optional: If you see an error message about missing Ansible lint, you can install the missing module or disable it. Perform any one of the following tasks:

- Install Ansible lint: For installation information, see the [Installing](https://ansible.readthedocs.io/projects/lint/installing/) section of the Ansible Lint documentation.
- Disable Ansible lint:
1. From the Activity bar, click the **Extensions** icon ![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/extensions-icon-vscode.png).
2. From the **Installed** extensions list, select **Ansible**.
3. From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings**.
4. Clear the **Ansible › Validation › Lint: Enabled** checkbox.

5.  Create a playbook or use an existing playbook. For more information, see the [Getting started with playbooks](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_playbooks) guide.

6.  In the playbook, provide the following information to request multitask code recommendations:
1.  Start a new YAML file comment by entering a pound symbol (#) at the correct indentation.
2.  Add a detailed natural language prompt in a sequence, separating each task by using the ampersand symbol (&).  **Example of a multitask prompt**

```
# Install postgresql-server & run postgresql-setup command
```
For better readability, split your multitask inline prompts over multiple lines. To achieve this, end your current line with an ampersand symbol (&) and start the next line with the hash symbol (#).

**Example of a multitask prompt split over multiple lines**

```
# Create a keypair called lightspeed-keypair & create a vpc & create vpc_id var &
# create a security group that allows SSH & create subnet with 10.0.1.0/24 cidr &
# create an internet gateway & create a route table
```

3.  Press **Enter** directly after the task description. Keep the cursor at the same location in your file, and wait for the code recommendation results to populate. The Ansible Lightspeed service is engaged, and it starts generating code recommendations for multiple tasks.

Important:
Ansible Lightspeed service takes around 5 seconds per task to populate the code recommendations. If you are using a multitask prompt, the Ansible Lightspeed service takes a bit longer (number of tasks times 5 seconds) to populate the results. Do not move your cursor or press any key while the code recommendation is being generated. If you change the cursor location or press any key, Ansible VS Code extension cancels the request and the Ansible Lightspeed service does not process your request.

When the Ansible Lightspeed service is engaged, a **Lightspeed** processing status indicator is displayed in the lower right of the screen to denote that your code recommendation is being generated.

![Lightspeed icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/lightspeed-task-in-progress.png)

7.  Optional: If multitask code recommendations are not being generated, log out of VS Code and log in again using your Red Hat account.
8.  View your code recommendations and ensure that the recommendations match your task intent. The following illustration shows the code recommendations generated by the Ansible Lightspeed service for the multitask prompt **Install postgresql-server & run postgresql-setup command**: :

![Lightspeed single task in progress](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/lightspeed-multitask-requests.png)

9.  Accept or reject the code recommendations:

- To accept a code recommendation, press **Tab**.
- To reject a code recommendation, press **Esc**.  Note:
If you reject a recommendation, you can modify the prompt and review the generated code recommendations once again to match your task intent.

10.  After you accept the code recommendation, click the **ANSIBLE** tab to see the content source matching results.
For each generated code recommendation, Ansible Lightspeed lists content source matches, including details such as potential source, content author, and relevant licenses. You can use this data to gain insight into potential training data sources used to generate the code recommendations.

11.  Click **Save** to save the code recommendation changes in your Ansible YAML file.

