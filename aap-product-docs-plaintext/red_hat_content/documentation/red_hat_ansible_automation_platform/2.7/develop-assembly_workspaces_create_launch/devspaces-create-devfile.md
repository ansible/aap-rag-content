# Create and launch an Ansible development workspace
## Create a devfile for an Ansible development workspace

To ensure your Ansible development workspace launches with the correct Ansible dev spaces image, you must add a `devfile` to your git repository. A `devfile` is a YAML file that defines the development environment for a project in Red Hat OpenShift Dev Spaces.

### About this task

### Procedure

1.  In your Git repository for your Ansible development workspace, create a new file named `devfile.yaml`.
2.  Copy and paste the following sample code into the `devfile.yaml` file:


```
schemaVersion: 2.3.0
attributes:
controller.devfile.io/storage-type: per-workspace
metadata:
name: ansible-devspaces
components:
- name: dev-tools
container:
image: registry.redhat.io/ansible-automation-platform-27/ansible-devspaces-rhel9:latest
cpuLimit: 4000m
cpuRequest: 250m
memoryRequest: 128Mi
memoryLimit: 8Gi
env:
- name: HOME
value: "/projects"
- name: VSCODE_DEFAULT_WORKSPACE
value: "/projects/ansible-devspaces/.code-workspace"
- name: "ADT_CONTAINER_ENGINE"
value: "podman"
```
The environment variables configure the following:

- `HOME`: Sets the home directory for the container.
- `VSCODE_DEFAULT_WORKSPACE`: Points VS Code to the `.code-workspace` configuration file.
- `ADT_CONTAINER_ENGINE`: Enables podman for container-in-container operations, including execution environments.

3. **Optional:** If you cannot pull images from the Red Hat Container Catalog (RHCC), modify the `image` value to point to your organization's internal registry.
4.  Add the `devfile.yaml` file to your Git repository and push the changes.

