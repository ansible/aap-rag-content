# 3. Working with templates
## 3.2. Adding a template to self-service automation portal




You can add a custom self-service template to the **Templates** view of your self-service automation portal instance. Custom self-service templates are stored in git repositories. self-service automation portal supports GitLab and GitHub Source Control Management (SCM).

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

- You must configure RBAC for your imported custom templates to allow users to view and run them. To do this, you must be logged into self-service automation portal as a platform administrator.

For more information, see [Setting up RBAC for custom self-service templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_self-service_automation_portal/index#self-service-set-up-rbac_self-service-rbac) .




