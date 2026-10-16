# Revert to ee-supported on a containerized installation

Remove the `control_plane_execution_environment` override and rerun the containerized installer to restore the default `ee-supported` image.

## Before you begin

- You have access to the installer configuration used to configure the containerized installation.
- You have permission to run the installer on the Ansible Automation Platform host.

## Procedure

1. Remove or unset `control_plane_execution_environment` in the installer configuration.
2. Rerun the containerized Ansible Automation Platform installer.

## What to do next

**Verification**

1. Confirm that the installer completes successfully and restores the default `ee-supported` image.
2. Select **Automation Execution** > **Infrastructure** > **Execution Environments**. Confirm that the **Image** value for **Control Plane Execution Environment** matches the default `ee-supported` image for your release.
3. Perform a project update and a constructed inventory source update, and confirm that both complete successfully.
