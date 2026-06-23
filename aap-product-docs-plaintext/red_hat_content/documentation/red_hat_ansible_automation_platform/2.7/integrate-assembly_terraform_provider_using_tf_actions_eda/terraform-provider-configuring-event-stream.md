# Use TF Actions with Event-Driven Ansible
## Configure an event stream for TF actions

To use TF Actions with Event-Driven Ansible, you must first configure the event stream in Ansible Automation Platform. TF actions will post events to this stream.

### Before you begin

- You have configured the AAP Terraform provider to authenticate with Ansible Automation Platform.
- You have configured the AWS Terraform provider to authenticate with Amazon Web Services. Note:
The example below uses Amazon Web Services (AWS) and requires an AWS account that might incur charges. You can adapt the pattern to use a different cloud provider.

- You have an Ansible Automation Platform inventory named **EDA Actions Demo Inventory** in the **Default** organization.
- You have job templates configured with:
* Inventory set to **EDA Actions Demo Inventory**.
* A machine credential (private key) matching a public key available in a local file.

### Procedure

1.  Log in to the Ansible Automation Platform user interface.
2.  Navigate to **Automation Decisions> (and then)Event Streams**.
3.  Click Create event stream.
4.  On the **Create event stream** page, edit the fields:

- **Name:** A descriptive, unique name for your event stream (such as `Terraform provider_Events`).
- **Organization:** Select the organization this event stream will belong to (usually `Default` or your specific organization).
- **Event stream type:** Select the type that matches how you want to receive events. **Basic Event Stream** (username/password) is supported with this integration.
- **Credential:** Select a credential that you have pre-created for authentication with this event stream.
- **Headers:** (Optional) Enter comma-separated HTTP header keys that you want to include in the event payload that gets forwarded to the rulebook. Leave this empty to include all headers.
- **Forward events to rulebook activation:** This option is typically enabled by default. Disabling it is useful for testing and diagnosing your connection and incoming data without inadvertently triggering any automation.

5.  Click Create event stream. Then navigate to **Automation Decisions> (and then)Event Streams** to verify the event stream was created and see the number of events received so far. You can also click on the specific stream to see its detailed configuration, including the organization, event stream type, associated credential, and event forwarding settings.

6.  Set up a rule book activation. Make sure to:
1.  Add the event stream to the rulebook.
2.  (Recommended) Select the **Rulebook activation enabled?** option to automatically start the activation after creation.
3.  Activate the rulebook.
7.  Select **Automation Decisions> (and then)Rulebook Activations** to verify that the rulebook is active and check its status.

