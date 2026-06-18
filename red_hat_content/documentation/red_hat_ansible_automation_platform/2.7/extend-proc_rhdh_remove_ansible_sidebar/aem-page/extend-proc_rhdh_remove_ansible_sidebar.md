+++
template = "docs/aem-title.html"
title = "Remove the Ansible sidebar navigation item - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-proc_rhdh_remove_ansible_sidebar"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-proc_rhdh_remove_ansible_sidebar/", "Remove the Ansible sidebar navigation item"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-proc_rhdh_remove_ansible_sidebar/aem-page/extend-proc_rhdh_remove_ansible_sidebar.html"
last_crumb = "Remove the Ansible sidebar navigation item"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Remove the Ansible sidebar navigation item"
oversized = "false"
page_slug = "extend-proc_rhdh_remove_ansible_sidebar"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-proc_rhdh_remove_ansible_sidebar"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-proc_rhdh_remove_ansible_sidebar/toc/toc.json"
type = "aem-page"
+++

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
