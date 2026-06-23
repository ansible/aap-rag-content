# New features and enhancements
## Self-service automation

- Added support for deployment on RHEL by providing appliance-based (VMDK and QCOW2) installation.
- The OpenShift Helm chart now supports installing the Ansible plugins directly from registry.redhat.io as OCI images, improving the current installation experience.
- Configurable "Support" link in the global header bar. Defaults to <https://access.redhat.com/support>. Customers override it to point to their own support portal (e.g. ServiceNow, internal help desk).
- Playbook authors can use ansible.builtin.debug messages to communicate results directly to self-service users (URLs, guidance, etc) displayed in the self-service portal template log output.
- AAP Job Template sync filtering now supports excludeLabels, allowing admins to exclude specific AAP Job Templates from being available in the automation portal using Ansible Automation Platform labels without needing to curate an explicit inclusion list.

