# Keep subscriptions for managed hosts in compliance
## View hosts automated in the user interface

Learn how to view and manage the hosts that have been automated in automation controller.

### Procedure

1.  In the navigation panel, select Automation Analytics> (and then)Host Metrics to view the activity associated with hosts, such as those that have been automated and deleted. Each unique hostname is listed and sorted by the user’s preference. ![Host metrics](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-host-metrics.png)

Note:
A scheduled task automatically updates these values on a weekly basis and deletes jobs with hosts that were last automated more than a year ago.

2.  Delete unnecessary hosts directly from the Host Metrics view by selecting the required hosts and clicking Delete. These are soft-deleted, meaning their records are not removed, but are not being used and thereby not counted towards your subscription.

