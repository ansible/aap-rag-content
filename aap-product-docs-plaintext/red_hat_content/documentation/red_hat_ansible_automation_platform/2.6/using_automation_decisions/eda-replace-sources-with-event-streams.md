# 10. Simplified event routing
## 10.6. Replacing sources and attaching event streams to activations




When you create rulebook activations, you can use event streams to swap out source mappings in rulebook activations and simplify routing from external sources to Event-Driven Ansible controller.

There are several key points to keep in mind regarding source mapping:

1. An event stream can only be used once in a rulebook source swap. If you have multiple sources in the rulebook, you can only replace each source once.
1. The source mapping happens only in the current rulebook activation. You must repeat this process for any other activations using the same rulebook.
1. The source mapping is valid only if the rulebook doesn’t get modified. If the rulebook gets modified during the source mapping process, the source mapping would fail and it would have to be repeated.
1. If the rulebook is modified after the source mapping has been created and a **Restart** happens, the rulebook activation fails.


**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Decisions→Rulebook Activations.
1. ClickCreate rulebook activation.
1. Insert the following:


1. ClickCreate rulebook activation.


**Results**

After you create your rulebook activation, the **Details** page is displayed. You can navigate to the **Event streams** page to confirm your events have been received.


