# 10. Simplified event routing
## 10.5. Verifying your event streams work




Verify that you can use your event stream to connect to a remote system and receive data.

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Decisions→Event Streams.
1. Select the event stream that you created to validate connectivity and ensure that the event stream sends data to the rulebook activation.
1. Verify that the events were received. The number of **Events received** is displayed along with a header that contains details about the event.

![Verify event streams work](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_decisions-en-US/images/81d7279d43ce002cec83527582737ca3/eda-verify-event-streams.png)


If you scroll down in the UI, you can also see the body of the payload with more information about the webhook.

The **Header** and **Body** sections for the event stream are displayed on the Details page. They differ based on the vendor who is sending the event. The header and body can be used to check the attributes in the event payload, which will help you in writing conditions in your rulebook.


1. Toggle the **Forward events to rulebook activation** option to enable you to push your events to a rulebook activation.


**Results**

This moves the event stream to production mode and makes it easy to attach to rulebook activations. When this option is toggled off, your ability to forward events to a rulebook activation is disabled and the **This event stream is disabled** message is displayed.


