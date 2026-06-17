+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_eda_set_up_credential"
title = "Set up credentials - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials/", "Configure credentials for Event-Driven Ansible"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_eda_set_up_credential/aem-page/secure-proc_eda_set_up_credential.html"
last_crumb = "Set up credentials"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Set up credentials"
oversized = "false"
page_slug = "secure-proc_eda_set_up_credential"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-proc_eda_set_up_credential"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_eda_set_up_credential/toc/toc.json"
type = "aem-page"
+++

# Set up credentials

Create a credential to securely store sensitive data (like tokens and passwords) required for rulebook activations to connect to source plugins or private registries.

## Procedure

1.  Log in to the Ansible Automation Platform Dashboard.
2.  From the navigation panel, select Automation Decisions> (and then)Infrastructure> (and then)Credentials.
3.  Click Create credential.
4.  Insert the following:
  

Name
Insert the name.

Description
This field is optional.

Organization
Click the list to select an organization or select **Default**.

Credential type
Click the list to select your Credential type.

  Note:
      When you select the credential type, the **Type Details** section is displayed with fields that are applicable for the credential type you chose.

5.  Complete the fields that are applicable to the credential type you selected.
6.  Click Create credential.

## What to do next

After saving the credential, the credentials details page is displayed. From there or the **Credentials** list view, you can edit or delete it.

## Credentials list view

The Credentials list view provides a single pane to monitor all authentication assets, including their type, organization, and usage status across the platform.

From the menu bar, you can search for credentials in the **Name** search field.

You also have the following options in the menu bar:

- **Manage columns** - You can choose how fields are shown in the list view by clicking this option. You have four ways you can arrange your fields:
  * **Column** - Shows the column in the table.
  * **Description** - Shows the column when the item is expanded as a full width description.
  * **Expanded** - Shows the column when the item is expanded as a detail.
  * **Hidden** - Hides the column.
- **List view** or **Card view** - You can choose between these views by clicking the applicable icons.

## Edit a credential

Edit credentials to update expired tokens, rotate secrets, or adjust permissions, ensuring secure and continuous access to external systems.

### Procedure

1.  Edit the credential by using one of these methods:

  - From the **Credentials** list view, click the Edit credential icon next to the desired credential.
  - From the **Credentials** list view, select the name of the credential, click Edit credential.

2.  Edit the appropriate details and click Save credential.

## Duplicate a credential

Use the **Duplicate credential** feature to rapidly generate a new credential based on an existing one, saving configuration time and reducing potential errors.

### Procedure

1.  On the Credentials list page, click the name of the credential that you want to duplicate. This takes you to the **Details** tab of the credential.
2.  Click Duplicate credential in the top right of the Details tab. Note:
      You can also click the Duplicate credential icon next to the desired credential on the Credentials list page.

    A message is displayed confirming that your selected credential has been duplicated: "<Name of credential> duplicated."

3.  Click the Back to credentials tab to view the credential you just duplicated. The duplicated credential is displayed with the same name as the original credential followed by a time stamp in 24-hour format (for example, **<Name of credential> @ 17:26:30**).

4.  Edit the details you prefer for your duplicated credential.
5.  Click Save credential.

## Delete a credential

You can permanently delete unused credentials. You must first ensure they are detached from any event stream before the deletion process can be completed.

### Before you begin

1. Ensure that your credential is not currently linked to any rulebook activations.

### Procedure

1.  Delete the credential by using one of these methods:

  - From the **Credentials** list view, click the More Actions icon **⋮** next to the desired credential and click Delete credential.
  - From the **Credentials** list view, select the name of the credential, click the More Actions icon **⋮** next to Edit credential, and click Delete credential.

2.  In the pop-up window, select **Yes, I confirm that I want to delete this credential**. Note:
      If your credential is still in use by other resources in your organization, a warning message is displayed letting you know that the credential cannot be deleted. Also, if your credential is being used in an event stream, you cannot delete it until the event stream is deleted or attached to a different credential. In general, avoid deleting a credential that is in use because it can lead to broken activations.

3.  Click Delete credential.

### Results

You can delete multiple credentials at a time by selecting the checkbox next to each credential, clicking the More Actions icon **⋮** in the menu bar, and then clicking Delete selected credentials.
