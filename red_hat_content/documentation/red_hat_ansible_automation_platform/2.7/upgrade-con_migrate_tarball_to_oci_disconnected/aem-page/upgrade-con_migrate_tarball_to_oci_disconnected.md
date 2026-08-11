+++
template = "docs/aem-title.html"
title = "Migrate in air-gapped and disconnected environments - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_migrate_tarball_to_oci_disconnected"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-assembly_self_service_upgrading/", "Upgrade Ansible automation portal"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_migrate_tarball_to_oci_disconnected/aem-page/upgrade-con_migrate_tarball_to_oci_disconnected.html"
last_crumb = "Migrate in air-gapped and disconnected environments"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Migrate in air-gapped and disconnected environments"
oversized = "false"
page_slug = "upgrade-con_migrate_tarball_to_oci_disconnected"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-con_migrate_tarball_to_oci_disconnected"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_migrate_tarball_to_oci_disconnected/toc/toc.json"
type = "aem-page"
+++

# Migrate in air-gapped and disconnected environments

For air-gapped or disconnected clusters, mirror the OCI images to your internal registry and configure the Helm chart to use your mirror.

For air-gapped or partially disconnected clusters, you must mirror the OCI images to your internal registry and configure the Helm chart to use your mirror instead of `registry.redhat.io`.

## Mirroring Ansible plug-in images

The Ansible plug-in OCI artifacts must be mirrored to your internal registry. Mirror the images from a host with access to `registry.redhat.io`:

```
$ podman pull registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>
$ podman tag registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version> \
  <your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
$ podman push <your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
```

When mirroring, you must preserve the original repository path. For example, mirror `registry.redhat.io/ansible-automation-platform/automation-portal:2.2` to `<your-mirror-registry>/ansible-automation-platform/automation-portal:2.2`.

## Configuring Helm values for mirror registry

Edit your `backup-values.yaml` to point to your mirror registry:

```yaml
redhat-developer-hub:
  global:
    pluginMode: oci
    imageTagInfo: "<plugin-version>"
    imageRegistry: "<your-mirror-registry-host>"
    catalogIndex:
      image:
        registry: "<your-mirror-registry-host>"
  upstream:
    backstage:
      image:
        repository: rhdh/rhdh-hub-rhel9
        tag: "<platform-version>"
    postgresql:
      image:
        repository: rhel9/postgresql-15
        tag: "latest"
```

Key points:

- `imageRegistry` must be the registry **host only** (for example, `yb-artifactory` or `mirror.example.com:5000`). Do not include a repository path.
- `catalogIndex.image.registry` must be set separately — it is not auto-derived from `imageRegistry`. This is required for RHDH 1.9+.
- If your mirror uses a non-standard repository path for the Ansible plug-in image, use `ociPluginImage` instead to specify the full path:

```yaml
redhat-developer-hub:
  global:
    imageRegistry: "<your-mirror-registry-host>"
    ociPluginImage: "<your-mirror-registry-host>/custom-path/automation-portal"
```

## Using custom CA certificates for private registries

If your mirror registry uses a self-signed or internal CA certificate, the `install-dynamic-plugins` init container will fail with an `x509: certificate signed by unknown authority` error. You must mount your CA certificate into the init container.

The recommended approach is to create a ConfigMap and mount it at the per-registry trust path. For complete instructions, see the RHDH documentation on installing plug-ins from OCI registries by using custom certificates.
