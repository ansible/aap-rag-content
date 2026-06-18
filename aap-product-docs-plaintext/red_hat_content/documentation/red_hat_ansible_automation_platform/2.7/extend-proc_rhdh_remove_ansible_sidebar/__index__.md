# Remove the Ansible sidebar navigation item

By default, the Ansible plug-ins add an Ansible item to the Red Hat Developer Hub sidebar navigation. You can remove the sidebar entry while keeping the `/ansible` route accessible by URL.

## About this task

If you are embedding the Ansible plug-ins into an existing Red Hat Developer Hub instance and do not want a separate Ansible sidebar entry, you can remove it by modifying the `dynamicRoutes` configuration for the frontend plug-in.

The `/ansible` route remains accessible by URL. Only the sidebar navigation item is removed.

## Procedure

1.  In your dynamic plug-ins configuration, locate the `ansible.plugin-backstage-rhaap` frontend plug-in entry.
2.  Remove the `menuItem` block from the `dynamicRoutes` section.
**Before (sidebar item enabled):**

```yaml
pluginConfig:
dynamicPlugins:
frontend:
ansible.plugin-backstage-rhaap:
appIcons:
- importName: AnsibleLogo
name: AnsibleLogo
dynamicRoutes:
- importName: AnsiblePage
menuItem:
icon: AnsibleLogo
text: Ansible
path: /ansible
```
**After (sidebar item removed):**

```yaml
pluginConfig:
dynamicPlugins:
frontend:
ansible.plugin-backstage-rhaap:
appIcons:
- importName: AnsibleLogo
name: AnsibleLogo
dynamicRoutes:
- importName: AnsiblePage
path: /ansible
```

3.  Apply the changes. For Helm deployments, click **Upgrade**. For Operator deployments, the deployment auto-reloads when the ConfigMap is updated.
