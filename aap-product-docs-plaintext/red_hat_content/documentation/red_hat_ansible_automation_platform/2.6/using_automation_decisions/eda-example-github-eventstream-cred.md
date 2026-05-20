# 14. Event-Driven Ansible user scenarios
## 14.1. Simplified Event Routing using GitHub event streams
### 14.1.2. Create a GitHub event stream credential

Creating a GitHub event stream credential establishes the necessary authentication for the Red Hat Ansible Automation Platform controller to securely access your event source. This credential ensures that only authorized webhook payloads trigger your rulebook activations.

**Procedure**

1. Log in to Ansible Automation Platform.

2. Select Automation Decisions → Infrastructure → Credentials.

3. Click Create credential.

4. Insert the following:



Name
Enter the name (for example, <_Your_GitHub_Credential_Name_>).

Description
This field is optional, but for this user scenario, enter a description (for example, <_GitHub credential_>).

Organization
Select **Default** from the list.

Credential type
From the list, select **GitHub Event Stream**.

Type Details / HMAC Secret
Enter a secret value and store for future use when you [configure a GitHub webhook](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/simplified-event-routing#eda-config-remote-sys-to-events).

5. Click **Create credential** to save your credential.

