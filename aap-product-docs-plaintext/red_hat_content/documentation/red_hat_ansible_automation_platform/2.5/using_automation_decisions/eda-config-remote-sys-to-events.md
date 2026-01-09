# 10. Simplified event routing
## 10.5. Configuring your remote system to send events




After you have created your event stream, you must configure your remote system to send events to Event-Driven Ansible controller. The method used for this configuration varies, depending on the vendor for the event stream credential type you select.

**Prerequisites**

- The URL that was generated when you created your event stream
- Secrets or passwords that you set up in your event stream credential


**Procedure**

The following example demonstrates how to configure webhooks in a remote system like GitHub to send events to Event-Driven Ansible controller. Each vendor will have unique methods for configuring your remote system to send events to Event-Driven Ansible controller.


1. Log in to your GitHub repository.
1. Click **Your profile name → Your repositories** .

Note
If you do not have a repository, click **New** to create a new one, select an owner, add a **Repository name** , and click **Create repository** .




1. Navigate to **Settings** (tool bar).
1. In the **General** navigation pane, select **Webhooks** .
1. Click **Add webhook** .
1. In the **Payload URL** field, paste the URL you saved when you created your event stream.
1. Select **application/json** in the **Content type** list.
1. Enter your **Secret** .
1. Click **Add webhook** .


**Results**

After the webhook has been added, it attempts to send a test payload to ensure there is connectivity between the two systems (GitHub and Event-Driven Ansible controller). If it can successfully send the data, you will see a green check mark next to the **Webhook URL** with the message, **Last delivery was successful** .


