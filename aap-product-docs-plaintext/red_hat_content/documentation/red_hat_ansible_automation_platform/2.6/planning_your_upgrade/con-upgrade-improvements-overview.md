# 1. Overview of upgrade improvements
## 1.1. Upgrade path details

Ansible Automation Platform 2.6 includes changes that improve the overall platform upgrade experience.

- [Upgrading from 2.5 to 2.6](#from-2.5)
- [Upgrading from 2.4 to 2.6](#from-2.4)

Note

You must be on the latest version of 2.4 or 2.5 before you upgrade to 2.6.

Upgrading from 2.5 to 2.6
Upgrading from 2.5 to 2.6 does not involve changes to the platform infrastructure requirements, architecture, or services. The improvements described in the 2.4 to 2.6 upgrade path are also present in the 2.5 to 2.6 upgrade path; however, the platform gateway service is already in place in 2.5.

Additionally, note the following:

- If you upgraded from 2.4 to 2.5, you must migrate your authentication methods and users before upgrading to 2.6 as that legacy authenticator functionality was removed.
- When you upgrade to 2.6, the system removes any users that the 2.4 to 2.5 upgrade did not fully migrate. The users that have previously merged their user records while on 2.5 will remain to function as is for 2.6.
- Upgrading to 2.6 prevents 2.4 automation controller users who never successfully logged into 2.5 from logging into the platform-gateway. These users retain backwards compatibility for direct Automation Execution access but cannot access the full platform. Ensure all users planning to use 2.6 have successfully logged into 2.5 before upgrading.
- Unified RBAC management across Ansible Automation Platform components: All Ansible Automation Platform collections, which support the Configuration-as-Code (CaC) approach, now use a standard global environment variable name and module variable name across Ansible Automation Platform components. For more details, see [What’s new around RBAC in 2.6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/release_notes), [What’s changed around RBAC for users moving from 2.5 to 2.6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/release_notes), and [`ansible.platform`](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/platform/) documentation in automation hub.

For more information about upgrading, see the upgrade document for your deployment type:

- [Containerized](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-infrastructure-changes#container_based_deployments)

- [RPM](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-infrastructure-changes#rpm_based_deployments)

- [OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-infrastructure-changes#operator_based_deployments)


Note
Upgrades from the latest 2.5 version to 2.6 are supported with all deployment types: RPM, containerized, and OpenShift Container Platform deployments.

Upgrading from 2.4 to 2.6
Note the following when upgrading from 2.4 to 2.6:

- **Upgrades from 2.4**: Ansible Automation Platform supports upgrading directly from the latest 2.4 version to 2.6. Directly upgrading to 2.6 is the recommended upgrade path from 2.4, as several improvements in 2.6 simplify and improve the upgrade experience.


Note
You can upgrade directly from the latest 2.4 version to 2.6 with RPM and OpenShift Container Platform deployments. However, upgrading Event-Driven Ansible 2.4 or from the 2.4 containerized deployment is not supported, as both features were Tech Preview in 2.4.

For more information, see the upgrade document for your deployment type. Either [RPM](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-support-matrix#upgrade-scenarios-rpm), or [OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-support-matrix#upgrade-scenarios-openshift).

- **Infrastructure changes**: Ansible Automation Platform RPM deployments require additional infrastructure compared with 2.4, due to the addition of the platform gateway service. Infrastructure needs vary depending on factors such as whether you implement a growth or an enterprise deployment.

For details about infrastructure and inventory file changes in various upgrade scenarios, see [Infrastructure changes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-infrastructure-changes).

- **Authentication changes**: Enterprise authentication configuration and mappings (for example, SAML, LDAP, OIDC) move from automation controller 2.4 to platform gateway 2.6 as part of the upgrade process. You do not need to manually reconfigure these authentication methods after you upgrade.

See [Access management and authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/index) for information about authentication options in general.


Note
Authentication upgrade improvements apply to RPM and OpenShift Container Platform deployments. Upgrades from the 2.4 containerized deployment Tech Preview release are not supported. Additionally, upgrading Event-Driven Ansible 2.4 is not supported.

- **Identify access management changes**: All automation controller Identity Access Management (IAM) data moves from automation controller 2.4 to the platform gateway in 2.6 as part of the upgrade process. With automation controller 2.4 as the default source of IAM data for the platform gateway in 2.6, users retain their memberships and are assigned appropriate platform-level roles in 2.6.

As part of the upgrade process:


- Users, teams, organizations, their memberships, and common roles in 2.4 move from automation controller 2.4 to the platform gateway in 2.6.

- Administrators in automation controller 2.4 become platform gateway administrators in 2.6.

- Controller admins in 2.4 become platform gateway admins in 2.6.

The more organizations, teams, and users being migrated during an upgrade, the longer the upgrade takes. As an example, upgrading and migrating 4,000 users, 400 teams, and 40 organizations can take close to two hours.


Note
Identity access management changes apply to RPM and OpenShift Container Platform deployments. Upgrades from the 2.4 containerized deployment Tech Preview release are not supported.

See [Data movement during upgrade](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-data-movement) for more information.

- **API changes**: Some APIs are being deprecated in 2.6. See [API changes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/planning_your_upgrade/index#upgrade-api-changes) for more information.

- **Unified RBAC management across Ansible Automation Platform components**: All Ansible Automation Platform collections, which support the Configuration-as-Code (CaC) approach, now use a standard global environment variable name and module variable name across Ansible Automation Platform components. For more details, see [What’s new around RBAC in 2.6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/release_notes), [What’s changed around RBAC for users moving from 2.5 to 2.6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/release_notes), and [`ansible.platform`](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/platform/) documentation in automation hub.

