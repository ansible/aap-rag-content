# 3. Manage containers in private automation hub
## 3.2. Configuring user access for container repositories in private automation hub
### 3.2.1. Remote registry team permissions

Create and assign permissions to a team in private automation hub to allow users to access specific features in the system.

New teams do not have any assigned permissions by default. You must add permissions when first creating a team or edit an existing team to add or remove permissions.

For more on managing access through teams, see [Teams](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#assembly-controller-teams_gw-manage-rbac) in the Access management and authentication guide.

The following table lists permissions you can grant to teams to ensure they have the correct level of access and privileges to your remote registries.

**Table 3.1. Team permissions for managing containers in private automation hub**

| Permission name | Description |
| --- | --- |
| <br>  Create new containers | <br>  Users can create new containers |
| <br>  Change container namespace permissions | <br>  Users can change permissions on the container repository |
| <br>  Change container | <br>  Users can change information on a container |
| <br>  Change execution environment tags | <br>  Users can modify execution environment tags |
| <br>  Push to existing container | <br>  Users can push an execution environment to an existing container |

