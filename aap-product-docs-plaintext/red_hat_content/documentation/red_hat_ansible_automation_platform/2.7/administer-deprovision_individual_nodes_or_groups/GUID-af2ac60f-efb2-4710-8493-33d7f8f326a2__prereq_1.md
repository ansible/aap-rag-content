# Deprovision individual nodes or groups
## Deprovision nodes in a containerized deployment
### Before you begin

**Prerequisites**

- You have root or sudo access to the host running the automation controller containers.
- You know the hostname of the node to deprovision, as it appears in the inventory file or the Instances list in the automation controller UI.
- The node you are deprovisioning is not the primary controller node (the first host in the `[automationcontroller]` group).

### Procedure

1. On the node you want to remove, stop all Ansible Automation Platform services:
`systemctl --user stop automation-controller-task`

`systemctl --user stop automation-controller-web`

`systemctl --user stop receptor`

If the node is an execution or hop node that runs only the receptor service:

`systemctl --user stop receptor`

2. On the primary automation controller node, run the deprovision command inside the automation controller task container. Replace `<hostname>` with the hostname of the node as it appears in the inventory file:
`podman exec -it automation-controller-task awx-manage deprovision_instance --hostname=<hostname>`     For example:

`podman exec -it automation-controller-task awx-manage deprovision_instance --hostname=exec-node-1.example.com`

3. Verify the node has been removed from the cluster by checking the Instances list:
`podman exec -it automation-controller-task awx-manage list_instances`

Confirm that the deprovisioned node no longer appears in the output.

You can also verify the node removal in the automation controller UI by navigating to Automation execution> (and then)Infrastructure> (and then)Instances and confirming that the node is no longer listed.

4. Remove the deprovisioned node from the inventory file used by the containerized installer, to prevent the node from being re-added if the installer is run again.
5. (Optional) On the deprovisioned node, uninstall the containerized platform components by running the uninstall playbook with an inventory file that contains only the deprovisioned node or nodes:
`ansible-playbook -i <deprovisioned-node-inventory> ansible.containerized_installer.uninstall`

Warning:
Do not use this command on your full cluster inventory file. The uninstall playbook removes Ansible Automation Platform components from every host in the inventory. To uninstall only the deprovisioned node, create a separate inventory file that lists only the node or nodes you want to clean up.
**Example inventory file for a single execution node (deprovisioned-inventory)**



```
[all]
exec-node-1.example.com
```

Then run:

`ansible-playbook -i deprovisioned-inventory ansible.containerized_installer.uninstall`

