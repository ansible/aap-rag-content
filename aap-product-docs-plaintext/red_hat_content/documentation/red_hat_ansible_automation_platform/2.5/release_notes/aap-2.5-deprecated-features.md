# Chapter 4. Deprecated features




Deprecated functionality is still included in Ansible Automation Platform and continues to be supported during this version’s support cycle. However, the functionality will be removed in a future release of Ansible Automation Platform and is not recommended for new deployments.

The following table provides information about features that were deprecated in Ansible Automation Platform 2.5:

| Component | Feature |
| --- | --- |
| Automation controller,
automation hub, and
Event-Driven Ansible controller | Tokens for the automation controller and the automation hub are deprecated. If you want to generate tokens, use the platform gateway to create them.

The platform gateway is the service that handles authentication and authorization for the Ansible Automation Platform. It provides a single entry into the Ansible Automation Platform and serves the platform user interface, so you can authenticate and access all of the Ansible Automation Platform services from a single location. |
| Automation controller and
automation hub | All non-local authentications into the automation controller and automation hub are deprecated. Use the platform gateway to configure external authentications, such as SAML, LDAP, and RADIUS. |
| Ansible-core | The `INI` configuration option in the **COLLECTIONS_PATHS** is deprecated. Use the singular form **COLLECTIONS_PATH** instead. |
| Ansible-core | The environment variable **ANSIBLE_COLLECTIONS_PATHS** is deprecated. Use the singular form **ANSIBLE_COLLECTIONS_PATH** instead. |
| Ansible-core | Old-style Ansible vars plug-ins that use the entry points `get_host_vars` or `get_group_vars` were deprecated in ansible-core 2.16, and will be removed in ansible-core 2.18. Update the Ansible plug-in to inherit from **BaseVarsPlugin** and define a `get_vars` method as the entry point. |
| Ansible-core | The **STRING_CONVERSION_ACTION** configuration option is deprecated as it is no longer used in the ansible-core code base. |
| Ansible-core | The **smart** option for setting a connection plug-in is being removed as its main purpose of choosing between SSH and Paramiko protocols is now irrelevant. Select an explicit connection plug-in instead. |
| Ansible-core | The undocumented `vaultid` parameter in the `vault` and `unvault` filters is deprecated and will be removed in ansible-core version 2.20. Use `vault_id` instead. |
| Ansible-core | The string parameter `keepcache` in the `yum_repository` is deprecated. |
| Ansible-core | The `required` parameter in the API `ansible.module_utils.common.process.get_bin_path` is deprecated. |
| Ansible-core |  `module_utils` - Importing the following convenience helpers from `ansible.module_utils.basic` has been deprecated:
`get_exception` , `literal_eval` , `_literal_eval` , `datetime` , `signal` , `types` , `chain` , `repeat` , `PY2` , `PY3` , `b` , `binary_type` , `integer_types` , `iteritems` , `string_types` , `test_type` , `map` , and `shlex_quote` .
Import the helpers from the source definition. |
| Ansible-core |  `ansible-doc` - Role `entrypoint` attributes are deprecated and eventually will no longer be shown in `ansible-doc` from ansible-core. |
| Automation execution environment | Execution environment-29 will be deprecated in the next major release after Ansible Automation Platform 2.5. |
| Installer | The Ansible team is exploring ways to improve the installation of the Ansible Automation Platform on Red Hat Enterprise Linux, which may include changes to how components are deployed using RPM directly on the host OS. RPMs will be replaced by packages deployed into containers that are run via Podman; this is similar to how automation currently executes on Podman in containers (execution environments) on the host OS. Changes will be communicated through release notes, but removal will occur in future revisions of the Ansible Automation Platform [lifecycle events](https://access.redhat.com/support/policy/updates/ansible-automation-platform) . |
| Automation mesh | The Work Python option has been deprecated and will be removed from automation mesh in a future release. |


