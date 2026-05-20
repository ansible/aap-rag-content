# 14. Event-Driven Ansible user scenarios
## 14.1. Simplified Event Routing using GitHub event streams
### 14.1.4. Configure your remote system to send events

Configuring a GitHub webhook establishes the outbound connection from your repository to the Red Hat Ansible Automation Platform controller. This configuration enables your remote system to transmit event data directly to your designated event stream URL.

**Procedure**

1. Go to your GitHub account to configure your event source.

2. In the top right of the GitHub page, click **Your profile name → Your repositories** and select the repository you want to configure.

3. Navigate to **Settings** in the tool bar.

4. In the left navigation, select **Webhooks**.

5. On the top right, click Add webhook to create a webhook in your GitHub repository that will send events to your event stream.

6. Complete the following fields:



Payload URL
Copy and paste the URL you saved from the event stream you created.

Content type
Select application/json from the list.

Secret
Add your secret from your event stream credential you created earlier.

SSL verification
If you’re using self-signed SSL certificates, select **Disable under SSL verification** to ensure a successful webhook connection. Otherwise, you can keep the Enable SSL verification toggled on.


Note
If you are using a test environment or SSL certifications, under SSL verification, select the **Disable** option to ensure your webhook connects successfully.

7. Click **Add webhook** to save your configuration.

**Results**

Your webhook is created, and you can return to Ansible Automation Platform.

