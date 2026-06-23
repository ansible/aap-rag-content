# Upgrade Ansible automation portal
## Troubleshooting the migration
### Duplicate registry path in OCI URLs

**Symptom:** Init container logs or Helm values show duplicate paths, for example: `oci://yb-artifactory/ansible-automation-platform/ansible-automation-platform/automation-portal:2.2`.

**Cause:** The `imageRegistry` value includes a repository path instead of being the registry host only.

**Resolution:** Edit your `backup-values.yaml` and set `imageRegistry` to the registry host only, without the repository path:

```yaml
# Incorrect (includes repository path):
imageRegistry: "yb-artifactory/ansible-automation-platform"

# Correct (host only):
imageRegistry: "yb-artifactory"
```
Then re-run `helm upgrade` with the corrected values file.

