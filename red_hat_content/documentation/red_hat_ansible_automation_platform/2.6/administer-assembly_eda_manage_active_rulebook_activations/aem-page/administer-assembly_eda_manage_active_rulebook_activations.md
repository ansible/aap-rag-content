+++
title = "Manage active event-driven automation integrations - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_manage_active_rulebook_activations"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_user_guide_overview/", "Trigger automation from events with Event-Driven Ansible"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_manage_active_rulebook_activations/aem-page/administer-assembly_eda_manage_active_rulebook_activations.html"
last_crumb = "Manage active event-driven automation integrations"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Manage active event-driven automation integrations"
oversized = "false"
page_slug = "administer-assembly_eda_manage_active_rulebook_activations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_manage_active_rulebook_activations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_manage_active_rulebook_activations/toc/toc.json"
type = "aem-page"
+++

# Manage active event-driven automation integrations

To maintain efficient event-driven workflows, you must manage the lifecycle of your rulebook activations. Managing these activations effectively ensures that your automation remains responsive, reduces resource duplication, and minimizes downtime during configuration updates.

## Enable and disable rulebook activations

Toggle the state of an activation to start or stop event processing instantly, allowing for temporary pauses, maintenance, or troubleshooting without deletion.

### Procedure

1.  Select the switch on the row level to enable or disable your chosen rulebook.
2.  In the window, select Yes, I confirm that I want to enable/disable these X rulebook activations.
3.  Select Enable/Disable rulebook activation.

## Restart rulebook activations

Restart an activation to immediately apply configuration changes, update rulebook content, or quickly recover from unexpected failures.

### About this task

Note:

You can only restart a rulebook activation if it is currently enabled and the restart policy was set to **Always** when it was created.

### Procedure

1.  Select the More Actions icon **⋮** next to **Rulebook Activation enabled/disabled** toggle.
2.  Select Restart rulebook activation.
3.  In the window, select Yes, I confirm that I want to restart these X rulebook activations.
4.  Select Restart rulebook activations.

## Edit a rulebook activation

Update a rulebook activation’s settings after deployment to adjust parameters, update variables, or troubleshoot an active automation failure

### Procedure

1.  On the Rulebook Activations page, next to the activation you want to edit, toggle the Rulebook Activation enabled button to the off position first to disable the activation. The **Disable rulebook activations** message is displayed asking you to confirm that you want to disable the activation.

2.  Select the **Yes, I confirm that I want to disable these <1> rulebook activations** checkbox and click Disable rulebook activations.
3.  Next to the rulebook activation, click the **Edit** icon. This takes you to the Edit form. Note:
      You can also access the **Edit** feature by clicking the rulebook activation on the Rulebook Activations page, toggling the Rulebook activation enabled button to the off position, confirming that you want to disable the activation, and clicking the Edit rulebook activation button on the top right of the page to access the Edit form.

4.  Edit the desired fields. Note:
      If you prefer to run your activation immediately, you can toggle the Rulebook activation enabled button to the on position, and then save your changes.

5.  Click Save rulebook activation.

### Results

This takes you back to the Rulebook Activations page.

## Delete rulebook activations

End and permanently remove a rulebook activation and its configuration when its automated event-driven workflow is no longer required.

### Procedure

1.  Select the More Actions icon **⋮** next to the **Rulebook Activation enabled/disabled** toggle.
2.  Select Delete rulebook activation.
3.  In the window, select Yes, I confirm that I want to delete these X rulebook activations.
4.  Select Delete rulebook activations.
