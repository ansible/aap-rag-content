+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_rule_audit"
title = "Audit pipeline-triggered automation activity - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_user_guide_overview/", "Trigger automation from events with Event-Driven Ansible"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_rule_audit/aem-page/administer-assembly_eda_rule_audit.html"
last_crumb = "Audit pipeline-triggered automation activity"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Audit pipeline-triggered automation activity"
oversized = "false"
page_slug = "administer-assembly_eda_rule_audit"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_rule_audit"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_rule_audit/toc/toc.json"
type = "aem-page"
+++

# Audit pipeline-triggered automation activity

Rule audit allows the auditing of rules which have been triggered by all the rules that were activated at some point.

The **Rule Audit** list view shows you a list of every time an event came in that matched a condition within a rulebook and triggered an action. The list shows you rules within your rulebook and each heading matches up to a rule that has been executed.

## View rule audit details

View the rule audit details to quickly identify the rulebook activation responsible, the event that matched the condition, and the overall execution history of the rule.

### Procedure

1.  From the navigation panel select **Automation Decisions> (and then)Rule Audit**.
2.  Select the desired rule, this brings you to the **Details** tab.

### Results

From here you can view when it was created, when it was last fired, and the rulebook activation that it corresponds to.

## View rule audit events

Review a rule’s event history to inspect the payload, source type, and timestamp of the raw event data that matched the condition and triggered the rule.

### Procedure

1.  From the navigation panel, select **Automation Decisions> (and then)Rule Audit**.
2.  Select the desired rule, this brings you to the **Details** tab. To view all the events that triggered an action, select the **Events** tab. This shows you the event that triggered actions.
3.  Select an event to view the **Event log**, along with the **Source type** and **Timestamp**.

## View rule audit actions

Review the output of executed actions within a triggered rule to confirm that the desired automated response was initiated and completed successfully.

### Procedure

1.  From the navigation panel select **Automation Decisions> (and then)Rule Audit**.
2.  Select the desired rule, then select the **Actions** tab.

### Results

From here, you can view executed actions that were taken. Some actions are linked out to Automation Execution where you can view the output.
