# 1. Using the Ansible plug-ins
## 1.5. Creating a project

Create a new Ansible Playbook project in the Red Hat Developer Hub by logging in, navigating to the Ansible section, and selecting the project creation template. You must have the correct access (RBAC) assigned by your administrator to view the templates.

**Prerequisite**

- You have the correct access (RBAC) to view the templates in Red Hat Developer Hub. Ask your administrator to assign access to you if necessary.

**Procedure**

1. Log in to your Red Hat Developer Hub UI.

2. Click the Ansible `A` icon in the Red Hat Developer Hub navigation panel.

3. Navigate to the **Overview** page.

4. Click **Create**.

5. Click **Create Ansible Git Project**. The **Available Templates** page opens.

6. Click **Create Ansible Playbook project**.

7. In the **Create Ansible Playbook Project** page, enter information for your new project in the form.

You can see sample values for this form in the Example project.

| Field | Description |
| --- | --- |
| <br>  Source code repository organization name or username | <br>  The name of your source code repository username or organization name |
| <br>  Playbook repository name | <br>  The name of your new Git repository |
| <br>  Playbook description (Optional) | <br>  A description of the new playbook project |
| <br>  Playbook project’s collection namespace | <br>  The new playbook Git project creates an example collection folder for you. Enter a value for the collection namespace. |
| <br>  Playbook project’s collection name | <br>  The name of the collection |
| <br>  Catalog Owner Name | <br>  The name of the Developer Hub catalog item owner. This is a Red Hat Developer Hub field. |
| <br>  Source code repository organization name or username | <br>  The name of your source code repository username or organization name |
| <br>  Playbook repository name | <br>  The name of your new Git repository |
| <br>  Playbook description (Optional) | <br>  A description of the new playbook project |
| <br>  System (Optional) | <br>  This is a Red Hat Developer Hub field |

Note
Collection namespaces must follow Python module naming conventions. Collections must have short, all lowercase names. You can use underscores in the collection name if it improves readability.

8. Click **Review**.

