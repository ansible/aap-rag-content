# Install the Ansible plug-ins
## Verify the plug-in installation

After configuring the dynamic plug-ins and sidecar container, verify that the Ansible plug-ins installed successfully.

### Procedure

1.  In the `install-dynamic-plugin` container logs, search for the Ansible plug-ins.
A successful installation shows:

```terminal
==> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-rhaap
==> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-self-service
==> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-backstage-plugin-catalog-backend-module-rhaap
==> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-scaffolder-backend-module-backstage-rhaap
```

2.  Verify that the Ansible plug-in is present in the navigation pane.
3.  Select **Administration** to view the installed plug-ins in the **Plugins** tab.
