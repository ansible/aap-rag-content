+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_simplified_event_routing"
template = "docs/aem-title.html"
title = "Respond to events from external systems - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_eda_user_guide_overview/", "Trigger automation from events with Event-Driven Ansible"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_simplified_event_routing/aem-page/administer-assembly_simplified_event_routing.html"
last_crumb = "Respond to events from external systems"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Respond to events from external systems"
oversized = "false"
page_slug = "administer-assembly_simplified_event_routing"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-assembly_simplified_event_routing"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_simplified_event_routing/toc/toc.json"
type = "aem-page"
+++

# Respond to events from external systems

Simplified event routing provides Event-Driven Ansible controller the capability to capture and analyze data from various remote systems (like GitHub or GitLab) using event streams. You can attach one or more event streams to an activation by swapping out sources in a rulebook.

Event streams simplify connecting sources to rulebooks. This capability enables the creation of a single endpoint to receive alerts from an event source for utilization in multiple rulebooks.

## Event streams

Event streams provide the secure, authenticated entry point for external systems to send events over the internet directly to Event-Driven Ansible controller,simplifying remote data ingestion.

Event-Driven Ansible controller supports six different event stream types.

*Table 1. Event Stream Types*

| Type                                                   | Description                                                                                                                                                                                                                                                                                | Vendor examples        |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| <br>Hashed Message Authentication Code (HMAC)          | <br>Uses a shared secret between Event-Driven Ansible controller and the vendors webhook server. This guarantees message integrity.                                                                                                                                                        | <br>Github             |
| <br>Basic Authentication                               | <br>Uses HTTP basic authentication.                                                                                                                                                                                                                                                        | <br>Datadog, Dynatrace |
| <br>Token Authentication                               | <br>Validates incoming event data using a security token passed in the request header. While the standard HTTP header used is **Authorization**, it can be customized for specific platforms, such as using **X-Gitlab-Token** for GitLab integrations.                                    | <br>Gitlab, ServiceNow |
| <br>OAuth2                                             | <br>Uses Machine-to-Machine (M2M) mode with a grant type called **client credentials**. The token is opaque.                                                                                                                                                                               | <br>Dynatrace          |
| <br>OAuth2 with JWT                                    | <br>Uses M2M mode with a grant type called **client credentials**. The token is JSON Web Token (JWT).                                                                                                                                                                                      | <br>Datadog            |
| <br>Elliptic Curve Digital Signature Algorithm (ECDSA) | <br>Verifies message authenticity using a public/private key pair. The sender signs the message with a private key, and the receiver (Event-Driven Ansible controller) validates it with a public key.                                                                                     | <br>SendGrid, Twilio   |
| <br>Mutual Transport Layer Security (mTLS)             | <br>Ensures two-way authentication between Event-Driven Ansible controller and the client sending events through an event stream. It has two sub-types:<br>CertificateSubject<br>Needs the vendor’s CA certificate to be present in our servers at startup. This supports non-repudiation. | <br>PagerDuty          |


 Important:

If you are using an mTLS event stream with a load balancer, you must enable SSL pass-through (or L4 routing) in your load balancer configuration.

This is required because the SSL termination and client certificate validation for mTLS must occur at the platform gateway proxy server. Consult your load balancer documentation for details on enabling SSL pass-through.

Event-Driven Ansible controller also supports four other specialized event streams that are based on the six basic event stream types:

- GitLab event stream
- GitHub event stream
- ServiceNow event stream
- Dynatrace event stream


These specialized types limit the parameters you use by adding default values. For example, the GitHub event stream is a specialization of the HMAC event stream with many of the fields already populated. After the GitHub event stream credential has been saved, the recommended defaults for this event stream are displayed.

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

## Create an event stream

Create a dedicated stream endpoint to simplify how external systems send events, making it easier to route data to multiple rulebook activations.

### Before you begin

- If you will be attaching your event stream to a rulebook activation, ensure that your activation has a decision environment and project already set up.
- If you plan to connect to automation controller to run your rulebook activation, ensure that you have created a Red Hat Ansible Automation Platform credential type in addition to the decision environment and project. For more information, see [Setting up a Red Hat Ansible Automation Platform credential](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_set_up_rhaap_credential#eda-set-up-rhaap-credential-type "When Event-Driven Ansible controller is deployed on Ansible Automation Platform, you can create a Red Hat Ansible Automation Platform credential to connect to automation controller through the use of an automation controller URL and a username and password.").

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
      If your automation relies on HTTP headers being present in the event payload, you must explicitly define them to avoid unintentional exposure of sensitive information. For more information about HTTP headers and how to securely configure them, see [HTTP headers](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_simplified_event_routing#eda-http-headers "In the context of Event-Driven Ansible and event streams, HTTP headers play a significant role because they carry the necessary context and security information about the incoming event from a third-party source (for example, GitHub, a monitoring tool, or a proprietary webhook).") and [Configuring HTTP headers securely for event streams](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_simplified_event_routing#eda-configure-http-headers "To enhance event stream security, you must explicitly define which HTTP headers are passed. These headers carry the critical context and authentication data required for processing.").

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

## HTTP headers

In the context of Event-Driven Ansible and event streams, HTTP headers play a significant role because they carry the necessary context and security information about the incoming event from a third-party source (for example, GitHub, a monitoring tool, or a proprietary webhook).

They include the following capabilities:

Authentication and non-repudiation
This is the most critical use. Headers often contain tokens, API keys, or security signatures (like an HMAC in an `X-Hub-Signature` header) that Event-Driven Ansible uses to *verify the sender’s identity* and ensure the event payload has not been tampered with. This supports non-repudiation—proof that the event came from a legitimate source.

Debugging and Logging
Headers provide crucial data points (`Date`, `User-Agent`, `X-Request-ID`) for tracing the event’s path, helping system administrators and SREs *debug* issues related to delayed or failed event processing.

Headers are essential for all HTTP communication, serving several distinct purposes:

- **Context and metadata:** Describe the data being sent (for example, `Content-Type: application/json, Content-Length: 1024`).
- **Client/Server Capabilities:** Inform the receiving party of the sender’s capabilities or preferences (for example, `Accept-Language: en-US`).
- **Authentication/Authorization:** Carry security credentials (for example, `Authorization: Bearer <token>`).
- **Caching:** Controls how content should be cached by clients and proxies (for example, `Cache-Control: max-age=3600`).
- **Routing and Tracking:** They facilitate network routing and transaction tracking, often via custom headers (for example, `X-Request-ID`).

## Configuring HTTP headers securely for event streams

To enhance event stream security, you must explicitly define which HTTP headers are passed. These headers carry the critical context and authentication data required for processing.

### Procedure

1.  To include all HTTP headers, enter an asterisk (*) in the Headers field. This allows all HTTP headers with the exception of a few headers:

  - **Excluded:** Headers that begin with `X-Envoy`, `X-Trusted-Proxy`, `X-Forwarded-For`, and `X-Real-Id`
  - **Redacted:** Authorization header (for example, `Authorization: Redacted`)
     Important:
            If the **Headers** field is empty, none of the HTTP headers will be added to the event payload in Production and Test mode.

2.  To include a specific set of HTTP headers, enter the names of the desired headers as a comma-delimited string (for example, `Host,Authorization,X-Request-ID`).

## Static Unique Universal Identifiers (UUIDs) for event streams

You can configure an event stream with a static Unique Universal Identifier (UUID) to ensure its webhook URL remains consistent, even if the event stream service is recreated.

This feature is relevant for disaster recovery scenarios where external systems, like firewalls or third-party webhooks, cannot be easily reconfigured to use a new URL. Here are key concepts when considering using static UUIDs:

Disaster recovery support
A static UUID ensures that the external webhook URL, which follows the format, `https://your-eda-server.com/api/eda/v1/external_event_stream/{uuid}/`, does not change upon service recreation.

Uniqueness
The UUID you provide must be unique across all existing event streams in the system.

Security warning
Static UUIDs make your webhook URLs predictable and, therefore, could reduce security. Only use this feature when URL consistency is critical and you have implemented strong additional security measures (like strong authentication and network restrictions). For normal operations, always use autogenerated (dynamic) UUIDs.

You must ensure that additional security measures are in place, such as robust credential types (HMAC, mTLS) and network restrictions.

## Update an event stream with a static UUID (API Method)

Access the API to set a static UUID, a feature critical for maintaining webhook URL consistency across service recreations, such as in disaster recovery scenarios.

### Before you begin

- Ansible Automation Platform 2.6-next

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Overview.
3.  In the URL, replaceOverview with the API endpoint, `api/eda/v1/` (for example, `https://<gateway-host>/api/eda/v1/`). The `Api V1 Root` page displays a list of Event-Driven Ansible resource URLs.

```
{
    "config": "http://<gateway-host>/api/eda/v1/config/",
    "status": "http://<gateway-host>/api/eda/v1/status/",
    "openapi-json": "http://<gateway-host>/api/eda/v1/openapi.json",
    "openapi-yaml": "http://<gateway-host>/api/eda/v1/openapi.yaml",
    "openapi-docs": "http://<gateway-host>/api/eda/v1/docs/",
    "openapi-redoc": "http://<gateway-host>/api/eda/v1/redoc/",
    "session-login": "http://<gateway-host>/api/eda/v1/auth/session/login/",
    "session-logout": "http://<gateway-host>/api/eda/v1/auth/session/logout/",
    "token-refresh": "http://<gateway-host>/api/eda/v1/auth/token/refresh/",
    "current-user": "http://<gateway-host>/api/eda/v1/users/me/",
    "project-list": "http://<gateway-host>/api/eda/v1/projects/",
    "rulebook-list": "http://<gateway-host>/api/eda/v1/rulebooks/",
    "activation-list": "http://<gateway-host>/api/eda/v1/activations/",
    "activationinstance-list": "http://<gateway-host>/api/eda/v1/activation-instances/",
    "auditrule-list": "http://<gateway-host>/api/eda/v1/audit-rules/",
    "user-list": "http://<aap.platform>/api/eda/v1/users/",
    "controller-token-list": "http://<gateway-host>/api/eda/v1/users/me/awx-tokens/",
    "credentialtype-list": "http://<gateway-host>/api/eda/v1/credential-types/",
    "edacredential-list": "http://<gateway-host>/api/eda/v1/eda-credentials/",
    "credentialinputsource-list": "http://<gateway-host>/api/eda/v1/credential-input-sources/",
    "decisionenvironment-list": "http://<gateway-host>/api/eda/v1/decision-environments/",
    "organization-list": "http://<gateway-host>/api/eda/v1/organizations/",
    "team-list": "http://<gateway-host>/api/eda/v1/teams/",
    "eventstream-list": "http://<gateway-host>/api/eda/v1/event-streams/"
```

4.  At the end of the list, click the `eventstream-list` URL. This takes you to the Event Stream List page.
5.  Locate and copy the `“id”` of the event stream UUID that you want to update. This can be found at the end of the event stream data.

```
},
"id": *1*,
"owner": "admin",
"url": "https://<platformURL>/eda-event-streams/api/eda/v1/external_event_stream/bab8dddd-51cc-424f-87a4-0ed8ebe0a755/post/",
"created_at": "2025-11-18T16:30:45.622363Z",
"modified_at": "2025-11-18T16:30:45.622374Z",
"test_content_type": "",
"test_content": "",
"test_error_message": "",
"test_headers": "",
"events_received": 0,
"last_event_received_at": null
```

6.  Paste the id at the end of the URL (for example, `https://<platformURL>.com/api/eda/v1/<id#>`) and press **Enter**. The **Event Stream Instance** page is displayed, including the current `“uuid”` value.
7.  In the form at the end of the **Event Stream Instance** page, update the value of the `“uuid”` field to a unique static string of your choice.
8.  Click **Patch**.

### Results

- Confirm that the UUID of your event stream has been updated to the new static string.

## Configure your remote system to send events

After you have created your event stream, you must configure your remote system to send events to Event-Driven Ansible controller. The method used for this configuration varies, depending on the vendor for the event stream credential type you select.

### Before you begin

- The URL that was generated when you created your event stream
- Secrets or passwords that you set up in your event stream credential

### About this task

The following example demonstrates how to configure webhooks in a remote system like GitHub to send events to Event-Driven Ansible controller. Each vendor will have unique methods for configuring your remote system to send events to Event-Driven Ansible controller.

### Procedure

1.  Log in to your GitHub repository.
2.  Click **Your profile name → Your repositories**.  Note:
      If you do not have a repository, click **New** to create a new one, select an owner, add a **Repository name**, and click **Create repository**.

3.  Navigate to **Settings** (tool bar).
4.  In the **General** navigation pane, select **Webhooks**.
5.  Click **Add webhook**.
6.  In the **Payload URL** field, paste the URL you saved when you created your event stream.
7.  Select **application/json** in the **Content type** list.
8.  Enter your **Secret**.
9.  Click **Add webhook**.

### Results

After the webhook has been added, it attempts to send a test payload to ensure there is connectivity between the two systems (GitHub and Event-Driven Ansible controller). If it can successfully send the data, you will see a green check mark next to the **Webhook URL** with the message, **Last delivery was successful**.

## Verify your event streams work

Confirm end-to-end event flow by verifying the event stream receives data from the remote system, validating the webhook URL and authentication setup.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Decisions> (and then)Event Streams.
3.  Select the event stream that you created to validate connectivity and ensure that the event stream sends data to the rulebook activation.
4.  Verify that the events were received. The number of **Events received** is displayed along with a header that contains details about the event. If you scroll down in the UI, you can also see the body of the payload with more information about the webhook.

    The **Header** and **Body** sections for the event stream are displayed on the Details page. They differ based on the vendor who is sending the event. The header and body can be used to check the attributes in the event payload, which will help you in writing conditions in your rulebook.

5.  Toggle the **Forward events to rulebook activation** option to enable you to push your events to a rulebook activation.

### Results

This moves the event stream to production mode and makes it easy to attach to rulebook activations. When this option is toggled off, your ability to forward events to a rulebook activation is disabled and the **This event stream is disabled** message is displayed.

## Replace sources and attach event streams to activations

Replace complex source mappings with pre-configured event streams to simplify rulebook activation design and centralize incoming event routing.

### About this task

There are several key points to keep in mind regarding source mapping:

1. An event stream can only be used once in a rulebook source swap. If you have multiple sources in the rulebook, you can only replace each source once.
2. The source mapping happens only in the current rulebook activation. You must repeat this process for any other activations using the same rulebook.
3. The source mapping is valid only if the rulebook doesn’t get modified. If the rulebook gets modified during the source mapping process, the source mapping would fail and it would have to be repeated.
4. If the rulebook is modified after the source mapping has been created and a **Restart** happens, the rulebook activation fails.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Decisions> (and then)Rulebook Activations.
3.  Click Create rulebook activation.
4.  Insert the following:
  

Name
Insert the name.

Description
This field is optional.

Organization
Enter your organization name or select Default from the list.

Project
Projects are a logical collection of rulebooks. This field is optional.

   Note:
      Although this field is optional, selecting a project helps refine your list of rulebooks choices.

Rulebook
Rulebooks are shown according to the project selected. Select a rulebook.

   Note:
      After you have selected a rulebook, the Event streams field is enabled. You can click the gear icon to display the Event streams mapping form.

Event streams
All the event streams available and set up to forward events to rulebook actiavtions are displayed. If you have not created any event streams, this field remains disabled.

    Click the gear icon to display the Event streams mapping UI.

     ![Event streams mapping UI](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/eda-latest-event-streams-mapping.png)

    Complete the following fields:

Rulebook source
A rulebook can contain multiple sources across multiple rulesets. You can map the same rulebook in multiple activations to multiple event streams. While managing event streams, unnamed sources are assigned temporary names (__SOURCE {n}) for identification purposes.

    Select __SOURCE_1 from the list.

Event stream
Select your event stream name from the list.

    Click Save.

    Event streams can replace matching sources in a rulebook, and are server-side webhooks that enable you to connect various event sources to your rulebook activations. Source types that can be replaced with the event stream’s source of type ansible.eda.pg_listener include ansible.eda.webhook and other compatible webhook source plugins. Replacing selected sources affects this activation only, and modifies the rulebook’s source type, source name, and arguments. Filters, rules, conditions, and actions are all unaffected.

    You can select which source you want to replace with a single event stream. If there are multiple sources in your rulebook, you can choose to replace each one of them with event streams, but you are not required to replace each one. The following image displays which sources can be replaced.

     ![Event streams replacement sources](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/eda-event-streams-swapping-sources.png)

    The items in pink demonstrate the sources that can be replaced: source type, source name, and arguments. The remaining items (filters, rules, and actions) are not replaced.

Credential
Select 0 or more credentials for this rulebook activation. This field is optional.

   Note:
      The credentials that display in this field are customized based on your rulebook activation and only include the following credential types: Vault, Red Hat Ansible Automation Platform, or any custom credential types that you have created. For more information on credentials, see [Credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials "You can use credentials to store secrets that can be used for authentication purposes with resources, such as decision environments, rulebook activations and projects for Event-Driven Ansible controller, and projects for automation controller.").

Decision environment
A decision environment is a container image used to run Ansible rulebooks.

   Note:
      In Event-Driven Ansible controller, you cannot customize the pull policy of the decision environment. By default, it follows the behavior of the always policy. Every time an activation is started, the system tries to pull the most recent version of the image.

Restart policy
This is the policy that determines how an activation should restart after the container process running the source plugin ends.

  - Policies:
    1. **Always**: This restarts the rulebook activation immediately, regardless of whether it ends successfully or not, and occurs no more than 5 times.
    2. **Never**: This never restarts a rulebook activation when the container process ends.
    3. **On failure**: This restarts the rulebook activation after 60 seconds by default, only when the container process fails, and occurs no more than 5 times.

Log level
This field defines the severity and type of content in your logged events.

  - Levels:
    1. **Error**: Logs that contain error messages that are displayed in the **History** tab of an activation.
    2. **Info**: Logs that contain useful information about rulebook activations, such as a success or failure, triggered action names and their related action events, and errors.
    3. **Debug**: Logs that contain information that is only useful during the debug phase and might be of little value during production. This log level includes both error and log level data.

Service name
This defines a service name for Kubernetes to configure inbound connections if the activation exposes a port. This field is optional.

Rulebook activation enabled?
This automatically enables the rulebook activation to run.

Variables
The variables for the rulebook are in a JSON or YAML format. The content would be equivalent to the file passed through the `--vars` flag of ansible-rulebook command.

Options
Check the **Skip audit events** option if you do not want to see your events in the Rule Audit.

5.  Click Create rulebook activation.

### Results

After you create your rulebook activation, the **Details** page is displayed. You can navigate to the **Event streams** page to confirm your events have been received.
