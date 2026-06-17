# 14. Event-Driven Ansible user scenarios
## 14.1. Simplified Event Routing using GitHub event streams
### 14.1.5. Verify your event streams work

Verifying the event stream connection confirms that the Red Hat Ansible Automation Platform controller is successfully receiving data from the remote system. This validation ensures the integration is active and ready to trigger rulebook activations.

1. From the navigation panel in Ansible Automation Platform, select Automation Decisions → Event Streams.
2. Select the event stream you created (for example, <_Your_Event_Stream_Name_>)
3. Toggle the **Forward events to rulebook activation** option in the top right to disable event forwarding. The **Disable forwarding of events** message is displayed.
4. In the **Disable forwarding of events** message window, click the **Yes, I confirm I want to disable the forwarding of events** checkbox.
5. Click Disable forwarding of events. A banner is displayed notifying you that events will not be forwarded to the rulebook activation where they are configured.
6. Verify that you received the most recent event and its associated payload.
7. In the **Repo Event Stream** that you just created, re-enable the event-forwarding capability by toggling the **Forward events to rulebook activation** option on.

