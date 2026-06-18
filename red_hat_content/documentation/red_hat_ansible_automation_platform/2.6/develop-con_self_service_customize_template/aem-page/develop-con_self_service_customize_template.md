+++
template = "docs/aem-title.html"
title = "Add and launch custom self-service templates - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-con_self_service_customize_template"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_self_service_customize_template/aem-page/develop-con_self_service_customize_template.html"
last_crumb = "Add and launch custom self-service templates"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Add and launch custom self-service templates"
oversized = "false"
page_slug = "develop-con_self_service_customize_template"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-con_self_service_customize_template"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_self_service_customize_template/toc/toc.json"
type = "aem-page"
+++

# Add and launch custom self-service templates

Custom self-service templates are stored as YAML files in repositories in GitHub or Gitlab. When a user launches a software template from Ansible automation portal, they must fill in a form with the values needed to run the associated job template in Ansible Automation Platform.

The custom self-service template YAML file must have a `token:` section that includes a `ui:field:` key for the authentication token for Ansible Automation Platform. This generates a field for the token in the form that appears when the user launches the template in Ansible automation portal. The user enters the token: it is used to authenticate job template execution in Ansible Automation Platform.

The following example shows the `token:` section in a template. For security reasons, set the value of `token.ui:backstage.review.show` to `false` to ensure that the token is not visible to the user.

```
spec:
  ...
  parameters:
    ...
      properties:
        token:
          title: Token
          type: string
          description: Oauth2 token
          ui:field: AAPTokenField
          ui:widget: hidden
          ui:backstage:
            review:
              show: false
```


Note:

Setting the `ui:widget: hidden` field hides the Red Hat Ansible Automation Platform token input in the form.

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

- You must configure RBAC for your imported custom templates to allow users to view and run them. To do this, you must be logged into Ansible automation portal as a platform administrator. For more information, see [Setting up RBAC for custom self-service templates](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_rbac#self-service-set-up-rbac "By default, Ansible Automation Platform administrators can define Ansible automation portal RBAC roles.").

## Launch a template

This procedure describes how to launch a template from a tile in the **Templates** view of your Ansible automation portal instance.

### Before you begin

- You have configured RBAC in Ansible Automation Platform for templates that are associated with Ansible Automation Platform job templates.

### Procedure

1.  In a browser, navigate to your Ansible automation portal instance and sign in with your Ansible Automation Platform credentials.
2.  Navigate to the **Templates** page. The templates you have set up are displayed as tiles on the page.
3.  In the template that you want to launch, click **Start**. A description of the template is displayed.

4.  Click **Launch** to begin configuring the parameters for running the template.
5.  Fill out the required fields.
6.  Click **Next**.
7.  Review the entered information.
8.  Click **Create** to launch the template.
9.  The progress for the template execution is displayed.
