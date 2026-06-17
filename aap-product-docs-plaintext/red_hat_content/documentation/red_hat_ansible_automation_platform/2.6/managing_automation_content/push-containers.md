# 3. Manage containers in private automation hub
## 3.3. Populating your private automation hub container registry
### 3.3.3. Pushing an execution environment to private automation hub

You can push tagged execution environments to private automation hub to create new containers and populate the remote registry.

**Prerequisites**

- You have permissions to create new containers.
- You have the FQDN or IP address of the Ansible Automation Platform instance.

**Procedure**

1. Log in to Podman using your Ansible Automation Platform location and credentials:

$ podman login -u=<username> -p=<password> <aap_url>


Warning
Let Podman prompt you for your password when you log in. Entering your password at the same time as your username can expose your password to the shell history.

2. Push your execution environment to your automation hub remote registry:

$ podman push <automation_hub_url>/<ee_name>

**Troubleshooting**

The `push` operation re-compresses image layers during the upload, which is not guaranteed to be reproducible and is client-implementation dependent. This may lead to image-layer digest changes and a failed push operation, resulting in `Error: Copying this image requires changing layer representation, which is not possible (image is signed or the destination specifies a digest)`.

**Verification**

1. Log in to your Ansible Automation Platform.
2. Navigate to Automation Content → Execution Environments.
3. Locate the container in the container repository list.

