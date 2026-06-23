# Create a notification template
## Notification types
### Slack

Slack is a collaborative team communication and messaging tool.

Give the following details to set up a Slack notification:

- A Slack application. For more information, see the [Quickstart](https://api.slack.com/authentication/basics) page of the Slack documentation on how to create one.
- **Token**: A token. For more information, see [Legacy bots](https://api.slack.com/legacy/enabling-bot-users) and specific details on bot tokens on the [Current token types](https://api.slack.com/authentication/token-types#bot) documentation page.
- **Destination Channel**: One Slack channel per line. The pound symbol (#) is required for channels. To respond to or start a thread to a specific message add the parent message Id to the channel where the parent message Id is 16 digits. A dot (.) must be manually inserted after the 10th digit. For example, :#destination-channel, 1231257890.006423.
- **Notification color**: Specify a notification color. Acceptable colors are hex color code, for example: #3af or #789abc. When you have a bot or app set up, you must complete the following steps:
1. Go to **Apps**.
2. Click the newly-created app and then go to **Add features and functionality**, which enables you to configure incoming webhooks, bots, and permissions, and **Install your app to your workspace**.

![Notification template slack](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-notification-template-slack.png)

