# Install Ansible automation portal in air-gapped OpenShift Container Platform environments
## Mirror container images

Use `skopeo copy` to mirror the required container images from the Red Hat registry to your disconnected registry for installing the Ansible automation portal in an isolated environment.

### Before you begin

- `skopeo` is installed.
- You have authenticated to `registry.redhat.io`:

```terminal
$ skopeo login registry.redhat.io
```

- You have authenticated to your disconnected registry:

```terminal
$ skopeo login <disconnected_registry_url>
```

### About this task

`skopeo copy` preserves SHA256 digests, so the Helm chart's default digest-based image references work without additional tag overrides.

If you mirror `registry.redhat.io` content to a different registry host (or to a registry prefix such as `quay.io/<org>`), you can set `redhat-developer-hub.global.imageRegistry` so the Helm chart pulls all of its images from that mirrored location. `imageRegistry` is a single override that controls the registry for the base application image, PostgreSQL image, OCI plug-in artifacts, and Ansible Dev Tools sidecar.

The dynamic plug-in init container does not use cluster-level image mirror configuration (for example, `ImageDigestMirrorSet` or `ImageTagMirrorSet`). You must set `imageRegistry` even if your cluster redirects `registry.redhat.io` pulls.

*Table 1. Required container images*

| Image                                                                                                                              | Source registry      | Purpose                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------ |
| `rhdh/rhdh-hub-rhel9:<rhdh_version>`                                                                                               | `registry.redhat.io` | Red Hat Developer Hub application and `install-dynamic-plugins` init container       |
| `rhel9/postgresql-<version>:<tag>`                                                                                                 | `registry.redhat.io` | Built-in PostgreSQL database (skip if using an external database)                    |
| `ansible-automation-platform-25/ansible-dev-tools-rhel8:latest` or `ansible-automation-platform-26/ansible-dev-tools-rhel9:latest` | `registry.redhat.io` | Ansible Dev Tools sidecar (base image varies by Ansible Automation Platform version) |
| `ansible-automation-platform/automation-portal:<plugin-version>`                                                                   | `registry.redhat.io` | Ansible plug-in OCI artifacts (OCI delivery only)                                    |
| `rhdh/rhdh-plugin-catalog-index-rhel9:<rhdh_version>`                                                                              | `registry.redhat.io` | Plug-in catalog index (rebuilt by `mirror-plugins.sh`)                               |


Replace version placeholders with the versions bundled with your Helm chart. See the [Ansible Automation Portal Lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page for version mappings.

### Procedure

1.  Copy the Red Hat Developer Hub hub image to your disconnected registry:


```terminal
$ skopeo copy \
docker://registry.redhat.io/rhdh/rhdh-hub-rhel9:<rhdh_version> \
docker://<disconnected_registry_url>/rhdh/rhdh-hub-rhel9:<rhdh_version>
```
This image is used for both the main application container and the `install-dynamic-plugins` init container. Replace `<rhdh_version>` with the Red Hat Developer Hub version bundled with your Helm chart.

2.  If you use the built-in PostgreSQL database, copy the PostgreSQL image.
An external database is the supported production architecture and does not require this step.

```terminal
$ skopeo copy \
docker://registry.redhat.io/rhel9/postgresql-<version>:<tag> \
docker://<disconnected_registry_url>/rhel9/postgresql-<version>:<tag>
```
Replace `<version>` with the PostgreSQL major version and `<tag>` with the image tag bundled with your Helm chart. See the [Ansible Automation Portal Lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page for version mappings.

3.  Copy the plug-in catalog index image:


```terminal
$ skopeo copy \
docker://registry.redhat.io/rhdh/rhdh-plugin-catalog-index-rhel9:<rhdh_version> \
docker://<disconnected_registry_url>/rhdh/rhdh-plugin-catalog-index-rhel9:<rhdh_version>
```
The Mirror dynamic plug-in artifacts procedure rebuilds this image with updated registry references. You must still mirror the original image because the script uses it as its source.

4.  If you use OCI container delivery, copy the Ansible plug-ins OCI artifacts image:


```terminal
$ skopeo copy \
docker://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version> \
docker://<disconnected_registry_url>/ansible-automation-platform/automation-portal:<plugin-version>
```

5.  Copy the Ansible Dev Tools sidecar image, using the path that matches your Ansible Automation Platform version.
**Ansible Automation Platform 2.5:**

```terminal
$ skopeo copy \
docker://registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest \
docker://<disconnected_registry_url>/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest
```
**Ansible Automation Platform 2.6:**

```terminal
$ skopeo copy \
docker://registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest \
docker://<disconnected_registry_url>/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest
```

### Results

Verify that each image is accessible in your disconnected registry. For example:

```terminal
$ skopeo inspect docker://<disconnected_registry_url>/rhdh/rhdh-hub-rhel9:<rhdh_version>
```
A successful response returns the image manifest metadata. An error indicates the image was not mirrored correctly.

