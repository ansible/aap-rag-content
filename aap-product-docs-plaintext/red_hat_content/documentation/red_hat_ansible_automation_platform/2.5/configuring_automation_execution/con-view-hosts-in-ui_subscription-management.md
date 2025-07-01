# 11. Subscription management in Ansible Automation Platform and automation controller
## 11.3. Keeping your subscription in compliance
### 11.3.1. Viewing hosts automated in the user interface




**Procedure**

1. In the navigation panel, selectAutomation Analytics→Host Metricsto view the activity associated with hosts, such as those that have been automated and deleted.

Each unique hostname is listed and sorted by the user’s preference. image::ug-host-metrics.png[Host metrics]

Note
A scheduled task automatically updates these values on a weekly basis and deletes jobs with hosts that were last automated more than a year ago.




1. Delete unnecessary hosts directly from the Host Metrics view by selecting the desired hosts and clickingDelete.

These are soft-deleted, meaning their records are not removed, but are not being used and thereby not counted towards your subscription.




For more information, see [Configuring automation execution](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution) /index#controller-keep-subscription-in-compliance[Keeping your subscription in compliance].

