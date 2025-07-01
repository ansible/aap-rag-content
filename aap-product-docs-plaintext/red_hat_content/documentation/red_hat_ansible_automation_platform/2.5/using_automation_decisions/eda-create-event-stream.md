# 10. Simplified event routing
## 10.3. Creating an event stream




You can create event streams that will be attached to a rulebook activation.

**Prerequisites**

- If you will be attaching your event stream to a rulebook activation, ensure that your activation has a decision environment and project already set up.
- If you plan to connect to automation controller to run your rulebook activation, ensure that you have created a Red Hat Ansible Automation Platform credential type in addition to the decision environment and project. For more information, see [Setting up a Red Hat Ansible Automation Platform credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_decisions/index#eda-set-up-rhaap-credential) .


**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Decisions→Event Streams.
1. ClickCreate event stream.
1. Insert the following:


1. ClickCreate event stream.


After creating your event stream, the following outputs occur:

- The Details page is displayed. From there or the Event Streams list view, you can edit or delete it. Also, the Event Streams page shows all of the event streams you have created and the following columns for each event: **Events received** , **Last event received** , and **Event stream type** . As the first two columns receive external data through the event stream, they are continuously updated to let you know they are receiving events from remote systems.
- If you disabled the event stream, the Details page is displayed with a warning message, **This event stream is disabled** .
- Your new event stream generates a URL that is necessary when you configure the webhook on the remote system that sends events.


Note
After an event stream is created, the associated credential cannot be deleted until the event stream it is attached to is deleted.



