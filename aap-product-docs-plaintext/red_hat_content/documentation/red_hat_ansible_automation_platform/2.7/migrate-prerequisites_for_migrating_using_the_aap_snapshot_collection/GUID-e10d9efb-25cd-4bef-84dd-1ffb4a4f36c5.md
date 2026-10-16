# Prerequisites for migrating using the aap_snapshot collection
## Prerequisites for containerized deployment import

Before running the `artifact_import` playbook, verify that your target containerized deployment, control node, and migration artifact are correctly configured.

### Target deployment

- Ansible Automation Platform is installed on the target hosts using the containerized installation program.
- All Ansible Automation Platform services on the target hosts are running.
- You have the inventory file used to install the target deployment.

### Control node

- Ansible Core is installed: version 2.14 or later for RHEL 9, version 2.16 or later for RHEL 10.

- The `ansible.aap_snapshot` collection is installed from automation hub. The collection is not included with the Ansible Automation Platform installation program and must be installed separately:

```console
ansible-galaxy collection install ansible.aap_snapshot
```

For more information, see [anaible.aap_snapshot on automation hub](https://console.redhat.com/ansible/automation-hub/collections/published/ansible/aap_snapshot/details).

- SSH access is available from the control node to all component hosts (automation controller, automation hub, platform gateway, and Event-Driven Ansible hosts).

- The export artifact file (`.tar`) produced by the `artifact_export` playbook is present on the control node and readable by the user running the playbook. Pass its full path using `artifact_file`. This variable has no default and the playbook fails at startup if it is not set.
