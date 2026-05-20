# 3. Working with templates
## 3.2. Understanding auto-generated templates
### 3.2.1. What users see

Auto-generated templates appear in the template catalog alongside custom templates. Users browse or search the catalog and select a template to run.

When a user opens an auto-generated template, self-service automation portal checks the Ansible Automation Platform Job Template for **Prompt on Launch** options and Survey questions. If the Job Template has **Prompt on Launch** options or Survey questions, self-service automation portal displays a form. Users select Ansible Automation Platform resources by name (such as Inventories or Credentials) and answer survey questions (such as application name or environment). self-service automation portal handles authentication automatically, so credentials are not visible on the form. If the Job Template has no **Prompt on Launch** options or Survey questions, the Job Template starts running automatically without displaying a form.

After the user submits the form or execution starts automatically, self-service automation portal launches the Ansible Automation Platform Job Template and displays an output page. The output page shows the job ID, job status, and optional links such as a direct link to the job in Ansible Automation Platform.

Users do not need to understand YAML or the template structure. The form collects the required input, and the output page displays the results.

