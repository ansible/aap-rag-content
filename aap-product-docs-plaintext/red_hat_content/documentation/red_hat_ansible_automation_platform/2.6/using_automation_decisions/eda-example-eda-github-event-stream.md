# 14. Event-Driven Ansible user scenarios
## 14.1. Simplified Event Routing using GitHub event streams
### 14.1.3. Create a GitHub event stream

Creating an event stream and linking it to a pre-configured credential generates a unique URL for webhook configuration. This URL serves as the dedicated endpoint for the Red Hat Ansible Automation Platform controller to receive and process incoming GitHub event payloads.

**Procedure**

1. From the Ansible Automation Platform navigation, click Automation Decisions → Event Streams.

2. Click **Create event stream**.

3. Insert the following:



Name
Enter the name of your event stream (for example, <_Your_event_stream_>).

Organization
Select **Default** from the list.

Event stream type
From the list, select **GitHub Event Stream**. After you select your type of event stream, more fields are displayed (for example, **Credential**).

Credential
Click the list and select the event stream credential you created in the previous steps (for example, <_Your_GitHub_Credential_Name_>).

URL
This URL is created for the event stream. Copy it and save for use in the webhook configuration process.

Forward events to rulebook activations
Toggle this button to disable your event stream for now. Disabling this option allows you to test the allows you to configure your webhook in GitHub first and test the connection with your remote system.

4. Click **Create event stream**.


Note
Your new event stream is displayed with a banner (warning) “This event stream is disabled.” This ensures that events will not be forwarded to rulebook activations causing rules and conditions to be triggered inadvertently while you are in test mode.

5. View the **Details** page of your new event stream, click Copy, and paste the URL to use when you configure your webhook.

