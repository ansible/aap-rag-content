# 14. Event-Driven Ansible user scenarios
## 14.1. Simplified Event Routing using GitHub event streams
### 14.1.6. Replace sources and attach event streams to activations

Attaching an event stream to a rulebook activation links your incoming GitHub data to specific automation rules. This process involves selecting a project and updating the event source to subscribe to the previously configured event stream.

**Prerequisites**

- Ensure that your projects have been set up properly. For more information, see [Setting up a new project](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_decisions/index#eda-set-up-new-project).

**Procedure**

1. From the Ansible Automation Platform navigation panel, select Automation Decisions → Rulebook Activations.

2. Click Create rulebook activation to create a rulebook for events on an application repository for Linux servers.

3. In the **Name** field, enter the name of your rulebook (for example, <_Your_rulebook_activation_>).

4. For your **Organization**, select **Default** from the list.

5. From the **Project** list, select the project with access to your rulebooks.

6. In the **Rulebook** field, select the )rulebook associated with your project (for example, <_Your-rulebook.yml_>).

7. In the **Event streams** field, click the gear icon to select which event stream the rulebook needs to subscribe to. The Event streams window is displayed.

8. In the required **Rulebook source** field, replace an `ansible.builtin.webhook` or compatible custom source with the desired event stream. This modifies the activation only, while leaving your filters intact.

9. Select <_Your_event_stream_> from the list of event streams that you created.

10. Click **Save** to save your event stream.

11. Next to the **Credential** field, click the **Search** icon to access automation controller and connect with job templates and workflows. The **Select credential** message is displayed.

12. Select the **AAP** credential and click **Confirm**.

13. Select the appropriate **Decision Environment** from the list.

14. Click **Create rulebook activation**. The activation status is displayed (if successful, the **Running** status displays).

15. Repeat the following steps to create an additional rulebook activation using the same process as your first activation:


1. In the **Event streams** field, click the gear icon to select which event stream the rulebook needs to subscribe to.
2. Select the **Repo Event Stream** from the list of event streams that you created.
3. Click **Save** to save your event stream.
4. Click **Create rulebook activation** to save the configuration and start the rulebook.

**Results**

Now, there are two rulebook activations running and you can commit some code to one of your repositories. An event has been received and routed to your rulebooks.

