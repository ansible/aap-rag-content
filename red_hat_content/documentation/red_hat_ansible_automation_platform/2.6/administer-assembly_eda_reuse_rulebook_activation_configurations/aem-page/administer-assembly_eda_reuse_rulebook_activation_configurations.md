+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_reuse_rulebook_activation_configurations"
template = "docs/aem-title.html"
title = "Reuse event-driven automation configurations - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_user_guide_overview/", "Trigger automation from events with Event-Driven Ansible"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_reuse_rulebook_activation_configurations/aem-page/administer-assembly_eda_reuse_rulebook_activation_configurations.html"
last_crumb = "Reuse event-driven automation configurations"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Reuse event-driven automation configurations"
oversized = "false"
page_slug = "administer-assembly_eda_reuse_rulebook_activation_configurations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_reuse_rulebook_activation_configurations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_reuse_rulebook_activation_configurations/toc/toc.json"
type = "aem-page"
+++

# Reuse event-driven automation configurations

Streamline your workflow by duplicating existing rulebook activations to reuse proven configurations. This section covers how to create copies, manage unique naming requirements, and navigate bulk-enablement safety warnings to avoid duplicate job failures.

## Duplicate a rulebook activation

When setting up a new rulebook activation with field inputs that are similar to one of your existing rulebook activations, you can use the **Duplicate rulebook activation** feature instead of manually entering input into each field.

### About this task

While setting up rulebook activations can be a lengthy process, the ability to duplicate the required fields from an existing activation saves time and, in some cases, reduces the possibility of human error.

### Procedure

1.  On the Rulebook Activations page, click the **More Actions** icon **⋮** on the row of the activation you want to duplicate. The More Actions list is displayed with three options:

  -  **Restart rulebook activation**
  -  **Duplicate rulebook activation**
  -  **Delete rulebook activation**

2.  Select Duplicate rulebook activation. A message is displayed: "<Name of rulebook activation 1> duplicated." Initially, the newly duplicated activation is displayed as disabled on the Rulebook Activations page with the same name as the original activation followed by a time stamp in 24-hour format (for example, <Name of rulebook activation 1> @ 18:43:27).

  Important:
      The original rulebook activation continues to run after you have duplicated it. If you try to enable the duplicated activation without editing the fields (including the Name field) to distinguish it from the original, a message is displayed reminding you that the rulebook activation was duplicated from an original, and enabling it might fail or result in duplicate jobs and other complications.

3.  Before you run the duplicated rulebook activation, edit the fields by completing the following:
  1.  Next to the duplicated rulebook activation, click the **Edit** icon. This takes you to the Edit form.
  2.  Edit the desired fields. Note:
            Ensure that you have given your newly duplicated activation a meaningful **Name** that distinguishes it from the original activation.

4.  Toggle the Enable rulebook activation button to the on position.
5.  After confirming all of your edits are complete, click Save rulebook activation.

### Results

This initiates the rulebook activation, and if it runs successfully, the status changes to **Running** or **Completed**.
