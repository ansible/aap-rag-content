# Chapter 4. Deprecated features




Deprecated functionality is still included in Ansible Automation Platform and continues to be supported during this version’s support cycle. However, the functionality will be removed in a future release of Ansible Automation Platform and is not recommended for new deployments.

The following table provides information about features that were deprecated in Ansible Automation Platform 2.5:

| Component | Feature |
| --- | --- |
| Access to service APIs for automation controller,
automation hub,
and Event-Driven Ansible | With the addition of platform gateway, a number of service-specific API endpoints are deprecated because their functionality will be removed or superseded with other capabilities in a future release.

Ansible Automation Platform 2.5 and 2.6 expose API access to individual services (automation controller, private automation hub, Event-Driven Ansible) to maintain compatibility with existing REST API integrations. This access will be removed in a future release.

For detailed information, see [API changes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-api-changes) in _Planning your upgrade_ . |
| Installer | The Ansible Automation Platform installer using Red Hat Enterprise Linux RPMs was deprecated (announced) in 2.5 and will be removed in Ansible Automation Platform 2.7.

The RPM installer will be supported for Red Hat Enterprise Linux 9 during the lifecycle of Ansible Automation Platform 2.6 to support migrations to existing supported topologies. Users are encouraged to migrate to the containerized topology on Red Hat Enterprise Linux or to the OpenShift Container Platform Operator installation method. See the [support matrix](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-support-matrix) for more information on upgrade and migration paths. |
| Ansible-core | ```
uri module:
- Using 'yes' or 'no' for 'follow_redirects' parameter is deprecated.
yum_repository:
- deprecated parameters:
- 'keepcache'
- 'async'
- "deltarpm_metadata_percentage"
- "gpgcakey"
- "http_caching"
- "keepalive"
- "metadata_expire_filter"
- "mirrorlist_expire"
- "protect"
- "ssl_check_cert_permissions"
- "ui_repoid_vars"`
url lookup:
- Using `yes` or `no` for `follow_redirects` parameter is deprecated.
``` |
| Execution environment | Removing `cisco.asa` from ee-supported as it is being deprecated

Removing `ibm.qradar` from ee-supported as it is being deprecated |
| Certified Collections | An `ansible.platform` collection is available as the preferred collection to replace the service-specific `ansible.controller` , `ansible.hub` , and `ansible.eda` collections. These service-specific collections will be replaced by `ansible.platform` after 2.6. |
| Ansible code bot code bot | The code bot (as described in the [Red Hat Ansible Lightspeed with IBM watsonx Code Assistant](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#using-code-bot-for-suggestions_lightspeed-user-guide) user guide) is being deprecated, and will be retired on December 31, 2025. |
| Ansible Content | Deprecation of the Notification Service for ServiceNow, which will not be supported on the ServiceNow Zurich and later releases. Support will end when the Yokohama release is end-of-life. |


