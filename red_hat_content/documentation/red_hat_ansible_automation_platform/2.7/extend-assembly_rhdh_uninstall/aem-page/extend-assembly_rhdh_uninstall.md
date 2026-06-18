+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_uninstall"
template = "docs/aem-title.html"
title = "Uninstall the Ansible plug-ins - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_intro/", "Ansible plug-ins for Red Hat Developer Hub"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_uninstall/aem-page/extend-assembly_rhdh_uninstall.html"
last_crumb = "Uninstall the Ansible plug-ins"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Uninstall the Ansible plug-ins"
oversized = "false"
page_slug = "extend-assembly_rhdh_uninstall"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_uninstall"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_uninstall/toc/toc.json"
type = "aem-page"
+++

# Uninstall the Ansible plug-ins

Uninstall the Ansible plug-ins from Red Hat Developer Hub for Helm chart and Operator deployments.

## Uninstall a Helm chart installation

To uninstall the Ansible plug-ins from a Helm chart installation, remove the plug-in configuration from the Helm chart YAML, remove the `extraContainers` section, and delete the Ansible block from the custom ConfigMap.

### Procedure

1.  In Red Hat Developer Hub, remove any software templates that use the `ansible:content:create` action.
2.  In the OpenShift Developer UI, navigate to **Helm** > **developer-hub** > **Actions** > **Upgrade** > **Yaml view**.
3.  Remove the Ansible plug-ins configuration under the `plugins` section (all `oci://registry.redhat.io/ansible-automation-platform/automation-portal` entries).
  
  Note:
      If you used the deprecated HTTP plug-in registry method, remove the `http://plugin-registry:8080/...` entries instead.

4.  Remove the `extraContainers` section.
  

```
upstream:
  backstage:
    ...
    extraContainers:
      - command:
          - adt
          - server
        image: >-
          registry.redhat.io/ansible-automation-platform-2.7/ansible-dev-tools-rhel9:latest
        imagePullPolicy: IfNotPresent
        name: ansible-devtools-server
        ports:
          - containerPort: 8000
```

5.  Click **Upgrade**.
6.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
7.  Remove the `ansible` section.
8.  Restart the Red Hat Developer Hub deployment.
9.  If you used OCI delivery, delete the registry auth secret:
  

```terminal
$ oc delete secret <deployment-name>-dynamic-plugins-registry-auth
```

10.  If you used the HTTP plug-in registry method, remove the plug-in registry application:
  

```terminal
$ oc delete all -l app=plugin-registry
```

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
