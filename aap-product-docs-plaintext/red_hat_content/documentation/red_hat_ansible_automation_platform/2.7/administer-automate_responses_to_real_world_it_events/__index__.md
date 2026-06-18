# Automate actions by routing external event streams: User scenarios

The following user scenario provides end-to-end instructions for integrating event streams with rulebook activations. You can automate responses to environmental events and streamline cross-platform workflows.

Modern IT environments generate a constant flow of operational data from diverse sources. Manually responding to these events creates bottlenecks and increases the risk of human error. Event-Driven Ansible addresses these challenges by creating a direct link between event-generating sources and automated remediation or orchestration tasks.

By implementing the scenarios in this chapter, you can move beyond simple point-to-point triggers to a more cohesive automation strategy. These workflows illustrate how the Red Hat Ansible Automation Platform controller acts as a central hub, receiving payloads from external platforms and transforming them into actionable, rule-based responses. This approach reduces time-to-resolution for common incidents and ensures that your infrastructure remains synchronized with your development and operational life cycles.

## Route GitHub event streams to rulebook activations

Routing GitHub event streams allows Event-Driven Ansible controller to automatically ingest webhook payloads. This connects your repository events directly to rulebook activations, instantly triggering automated responses to code changes.

Event-driven automation relies on a consistent connection between an event source and the instructions that process those events. By using GitHub event streams, you create a secure, direct integration point for webhooks triggered by repository activities, such as pull requests, issues, or code pushes. This integration serves as the bridge between the external Git provider and the Ansible ecosystem.

Simplified event routing optimizes this connection by automatically directing incoming GitHub payloads to the appropriate rulebook activation. This architecture reduces the complexity of managing multiple webhook endpoints and ensures that the metadata from the GitHub event is accurately passed to your automation rules. This allows for near real-time responses to development workflows, such as automatically running a CI/CD playbook or updating a ticket when a branch is merged.

### Prepare your GitHub repository and platform environment

Before configuring simplified event routing, you must prepare your Red Hat Ansible Automation Platform environment and GitHub repository. Ensuring that your decision environment, credentials, and rulebooks are properly aligned prevents errors during activation.

To successfully integrate GitHub event streams with rulebook activations, verify that the following components and configurations are in place:

Decision environment
Use the image version that corresponds to your specific Ansible Automation Platform instance (for example, `de-minimal-rhel9`).

Event stream credentials
Configure credentials specifically for simplified event routing within the controller interface.

Project synchronization
Ensure your Ansible project is synced to the Git repository containing your rulebook YAML files.

Plugin compatibility
Verify that your decision environment supports the required event source plugins (for example, `eda.builtin`).

User Permissions
Confirm you have sufficient permissions to create and manage rulebook activations in the controller.

Active Event Source
A functional webhook or message bus must be configured to send signals to the controller.

Correct Namespacing
Ensure your rulebooks call current plugin namespaces (for example, using `amazon.aws` rather than deprecated `ansible.eda paths`).

Rulebook Configuration
Your rulebook must conform to the standard YAML format and specify the correct source and port (as in the following example).

**YAML**

```

---
- name: Listen for GitHub Events
hosts: all
sources:
- ansible.builtin.webhook:
port: 5000
rules:
- name: Respond to a Pull Request
condition: event.payload.action == "opened"
action:
debug:
msg: "A new pull request was opened!"
```

### Create a GitHub event stream credential

Creating a GitHub event stream credential establishes the necessary authentication for the Red Hat Ansible Automation Platform controller to securely access your event source. This credential ensures that only authorized webhook payloads trigger your rulebook activations.

#### Procedure

1.  Log in to Ansible Automation Platform.
2.  Select Automation Decisions> (and then)Infrastructure> (and then)Credentials.
3.  Click Create credential.
4.  Insert the following:


Name
Enter the name (for example, `<_Your_GitHub_Credential_Name_>`).

Description
This field is optional, but for this user scenario, enter a description (for example, `<_GitHub credential_>`).

Organization
Select Default from the list.

Credential type
From the list, select GitHub Event Stream.

Type Details / HMAC Secret
Enter a secret value and store for future use when you [configure a GitHub webhook](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing#eda-config-remote-sys-to-events "After you have created your event stream, you must configure your remote system to send events to Event-Driven Ansible controller. The method used for this configuration varies, depending on the vendor for the event stream credential type you select.").

5.  Click Create credential to save your credential.

### Create a GitHub event stream

Creating an event stream and linking it to a pre-configured credential generates a unique URL for webhook configuration. This URL serves as the dedicated endpoint for the Red Hat Ansible Automation Platform controller to receive and process incoming GitHub event payloads.

#### Procedure

1.  From the Ansible Automation Platform navigation, click Automation Decisions> (and then)Event Streams
2.  Click Create event stream.
3.  Insert the following:


Name
Enter the name of your event stream (for example, `<_Your_event_stream_>`).

Event stream type
From the list, select GitHub Event Stream. After you select your type of event stream, more fields are displayed (for example, Credential).

URL
This URL is created for the event stream. Copy it and save for use in the webhook configuration process.

Forward events to rulebook activations
Toggle this button to disable your event stream for now. Disabling this option allows you to test the allows you to configure your webhook in GitHub first and test the connection with your remote system.

4.  Click Create event stream.

Note:
Your new event stream is displayed with a banner (warning) “This event stream is disabled.” This ensures that events will not be forwarded to rulebook activations causing rules and conditions to be triggered inadvertently while you are in test mode.

5.  View the Details page of your new event stream, click Copy, and paste the URL to use when you configure your webhook.

### Configure your remote system to send events through GitHub webhooks

Configuring a GitHub webhook establishes the outbound connection from your repository to the Red Hat Ansible Automation Platform controller. This configuration enables your remote system to transmit event data directly to your designated event stream URL.

#### Procedure

1.  Go to your GitHub account to configure your event source.
2.  In the top right of the GitHub page, clickYour profile name> (and then)Your repositories and select the repository you want to configure.
3.  Navigate to Settings in the tool bar.
4.  In the left navigation, select Webhooks.
5.  On the top right, click Add webhook to create a webhook in your GitHub repository that will send events to your event stream.
6.  Complete the following fields:


Payload URL
Copy and paste the URL you saved from the event stream you created.

Content type
Select application/json from the list.

Secret
Add your secret from your event stream credential you created earlier.

SSL verification
If you’re using self-signed SSL certificates, select Disable under SSL verification to ensure a successful webhook connection. Otherwise, you can keep the Enable SSL verification toggled on.

7.  Click Add webhook to save your configuration.

#### Results

Your webhook is created, and you can return to Ansible Automation Platform.

### Verify your GitHub event streams work

Verifying the event stream connection confirms that the Red Hat Ansible Automation Platform controller is successfully receiving data from the remote system. This validation ensures the integration is active and ready to trigger rulebook activations.

#### Procedure

1.  From the navigation panel in Ansible Automation Platform, select Automation Decisions> (and then)Event Streams.
2.  Select the event stream you created (for example, `<_Your_Event_Stream_Name_>`.
3.  Toggle the Forward events to rulebook activation option in the top right to disable event forwarding. The Disable forwarding of events message is displayed.
4.  In the Disable forwarding of events message window, click the Yes, I confirm I want to disable the forwarding of events checkbox.
5.  Click Disable forwarding of events. A banner is displayed notifying you that events will not be forwarded to the rulebook activation where they are configured.
6.  Verify that you received the most recent event and its associated payload.
7.  In the Repo Event Stream that you just created, re-enable the event-forwarding capability by toggling the Forward events to rulebook activation option on.

### Replace sources and attach GitHub event streams to activations

Attaching an event stream to a rulebook activation links your incoming GitHub data to specific automation rules. This process involves selecting a project and updating the event source to subscribe to the previously configured event stream.

#### Before you begin

Ensure that your projects have been set up properly. For more information, see [Set up a new project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_projects#GUID-0372bdfb-6b7f-4de7-9a43-bd4431aab994 "Set up a project to connect Event-Driven Ansible controller to a Git repository, enabling it to pull, sync, and manage the rulebooks used by your automation.")

#### Procedure

1.  From the Ansible Automation Platform navigation panel, select Automation Decisions> (and then)Rulebook Activations.
2.  Click Create rulebook activation to create a rulebook for events on an application repository for Linux servers.
3.  In the Name field, enter the name of your rulebook (for example, `<_Your_rulebook_activation_>`).
4.  For your Organization, select Default from the list.
5.  From the Project list, select the project with access to your rulebooks.
6.  In the Rulebook field, select the )rulebook associated with your project (for example, `<_Your-rulebook.yml_>`).
7.  In the Event streams field, click the gear icon to select which event stream the rulebook needs to subscribe to. The Event streams window is displayed.
8.  In the required Rulebook source field, replace an `ansible.builtin.webhook` or compatible custom source with the desired event stream. This modifies the activation only, while leaving your filters intact.
9.  Select <_Your_event_stream_> from the list of event streams that you created.
10.  Click Save to save your event stream.
11.  Next to the Credential field, click the Search icon to access automation controller and connect with job templates and workflows. The **Select credential** message is displayed.
12.  Select the Red Hat AAP credential and click Confirm.
13.  Select the appropriate Decision Environment from the list.
14.  Click Create rulebook activation. The activation status is displayed (if successful, the Running status displays).
15.  Repeat the following steps to create an additional rulebook activation using the same process as your first activation:
1.  In the Event streams field, click the gear icon to select which event stream the rulebook needs to subscribe to.
2.  Select the Repo Event Stream from the list of event streams that you created.
3.  Click Save to save your event stream.
4.  Click Create rulebook activation to save the configuration and start the rulebook.

#### Results

Now, there are two rulebook activations running and you can commit some code to one of your repositories. An event has been received and routed to your rulebooks.

### Resend webhook data from your event stream type

Resending webhook data allows for efficient testing of new event routing configurations. This process verifies that the event stream successfully triggers the rulebook activation using existing payloads, eliminating the need to manually recreate events.

#### Procedure

1.  Go back to the GitHub Webhook / Manage webhook page.
2.  Click the Recent Deliveries tab.
3.  Click the ellipsis.
4.  Click Redeliver. A Redeliver payload window is displayed with a delivery message.
5.  Click Yes, redeliver this payload.
6.  Return to the Ansible Automation Platform to check your rule audit.

### Check the Rule Audit for events on your new event stream

Checking the Rule Audit provides a detailed record of events associated with a specific event stream. This administrative view allows for the verification of successful event processing and the inspection of actions triggered by incoming payloads.placeholder

#### Procedure

1.  From the Ansible Automation Platform navigation panel, select Automation Decisions> (and then)Rule Audit  to see the event and actions.
2.  Select the name of the event in the list that is associated with the rulebook activation you created. The Details tab is displayed.
3.  Click the Events tab to view the event details.
4.  Click the Actions tab to see what action took place.
5.  If desired, click the Name of the action and view the Details tab to check the status.

#### Results

Your code is pushed and your applications are deployed.
