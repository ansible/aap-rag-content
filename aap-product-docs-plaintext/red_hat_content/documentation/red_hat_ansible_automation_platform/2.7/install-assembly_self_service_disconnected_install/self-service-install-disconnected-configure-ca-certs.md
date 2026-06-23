# Install Ansible automation portal in air-gapped OpenShift Container Platform environments
## Configure CA certificates for private registries

If your private registry uses a certificate signed by an internal or self-signed CA, mount the CA certificate into the `install-dynamic-plugins` init container so that `skopeo` trusts the registry.

### Procedure

1.  Obtain the CA certificate chain that signed your mirror registry's TLS certificate.
If the registry uses a certificate chain, include the full chain:

```terminal
$ cat registry.crt intermediate.crt root.crt > ca-bundle.crt
```

2.  Create a ConfigMap from the CA certificate:


```terminal
$ oc create configmap registry-ca-crt \
--from-file=ca.crt=ca-bundle.crt -n *namespace*
```

3.  Add the volume and mount to your values file.
Add the `registry-ca-crt` volume to `extraVolumes`, and add the CA certificate volume mount to the `install-dynamic-plugins` init container:

```yaml
redhat-developer-hub:
upstream:
backstage:
extraVolumes:
- name: registry-ca-crt
configMap:
name: registry-ca-crt
initContainers:
- name: install-dynamic-plugins
volumeMounts:
- name: registry-ca-crt
mountPath: /etc/containers/certs.d/*registry-host*
readOnly: true
```
Note:
The `mountPath` for the CA certificate must be the registry hostname only (for example, `/etc/containers/certs.d/mirror.example.com`). Do not include repository paths. If the registry uses a non-standard port, include it in the path (for example, `/etc/containers/certs.d/mirror.example.com:5000`).

### Results

After the deployment restarts, check the `install-dynamic-plugins` init container logs for certificate errors:

```terminal
$ oc logs *pod-name* -c install-dynamic-plugins -n *namespace* | grep -i "x509\|certificate"
```
If the CA certificate is mounted correctly, there are no `x509: certificate signed by unknown authority` errors.

