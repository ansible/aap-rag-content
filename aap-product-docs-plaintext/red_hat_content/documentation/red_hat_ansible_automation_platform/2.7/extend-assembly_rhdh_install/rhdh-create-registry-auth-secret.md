# Install the Ansible plug-ins
## Create the registry authentication secret

Red Hat Developer Hub pulls the Ansible plug-ins directly from `registry.redhat.io` as OCI artifacts during startup. This requires a registry authentication secret in the same OpenShift Container Platform project as your Red Hat Developer Hub deployment.

### Procedure

1.  Log in to the container image registry:


```terminal
$ podman login --authfile auth.json registry.redhat.io
```
To authenticate to multiple registries, run `podman login` for each registry. The `auth.json` file accumulates credentials for all registries you log in to.

2.  Create a secret from the `auth.json` file in the same OpenShift Container Platform project as your Red Hat Developer Hub deployment.
For an Operator-based deployment:

```terminal
$ oc create secret generic dynamic-plugins-registry-auth \
--from-file=auth.json=auth.json \
-n <your_rhdh_namespace>
```
For a Helm-based deployment:

```terminal
$ oc create secret generic <release_name>-dynamic-plugins-registry-auth \
--from-file=auth.json=auth.json \
-n <your_rhdh_namespace>
```
Replace `<release_name>` with your Helm release name.

Important:
The secret name is fixed. The Red Hat Developer Hub Operator and Helm chart expect these exact names. You cannot use a custom name.

*Table 1. Secret names by deployment method*

| Deployment method | Secret name                                    |
| ----------------- | ---------------------------------------------- |
| Operator          | `dynamic-plugins-registry-auth`                |
| Helm chart        | `<release_name>-dynamic-plugins-registry-auth` |
Note:
For disconnected or restricted network environments, mirror the `automation-portal` OCI image to an internal registry and use OCI references pointing to that registry instead.

### Results

Verify that the secret exists in the project.

For an Operator-based deployment:

```terminal
$ oc get secret dynamic-plugins-registry-auth -n <your_rhdh_namespace>
```
For a Helm-based deployment:

```terminal
$ oc get secret <release_name>-dynamic-plugins-registry-auth -n <your_rhdh_namespace>
```

