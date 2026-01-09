# 10. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 10.3. Prerequisites




To upgrade to a newer version of Ansible Automation Platform Operator, you must:

- Ensure your system meets the system requirements detailed in the [Operator topologies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/ocp-topologies) section of the _Tested deployment models_ guide.
- Create AutomationControllerBackup and AutomationHubBackup objects. For help with this see [Backup and recovery for operator environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/backup_and_recovery_for_operator_environments)
- Review the [Release notes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/release_notes) for the new Ansible Automation Platform version to which you are upgrading and any intermediate versions.
- Determine the type of upgrade you want to perform. See the [Channel Upgrades](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#operator-channel-upgrade_operator-upgrade) section for more information.


