# Integrate with the cloud.terraform collection
## Create a credential for using cloud.terraform

You can set up credentials directly from the Ansible Automation Platform user interface. The credentials are provided to the execution environment and Ansible Automation Platform reads them from there. This eliminates the need to manually update each playbook.

### Before you begin

- You must have a Terraform API token.
- Install the certified `cloud.terraform` collection from automation hub. (You need an Ansible subscription to access and download collections on automation hub.)

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select **Automation Execution> (and then)Infrastructure> (and then)Credential Types**.
3.  Click Create credential type. The **Create Credential Type** page opens and displays the **Details** tab.
4.  For the **Credential Type**, enter a name.
5.  In the **Input configuration** field, enter the following YAML parameter and values:


```
fields:
- id: token
type: string
label: token
secret: true
```

6.  In the **Injector configuration** field, enter the following configuration.   - For Terraform Enterprise, the hostname is the location where you have deployed TFE:

```
env:
TF_TOKEN_<hostname>:  ‘{{ token }}’
```

- For HCP Terraform, use:

```
env:
TF_TOKEN_app_terraform_io:   ‘{{ token }}’
```

7.  To save your configuration, click Create Credential Type again. The new credential type is created.
8.  To create an instance of your new credential type, select **Automation Execution> (and then)Infrastructure> (and then)Credentials** page, and select Create credential.
9.  From the **Credential type**, select the name of the credential type you created earlier.
10.  In the **Token** field, enter the Terraform API token.
11.  (Optional) Edit the **Description** and select the TF organization from the **Organization** list.
12.  Click Save credential.

