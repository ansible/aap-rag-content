# Create a notification template

Use the following procedure to create a notification template.

## Procedure

1.  From the navigation panel, select Automation Execution> (and then)Administration> (and then)Notifiers.
2.  Click Add notifier.
3.  Complete the following fields:

- **Name**: Enter the name of the notification.
- **Description**: Enter a description for the notification. This field is optional.
- **Organization**: Specify the organization that the notification belongs to.
- **Type**: Choose a type of notification from the drop-down menu. For more information, see the [Notification types](/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-proc_controller_create_notification_template#controller-notification-types "Automation controller supports multiple notification types that you can use to send notifications about job status and other events.") section.

4.  Click Save notifier.

## Notification types

Automation controller supports multiple notification types that you can use to send notifications about job status and other events.

The following notification types are supported with automation controller:

- Email
- Grafana
- IRC
- Mattermost
- PagerDuty
- Rocket.Chat
- Slack
- Twilio
- Webhook


Each notification type has its own configuration and behavioral semantics. You might need to test them in different ways. Additionally, you can customize each type of notification down to a specific detail or a set of criteria to trigger a notification.

### Email

The email notification type supports a wide variety of SMTP servers and has support for SSL/TLS connections.

Provide the following details to set up an email notification:

-  **Host**
-  **Recipient list**
-  **Sender e-mail**
-  **Port**
- **Timeout** (in seconds): You can set this up to 120 seconds. This is the length of time that automation controller tries to connect to the email server before failure.

![Notification template email](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-notification-template-email.png)

### Grafana

You can configure automation controller to send notifications to Grafana.

To integrate Grafana, you must first create an API key in the [Grafana system](http://docs.grafana.org/tutorials/api_org_token_howto/). This is the token that is given to automation controller.

Provide the following details to set up a Grafana notification:

- **Grafana URL**: The URL of the Grafana API service, such as: http://yourcompany.grafana.com.
- **Grafana API key**: You must first create an API key in the Grafana system.
- Optional: **ID of the dashboard**: When you create an API key for the Grafana account, you can set up a dashboard with a unique ID.
- Optional: **ID of the panel**: If you added panels and graphs to your Grafana interface, you can give its ID here.
- Optional: **Tags for the annotation**: Enter keywords to identify the types of events of the notification that you are configuring.
- **Disable SSL verification**: SSL/TLS verification is on by default, but you can turn off verification of the authenticity of the target’s certificate. Select this option to disable verification for environments that use internal or private CA’s.

![Notification template Grafana](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-notification-template-grafana.png)

### IRC

You can configure automation controller to send notifications by using IRC (Internet Relay Chat).

The IRC notification takes the form of an IRC bot that connects, delivers its messages to channels or individual users, and then disconnects. The notification bot also supports SSL/TLS authentication. The bot does not currently support Nickserv identification. If a channel or user does not exist or is not online then the notification fails. The failure scenario is reserved specifically for connectivity.

Provide the following details to set up an IRC notification:

- Optional: **IRC server password**: IRC servers can require a password to connect. If the server does not require one leave it blank. **IRC Server Port**: The IRC server port. **IRC Server Address**: The hostname or address of the IRC server. **IRC Nick**: The bot’s nickname once it connects to the server. **Destination Channels or Users**: A list of users or channels to which the notification is sent.
- Optional: **Disable SSL verification**: Check if you want the bot to use SSL/TLS when connecting.

![Notification template IRC](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-notification-template-irc.png)

### Mattermost

The Mattermost notification type provides a simple interface to Mattermost’s messaging and collaboration workspace.

Provide the following details to set up a Mattermost notification:

- **Target URL**: The full URL that is posted to.
- Optional: **Username**: Enter a username for the notification.
- Optional: **Channel**: Enter a channel for the notification.
- **Icon URL**: Specifies the icon to display for this notification.
- **Disable SSL verification**: Turns off verification of the authenticity of the target’s certificate. Select this option to disable verification for environments that use internal or private CA’s.

![Notification template Mattermost](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-notification-template-mattermost.png)

### Pagerduty

To integrate Pagerduty, you must first create an API key in the [PagerDuty system](http://docs.grafana.org/tutorials/api_org_token_howto/). This is the token that is given to automation controller. Then create a **Service** which provides an **Integration Key** that is also given to automation controller.

Provide the following details to set up a Pagerduty notification:

- **API Token**: You must first create an API key in the Pagerduty system. This is the token that is given to automation controller.
- **PagerDuty subdomain**: When you sign up for the Pagerduty account, you receive a unique subdomain to communicate with. For example, if you signed up as "testuser", the web dashboard is at `testuser.pagerduty.com` and you give the API `testuser` as the subdomain, not the full domain.
- **API service/Integration Key**: Enter the API service/integration key created in Pagerduty.
- **Client Identifier**: This is sent along with the alert content to the Pagerduty service to help identify the service that is using the API key and service. This is helpful if multiple integrations are using the same API key and service.

![Notification template Pagerduty](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-notification-template-pagerduty.png)

### Rocket.Chat

The Rocket.Chat notification type provides an interface to Rocket.Chat’s collaboration and communication platform.

Provide the following details to set up a Rocket.Chat notification:

- **Target URL**: The full URL that is `POSTed` to.
- Optional: **Username**: Enter a username.
- Optional: **Icon URL**: Specifies the icon to display for this notification
- **Disable SSL Verification**: Turns off verification of the authenticity of the target’s certificate. Select this option to disable verification for environments that use internal or private CA’s.

![Notification template rocketchat](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-notification-template-rocketchat.png)

### Slack

Slack is a collaborative team communication and messaging tool.

Give the following details to set up a Slack notification:

- A Slack application. For more information, see the [Quickstart](https://api.slack.com/authentication/basics) page of the Slack documentation on how to create one.
- **Token**: A token. For more information, see [Legacy bots](https://api.slack.com/legacy/enabling-bot-users) and specific details on bot tokens on the [Current token types](https://api.slack.com/authentication/token-types#bot) documentation page.
- **Destination Channel**: One Slack channel per line. The pound symbol (#) is required for channels. To respond to or start a thread to a specific message add the parent message Id to the channel where the parent message Id is 16 digits. A dot (.) must be manually inserted after the 10th digit. For example, :#destination-channel, 1231257890.006423.
- **Notification color**: Specify a notification color. Acceptable colors are hex color code, for example: #3af or #789abc. When you have a bot or app set up, you must complete the following steps:
1. Go to **Apps**.
2. Click the newly-created app and then go to **Add features and functionality**, which enables you to configure incoming webhooks, bots, and permissions, and **Install your app to your workspace**.

![Notification template slack](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-notification-template-slack.png)

### Twilio

Configure automation controller to send notifications by using Twilio.

Twilio is a voice and SMS automation service. When you are signed in, you must create a telephone number from which the messages are sent. You can then define a **Messaging Service** under **Programmable SMS** and associate the number you previously created with it.

You might need to verify this number or some other information before you are permitted to use it to send to any numbers. The **Messaging Service** does not require a status callback URL and it does not need the ability to process inbound messages.

Under your individual (or sub) account settings, you have API credentials. Twilio uses two credentials to determine which account an API request is coming from. The **Account SID**, which acts as a username, and the **Auth Token** which acts as a password.

Provide the following details to set up a Twilio notification:

- **Account SID**: Enter the account SID.
- **Account Token**: Enter the account token.
- **Source Phone Number**: Enter the number associated with the messaging service in the form of "+15556667777".
- **Destination SMS Numbers**: Enter the list of numbers you want to receive the SMS. It must be a 10 digit telephone number.

![Notification template Twilio](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-notification-template-twilio.png)

### Webhook

The webhook notification type provides a simple interface for sending `POSTs` to a predefined web service.

Automation controller `POSTs` to this address by using application and JSON content type with the data payload containing the relevant details in JSON format. Some web service APIs expect HTTP requests to be in a certain format with certain fields.

Configure the webhook notification with the following:

- Configure the HTTP method, usingBasic authentication `PUT`.
- The body of the outgoing request.
- Configure authentication, using Basic authentication.


Provide the following details to set up a webhook notification:

- Optional: **Username**: Enter a username.
- Optional: **Basic auth password**:
- **Target URL**: Enter the full URL to which the webhook notification is `PUT` or `POSTed`.
- **HTTP Headers**: Enter Headers in JSON format where the keys and values are strings. For example:

```
{"Authentication": "988881adc9fc3655077dc2d4d757d480b5ea0e11", "MessageType": "Test"}`.
```


- **Disable SSL Verification**: SSL/TLS verification is on by default, but you can choose to turn off verification of the authenticity of the target’s certificate. Select this option to disable verification for environments that use internal or private CA’s.
- **HTTP Method**: Select the method for your webhook:
- **POST**: Creates a new resource. It also acts as a catch-all for operations that do not fit into the other categories. It is likely that you need to **POST** unless you know your webhook service expects a **PUT**.
- **PUT**: Updates a specific resource (by an identifier) or a collection of resources. You can also use **PUT** to create a specific resource if the resource identifier is known beforehand.

![Notification template webhook](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-notification-template-webhook.png)
