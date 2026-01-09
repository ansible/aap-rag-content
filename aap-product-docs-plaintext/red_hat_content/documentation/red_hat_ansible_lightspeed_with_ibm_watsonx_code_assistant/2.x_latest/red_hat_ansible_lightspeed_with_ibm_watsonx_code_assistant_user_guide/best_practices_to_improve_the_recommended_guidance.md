# 5. Developing Ansible content
## 5.3. Creating task recommendations
### 5.3.1. Best practices to improve the recommended guidance




Follow these guidelines to improve the likelihood of a quality code recommendation.

- Ensure that your YAML file is properly formatted. See the [Ansible YAML syntax guidelines](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html) for details.
- Avoid context switching within a single playbook file.

The Ansible Lightspeed service attempts to correlate earlier tasks to the active recommendation, and the entire contents of the file before the cursor position are used as context by the model. If the earlier task is not relevant to your prompt, VS code provides inline suggestions instead of code recommendations.


- Reword your natural language prompts to get code recommendations that match your task intent.

If you get a recommendation that does not align with the intent of your task name, then rewording your prompt to provide more information about what is desired can lead to improved results.


- Use descriptive prompts and provide additional content to improve the code recommendations.

Red Hat Ansible Lightspeed reads the full Ansible YAML file when generating a code recommendation. Using descriptive prompts and having additional YAML file content related to the desired task improves the code recommendation. For example, you can add the previous Ansible tasks and appropriate playbook and variable names to improve the code recommendations.




