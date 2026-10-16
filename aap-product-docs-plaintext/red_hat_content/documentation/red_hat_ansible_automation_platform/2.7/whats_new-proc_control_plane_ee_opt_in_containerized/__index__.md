# Opt in to control-plane-ee on a containerized installation

For an existing containerized installation, set `control_plane_execution_environment` to `registry.redhat.io/ansible-automation-platform-27/ee-control-plane-rhel9:latest` in the installer configuration and rerun the Ansible Automation Platform installer.

## Before you begin

- You have an Ansible Automation Platform 2.7 containerized installer that supports the `control_plane_execution_environment` variable.
- You have the approved `control-plane-ee` image reference and access to its registry.
- You have permission to run the installer on the Ansible Automation Platform host.

## Procedure

1. Set `control_plane_execution_environment` to `registry.redhat.io/ansible-automation-platform-27/ee-control-plane-rhel9:latest` in the installer configuration:


```
control_plane_execution_environment: "registry.redhat.io/ansible-automation-platform-27/ee-control-plane-rhel9:latest"
```

2. Rerun the containerized Ansible Automation Platform installer.

## What to do next

**Verification**

1. Confirm that the installer completes successfully and pulls the configured `control-plane-ee` image to the target host.
2. Select **Automation Execution** > **Infrastructure** > **Execution Environments**. Confirm that the **Image** value for **Control Plane Execution Environment** matches the configured `control-plane-ee` image.
3. Perform a project update and a constructed inventory source update, and confirm that both complete successfully.
