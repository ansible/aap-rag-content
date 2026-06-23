# Add and launch custom self-service templates
## Add a template to Ansible automation portal

You can add a custom self-service template to the **Templates** view of your Ansible automation portal instance. Custom self-service templates are stored in git repositories. Ansible automation portal supports GitLab and GitHub Source Control Management (SCM).

### Before you begin

- You have created repositories in your Git SCM for the templates that you want to use.
- In the git repository for your custom templates, ensure that the `metadata.name` field is unique and does not match an existing auto-generated template or another custom self-service template. For example, append `*-custom` to the value of the `metadata.name` key.

```
metadata:
name: provision-database-custom
```


- You must be logged in to Ansible automation portal as an Ansible Automation Platform platform administrator.

### About this task

Note:

Names for custom self-service templates must be unique. Custom self-service templates must have a different name to auto-generated job templates and also to other custom self-service templates.

### Procedure

1.  In a browser, navigate to your Ansible automation portal instance and sign in with your Ansible Automation Platform credentials.
2.  Navigate to the **Templates** Page.
3.  Click Add template.
4.  Enter a valid Git SCM URL for the template that you want to add.
5.  Click Analyze to fetch the template.
6.  After the template has been fetched, review the list of what will be imported and added to the catalog.
7.  Click Import.

### Results

After the import is complete, return to the **Templates** page to view the newly created template. You can now launch your template.

### What to do next

- You must configure RBAC for your imported custom templates to allow users to view and run them. To do this, you must be logged into Ansible automation portal as a platform administrator. For more information, see [Setting up RBAC for custom self-service templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_rbac#self-service-set-up-rbac "By default, Ansible Automation Platform administrators can define Ansible automation portal RBAC roles.").

