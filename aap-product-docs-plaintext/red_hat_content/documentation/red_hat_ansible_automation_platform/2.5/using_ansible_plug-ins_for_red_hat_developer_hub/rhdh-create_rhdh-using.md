# 1. Using the Ansible plug-ins
## 1.5. Creating a project




**Prerequisite**

- Ensure you have the correct access (RBAC) to view the templates in Red Hat Developer Hub. Ask your administrator to assign access to you if necessary.


**Procedure:**

1. Log in to your Red Hat Developer Hub UI.
1. Click the Ansible `    A` icon in the Red Hat Developer Hub navigation panel.
1. Navigate to the **Overview** page.
1. Click **Create** .
1. Click **Create Ansible Git Project** . The **Available Templates** page opens.
1. Click **Create Ansible Playbook project** .
1. In the **Create Ansible Playbook Project** page, enter information for your new project in the form.

You can see sample values for this form in the Example project.

| Field | Description |
| --- | --- |
| Source code repository organization name or username | The name of your source code repository username or organization name |
| Playbook repository name | The name of your new Git repository |
| Playbook description (Optional) | A description of the new playbook project |
| Playbook project’s collection namespace | The new playbook Git project creates an example collection folder for you. Enter a value for the collection namespace. |
| Playbook project’s collection name | The name of the collection |
| Catalog Owner Name | The name of the Developer Hub catalog item owner. This is a Red Hat Developer Hub field. |
| Source code repository organization name or username | The name of your source code repository username or organization name |
| Playbook repository name | The name of your new Git repository |
| Playbook description (Optional) | A description of the new playbook project |
| System (Optional) | This is a Red Hat Developer Hub field |


Note
Collection namespaces must follow Python module naming conventions. Collections must have short, all lowercase names. You can use underscores in the collection name if it improves readability.

For more information, see the [Ansible Collection naming conventions documentation](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_in_groups.html#naming-conventions) .




1. Click **Review** .


