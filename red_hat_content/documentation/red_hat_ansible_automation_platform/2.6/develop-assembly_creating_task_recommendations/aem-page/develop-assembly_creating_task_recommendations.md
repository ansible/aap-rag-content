+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_creating_task_recommendations"
template = "docs/aem-title.html"
title = "Create task recommendations - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_creating_task_recommendations/aem-page/develop-assembly_creating_task_recommendations.html"
last_crumb = "Create task recommendations"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Create task recommendations"
oversized = "false"
page_slug = "develop-assembly_creating_task_recommendations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_creating_task_recommendations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_creating_task_recommendations/toc/toc.json"
type = "aem-page"
+++

# Create task recommendations

Red Hat Ansible Lightspeed is integrated into Visual Studio (VS) Code through the Ansible VS Code extension. You can request code recommendations for your task intent by using Ansible VS Code extension.

You can perform the following tasks from the Ansible VS Code extension:

-  **Create single task or multitask requests by using natural language prompts**
  * Create a single task prompt         Write a description of your task in the `- name:` key of a new task line in your Ansible file. For example, to automate a task of installing PostgreSQL server, you can enter the prompt `- name: Install postgresql-server`.

  * Create a multitask prompt         Place your cursor on a new line in your Ansible YAML file at the correct indentation, and start your prompt with a Pound key (#).

         Write the descriptions of your tasks, separating each prompt by using Ampersand symbols (&). For example, to automate a multitask of installing PostgreSQL server and running the initial PostgreSQL setup command, you can enter the prompt `# Install postgresql-server & run postgresql-setup command`.

         The Ansible Lightspeed service reads the text, interacts with the IBM watsonx Code Assistant model, and generates Ansible task recommendations based on your natural language prompt.

     Note:
            Currently, Red Hat Ansible Lightspeed supports user prompts in English language only. However, there could be instances where the training data that was used to train the IBM watsonx Code Assistant models included non-English language. In such scenarios, the model can generate code recommendations for prompts made in the same non-English language, but the generated code recommendations might or might not be accurate.

-  **View the content source matching results** For each generated code recommendation, Red Hat Ansible Lightspeed lists content source matches, including details such as potential source, content author, and relevant licenses. You can use this data to gain insight into potential training data sources used to generate the code recommendations.

-  **Provide feedback on the Ansible Lightspeed service** The Ansible Lightspeed service learns your organizational patterns and improves the code recommendation experience over time. You can provide feedback on whether the generated code recommendations were suitable for your task intent. This feedback enables Red Hat Ansible Lightspeed with IBM watsonx Code Assistant to improve on the quality of its suggestions.

## Best practices to improve the recommended guidance

Follow these guidelines to improve the likelihood of a quality code recommendation.

- Ensure that your YAML file is properly formatted.

- Avoid context switching within a single playbook file. The Ansible Lightspeed service attempts to correlate earlier tasks to the active recommendation, and the entire contents of the file before the cursor position are used as context by the model. If the earlier task is not relevant to your prompt, VS code provides inline suggestions instead of code recommendations.

- Reword your natural language prompts to get code recommendations that match your task intent. If you get a recommendation that does not align with the intent of your task name, then rewording your prompt to provide more information about what is desired can lead to improved results.

- Use descriptive prompts and provide additional content to improve the code recommendations. Red Hat Ansible Lightspeed reads the full Ansible YAML file when generating a code recommendation. Using descriptive prompts and having additional YAML file content related to the desired task improves the code recommendation. For example, you can add the previous Ansible tasks and appropriate playbook and variable names to improve the code recommendations.

## Create single task recommendations

You can request code recommendations for a single task by entering natural language prompts in Ansible VS Code extension. The Ansible Lightspeed service reads the text, interacts with the IBM watsonx Code Assistant model, and generates the code recommendations.

### Before you begin

- You meet **one** of the following requirements:
  * Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
  * Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.
- You have [installed and configured the Ansible VS Code extension](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_install_ansible_vscode_extension#installing-ansible-vscode-extension "Red Hat Ansible Lightspeed with IBM watsonx Code Assistant integrates with the Ansible Visual Studio (VS) Code extension. When enabled, the extension automatically collects recommendations, usage telemetry, and Ansible YAML file state through automated events.").

### Procedure

1.  Log in to VS Code with your Red Hat account.
2.  Create a new YAML file or use an existing YAML file:

  - Create a YAML file:
    1. Select File> (and then)New Text File.
    2. From the lower right of the screen, click **Plain Text**, and in the language mode, select **Ansible**.
    3. Save the file as a YAML file format extension (`.yml` or `.yaml`).
  - Use an existing YAML file:
    1. On the bottom right of the screen, click the existing language mode, and in the language mode settings, select **Ansible**.  Note:
                  If you do not see the language mode section in your VS Code editor, from the Command Palette, select Configure Language Mode> (and then)Ansible.

3.  Verify that you see an entry for **Lightspeed** on the status bar at the lower right of VS Code. If **Ansible** is already selected as the desired language but the **Lightspeed** entry is not displayed, re-select **Ansible** as the language mode. The following illustration shows **Lightspeed** and **Ansible** entries on the VS Code status bar.

*Figure 1. Ansible and Lightspeed set as selected language mode*

![Settings show Ansible and Lightspeed as selected language mode](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/lightspeed-vs-code.png)

4.  Optional: If you see an error message about missing Ansible lint, you can install the missing module or disable it. Perform any one of the following tasks:

  - Install Ansible lint: For installation information, see the [Installing](https://ansible.readthedocs.io/projects/lint/installing/) section of the Ansible Lint documentation.
  - Disable Ansible lint:
    1. From the Activity bar, click the **Extensions** icon ![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/extensions-icon-vscode.png).
    2. From the **Installed** extensions list, select **Ansible**.
    3. From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings**.
    4. Clear the **Ansible › Validation › Lint: Enabled** checkbox.

5.  Create a playbook or use an existing playbook. For more information, see the [Getting started with playbooks](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_playbooks) guide.

6.  In the playbook, provide the following information to request code recommendations for a single task:
  1.  Add a new Ansible task by starting a new line with `- name:` at the correct indentation.
  2.  Add a detailed natural language prompt in the task description after `- name:` on the same line. For example, you can specify the following single task prompt: `- name: Install postgresql-server`
  3.  Press **Enter** directly after the task description. Keep the cursor at the same location in your file, and wait for the code recommendation results to populate. The Ansible Lightspeed service is engaged, and it starts generating code recommendations for a single task.

     Important:
            Ansible Lightspeed service takes around 5 seconds per task to populate the code recommendations. If you are using a multitask prompt, the Ansible Lightspeed service takes a bit longer (number of tasks times 5 seconds) to populate the results. Do not move your cursor or press any key while the code recommendation is being generated. If you change the cursor location or press any key, Ansible VS Code extension cancels the request and the Ansible Lightspeed service does not process your request.

        When the Ansible Lightspeed service is engaged, a **Lightspeed** processing status indicator is displayed in the lower right of the screen to denote that your code recommendation is being generated.

         ![Lightspeed icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/lightspeed-task-in-progress.png)

7.  View your code recommendations and ensure that the recommendations match your task intent. The following illustration shows the code recommendations generated by the Ansible Lightspeed service for the single task **Install postgresql-server**:

     ![Lightspeed single task in progress](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/lightspeed-single-task-in-progress.png)

8.  Accept or reject the code recommendations:

  - To accept a code recommendation, press **Tab**.
  - To reject a code recommendation, press **Esc**.  Note:
            If you reject a recommendation, you can modify the prompt and review the generated code recommendations once again to match your task intent.

9.  After you accept the code recommendation, click the **ANSIBLE** tab to see the content source matching results.
      For each generated code recommendation, Ansible Lightspeed lists content source matches, including details such as potential source, content author, and relevant licenses. You can use this data to gain insight into potential training data sources used to generate the code recommendations.

10.  Click **Save** to save the code recommendation changes in your Ansible YAML file.

## Create multitask recommendations

You can request multitask code recommendations by entering a sequence of natural language task prompts in Ansible VS Code extension. In a YAML file, start your prompt with a pound symbol (#), and separate each prompt by using the ampersand symbol (&).

### Before you begin

- You meet **one** of the following requirements:
  * Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
  * Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.
- You have [installed and configured the Ansible VS Code extension](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_install_ansible_vscode_extension#installing-ansible-vscode-extension "Red Hat Ansible Lightspeed with IBM watsonx Code Assistant integrates with the Ansible Visual Studio (VS) Code extension. When enabled, the extension automatically collects recommendations, usage telemetry, and Ansible YAML file state through automated events.").

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

![Settings show Lightspeed as selected language mode](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/lightspeed-multitask-vs-code.png)

4.  Optional: If you see an error message about missing Ansible lint, you can install the missing module or disable it. Perform any one of the following tasks:

  - Install Ansible lint: For installation information, see the [Installing](https://ansible.readthedocs.io/projects/lint/installing/) section of the Ansible Lint documentation.
  - Disable Ansible lint:
    1. From the Activity bar, click the **Extensions** icon ![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/extensions-icon-vscode.png).
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

         ![Lightspeed icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/lightspeed-task-in-progress.png)

7.  Optional: If multitask code recommendations are not being generated, log out of VS Code and log in again using your Red Hat account.
8.  View your code recommendations and ensure that the recommendations match your task intent. The following illustration shows the code recommendations generated by the Ansible Lightspeed service for the multitask prompt **Install postgresql-server & run postgresql-setup command**: :

     ![Lightspeed single task in progress](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/lightspeed-multitask-requests.png)

9.  Accept or reject the code recommendations:

  - To accept a code recommendation, press **Tab**.
  - To reject a code recommendation, press **Esc**.  Note:
            If you reject a recommendation, you can modify the prompt and review the generated code recommendations once again to match your task intent.

10.  After you accept the code recommendation, click the **ANSIBLE** tab to see the content source matching results.
      For each generated code recommendation, Ansible Lightspeed lists content source matches, including details such as potential source, content author, and relevant licenses. You can use this data to gain insight into potential training data sources used to generate the code recommendations.

11.  Click **Save** to save the code recommendation changes in your Ansible YAML file.

## View the Ansible Lightspeed training matches

The Red Hat Ansible Lightspeed with IBM watsonx Code Assistant machine learning model is trained on the following content:

- Existing public or private Git repositories
- Content from Ansible Galaxy


IBM watsonx Code Assistant uses generative AI technology and various types of Ansible content to train the model. Therefore, it is not possible to trace the specific training data that produced a given code recommendation.

For each generated code recommendation, Red Hat Ansible Lightspeed lists the content source matches, including details such as potential source, content author, and relevant licenses. You can use this data to gain insight into potential training data sources used to generate the code recommendations.

After you enter a natural language prompt in VS Code and see the generated code recommendations, you can view the content source matches on the **ANSIBLE: LIGHTSPEED TRAINING MATCHES** tab.

For example, the following illustration shows the training matches for the multitask recommendation **Install postgresql-server & run postgresql-setup command**:

*Figure 3. Training matches for a multitask recommendation*

![Training matches for multitask recommendation](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/lightspeed-multitask-content-matches.png)

This capability enables you to find out the open source license terms that are associated with related training data. However, it is unlikely that either the training data used in fine-tuning the code or the output recommendations themselves are protected by copyright, or that the output reproduces training data that is controlled by copyright licensing terms.

 Note:

Red Hat does not claim any copyright or other intellectual property rights in the suggestions generated by Red Hat Ansible Lightspeed with IBM watsonx Code Assistant.
