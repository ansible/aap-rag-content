# Changed features
## Changed features

Ansible plug-ins for Red Hat Developer Hub

- **OCI container plug-in delivery**: OCI container delivery is now the recommended method for installing automation portal plug-ins. Set `pluginMode: oci` in the Helm chart configuration. The tarball delivery method is deprecated.
- **Templates and History menus require RBAC permissions**: The Templates and History navigation menus are now gated by role-based access control. After upgrading, these menus are hidden unless administrators grant the required permissions. For more information, see the automation portal upgrade documentation.
