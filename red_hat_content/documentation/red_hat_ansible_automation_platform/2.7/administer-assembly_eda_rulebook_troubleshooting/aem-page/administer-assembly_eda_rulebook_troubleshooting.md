+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_rulebook_troubleshooting"
template = "docs/aem-title.html"
title = "Troubleshoot failed event-driven automation triggers - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_user_guide_overview/", "Trigger automation from events with Event-Driven Ansible"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_rulebook_troubleshooting/aem-page/administer-assembly_eda_rulebook_troubleshooting.html"
last_crumb = "Troubleshoot failed event-driven automation triggers"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Troubleshoot failed event-driven automation triggers"
oversized = "false"
page_slug = "administer-assembly_eda_rulebook_troubleshooting"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_rulebook_troubleshooting"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_rulebook_troubleshooting/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot failed event-driven automation triggers

Rulebook activations might occasionally fail due to various reasons. While many issues can be resolved through basic checks, diagnosing failures across a distributed system requires robust logging.

Event-Driven Ansible’s enhanced logging strategy includes the addition of unique tracking identifiers to all output to significantly improve troubleshooting.

Review the list of possible issues contained in this chapter that can cause activation failures and suggestions on how you can resolve them. For detailed log filtering using the new identifiers, see Event-Driven Ansible log filtering.

## Event-Driven Ansible log filtering

Event-Driven Ansible includes tracking identifiers in all log output to significantly improve troubleshooting. These identifiers help track user actions and activation processes across multiple services and log files.

*Table 1. Event\-Driven Ansible log tracking IDs*

| Identifier                 | Abbreviation | Purpose                                                                                                                                                                              | Location                                                                                                              |
| -------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| <br>X-REQUEST-ID           | <br> `rid`   | <br>Tracks HTTP requests from the platform gateway through the entire Event-Driven Ansible request lifecycle. Use this to correlate UI actions or API calls with backend processing. | <br>Included in the HTTP response headers and Event-Driven Ansible log entries.                                       |
| <br>Log Tracking ID        | <br> `tid`   | <br>Tracks the **activation lifecycle** from creation through completion, persisting across restarts and multiple log files.                                                         | <br>Included in all activation-related log entries. It can be obtained from the activation **History** tab in the UI. |
| <br>Activation Instance ID | <br> `aiid`  | <br>Identifies the logs specific to a single execution instance of a rulebook activation, allowing you to view `ansible-rulebook` output for that run.                               | <br>Included in activation logs.                                                                                      |


Note:

Not all processes originate from a user or external client. When an Event-Driven Ansible orchestrator internally triggers a process (for example, a monitor request), the `rid` UUID is generated internally to track that process lifecycle and will not be present in the platform gateway logs.

The enhanced log format places these identifiers at the start of the message, making them easy to filter:

```
`[rid: <UUID>] [tid: <UUID>] [aiid: <ID>] aap_eda.tasks.orchestrator Processing request...`
```

## Use log filtering for troubleshooting

Learn to filter logs using specialized tracking identifiers for efficient troubleshooting of activation issues and API request lifecycles.

### Procedure

1.   **Collect identifiers:**   1.  When an issue occurs, retrieve the **Log Tracking ID** (`tid`) from the failed activation instance’s logs in the UI **History tab**.
  2.  If the issue was triggered by a user action (like restarting an activation), obtain the **X-REQUEST-ID** (`rid`) from the HTTP response headers.
2.   **Search system logs:**   1.  Use the collected UUID to search through your backend logs (worker, scheduler, API, and the like.). This filters out irrelevant noise, allowing you to focus on the full timeline of the specific request or activation across all services.
3.   **Correlate timeline:**   1.  Use the common `tid` to follow the activation’s progress (or failure) across different log files and services.
4.   **Use support tools:**   1.  If necessary, use `sosreport` or `mustgather` tools, which automatically collect all relevant Event-Driven Ansible logs from `/var/log/ansible-automation-platform/eda/`.

## Resolve rulebook activations stuck in pending state

Diagnose and resolve issues preventing a rulebook activation from transitioning from Pending to a running, operational state.

### Procedure

 Confirm whether there are other running activations and if you have reached the limits (for example, memory or CPU limits). 1.  If there are other activations running, terminate one or more of them, if possible.
2.  If not, verify that the `dispatcherd` service and the PostgreSQL database are running and reachable.

  - Use the `dispatcherctl alive` command to verify the health and availability of background task workers.
  - Check the status of the **PostgreSQL** service to ensure it can accept connections, as a database failure will prevent activations from transitioning out of the Pending state.

3.  If all systems are working as expected, check your eda-server internal logs in the worker, scheduler, API, and nginx containers and services to see if the problem can be determined. These logs reveal the source of the issue, such as an exception thrown by the code, a runtime error with network issues, or an error with the rulebook code. If your internal logs do not provide information that leads to resolution, report the issue to Red Hat support.

## Fix rulebook activations stuck in a restart loop

Troubleshoot rulebook activations that restart repeatedly (indicating persistent errors) to diagnose and fix core issues preventing stable, continuous automation execution.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Decisions> (and then)Rulebook Activations.
3.  From the **Rulebook Activations** page, select the activation in your list that keeps restarting. The Details page is displayed.
4.  Click the **History** tab for more information and select the rulebook activation that keeps restarting. The Details tab is displayed and shows the output information.
5.  Check the **Restart policy** field for your activation. There are three selections available: **On failure** (restarts a rulebook activation when the container process fails), **Always** (always restarts regardless of success or failure with no more than 5 restarts), or **Never** (never restarts when the container process ends).

  1.  Confirm that your rulebook activation Restart policy is set to **On failure**. This is an indication that an issue is causing it to fail.
  2.  To possibly diagnose the problem, check the YAML code and the instance logs of the rulebook activation for errors.
  3.  If you cannot find a solution with the restart policy values, proceed to the next steps related to the **Log level**.

6.  Check your log level for your activation.   1.  If your default log level is **Error**, go back to the **Rulebook Activation** page and recreate your activation following procedures in [Setting up rulebook a activation](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_rulebook_activations#eda-set-up-rulebook-activation "Create a rulebook activation to link a rulebook to a decision environment and event sources, initiating the event-driven automation process.").
  2.  Change the **Log level** to **Debug**.
  3.  Run the activation again and navigate to the **History** tab from the activation details page.
  4.  On the **History** page, click one of your recent activations and view the **Output**.

## Resolve event processing failures in rulebook activations

Troubleshoot why a running rulebook activation is failing to process events, focusing on common causes like source definition mismatches or internal processing errors.

### Procedure

1.  **Check the rulebook source:** Review the source plugin defined in your rulebook YAML (for example, ansible.eda.webhook, ansible.eda.kafka).
2.  **Verify event input:** Confirm that the events you are sending to Event-Driven Ansible controller are compatible with the source plugin defined in the rulebook. If the rulebook expects a Kafka message, it cannot process a generic webhook event.
3.  **Confirm activation mapping:** If you are using event streams, ensure the correct event stream is mapped to the rulebook during the activation setup. A mismatch here will result in the activation receiving no data.

## Troubleshoot actions that fail to trigger after receiving events

If your rulebook activation is **Running** and successfully receiving events, but no actions are being executed, the issue is likely within the logic of your rulebook.

### Procedure

1.  **Check rule conditions:** Review the rulebook YAML to confirm that the conditions (the when statements) are accurately written and precisely match the structure and values of the incoming event payload.
2.  **Verify indentation and syntax:** Ensure all rulebook syntax and indentation are correct, as a simple error can prevent the rule engine from evaluating conditions.
3.  **Validate actions:** Confirm that the specified action is a recognized and correctly configured action (for example, `run_job_template` with the proper arguments).

## Troubleshoot event streams that fail to send events

Diagnose issues where an event stream is receiving data but failing to forward it, ensuring proper connectivity and correct credential setup.

### Procedure

 Try the following options to resolve this. 1.  Ensure that each of your event streams in Event-Driven Ansible controller is *not* in **Test** mode . This means activations would not receive the events.
2.  Verify that the origin service is sending the request properly.
3.  Check that the network connection to your platform gateway instance is stable. If you have set up event streams, this is the entry of the event stream request from the sender.
4.  Verify that the proxy in the platform gateway is running.
5.  Confirm that the event stream worker is up and running, and able to process the request.
6.  Verify that your credential is correctly set up in the event stream.
7.  Confirm that the request complies with the authentication mechanism determined by the set credential (for example, basic must contain a header with the credentials or HMAC must contain the signature of the content in a header, and similar). Note:
      The credentials might have been changed in Event-Driven Ansible controller, but not updated in the origin service.

8.  Verify that the rulebook that is running in the activation reacts to these events. This would indicate that you wrote down the event source *and* added actions that consume the events coming in. Otherwise, the event does reach the activation but there is nothing to activate it.
9.  If you are using self-signed certificates, you might want to disable certificate validation when sending webhooks from vendors. Most of the vendors have an option to disable certificate validation for testing or non-production environments.
