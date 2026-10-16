+++
title = "Deprovision individual nodes or groups - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-deprovision_individual_nodes_or_groups"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_planning_mesh/", "Scale automation across your infrastructure with automation mesh"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-deprovision_individual_nodes_or_groups/aem-page/administer-deprovision_individual_nodes_or_groups.html"
last_crumb = "Deprovision individual nodes or groups"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Deprovision individual nodes or groups"
oversized = "false"
page_slug = "administer-deprovision_individual_nodes_or_groups"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-deprovision_individual_nodes_or_groups"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-deprovision_individual_nodes_or_groups/toc/toc.json"
type = "aem-page"
+++

# Deprovision individual nodes or groups

You can deprovision automation mesh nodes and instance groups by using the Ansible Automation Platform installer. Learn how to deprovision specific nodes or entire groups, with example inventory files.

Important:

Containerized Ansible Automation Platform deployments do not support the `node_state=deprovision ` parameter. For containerized deployments, use the `awx-manage` command to deprovision nodes and groups.

## Deprovision nodes in a containerized deployment

In a containerized Ansible Automation Platform deployment, you cannot use the `node_state=deprovision` inventory parameter to remove nodes. Instead, use the `awx-manage` utility from the automation controller container to deregister nodes from the cluster.

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

## Deprovision instance groups in a containerized deployment

Unregister instance groups using the `awx-manage` command to cleanly remove group definitions from a containerized Ansible Automation Platform deployment without impacting member nodes.

### Before you begin

Deprovisioning nodes removes them from the mesh. For instance groups, you unregister the group from the controller's cluster registry by using the `awx-manage unregister_queue `command. This removes the group definition but does not deprovision its member nodes

**Prerequisites**

- You have root or sudo access to the host running the automation controller containers.
- You know the name of the instance group to remove.
- No active jobs are running on nodes that are members of the instance group.

### Procedure

1. Ensure that no jobs are currently running on instances in the group. In the automation controller UI, navigate to Automation execution> (and then)Jobsand confirm that no jobs with a status of Running or Pending are assigned to instances in the group.
2. On the primary automation controller node, run the unregister command inside the automation controller task container. Replace `<group_name>` with the name of the instance group:
      `podman exec -it automation-controller-task awx-manage unregister_queue --queuename=<group_name>`

    For example:

    `podman exec -it automation-controller-task awx-manage unregister_queue --queuename=remote_execution_group`

3. (Optional) If the instance group contains nodes that should also be deprovisioned, deprovision each node using the procedure in <xref here>. Deprovisioning a node automatically removes its membership from any instance groups, so no specific order of operations is required.
4. Verify the instance group has been removed by checking the Instance Groups list in the automation controller UI:
      Navigate to Automation execution> (and then)Infrastructure> (and then)Instance groups and confirm the group no longer appears.

## Run deprovisioning commands

To safely remove nodes or instance groups from a containerized Ansible Automation Platform cluster without disrupting service, execute deprovisioning commands from inside the automation controller container.

For containerized AAP deployments, all `awx-manage` commands must be executed from inside the automation controller container on the primary controller node:

`podman exec -it automation-controller-task awx-manage <command>`

The `automation-controller-task` container runs as a rootless Podman container under the AAP service user. Ensure you are logged in as the correct user (the user who installed the AAP containers) before running Podman commands.

To confirm you are operating on the correct host, list the running containers:

`podman ps --all --format "{{.Names}}" | grep controller`

Expected output includes:

```
automation-controller-task
automation-controller-web
automation-controller-rsyslog
```

## Post removal checks

After deprovisioning nodes or instance groups, perform the following verification steps:

### Procedure

1. Confirm the node or group is removed from the cluster:
      `podman exec -it automation-controller-task awx-manage list_instances`

2. Check the automation controller UI:
      Navigate to Infrastructure> (and then)Instances to verify node removal.

    Navigate to Infrastructure> (and then)Instance Groups to verify group removal.

3. Verify that remaining mesh connections are healthy:
      In the UI, check the topology view under Infrastructure> (and then)Topology view for any broken links or error indicators.

4. Run a test job on any remaining execution nodes to ensure the mesh is functioning correctly after the node removal.
5. Update the inventory file to remove the deprovisioned host entries, so they are not re-added on a subsequent installer run.
