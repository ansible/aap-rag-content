+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_cloud_terraform_integrating"
template = "docs/aem-title.html"
title = "Integrate with the cloud.terraform collection - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_introduction/", "Integrate with IBM HashiCorp Terraform"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-assembly_cloud_terraform_integrating/aem-page/integrate-assembly_cloud_terraform_integrating.html"
last_crumb = "Integrate with the cloud.terraform collection"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Integrate with the cloud.terraform collection"
oversized = "false"
page_slug = "integrate-assembly_cloud_terraform_integrating"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/integrate-assembly_cloud_terraform_integrating"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-assembly_cloud_terraform_integrating/toc/toc.json"
type = "aem-page"
+++

# Integrate with the cloud.terraform collection

When you integrate with `cloud.terraform`, you must create a credential, build an execution environment, and launch a job template in Ansible Automation Platform.

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

## Build an execution environment in Ansible Automation Platform

You must build an execution environment using the automation controller so that Ansible Automation Platform can provide the credentials necessary for using its automation features.

### Before you begin

- You need a pre-existing execution environment with the latest version of `cloud.terraform` collection before you can create it using an automation controller. You cannot use the default execution environment provided by Ansible Automation Platform because the default environment does not include the `terraform` CLI binary.  Note:
      If you have migrated from Terraform Community Edition, you can continue to use your existing execution environment and update it to the latest version of `cloud.terraform`.

- Install the `terraform` CLI binary in your pre-existing execution environment. See **Additional resources** below for a link to the binary.

### Procedure

1.  From the navigation panel, select **Automation Execution> (and then)Infrastructure> (and then)Execution Environments**.
2.  Click Create execution environment.  
![Create a new execution environment page](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ee-create-new.png)  
3.  For **Name**, enter a name for your Ansible Automation Platform execution environment.
4.  For **Image**, enter the repository link to the image for your pre-existing execution environment.
5.  Click Create execution environment. Your newly added execution environment is ready to be used in a job template.

## Create and launch a job template

Create and launch a job template to complete the integration and use the automation features in Ansible Automation Platform.

### Procedure

1.  From the navigation panel, select **Automation Execution> (and then)Templates**.
2.  Select **Create template > Create Job Template**.
3.  From the **Execution Environment** list, select the environment you created.
4.  From the **Credentials** list, select the credentials instance you created previously. If you do not see the credentials, click Browse to see more options in the list.
5.  Enter any additional information for the required fields.
6.  Click Create job template.
7.  Click Launch template.
8.  To launch the job, click Next and Finish. The job output shows that the job has run.

### Results

To see that the job has run successfully from the Terraform user interface, select **Workspaces > Ansible-Content-Integration > Run**. The Run list shows the state of the Triggered via CLI job. You can see it go from the Queued to the Plan Finished state.
