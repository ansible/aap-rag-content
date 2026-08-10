+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_self_service_download_tar"
template = "docs/aem-title.html"
title = "Download the plug-in TAR files (deprecated) - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-assembly_self_service_upgrading/", "Upgrade Ansible automation portal"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-proc_self_service_download_tar/aem-page/upgrade-proc_self_service_download_tar.html"
last_crumb = "Download the plug-in TAR files (deprecated)"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Download the plug-in TAR files (deprecated)"
oversized = "false"
page_slug = "upgrade-proc_self_service_download_tar"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-proc_self_service_download_tar"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-proc_self_service_download_tar/toc/toc.json"
type = "aem-page"
+++

# Download the plug-in TAR files (deprecated)

Download the latest `.tar.gz` plug-in bundle for Ansible automation portal from the Red Hat Customer Portal.

## About this task

Important:

The HTTP plug-in registry method is deprecated and will be removed in a future release of Ansible Automation Platform. Red Hat recommends OCI container delivery. Use this procedure only if you cannot migrate to OCI yet and your deployment uses `pluginMode: tarball`.

## Procedure

1.  Create a directory on your local machine and set an environment variable to represent the directory path:
  

```
$ mkdir /path/to/<automation-portal-plugins>
$ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/<automation-portal-plugins>
```

2.  In a browser, open the Red Hat Ansible Automation Platform product software downloads page and select the Product Software tab.
3.  Download the Ansible automation portal setup bundle that matches your target chart version on the lifecycle page or the Product Software tab.
      The filename format is `ansible-backstage-rhaap-bundle-<plugin-version>.tar.gz`.

4.  Extract the archive into `$DYNAMIC_PLUGIN_ROOT_DIR`:
  

```
$ tar --exclude='*code*' -xzf ansible-backstage-rhaap-bundle-<plugin-version>.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR
```

## Results

Verify extracted files:

```
$ ls $DYNAMIC_PLUGIN_ROOT_DIR
```

You should see `.tgz` plug-in files and matching `.integrity` files.
