# 3. Manage containers in private automation hub
## 3.5. Pulling images from a container repository
### 3.5.2. Syncing images from a container repository




You can pull automation execution environments from the private automation hub remote registry to sync an image to your local machine. To sync an execution environment from a remote registry, you must first configure a remote registry.

**Prerequisites**

You must have permission to view and pull from a private container repository.


**Procedure**

1. From the navigation panel, selectAutomation Content→Execution Environments.
1. Add `    <a class="link" href="https://registry.redhat.io">https://registry.redhat.io</a>` to the registry.
1. Add any required credentials to authenticate.

Note
Some remote registries are aggressive with rate limiting. Set a rate limit under **Advanced Options** .




1. From the navigation panel, selectAutomation Content→Execution Environments.
1. ClickCreate execution environmentin the page header.
1. Select the registry you want to pull from. The **Name** field displays the name of the automation execution environments displayed on your local registry.

Note
The **Upstream name** field is the name of the image on the remote server. For example, if the upstream name is set to "alpine" and the **Name** field is "local/alpine", the alpine image is downloaded from the remote and renamed to "local/alpine".




1. Set a list of tags to include or exclude. Note that syncing automation execution environments with a large number of tags is time consuming and uses a lot of disk space.


**Additional resources**

-  [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication)
-  [What is Podman?](http://docs.podman.io/en/latest/index.html)


