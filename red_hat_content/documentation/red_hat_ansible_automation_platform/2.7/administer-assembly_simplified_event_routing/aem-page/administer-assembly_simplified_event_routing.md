+++
title = "Respond to events from external systems - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_user_guide_overview/", "Trigger automation from events with Event-Driven Ansible"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing/aem-page/administer-assembly_simplified_event_routing.html"
last_crumb = "Respond to events from external systems"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Respond to events from external systems"
oversized = "false"
page_slug = "administer-assembly_simplified_event_routing"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing/toc/toc.json"
type = "aem-page"
+++

# Respond to events from external systems

Simplified event routing provides Event-Driven Ansible controller the capability to capture and analyze data from various remote systems (like GitHub or GitLab) using event streams. You can attach one or more event streams to an activation by swapping out sources in a rulebook.

Event streams simplify connecting sources to rulebooks. This capability enables the creation of a single endpoint to receive alerts from an event source for utilization in multiple rulebooks.

## Event streams

Event streams provide the secure, authenticated entry point for external systems to send events over the internet directly to Event-Driven Ansible controller, simplifying remote data ingestion.

Event-Driven Ansible controller supports six different event stream types.

*Table 1. Event Stream Types*

| Type                                                   | Description                                                                                                                                                                                              | Vendor examples        |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| <br>Hashed Message Authentication Code (HMAC)          | <br>Uses a shared secret between Event-Driven Ansible controller and the vendors webhook server. This guarantees message integrity.                                                                      | <br>Github             |
| <br>Basic Authentication                               | <br>Uses HTTP basic authentication.                                                                                                                                                                      | <br>Datadog, Dynatrace |
| <br>Token Authentication                               | <br>Validates incoming event data using a security token passed in the request header. While the standard HTTP header used is **Authorization**, it can be customized for specific platforms, such as using **X-Gitlab-Token** for GitLab integrations. | <br>Gitlab, ServiceNow |
| <br>OAuth2                                             | <br>Uses Machine-to-Machine (M2M) mode with a grant type called **client credentials**. The token is opaque.                                                                                             | <br>Dynatrace          |
| <br>OAuth2 with JWT                                    | <br>Uses M2M mode with a grant type called **client credentials**. The token is JSON Web Token (JWT).                                                                                                    | <br>Datadog            |
| <br>Elliptic Curve Digital Signature Algorithm (ECDSA) | <br>Verifies message authenticity using a public/private key pair. The sender signs the message with a private key, and the receiver (Event-Driven Ansible controller) validates it with a public key.   | <br>SendGrid, Twilio   |
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

### Create an event stream credential

Create a credential to establish the authentication mechanism (like basic auth or HMAC) required for external systems to securely send events to an event stream.

#### Before you begin

- Each event stream must have exactly one credential.

#### Procedure

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

#### Results

The Details page is displayed. From there or the **Credentials** list view, you can edit or delete it.

### Create an event stream

Create a dedicated stream endpoint to simplify how external systems send events, making it easier to route data to multiple rulebook activations.

#### Before you begin

- If you will be attaching your event stream to a rulebook activation, ensure that your activation has a decision environment and project already set up.
- If you plan to connect to automation controller to run your rulebook activation, ensure that you have created a Red Hat Ansible Automation Platform credential type in addition to the decision environment and project. For more information, see [Setting up a Red Hat Ansible Automation Platform credential](/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_eda_set_up_rhaap_credential "When Event-Driven Ansible controller is deployed on Ansible Automation Platform, you can create a Red Hat Ansible Automation Platform credential to connect to automation controller through the use of an automation controller URL and a username and password.").

#### Procedure

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
      If your automation relies on HTTP headers being present in the event payload, you must explicitly define them to avoid unintentional exposure of sensitive information. For more information about HTTP headers and how to securely configure them, see [HTTP headers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing#eda-http-headers "In the context of Event-Driven Ansible and event streams, HTTP headers play a significant role because they carry the necessary context and security information about the incoming event from a third-party source (for example, GitHub, a monitoring tool, or a proprietary webhook).") and [Configuring HTTP headers securely for event streams](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing#eda-configure-http-headers "To enhance event stream security, you must explicitly define which HTTP headers are passed. These headers carry the critical context and authentication data required for processing.").

Forward events to rulebook activation
Use this option to enable or disable the capability of forwarding events to rulebook activations.

   Note:
      The event stream’s event forwarding can be disabled for testing purposes while diagnosing connections and evaluating the incoming data. Disabling the **Forward events to rulebook activation** option allows you to test the event stream connection with the remote system, analyze the header and payload, and if necessary, diagnose credential issues. This ensures that events are not be forwarded to rulebook activations causing rules and conditions to be triggered inadvertently while you are in test mode. Some enterprises might have policies to change secrets and passwords at regular cadence. You can enable/disable this option anytime after the event stream is created.

5.  Click Create event stream.

#### Results

After creating your event stream, the following outputs occur:

- The Details page is displayed. From there or the Event Streams list view, you can edit or delete it. Also, the Event Streams page shows all of the event streams you have created and the following columns for each event: **Events received**, **Last event received**, and **Event stream type**. As the first two columns receive external data through the event stream, they are continuously updated to let you know they are receiving events from remote systems.
- If you disabled the event stream, the Details page is displayed with a warning message, **This event stream is disabled**.  Note:
      After an event stream is created, the associated credential cannot be deleted until the event stream it is attached to is deleted.

- Your new event stream generates a URL that is necessary when you configure the webhook on the remote system that sends events.

### HTTP headers

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

### Configuring HTTP headers securely for event streams

To enhance event stream security, you must explicitly define which HTTP headers are passed. These headers carry the critical context and authentication data required for processing.

#### Procedure

1.  To include all HTTP headers, enter an asterisk (*) in the Headers field. This allows all HTTP headers with the exception of a few headers:

  - **Excluded:** Headers that begin with `X-Envoy`, `X-Trusted-Proxy`, `X-Forwarded-For`, and `X-Real-Id`
  - **Redacted:** Authorization header (for example, `Authorization: Redacted`)
     Important:
            If the **Headers** field is empty, none of the HTTP headers will be added to the event payload in Production and Test mode.

2.  To include a specific set of HTTP headers, enter the names of the desired headers as a comma-delimited string (for example, `Host,Authorization,X-Request-ID`).

### Static Unique Universal Identifiers (UUIDs) for event streams

You can configure an event stream with a static Unique Universal Identifier (UUID) to ensure its webhook URL remains consistent, even if the event stream service is recreated.

This feature is relevant for disaster recovery scenarios where external systems, like firewalls or third-party webhooks, cannot be easily reconfigured to use a new URL. Here are key concepts when considering using static UUIDs:

Disaster recovery support
A static UUID ensures that the external webhook URL, which follows the format, `https://your-eda-server.com/api/eda/v1/external_event_stream/{uuid}/`, does not change upon service recreation.

Uniqueness
The UUID you provide must be unique across all existing event streams in the system.

Security warning
Static UUIDs make your webhook URLs predictable and, therefore, could reduce security. Only use this feature when URL consistency is critical and you have implemented strong additional security measures (like strong authentication and network restrictions). For normal operations, always use autogenerated (dynamic) UUIDs.

You must ensure that additional security measures are in place, such as robust credential types (HMAC, mTLS) and network restrictions.

### Update an event stream with a static UUID (API Method)

Access the API to set a static UUID, a feature critical for maintaining webhook URL consistency across service recreations, such as in disaster recovery scenarios.

#### Before you begin

- Ansible Automation Platform 2.6-next

#### Procedure

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

#### Results

- Confirm that the UUID of your event stream has been updated to the new static string.

### Configure your remote system to send events

After you have created your event stream, you must configure your remote system to send events to Event-Driven Ansible controller. The method used for this configuration varies, depending on the vendor for the event stream credential type you select.

#### Before you begin

- The URL that was generated when you created your event stream
- Secrets or passwords that you set up in your event stream credential

#### About this task

The following example demonstrates how to configure webhooks in a remote system like GitHub to send events to Event-Driven Ansible controller. Each vendor will have unique methods for configuring your remote system to send events to Event-Driven Ansible controller.

#### Procedure

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

#### Results

After the webhook has been added, it attempts to send a test payload to ensure there is connectivity between the two systems (GitHub and Event-Driven Ansible controller). If it can successfully send the data, you will see a green check mark next to the **Webhook URL** with the message, **Last delivery was successful**.

### Verify your event streams work

Confirm end-to-end event flow by verifying the event stream receives data from the remote system, validating the webhook URL and authentication setup.

#### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Decisions> (and then)Event Streams.
3.  Select the event stream that you created to validate connectivity and ensure that the event stream sends data to the rulebook activation.
4.  Verify that the events were received. The number of **Events received** is displayed along with a header that contains details about the event. If you scroll down in the UI, you can also see the body of the payload with more information about the webhook.

    The **Header** and **Body** sections for the event stream are displayed on the Details page. They differ based on the vendor who is sending the event. The header and body can be used to check the attributes in the event payload, which will help you in writing conditions in your rulebook.

5.  Toggle the **Forward events to rulebook activation** option to enable you to push your events to a rulebook activation.

#### Results

This moves the event stream to production mode and makes it easy to attach to rulebook activations. When this option is toggled off, your ability to forward events to a rulebook activation is disabled and the **This event stream is disabled** message is displayed.

### Replace sources and attach event streams to activations

Replace complex source mappings with pre-configured event streams to simplify rulebook activation design and centralize incoming event routing.

#### About this task

There are several key points to keep in mind regarding source mapping:

1. An event stream can only be used once in a rulebook source swap. If you have multiple sources in the rulebook, you can only replace each source once.
2. The source mapping happens only in the current rulebook activation. You must repeat this process for any other activations using the same rulebook.
3. The source mapping is valid only if the rulebook doesn’t get modified. If the rulebook gets modified during the source mapping process, the source mapping would fail and it would have to be repeated.
4. If the rulebook is modified after the source mapping has been created and a **Restart** happens, the rulebook activation fails.

#### Procedure

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

     ![Event streams mapping UI](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/eda-latest-event-streams-mapping.png)

    Complete the following fields:

Rulebook source
A rulebook can contain multiple sources across multiple rulesets. You can map the same rulebook in multiple activations to multiple event streams. While managing event streams, unnamed sources are assigned temporary names (__SOURCE {n}) for identification purposes.

    Select __SOURCE_1 from the list.

Event stream
Select your event stream name from the list.

    Click Save.

    Event streams can replace matching sources in a rulebook, and are server-side webhooks that enable you to connect various event sources to your rulebook activations. Source types that can be replaced with the event stream’s source of type ansible.eda.pg_listener include ansible.eda.webhook and other compatible webhook source plugins. Replacing selected sources affects this activation only, and modifies the rulebook’s source type, source name, and arguments. Filters, rules, conditions, and actions are all unaffected.

    You can select which source you want to replace with a single event stream. If there are multiple sources in your rulebook, you can choose to replace each one of them with event streams, but you are not required to replace each one. The following image displays which sources can be replaced.

     ![Event streams replacement sources](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/eda-event-streams-swapping-sources.png)

    The items in pink demonstrate the sources that can be replaced: source type, source name, and arguments. The remaining items (filters, rules, and actions) are not replaced.

Credential
Select 0 or more credentials for this rulebook activation. This field is optional.

   Note:
      The credentials that display in this field are customized based on your rulebook activation and only include the following credential types: Vault, Red Hat Ansible Automation Platform, or any custom credential types that you have created. For more information on credentials, see [Credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_eda_credentials "You can use credentials to store secrets that can be used for authentication purposes with resources, such as decision environments, rulebook activations and projects for Event-Driven Ansible controller, and projects for automation controller.").

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

#### Results

After you create your rulebook activation, the **Details** page is displayed. You can navigate to the **Event streams** page to confirm your events have been received.

### Event buses

An event bus enables Event-Driven Ansible to consume events from a message broker, providing a resilient and scalable integration pattern for high-volume event processing.

An event bus is a messaging infrastructure pattern where events are published to a central broker and consumed by one or more subscribers. In Event-Driven Ansible, the Kafka source plugin in the ansible.eda collection enables rulebook activations to consume events directly from Apache Kafka topics. Other supported event buses, such as Azure Service Bus, are available in the certified content collections available in Automation Hub (see the following **Related information** section).

When your event-driven integrations require added resiliency, use an event bus to connect to external sources. Unlike webhooks, which depend on a direct point-to-point connection between the sender and Event-Driven Ansible, an event bus decouples the event producer from the consumer. Events persist in the broker until they are consumed, reducing the risk of lost events during network disruptions or Event-Driven Ansible restarts.

#### AVRO support for Kafka event sources configuration

Event-Driven Ansible supports consuming Kafka messages encoded in standard formats including JSON and AVRO. AVRO is an industry-standard serialization format used in large-scale data platforms and data engineering pipelines. Compared to JSON, AVRO provides smaller message payloads and built-in schema evolution with compatibility management, making it suitable for high-volume environments where data schemas change over time.

There are several benefits of using AVRO with Kafka in Event-Driven Ansible:

- AVRO provides smaller payloads compared to JSON, which is relevant for high-volume event streams.
- Schema evolution and compatibility management are built into AVRO, making it suitable for environments where data schemas change frequently.
- Many enterprise Kafka deployments use AVRO as their standard serialization format.

For environments that use AVRO as their serialization standard, the Kafkasource plugin supports three schema resolution modes in a *deserialization fallback chain*:

- **Schema Registry**
- **Local schema file**
- **Avro Object Container Format (OCF) messages** (self-describing)

#### Create a Kafka-Avro custom credential type

Create a custom credential type for the Kafka source plugin to securely inject Kafka, SSL, Avro, and Schema Registry parameters into rulebook activations at runtime.

##### Before you begin

You must have System administrator (superuser) permissions to create and edit a credential type.

##### About this task

A sample Event-Driven Ansible credential type for this plugin is included in the `ansible.eda` collection at extensions/eda/plugins/event_source/credential_types/kafka-avro/. A new credential type must be created manually in the Event-Driven Ansible controller UI.

##### Procedure

1.  From the navigation panel, select Automation Decisions> (and then)Infrastructure> (and then)Credential Types
2.  Click **Create credential type**.
3.  Insert the following:
  

**Name**
Insert the name.

**Description**
This field is optional.

4.  In the Input Configuration field, specify an input schema that defines a set of ordered fields for that type. The format can be in YAML or JSON as in the following example:
  

```
---
# EDA Kafka Avro + Schema Registry — Custom Credential Type (Input)
fields:
  # --- Kafka Broker ---
  - id: host
    type: string
    label: Kafka Host
    default: localhost
    help_text: The host where the Kafka broker is running.
  - id: port
    type: string
    label: Kafka Port
    default: "9092"
    help_text: The port where the Kafka broker is listening.
  - id: topic
    type: string
    label: Topic
    help_text: The Kafka topic to subscribe to.
  - id: group_id
    type: string
    label: Group ID
    help_text: A Kafka consumer group ID.
  - id: offset
    type: string
    label: Reading Offset
    choices:
      - earliest
      - latest
    default: latest
    help_text: Where to automatically reset the offset.

    # --- Security Protocol ---
  - id: security_protocol
    type: string
    label: Security Protocol
    choices:
      - PLAINTEXT
      - SSL
      - SASL_PLAINTEXT
      - SASL_SSL
    default: PLAINTEXT
    help_text: Protocol used to communicate with the Kafka broker.
  - id: sasl_mechanism
    type: string
    label: SASL Mechanism
    choices:
      - PLAIN
      - GSSAPI
      - SCRAM-SHA-256
      - SCRAM-SHA-512
      - OAUTHBEARER
    default: PLAIN
    help_text: >-
      Authentication mechanism when security_protocol is SASL_PLAINTEXT or
      SASL_SSL.
  - id: sasl_plain_username
    type: string
    label: SASL Username
    help_text: Username for SASL PLAIN or SCRAM authentication.
  - id: sasl_plain_password
    type: string
    label: SASL Password
    secret: true
    help_text: Password for SASL PLAIN or SCRAM authentication.

    # --- SSL / mTLS ---
  - id: cafile
    type: string
    label: CA Certificate
    multiline: true
    help_text: >-
      PEM-encoded CA certificate(s) used to verify the Kafka broker.
      Paste the certificate content here.
  - id: certfile
    type: string
    label: Client Certificate
    multiline: true
    help_text: >-
      PEM-encoded client certificate for mTLS authentication.
      Paste the certificate content here.
  - id: keyfile
    type: string
    label: Client Key
    multiline: true
    secret: true
    help_text: >-
      PEM-encoded client private key for mTLS authentication.
      Paste the key content here.
  - id: password
    type: string
    label: Client Key Password
    secret: true
    help_text: Password for the encrypted Kafka client key file.
  - id: check_hostname
    type: boolean
    label: Check Hostname
    default: true
    help_text: Enable SSL hostname verification.
  - id: verify_mode
    type: string
    label: Verify Mode
    choices:
      - CERT_NONE
      - CERT_OPTIONAL
      - CERT_REQUIRED
    default: CERT_REQUIRED
    help_text: How to verify the broker's SSL certificate.

    # --- Avro ---
  - id: message_format
    type: string
    label: Message Format
    choices:
      - json
      - avro
    default: json
    help_text: >-
      Deserialization format for Kafka message values. Set to 'avro' to enable
      Avro deserialization.
  - id: avro_schema_file
    type: string
    label: Avro Schema
    multiline: true
    help_text: >-
      Avro schema definition in JSON format. Paste the .avsc content here.  
      Required when message_format is 'avro' and messages are in raw binary
      format (no Schema Registry).

    # --- Schema Registry ---
  - id: schema_registry_url
    type: string
    label: Schema Registry URL
    help_text: >-
     URL of a Confluent-compatible Schema Registry (e.g.,
     https://registry.example.com:8081).
  - id: schema_registry_basic_auth
    type: string
    label: Schema Registry Basic Auth
    secret: true
    help_text: Basic auth credentials in 'user:password' format.
  - id: schema_registry_bearer_token
    type: string
    label: Schema Registry Bearer Token
    secret: true
    help_text: Static bearer or JWT token for Schema Registry authentication.
  - id: schema_registry_oauth_client_id
    type: string
    label: Schema Registry OAuth Client ID
    help_text: OAuth 2.0 client ID for Schema Registry (Client Credentials flow).
  - id: schema_registry_oauth_client_secret
    type: string
    label: Schema Registry OAuth Client Secret
    secret: true
    help_text: OAuth 2.0 client secret for Schema Registry authentication.
  - id: schema_registry_oauth_token_url
    type: string
    label: Schema Registry OAuth Token URL
    help_text: OAuth 2.0 token endpoint URL for obtaining access tokens.
  - id: schema_registry_oauth_scope
    type: string
    label: Schema Registry OAuth Scope
    help_text: OAuth 2.0 scope to request when obtaining access tokens.
  - id: schema_registry_ssl
    type: boolean
    label: Schema Registry SSL
    default: true
    help_text: >-
     When true, reuse the Kafka SSL settings (cafile, certfile, keyfile) for Schema Registry HTTPS connections.
  - id: schema_registry_cafile
    type: string
    label: Schema Registry CA Certificate
    multiline: true
    help_text: >-
      PEM-encoded CA certificate for Schema Registry HTTPS. When blank, the Kafka CA certificate is reused.
  - id: schema_registry_certfile
    type: string
    label: Schema Registry Client Certificate
    multiline: true
    help_text: >-
     PEM-encoded client certificate for mTLS with Schema Registry. When blank, the Kafka client certificate is reused.
  - id: schema_registry_keyfile
    type: string
    label: Schema Registry Client Key
    multiline: true
    secret: true
    help_text: >-
     PEM-encoded client key for mTLS with Schema Registry. When blank, the Kafka client key is reused.
  - id: schema_registry_password
    type: string
    label: Schema Registry Key Password
    secret: true
    help_text: Password for the Schema Registry client key file.
  required:
    - host
    - port
    - topic
```

5.  In the Injector Configuration field, enter environment variables or extra variables that specify the values a credential type can inject. The format can be in YAML or JSON as in the following example:
  

```
---
file:
  template.avro_schema_file: "{{ avro_schema_file }}"
  template.cafile: "{{ cafile }}"
  template.certfile: "{{ certfile }}"
  template.keyfile: "{{ keyfile }}"
  template.schema_registry_cafile: "{{ schema_registry_cafile }}"  
  template.schema_registry_certfile: "{{ schema_registry_certfile }}"
  template.schema_registry_keyfile: "{{ schema_registry_keyfile }}"extra_vars:
  check_hostname: "{{ check_hostname }}"
  kafka_avro_group_id: "{{ group_id }}"
  kafka_avro_host: "{{ host }}"
  kafka_avro_offset: "{{ offset }}"
  kafka_avro_port: "{{ port }}"
  kafka_avro_topic: "{{ topic }}"
  message_format: "{{ message_format }}"
  password: "{{ password }}"
  sasl_mechanism: "{{ sasl_mechanism }}"
  sasl_plain_password: "{{ sasl_plain_password }}"
  sasl_plain_username: "{{ sasl_plain_username }}"
  schema_registry_basic_auth: "{{ schema_registry_basic_auth }}"  
  schema_registry_bearer_token: "{{ schema_registry_bearer_token }}"
  schema_registry_oauth_client_id: "{{ schema_registry_oauth_client_id }}"
  schema_registry_oauth_client_secret: "{{ schema_registry_oauth_client_secret }}"
  schema_registry_oauth_scope: "{{ schema_registry_oauth_scope }}"
  schema_registry_oauth_token_url: "{{ schema_registry_oauth_token_url }}"
  schema_registry_ssl: "{{ schema_registry_ssl }}"
  schema_registry_url: "{{  schema_registry_url }}"
  schema_ssl_password: "{{  schema_registry_password }}"
  security_protocol: "{{ security_protocol }}"
  verify_mode: "{{ verify_mode }}"
```

6.  Click Create credential type.

##### Results

Your newly created credential type is displayed on the list of credential types.

##### What to do next

1. Verify that the newly created credential type can be selected from the Credential Type  list when creating a new credential.
2. Click the Edit icon to modify the details or delete the credential type options.  Note:
  If the Delete option is disabled, this means that the credential type is being used by a credential, and you must delete the credential type from all the credentials that use it before you can delete it.

#### Configure AVRO support for Kafka event sources

Configure the Kafka source plugin to process AVRO-encoded messages from Kafka topics using a Schema Registry, a local schema file, or self-describing Avro Object Container Format (OCF) messages.

##### Before you begin

- A Kafka broker publishing AVRO-encoded messages
- A valid Avro credential type (See[Create a Kafka-Avro custom credential type](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing#GUID-07e12b4e-84af-442e-8c47-c24301933128 "Create a custom credential type for the Kafka source plugin to securely inject Kafka, SSL, Avro, and Schema Registry parameters into rulebook activations at runtime."). )
- If using a Schema Registry: the registry URL and any required authentication credentials.
- If using a local schema file: the Avro schema definition in JSON format (`.avsc` content). You must provide this when creating a credential — either by pasting the JSON into the Avro Schema (JSON) field or uploading an `.avsc` file.

##### About this task

The Kafka source plugin uses a deserialization fallback chain to process AVRO-encoded messages.

##### Procedure

1.  In your rulebook source configuration, set message_format to `avro` for the `ansible.eda.kafka` source plugin.
2.  Configure schema resolution for your environment using one of the following options:
  - **Schema Registry:** Set `schema_registry_url` to the URL of your Confluent-compatible Schema Registry.
  - **Local schema file:** Paste the content of your `.avsc` file into the avro_schema_file field when creating the credential. The schema file must be valid JSON containing an Avro schema definition. See Configuration parameters for a full description and example.  Important:
    Do not set `avro_schema_file` when your messages use Avro OCF format. See the deserialization fallback chain in [Event buses](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_simplified_event_routing#GUID-dd4d7a8d-7a17-4c8e-839d-81c7037b6eb5 "An event bus enables Event-Driven Ansible to consume events from a message broker, providing a resilient and scalable integration pattern for high-volume event processing.") for details.

  - **Avro OCF (zero configuration):** Set only message_format: avro. No additional schema parameters are needed. Each message carries its own embedded schema.

#### Configure Schema Registry authentication

If you are using a Schema Registry, you can optionally configure authentication.

##### Procedure

 Configure one of the following mutually exclusive methods:

- **No authentication (default)**- No additional parameters are required.
- **Basic Auth** - Set schema_registry_basic_auth to your credentials in `user:password` format.
- **Bearer token** - Set schema_registry_bearer_token to your static bearer or JWT token.
- **OAuth 2.0 Client Credentials** - Set the following parameters:
  * `schema_registry_oauth_client_id `- OAuth 2.0 client ID (required)
  * `schema_registry_oauth_client_secret` - OAuth 2.0 client secret (required)
  * `schema_registry_oauth_token_url `- Token endpoint URL (required)
  * `schema_registry_oauth_scope` - Scope to request (optional)

The plugin acquires an access token from the token endpoint, caches it, and refreshes it automatically before expiry.

 Note:

The plugin raises an error if more than one method is configured.

#### Configure SSL/TLS for Schema Registry

Configure dedicated SSL/TLS certificates when your Schema Registry uses adifferent certificate authority than the Kafka broker.

##### Procedure

1.  If your Schema Registry uses HTTPS, the plugin reuses the Kafka broker's SSL settings by default (schema_registry_ssl defaults to true).
2.  If the Schema Registry uses a different CA than the Kafka broker, provide dedicated certificates:

  - `schema_ssl_cafile` - CA certificate for registry HTTPS connections
  - `schema_ssl_certfile` - Client certificate for mTLS with the registry
  - `schema_ssl_keyfile` - Client key for mTLS with the registry
  - `schema_ssl_password` - Password for the client key file (if encrypted)
   Note:
  When using OAuth 2.0 with an identity provider (Keycloak, Okta, Azure AD), the same `schema_ssl_cafile` is used for both the OAuth token endpoint and the Schema Registry API. If they use different CAs, concatenate both CA certificates into a single PEM file.

3.  

#### Configuration parameters

Avro and Schema Registry parameters enable message schema validation and deserialization in Event-Driven Ansible. These specialized settings complement the core connection parameters managed by the `ansible.eda.kafka` plugin.

 The following parameters are specific to AVRO and Schema Registryconfiguration. For general Kafka source plugin parameters (`host`, `port,` `topic`, `group_id`, `offset`, `security_protocol`, `SSL`, and `SASL` settings), see the ansible.eda.kafka plugin documentation.

| Parameter                             | Type    | Description                                                                                                                                                                                              |
| ------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `message_format`                      | string  | Deserialization format. Set to `avro` for AVRO messages. Default: `json`. Choices: `json`, `avro`.                                                                                                       |
| `avro_schema_file`                    | string  | Avro schema definition in JSON format. Do not use this file with Avro OCF messages. Can be used together with `schema_registry_url`; the local schema becomes the reader schema for Avro schema evolution. |
| `schema_registry_url`                 | string  | URL of a Confluent-compatible Schema Registry (HTTP or HTTPS).                                                                                                                                           |
| `schema_registry_basic_auth`          | string  | Basic auth credentials in `user:password` format. Mutually exclusive with bearer token and OAuth.                                                                                                        |
| `schema_registry_bearer_token`        | string  | Static bearer or JWT token. Mutually exclusive with basic auth and OAuth.                                                                                                                                |
| `schema_registry_oauth_client_id`     | string  | OAuth 2.0 client ID. Requires `_client_secret` and `_token_url`. Mutually exclusive with basic auth and bearer token.                                                                                    |
| `schema_registry_oauth_client_secret` | string  | OAuth 2.0 client secret.                                                                                                                                                                                 |
| `schema_registry_oauth_token_url`     | string  | OAuth 2.0 token endpoint URL.                                                                                                                                                                            |
| `schema_registry_oauth_scope`         | string  | OAuth 2.0 scope to request (optional).                                                                                                                                                                   |
| `schema_registry_ssl`                 | boolean | SSL configuration parameters for the Schema Registry. The `ansible.eda` collection includes a sample Event-Driven Ansible credential type at extensions/eda/plugins/event\_source/credential\_types/kafka-avro/. You must manually create a new credential type in the Event-Driven Ansible controller Credential types interface. |
| `schema_ssl_cafile`                   | string  | CA certificate for registry HTTPS. Overrides Kafka `cafile` for registry connections.                                                                                                                    |
| `schema_ssl_certfile`                 | string  | Client certificate for registry mTLS. Overrides Kafka `certfile`.                                                                                                                                        |
| `schema_ssl_keyfile`                  | string  | Client key for registry mTLS. Overrides Kafka `keyfile`.                                                                                                                                                 |
| `schema_ssl_password`                 | string  | Password for the registry client key file. Overrides Kafka `password`.                                                                                                                                   |

#### Rulebook examples

Rulebook configurations demonstrate how to integrate Event-Driven Ansible with varying Apache Avro serialization and security environments. Utilizing these exact patterns ensures robust message delivery and authorized Schema Registry access.

The following examples show how to configure the Kafka source plugin for each AVRO schema resolution mode and Schema Registry authentication method.

**Schema Registry with no authentication**

```
YAML
- ansible.eda.kafka:
    host: "localhost"
    port: "9092"
    topic: "avro-events"
    group_id: "eda-sr-consumer"
    offset: "earliest"
    message_format: "avro"
    schema_registry_url: "http://localhost:8081"
```

**Schema Registry with Basic Auth**

```
YAML
- ansible.eda.kafka:
    host: "localhost"
    port: "9092"
    topic: "avro-events"
    group_id: "eda-sr-basic"
    offset: "earliest"
    message_format: "avro"
    schema_registry_url: "https://registry.example.com:8081"
    schema_registry_basic_auth: "user:password"
```

**Schema Registry with OAuth 2.0 Client Credentials**

```
YAML
- ansible.eda.kafka:
    host: "localhost"
    port: "9092"
    topic: "avro-events"
    group_id: "eda-sr-oauth"
    offset: "earliest"
    message_format: "avro"
    schema_registry_url: "https://registry.example.com:8081"
    schema_registry_oauth_client_id: "my-client-id"
    schema_registry_oauth_client_secret: "my-client-secret"
    schema_registry_oauth_token_url: "https://auth.example.com/oauth/token"
    schema_registry_oauth_scope: "registry:read"
```

**Schema Registry with dedicated SSL certificates**

```
YAML
- ansible.eda.kafka:
    host: "kafka.example.com"
    port: "9093"
    topic: "avro-events"
    group_id: "eda-sr-ssl"
    offset: "earliest"
    security_protocol: "SSL"
    cafile: "/certs/kafka-ca.pem"
    certfile: "/certs/kafka-client.pem"
    keyfile: "/certs/kafka-client-key.pem"
    message_format: "avro"
    schema_registry_url: "https://registry.example.com:8081"
    schema_registry_ssl: true
    schema_ssl_cafile: "/certs/registry-ca.pem"
    schema_ssl_certfile: "/certs/registry-client.pem"
    schema_ssl_keyfile: "/certs/registry-client-key.pem"
```

**Schema Registry with Apicurio Registry**

```
YAML
- ansible.eda.kafka:
    host: "localhost"
    port: "9092"
    topic: "avro-events"
    group_id: "eda-apicurio"
    offset: "earliest"
    message_format: "avro"
    schema_registry_url: "https://apicurio.example.com:8080/apis/ccompat/v7"
    schema_registry_basic_auth: "user:password"
```

**Local schema file**

```
YAML
- ansible.eda.kafka:
    host: "localhost"
    port: "9092"
    topic: "avro-events"
    group_id: "eda-avro-consumer"
    offset: "earliest"
    message_format: "avro"
    avro_schema_file: "/path/to/schema.avsc"
```

**Avro OCF (self-describing messages)**

```
YAML
- ansible.eda.kafka:
    host: "localhost"
    port: "9092"
    topic: "avro-ocf-events"
    group_id: "eda-ocf-consumer"
    offset: "earliest"
    message_format: "avro"
```
