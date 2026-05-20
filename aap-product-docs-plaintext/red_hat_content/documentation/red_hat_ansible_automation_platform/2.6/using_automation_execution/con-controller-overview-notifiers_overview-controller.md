# 1. Automation controller overview
## 1.11. Integrated notifications

Keep track of the status of your automation.

You can configure the following notifications:

- stackable notifications for job templates, projects, or entire organizations
- different notifications for job start, job success, job failure, and job approval (for workflow nodes)

The following notification sources are supported:

- [Email](#controller-notification-email "25.4.1.&nbsp;Email")
- [Grafana](#controller-notification-grafana "25.4.2.&nbsp;Grafana")
- [IRC](#controller-notification-irc "25.4.3.&nbsp;IRC")
- [Mattermost](#controller-notification-mattermost "25.4.4.&nbsp;Mattermost")
- [PagerDuty](#controller-notification-pagerduty "25.4.5.&nbsp;Pagerduty")
- [Rocket.Chat](#controller-notification-rocketchat "25.4.6.&nbsp;Rocket.Chat")
- [Slack](#controller-notification-slack "25.4.7.&nbsp;Slack")
- [Twilio](#controller-notification-twilio "25.4.8.&nbsp;Twilio")
- [Webhook](#controller-notification-webhook "25.4.9.&nbsp;Webhook") (post to an arbitrary webhook, for integration into other tools)

You can also customize notification messages for each of the preceding notification types.

