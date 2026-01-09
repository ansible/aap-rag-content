# 3. Manage containers in private automation hub
## 3.2. Configuring user access for container repositories in private automation hub
### 3.2.1. Remote registry team permissions




Create and assign permissions to a team in private automation hub to allow users to access specific features in the system.

New teams do not have any assigned permissions by default. You must add permissions when first creating a team or edit an existing team to add or remove permissions.

For more on managing access through teams, see [Teams](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#assembly-controller-teams_gw-manage-rbac) in the Access management and authentication guide.

The following table lists permissions you can grant to teams to ensure they have the correct level of access and privileges to your remote registries.


<span id="idm140126403630704"></span>
**Table 3.1. Team permissions for managing containers in private automation hub**

| Permission name | Description |
| --- | --- |
| Create new containers | Users can create new containers |
| Change container namespace permissions | Users can change permissions on the container repository |
| Change container | Users can change information on a container |
| Change execution environment tags | Users can modify execution environment tags |
| Push to existing container | Users can push an execution environment to an existing container |




