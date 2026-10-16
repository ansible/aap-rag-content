# Prerequisites for migrating using the aap_snapshot collection
## Prerequisites for the OCP deployment import
### Control node requirements

Ansible Core version
Ansible Core 2.16.0 or later is installed.

Collection installation
The `ansible.aap_snapshot` collection is installed
from automation hub:

```
ansible-galaxy collection install ansible.aap_snapshot
```

Migration artifact
The `.tar` artifact from the export workflow is present on the control node and readable by the user running the playbook. Pass its full path using `artifact_file`. This variable has no default and the playbook fails at startup if it is not set.

