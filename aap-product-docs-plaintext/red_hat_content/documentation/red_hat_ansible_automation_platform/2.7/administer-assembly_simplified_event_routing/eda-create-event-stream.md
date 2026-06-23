# Respond to events from external systems
## Create an event stream

Create a dedicated stream endpoint to simplify how external systems send events, making it easier to route data to multiple rulebook activations.

### Before you begin

- If you will be attaching your event stream to a rulebook activation, ensure that your activation has a decision environment and project already set up.
- If you plan to connect to automation controller to run your rulebook activation, ensure that you have created a Red Hat Ansible Automation Platform credential type in addition to the decision environment and project. For more information, see [Setting up a Red Hat Ansible Automation Platform credential](/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_eda_set_up_rhaap_credential "When Event-Driven Ansible controller is deployed on Ansible Automation Platform, you can create a Red Hat Ansible Automation Platform credential to connect to automation controller through the use of an automation controller URL and a username and password.").

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Decisions> (and then)Event Streams.
3.  Click Create event stream.
4.  Insert the following:


Name
Insert the name.

Organization
Click the list to select an organization or select **Default**.

Event stream type
Select the event stream type you prefer.

Note:
This list displays at least 10 default event stream types that can be used to authenticate the connection coming from your remote server.

Credentials
Select a credential from the list, preferably the one you created for your event stream.

Headers
Enter HTTP header keys, separated by commas, that you want to include in the event payload.

Important:
If your automation relies on HTTP headers being present in the event payload, you must explicitly define them to avoid unintentional exposure of sensitive information. For more information about HTTP headers and how to securely configure them, see [HTTP headers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing#eda-http-headers "In the context of Event-Driven Ansible and event streams, HTTP headers play a significant role because they carry the necessary context and security information about the incoming event from a third-party source (for example, GitHub, a monitoring tool, or a proprietary webhook).") and [Configuring HTTP headers securely for event streams](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing#eda-configure-http-headers "To enhance event stream security, you must explicitly define which HTTP headers are passed. These headers carry the critical context and authentication data required for processing.").

Forward events to rulebook activation
Use this option to enable or disable the capability of forwarding events to rulebook activations.

Note:
The event stream’s event forwarding can be disabled for testing purposes while diagnosing connections and evaluating the incoming data. Disabling the **Forward events to rulebook activation** option allows you to test the event stream connection with the remote system, analyze the header and payload, and if necessary, diagnose credential issues. This ensures that events are not be forwarded to rulebook activations causing rules and conditions to be triggered inadvertently while you are in test mode. Some enterprises might have policies to change secrets and passwords at regular cadence. You can enable/disable this option anytime after the event stream is created.

5.  Click Create event stream.

### Results

After creating your event stream, the following outputs occur:

- The Details page is displayed. From there or the Event Streams list view, you can edit or delete it. Also, the Event Streams page shows all of the event streams you have created and the following columns for each event: **Events received**, **Last event received**, and **Event stream type**. As the first two columns receive external data through the event stream, they are continuously updated to let you know they are receiving events from remote systems.
- If you disabled the event stream, the Details page is displayed with a warning message, **This event stream is disabled**.  Note:
After an event stream is created, the associated credential cannot be deleted until the event stream it is attached to is deleted.

- Your new event stream generates a URL that is necessary when you configure the webhook on the remote system that sends events.

