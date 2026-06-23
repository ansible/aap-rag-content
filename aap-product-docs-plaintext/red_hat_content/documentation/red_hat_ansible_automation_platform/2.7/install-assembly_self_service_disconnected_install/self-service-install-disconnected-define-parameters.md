# Install Ansible automation portal in air-gapped OpenShift Container Platform environments
## Configure plug-in delivery for disconnected environments

Create the registry authentication secret so the dynamic plug-in init container can pull OCI artifacts from your disconnected registry.

### Before you begin

- You have mirrored the required container images and plug-in artifacts to your disconnected registry.
- You have credentials for your disconnected registry.

### Procedure

1.  Create an auth.json file with credentials for your disconnected registry:


```
{
"auths": {
"<disconnected_registry_url>": {
"auth": "<base64-encoded-registry-credentials>"
}
}
}
```
Generate the base64-encoded value:

```
$ printf '%s' '<registry_username>:<registry_password>' | base64 -w0
```

2.  Create the registry authentication secret:


```
$ oc create secret generic <release-name>-dynamic-plugins-registry-auth \
--from-file=auth.json=./auth.json \
-n <project_name>
```
Replace `<release-name>` with your Helm release name. If you use the default release name from the OpenShift catalog, the secret name is `redhat-rhaap-portal-dynamic-plugins-registry-auth`.

### Results

Verify that the secret exists in the project:

```
$ oc get secret <release-name>-dynamic-plugins-registry-auth -n <project_name>
```

