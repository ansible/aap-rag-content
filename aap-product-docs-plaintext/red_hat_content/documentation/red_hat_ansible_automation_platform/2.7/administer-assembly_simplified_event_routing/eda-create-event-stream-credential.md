# Respond to events from external systems
## Create an event stream credential

Create a credential to establish the authentication mechanism (like basic auth or HMAC) required for external systems to securely send events to an event stream.

### Before you begin

- Each event stream must have exactly one credential.

### Procedure

1.  Log in to the Ansible Automation Platform Dashboard.
2.  From the navigation panel, select Automation Decisions> (and then)Infrastructure> (and then)Credentials.
3.  Click Create credential.
4.  Insert the following:


Name
Insert the name.

Description
This field is optional.

Organization
Click the list to select an organization or select **Default**.

Credential type
Click the list to select your Credential type.

Note:
When you select the credential type, the **Type Details** section is displayed with fields that are applicable for the credential type you selected.

Type Details
Add the requested information for the credential type you selected. For example, if you selected the GitHub Event Stream credential type, you are required to add an HMAC Secret (symmetrical shared secret) between Event-Driven Ansible controller and the remote server.

5.  Click Create credential.

### Results

The Details page is displayed. From there or the **Credentials** list view, you can edit or delete it.

