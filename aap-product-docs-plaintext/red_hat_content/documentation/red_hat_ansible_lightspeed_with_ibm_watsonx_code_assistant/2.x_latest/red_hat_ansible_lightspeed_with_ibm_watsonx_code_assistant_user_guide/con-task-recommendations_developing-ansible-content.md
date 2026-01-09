# 5. Developing Ansible content
## 5.3. Creating task recommendations




Red Hat Ansible Lightspeed is integrated into Visual Studio (VS) Code through the Ansible VS Code extension. You can request code recommendations for your task intent by using Ansible VS Code extension.

You can perform the following tasks from the Ansible VS Code extension:

-  **Create single task or multitask requests by using natural language prompts**


- Create a single task prompt

Write a description of your task in the `        - name:` key of a new task line in your Ansible file. For example, to automate a task of installing PostgreSQL server, you can enter the prompt `        - name: Install postgresql-server` .


- Create a multitask prompt

Place your cursor on a new line in your Ansible YAML file at the correct indentation, and start your prompt with a Pound key (#).

Write the descriptions of your tasks, separating each prompt by using Ampersand symbols (&). For example, to automate a multitask of installing PostgreSQL server and running the initial PostgreSQL setup command, you can enter the prompt `        # Install postgresql-server &amp; run postgresql-setup command` .

The Ansible Lightspeed service reads the text, interacts with the IBM watsonx Code Assistant model, and generates Ansible task recommendations based on your natural language prompt.

Note
Currently, Red Hat Ansible Lightspeed supports user prompts in English language only. However, there could be instances where the training data that was used to train the IBM watsonx Code Assistant models included non-English language. In such scenarios, the model can generate code recommendations for prompts made in the same non-English language, but the generated code recommendations might or might not be accurate.





-  **View the content source matching results**

For each generated code recommendation, Red Hat Ansible Lightspeed lists content source matches, including details such as potential source, content author, and relevant licenses. You can use this data to gain insight into potential training data sources used to generate the code recommendations.


-  **Provide feedback on the Ansible Lightspeed service**

The Ansible Lightspeed service learns your organizational patterns and improves the code recommendation experience over time. You can provide feedback on whether the generated code recommendations were suitable for your task intent. This feedback enables Red Hat Ansible Lightspeed with IBM watsonx Code Assistant to improve on the quality of its suggestions.




