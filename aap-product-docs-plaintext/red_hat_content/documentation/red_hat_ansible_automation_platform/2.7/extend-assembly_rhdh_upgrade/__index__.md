# Upgrade the Ansible plug-ins

Upgrade the Ansible plug-ins for Red Hat Developer Hub to a newer version.

## Upgrade the Ansible plug-ins using OCI delivery

To upgrade the Ansible plug-ins for Red Hat Developer Hub, update the OCI image tag in your dynamic plug-ins configuration to the new version.

### Before you begin

- You have installed the Ansible plug-ins using OCI container delivery.
- You have the new Ansible plug-ins image tag for your release.

### Procedure

1.  Edit your dynamic plug-ins configuration:

- For Operator deployments, edit the dynamic plug-ins ConfigMap (for example, `dynamic-plugins-rhdh`).
- For Helm deployments, in the OpenShift Container Platform Developer UI, navigate to **Helm** > **developer-hub** > **Actions** > **Upgrade** > **Yaml view**.

2.  Update the `<tag>` value in each `oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>` reference to the new version.
3.  Apply the changes:

- For Operator deployments, click **Save**. The Red Hat Developer Hub pod restarts automatically with the updated plug-ins.
- For Helm deployments, click **Upgrade**.

### Results

Verify the upgrade:

1. Check the `install-dynamic-plugin` container logs for the new version.
2. Verify that the Ansible plug-in is present in the navigation pane.
