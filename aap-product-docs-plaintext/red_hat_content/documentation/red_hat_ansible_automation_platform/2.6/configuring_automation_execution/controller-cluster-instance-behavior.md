# 6. Clustering
## 6.4. Instance services and failure behavior




Each automation controller instance is made up of the following different services working collaboratively:

Automation controller is configured so that if any of these services or their components fail, then all services are restarted. If these fail often in a short span of time, then the entire instance is placed offline in an automated fashion to allow remediation without causing unexpected behavior.

For backing up and restoring a clustered environment, see the [Backup and restore clustered environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/index#controller-backup-restore-clustered-environments) section.

