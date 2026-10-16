# Deprovision individual nodes or groups
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
