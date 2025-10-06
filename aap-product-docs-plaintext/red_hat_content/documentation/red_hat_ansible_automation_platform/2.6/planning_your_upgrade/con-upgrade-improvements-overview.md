# 1. Overview of upgrade improvements
## 1.1. Overview of upgrade improvements




Ansible Automation Platform 2.6 includes changes that significantly improve the upgrade experience when moving from Ansible Automation Platform 2.4 to 2.6.

Note
You must be on the latest version of 2.4 or 2.5 before you upgrade to 2.6.



| Scenario | Changes | Additional information |
| --- | --- | --- |
| Upgrading from 2.5 to 2.6 | Upgrading from 2.5 to 2.6 does not involve changes to the platform infrastructure requirements, architecture, or services. The improvements described in the 2.4 to 2.6 upgrade path are also present in the 2.5 to 2.6 upgrade path; however, the platform gateway service is already in place in 2.5.

If you upgraded from 2.4 to 2.5, you must migrate your authentication methods and users before upgrading to 2.6 as that legacy authenticator functionality was removed.

Any users that were created during the 2.4 to 2.5 upgrade that were not fully migrated will be removed from the system when upgrading to 2.6. The users that have previously merged their user records while on 2.5 will continue to function as is for 2.6.

Any 2.4 automation controller users that have not successfully logged into 2.5 since upgrading from 2.4, will be unable to log into Ansible Automation Platform UI after upgrading to 2.6. The user will be backwards compatible for direct automation execution access but unable to access the full platform. Please ensure all users planning to leverage 2.6 have successfully logged into 2.5 prior to upgrading.

**Note:** Upgrades from the latest 2.5 version to 2.6 are supported with all deployment types: RPM, containerized, and OpenShift Container Platform deployments. | See the upgrade document for your deployment type:

-  [Containerized](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/aap-containerized-installation#updating-containerized-ansible-automation-platform)
-  [RPM](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_upgrade)
-  [OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_on_openshift_container_platform/operator-upgrade_licensing-gw) |
| Upgrading from 2.4 to 2.6 | Ansible Automation Platform supports upgrading directly from the latest 2.4 version to 2.6. Directly upgrading to 2.6 is the recommended upgrade path from 2.4, as a number of improvements in 2.6 simplify and improve the upgrade experience.

**Note:** You can upgrade directly from the latest 2.4 version to 2.6 with RPM and OpenShift Container Platform deployments. However, upgrading Event-Driven Ansible 2.4 or from the 2.4 containerized deployment is not supported, as both features were Tech Preview in 2.4. | See the upgrade document for your deployment type:

-  [RPM](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_upgrade)
-  [OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_on_openshift_container_platform/operator-upgrade_licensing-gw) |
|  | Ansible Automation Platform RPM deployments require additional infrastructure compared with 2.4, due to the addition of the platform gateway service. Infrastructure needs vary depending on factors such as whether you implement a growth or an enterprise deployment.

**Note:** Additional infrastructure requirements apply only when upgrading RPM deployments. | See [Infrastructure changes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-infrastructure-changes) for details about infrastructure and inventory file changes in various upgrade scenarios. |
|  | Enterprise authentication configuration and mappings (for example, SAML, LDAP, OIDC) move from automation controller 2.4 to platform gateway 2.6 as part of the upgrade process. You do not need to manually reconfigure these authentication methods after you upgrade.

**Note:** Authentication upgrade improvements apply to RPM and OpenShift Container Platform deployments. Upgrades from the 2.4 containerized deployment Tech Preview release are not supported. Additionally, upgrading Event-Driven Ansible 2.4 is not supported. | See [Access management and authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication) for information about authentication options in general. |
|  | All automation controller Identity Access Management (IAM) data moves from automation controller 2.4 to the platform gateway in 2.6 as part of the upgrade process. With automation controller 2.4 as the default source of IAM data for the platform gateway in 2.6, users retain their memberships and are assigned appropriate platform-level roles in 2.6.

As part of the upgrade process:

- Users, teams, organizations, their memberships, and common roles in 2.4 move from automation controller 2.4 to the platform gateway in 2.6.
- Administrators in automation controller 2.4 become platform gateway administrators in 2.6.
- Controller admins in 2.4 become platform gateway admins in 2.6.


The more organizations, teams, and users being migrated during an upgrade, the longer the upgrade takes. As an example, upgrading and migrating 4,000 users, 400 teams, and 40 organizations may take close to two hours.

**Note:** Identity access management changes apply to RPM and OpenShift Container Platform deployments. Upgrades from the 2.4 containerized deployment Tech Preview release are not supported. | See [Data movement during upgrade](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-data-movement) for more information. |
|  | Some APIs are being deprecated in 2.6. | See [API changes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-api-changes) for more information. |
| Upgrading from 2.5 to 2.6 and upgrading from 2.4 to 2.6 | All Ansible Automation Platform collections, which support the Configuration-as-Code (CaC) approach, now use a standard global environment variable name and module variable name across Ansible Automation Platform components. For more details, see [What’s new around RBAC in 2.6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/release_notes) and [What’s changed around RBAC for users moving from 2.5 to 2.6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/release_notes) | See the documentation for [ansible.platform](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/platform/) in automation hub for more information. |


