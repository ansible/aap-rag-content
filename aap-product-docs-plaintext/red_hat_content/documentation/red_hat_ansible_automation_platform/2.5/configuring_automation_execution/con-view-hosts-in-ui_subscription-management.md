# 11. Subscription management in Ansible Automation Platform and automation controller
## 11.3. Keeping your subscription in compliance
### 11.3.1. Viewing hosts automated in the user interface




**Procedure**

1. In the navigation panel, selectAutomation Analytics→Host Metricsto view the activity associated with hosts, such as those that have been automated and deleted.

Each unique hostname is listed and sorted by the user’s preference.![Host metrics](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/530c55b865c4d190d2a44c4087954223/ug-host-metrics.png)


Note
A scheduled task automatically updates these values on a weekly basis and deletes jobs with hosts that were last automated more than a year ago.




1. Delete unnecessary hosts directly from the Host Metrics view by selecting the required hosts and clickingDelete.

These are soft-deleted, meaning their records are not removed, but are not being used and thereby not counted towards your subscription.




**Additional resources**

-  [Keeping your subscription in compliance](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-subscription-management#controller-keep-subscription-in-compliance_subscription-management)


