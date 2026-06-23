# Pull execution environments for use in automation hub
## Pull and sync images from automation hub to your local system
### Sync images from a container registry

You can pull automation execution environments from the private automation hub remote registry to sync an image to your local machine. To sync an execution environment from a remote registry, you must first configure a remote registry.

#### Before you begin

You must have permission to view and pull from a private container repository.

#### Procedure

1.  From the navigation panel, select Automation Content> (and then)Execution Environments.
2.  Add `<https://registry.redhat.io>` to the registry.
3.  Add any required credentials to authenticate. Note:
Some remote registries are aggressive with rate limiting. Set a rate limit under **Advanced Options**.

4.  From the navigation panel, select Automation Content> (and then)Execution Environments.
5.  Click Create execution environment in the page header.
6.  Select the registry you want to pull from. The **Name** field displays the name of the automation execution environments displayed on your local registry. Note:
The **Upstream name** field is the name of the image on the remote server. For example, if the upstream name is set to "alpine" and the **Name** field is "local/alpine", the alpine image is downloaded from the remote and renamed to "local/alpine".

7.  Set a list of tags to include or exclude. Note that syncing automation execution environments with a large number of tags is time consuming and uses a lot of disk space.

