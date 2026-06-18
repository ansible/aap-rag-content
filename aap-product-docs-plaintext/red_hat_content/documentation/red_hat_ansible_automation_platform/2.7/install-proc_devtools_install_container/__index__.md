# Install Ansible development tools on a container inside VS Code

The Dev Containers VS Code extension requires a `.devcontainer` file to store settings for your dev containers. You must use the Ansible extension to scaffold a config file for your dev container, and reopen your directory in a container in VS Code.

## Before you begin

- You have installed a containerization platform, for example Podman, Podman Desktop, Docker, or Docker Desktop.
- You have a Red Hat login and you have logged in to the Red Hat registry at `registry.redhat.io`. For information about logging in to `registry.redhat.io`, see [Authenticating with the Red Hat container registry](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_devtools_requirements#devtools-setup-registry-redhat-io "All container images available through the Red Hat container catalog are hosted on an image registry, registry.redhat.io. The registry requires authentication for access to images.").
- You have installed VS Code.
- You have installed the Ansible extension in VS Code.
- You have installed the [Microsoft Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code.
- If you are installing Ansible development tools on Windows, launch VS Code and connect to the WSL machine. Click the `Remote`(![Remote](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/vscode-remote-icon.png)) icon. In the dropdown menu that appears, select the option to connect to the WSL machine.

## About this task

## Procedure

1.  In VS Code, navigate to your project directory.
2.  Click the Ansible icon in the VS Code activity bar to open the Ansible extension.
3.  In the **Ansible Development Tools** section of the Ansible extension, scroll down to the **ADD** option and select **Devcontainer**.
4.  In the **Create a devcontainer** page, select the **Downstream** container image from the **Container image** options. This action adds `devcontainer.json` files for both Podman and Docker in a `.devcontainer` directory.

5.  Reopen or reload the project directory:

- If VS Code detects that your directory contains a `devcontainer.json` file, the following notification appears:
![Reopen in container](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/devtools-reopen-in-container.png)
Click **Reopen in Container**.

- If the notification does not appear, click the `Remote` (![Remote](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/vscode-remote-icon.png)) icon. In the dropdown menu that appears, select **Reopen in Container**.

6.  Select the dev container for Podman or Docker according to the containerization platform you are using. The **Remote ()** status in the VS Code Status bar displays `opening Remote` and a notification indicates the progress in opening the container.

## Results

When the directory reopens in a container, the **Remote ()** status displays `Dev Container: ansible-dev-container`.

Note:

The base image for the container is a Universal Base Image Minimal (UBI Minimal) image that uses `microdnf` as a package manager. The `dnf` and `yum` package managers are not available in the container.

For information about using `microdnf` in containers based on UBI Minimal images, see [Adding software in a minimal UBI container](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/assembly_adding-software-to-a-ubi-container_building-running-and-managing-containers#proc_adding-software-in-a-minimal-ubi-container_assembly_adding-software-to-a-ubi-container) in the Red Hat Enterprise Linux *Building, running, and managing containers* guide.
