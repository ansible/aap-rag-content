# Upgrade Ansible automation portal
## Migrating in air-gapped and disconnected environments
### Configuring Helm values for mirror registry

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

