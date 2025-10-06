# 3. Working with templates
## 3.2. Adding a template to self-service automation portal




You can add a tile for a custom self-service template to the **Templates** view of your self-service automation portal instance. The custom self-service template is defined in a git repository.

Note
Names for custom self-service templates must be unique. Custom self-service templates must have a different name to auto-generated job templates and also to other custom self-service templates.



**Prerequisites**

- You have created repositories in your Git SCM for the templates that you want to use.
- In the git repository for your custom templates, ensure that the `    metadata.name` field is unique and does not match an existing auto-generated template or another custom self-service template. For example, append `    *-custom` to the value of the `    metadata.name` key.


```
metadata:
name: provision-database-custom
```

- You must be logged in to self-service automation portal as an Ansible Automation Platform platform administrator.


**Procedure**

1. In a browser, navigate to your self-service automation portal instance and sign in with your Ansible Automation Platform credentials.
1. Navigate to the **Templates** Page.
1. ClickAdd template.
1. Enter a valid Git SCM URL for the template that you want to add.
1. ClickAnalyzeto fetch the template.
1. After the template has been fetched, review the list of what will be imported and added to the catalog.
1. ClickImport.


**Verification**

After the import is complete, return to the **Templates** page to view the newly created template. You can now launch your template.


**Next steps**

- You must configure RBAC for your imported custom templates, bearing in mind that a user who wants to launch a template that is associated with a job template in Ansible Automation Platform must have access to that job template.


