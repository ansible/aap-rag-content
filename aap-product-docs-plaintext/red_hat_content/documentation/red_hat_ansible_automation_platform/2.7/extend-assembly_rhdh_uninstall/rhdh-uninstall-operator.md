# Uninstall the Ansible plug-ins
## Uninstall from an Operator installation

To uninstall the Ansible plug-ins from an Operator installation, edit the ConfigMaps that reference Ansible. The deployment auto-reloads when the ConfigMaps are updated.

### Procedure

1.  Remove the Ansible plug-in entries from the `plugins:` block in your dynamic plug-ins ConfigMap.
Alternatively, set `disabled: true` for each Ansible plug-in entry.

2.  Edit your custom Red Hat Developer Hub ConfigMap (for example, `app-config-rhdh`):
1.  Remove the Ansible software templates entry from the `catalog.locations` block.
2.  Remove the entire `ansible` block (including `creatorService`, `rhaap`, `devSpaces`, and `automationHub` entries).
3.  Click **Save**.
3.  Modify the Backstage custom resource and remove the `containers` block for the Ansible Developer Tools sidecar from the `spec.deployment.patch.spec.template.spec` block. Click **Save**.
