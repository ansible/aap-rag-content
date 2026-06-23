# Develop automation content in your workspace
## Configure ansible-navigator for execution environments

Customize `ansible-navigator` settings in your Ansible development workspace to configure execution environment options, logging, and output format.

### About this task

The `ansible-navigator` tool uses a YAML configuration file to define settings for execution environments, container engines, and output behavior. An example `ansible-navigator.yaml` file is available in the [Ansible Development Workspace Sample](https://github.com/redhat-cop/ansible-devspaces) repository.

### Procedure

1.  In your Ansible development workspace, create a file named `ansible-navigator.yaml` in the root of your project directory.
2.  Add the following minimal configuration and modify it to suit your requirements:


```
ansible-navigator:
execution-environment:
container-engine: podman
logging:
level: critical
playbook-artifact:
enable: false
```
The Ansible dev spaces image includes a default execution environment. You only need to add additional settings such as `environment-variables`, `volume-mounts`, or `container-options` if your project requires them.

3. **Optional:** To override the default execution environment image, add the `image` setting under the `execution-environment` section:


```
execution-environment:
image: registry.redhat.io/ansible-automation-platform-27/ee-supported-rhel9:latest
```

4.  Save the file. The `ansible-navigator` tool automatically loads the configuration from the current working directory or from the default locations.
For more information about `ansible-navigator` settings, see [ansible-navigator settings](https://docs.ansible.com/projects/navigator/settings) in the ansible-navigator documentation.

