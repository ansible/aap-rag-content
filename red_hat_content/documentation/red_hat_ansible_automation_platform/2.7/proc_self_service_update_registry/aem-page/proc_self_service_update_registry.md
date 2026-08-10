+++
title = "Update the plug-in registry (deprecated) - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/proc_self_service_update_registry"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/proc_self_service_update_registry/aem-page/proc_self_service_update_registry.html"
last_crumb = "Update the plug-in registry (deprecated)"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Update the plug-in registry (deprecated)"
oversized = "false"
page_slug = "proc_self_service_update_registry"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/proc_self_service_update_registry"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/proc_self_service_update_registry/toc/toc.json"
type = "aem-page"
+++

# Update the plug-in registry (deprecated)

Upload refreshed plug-in tarball files to OpenShift Container Platform and start a new plug-in registry build.

## Before you begin

- You have downloaded the plug-in TAR files for Ansible automation portal.
- You have set an environment variable `$DYNAMIC_PLUGIN_ROOT_DIR` to the directory that contains the TAR files.

## About this task

Important:

Use this procedure only with `pluginMode: tarball`. OCI upgrades do not require a plug-in registry update.

## Procedure

1.  Log in to your OpenShift Container Platform cluster.
2.  Select your automation portal project:
  

```
$ oc project <namespace>
```

3.  List build configurations and identify your plug-in registry build configuration, for example `plugin-registry` or a legacy name such as `aap-self-service-plugins`:
  

```
$ oc get buildconfig
```

4.  Start a new build from your local directory:
  

```
$ oc start-build <build_config_name> --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
```

    Replace `<build_config_name>` with the build configuration name you identified in the previous step.

## Results

Verify the registry update:

1. In the **Topology** view, open the **plugin-registry** details pane.
2. In the **Pods** section, select **View logs** for the new build pod.
3. In the build pod terminal, run `ls` and confirm the new `.tgz` files are present.

After you verify the registry, upgrade the Helm release.
