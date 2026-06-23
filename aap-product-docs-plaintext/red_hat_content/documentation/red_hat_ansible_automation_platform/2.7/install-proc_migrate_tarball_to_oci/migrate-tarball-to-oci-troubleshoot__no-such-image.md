# Migrate from HTTP plug-in registry to OCI container delivery
## Troubleshooting the migration
### No such image error

**Symptom:** Init container logs show `Error: no such image` or `manifest not found`.

**Cause:** The OCI image does not exist in the specified registry, or the `imageTagInfo` version does not match what is available.

**Resolution:**

1. Verify the `imageTagInfo` value in your Helm release matches an available version. Check the [Ansible automation portal lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page.
2. If using a mirror registry, ensure the image was mirrored to the correct path. Run:

```
$ podman search <your-mirror-registry>/ansible-automation-platform/automation-portal
```

3. Confirm that `imageRegistry` is set correctly and does not include a duplicate repository path (see the Duplicate registry path section above).

