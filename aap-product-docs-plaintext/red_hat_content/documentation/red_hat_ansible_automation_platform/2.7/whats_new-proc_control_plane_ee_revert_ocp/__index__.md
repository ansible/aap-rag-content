# Revert to ee-supported on OpenShift Container Platform

If you encounter problems with project updates or constructed inventory source updates after opting in, revert to the default `ee-supported` control-plane execution environment.

## About this task

Note:

This procedure applies only to OpenShift Container Platform deployments.

## Procedure

1. In the OpenShift Container Platform web console, open the top-level `AnsibleAutomationPlatform` custom resource for your deployment.
2. Remove the `spec.controller.control_plane_ee_image` field.
3. Save the custom resource.

## Results

The operator reconciles the controller deployment and restores the default `ee-supported` image.

Note:

Removing this field also causes the operator to reconcile the controller deployment. Wait for the deployment rollout to complete before running project or inventory updates.

## What to do next

**Verification**

1. Select **Automation Execution** > **Infrastructure** > **Execution Environments**. Confirm that the **Image** value for **Control Plane Execution Environment** matches the default `ee-supported` image for your release.
2. Run a project update and a constructed inventory source update, and confirm that both complete successfully.
