# Upgrade Ansible automation portal
## Troubleshooting the migration
### Authentication failures

**Symptom:** Init container logs show `authentication required` or `unauthorized: access denied`.

**Cause:** The `<release-name>-dynamic-plugins-registry-auth` secret is missing, malformed, or has incorrect credentials.

**Resolution:**

1. Verify the secret exists:

```
$ oc get secret <release-name>-dynamic-plugins-registry-auth -n <namespace>
```

2. Check the secret contents:

```
$ oc get secret <release-name>-dynamic-plugins-registry-auth \
-o jsonpath='{.data.auth\.json}' -n <namespace> | base64 -d
```
The output should be valid JSON with your credentials.

3. Ensure the secret name matches your Helm release name exactly. For example, if your release is `redhat-rhaap-portal`, the secret must be `redhat-rhaap-portal-dynamic-plugins-registry-auth`.

4. Recreate the secret with correct credentials if needed:

```
$ oc delete secret <release-name>-dynamic-plugins-registry-auth -n <namespace>
$ oc create secret generic <release-name>-dynamic-plugins-registry-auth \
--from-file=auth.json=./auth.json -n <namespace>
```

