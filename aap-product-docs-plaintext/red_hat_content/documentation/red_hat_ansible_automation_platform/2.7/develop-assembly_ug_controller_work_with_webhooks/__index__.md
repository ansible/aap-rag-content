# Trigger automation with webhooks

Use webhooks to run specified commands between applications over the web. Automation controller currently provides webhook integration with GitHub and GitLab.

Set up a webhook using GitHub or GitLab, then view the payload output.

The webhook post-status-back functionality for GitHub and GitLab is designed to work only under certain CI events. Receiving another kind of event results in messages such as the following in the service log:

`awx.main.models.mixins Webhook event did not have a status API endpoint associated, skipping.`

