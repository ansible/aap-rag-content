# 10. Patch releases
## 10.17. Ansible Automation Platform patch release December 3, 2024
### 10.17.2. Bug fixes




#### 10.17.2.1. General




With this update, the following CVEs have been addressed:

-  [CVE-2024-52304](https://access.redhat.com/security/cve/CVE-2024-52304)  `    automation-controller` : `    aiohttp` vulnerable to request smuggling due to wrong parsing of chunk extensions.


#### 10.17.2.2. Ansible Automation Platform Operator




- With this update, missing Ansible Automation Platform Operator custom resource definitions (CRDs) are added to the `    aap-must-gather` container image.(AAP-35226)
- Disabled platform gateway authentication in the proxy configuration to prevent HTTP 502 errors when the control plane is down.(AAP-36527)
- The Red Hat favicon is now correctly displayed on automation controller and Event-Driven Ansible API tabs.(AAP-30810)
- With this update, the automation controller admin password is now reused during upgrade from Ansible Automation Platform 2.4 to 2.5.(AAP-35159)
- Fixed undefined variable ( `    _controller_enabled` ) when reconciling an `    AnsibleAutomationPlatformRestore` . Fixed automation hub Operator `    pg_restore` error on restores due to a wrong database secret being set.(AAP-35815)


#### 10.17.2.3. Automation controller




- Updated the minor version of uWSGI to obtain updated log verbiage.(AAP-33169)
- Fixed job schedules running at the wrong time when the `    rrule` interval was set to `    HOURLY` or `    MINUTELY` .(AAP-36572)
- Fixed an issue where sensitive data was displayed in the job output.(AAP-35584)
- Fixed an issue where unrelated jobs could be marked as a dependency of other jobs.(AAP-35309)
- Included pod anti-affinity configuration on default container group pod specification to optimally spread workload.(AAP-35055)


#### 10.17.2.4. Container-based Ansible Automation Platform




- With this update, you cannot change the `    postgresql_admin_username` value when using a managed database node.(AAP-36577)
- Added update support for PCP monitoring role.
- Disabled platform gateway authentication in the proxy configuration to prevent HTTP 502 errors when the control plane is down.
- With this update, you can use dedicated nodes for the Redis group.
- Fixed an issue where disabling TLS on platform gateway would cause installation to fail.
- Fixed an issue where disabling TLS on platform gateway proxy would cause installation to fail.
- Fixed an issue where platform gateway uninstall would leave container systemd unit files on disk.
- Fixed an issue where the automation hub container signing service creation failed when `    hub_collection_signing=false` but `    hub_container_signing=true` .
- Fixed an issue with the `    HOME` environment variable for receptor containers which would cause a “Permission denied” error on the containerized execution node.
- Fixed an issue where not setting up the GPG agent socket properly when many hub nodes are configured, resulted in not creating a GPG socket file in `    /var/tmp/pulp` .
- With this update, you can now change the platform gateway port value after the initial deployment.


#### 10.17.2.5. Receptor




- Fixed an issue that caused a Receptor runtime panic error.


#### 10.17.2.6. RPM-based Ansible Automation Platform




- Fixed an issue where the `    metrics-utility` command failed to run after updating automation controller.
- Fixed the owner and group permissions on the `    /etc/tower/uwsgi.ini` file.
- Fixed an issue where not having `    eda_node_type` defined in the inventory file would result in backup failure.
- Fixed an issue where not having `    routable_hostname` defined in the inventory file would result in a restore failure.
- With this update, the `    inventory-growth` file is now included in the RPM installer.
- Fixed an issue where the dispatcher service went into `    FATAL` status and failed to process new jobs after a database outage of a few minutes.
- Disabled platform gateway authentication in the proxy configuration to allow access to the UI when the control plane is down.
- With this update, the Receptor data directory can now be configured using the `    receptor_datadir` variable.


