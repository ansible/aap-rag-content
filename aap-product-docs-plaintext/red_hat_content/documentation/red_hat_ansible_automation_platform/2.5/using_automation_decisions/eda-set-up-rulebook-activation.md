# 7. Rulebook activations
## 7.1. Setting up a rulebook activation




You can create and configure a rulebook activation within the Ansible Automation Platform Dashboard. This process ensures effective management and deployment of your event-driven automation.

**Prerequisites**

- You are logged in to the Ansible Automation Platform Dashboard as a Content Consumer.
- You have set up a project.
- You have set up a decision environment.


**Procedure**

1. Log in to Ansible Automation Platform.
1. Navigate to theAutomation Decisions→Rulebook Activations.
1. ClickCreate rulebook activation.
1. Insert the following:


1. ClickCreate rulebook activation.


**Results**

Your rulebook activation is now created and can be managed on the **Rulebook Activations** page.


After saving the new rulebook activation, the rulebook activation’s details page is displayed, with either a **Pending** , **Running** , or **Failed** status. From there or the **Rulebook Activations** list view, you can restart or delete it.

Note
Occasionally, when a source plugin shuts down, it causes a rulebook to exit gracefully after a certain amount of time. When a rulebook activation shuts down, any tasks that are waiting to be performed will be canceled, and an info level message is sent to the activation log. For more information, see [Rulebooks](https://ansible.readthedocs.io/projects/rulebook/en/stable/rulebooks.html#) .



