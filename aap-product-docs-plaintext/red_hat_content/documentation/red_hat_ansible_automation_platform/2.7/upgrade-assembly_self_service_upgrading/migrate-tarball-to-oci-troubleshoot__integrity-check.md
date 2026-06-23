# Upgrade Ansible automation portal
## Troubleshooting the migration
### Integrity check errors

**Symptom:** Init container logs show `integrity check failed` or `digest mismatch`.

**Cause:** The OCI image in your registry does not match the expected digest, or the image was corrupted during mirroring.

**Resolution:**

1. Re-mirror the image from `registry.redhat.io` using `skopeo copy` instead of `podman tag/push`. The `skopeo copy` command preserves the original manifest digest:

```
$ skopeo copy \
docker://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version> \
docker://<your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
```

2. If the error persists, verify the image in your mirror registry:

```
$ skopeo inspect docker://<your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
```

3. Ensure you are not using a stale local image cache. Delete and re-pull if needed.

