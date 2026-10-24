# Configure custom TLS certificates for the automation portal operator

Configure a custom CA certificate bundle or a custom TLS certificate for the automation portal route when your environment uses certificates signed by a private certificate authority.

## Before you begin

- The automation portal operator installed and running on your OpenShift cluster.
- The `oc` CLI installed and authenticated to your OpenShift cluster.

## About this task

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

The automation portal operator supports two TLS certificate configurations:

- **Custom CA bundle** — provides CA certificates that the automation portal uses to validate connections to internal services, such as your AAP instance or a private container registry. Use this when your environment uses certificates signed by a private certificate authority.
- **Custom route TLS certificate** — replaces the default OpenShift-managed TLS certificate on the automation portal route with a certificate you provide.

You can configure one or both options independently.

## Procedure

1. **Optional:** To configure a custom CA bundle, create a Secret containing your CA certificate bundle.


```terminal
$ oc create secret generic portal-ca-bundle \
--from-file=ca-bundle.crt=/path/to/ca-bundle.pem \
-n automation-portal
```

The Secret key must be named `ca-bundle.crt`. The file can contain multiple PEM-encoded certificates concatenated together.

Add the Secret reference to the `AutomationPortal` custom resource:



```yaml
spec:
backstage:
caCertificates:
secretRef: portal-ca-bundle
```

The operator mounts the CA bundle in all automation portal containers and sets the `NODE_EXTRA_CA_CERTS`, `REQUESTS_CA_BUNDLE`, and `SSL_CERT_FILE` environment variables so that the portal trusts your internal CA without disabling SSL verification.

Important:
Use `caCertificates.secretRef` instead of setting `spec.aap.checkSSL: false`. Disabling SSL verification exposes credentials to man-in-the-middle attacks. Set `checkSSL: false` only as a last resort when you cannot provide a CA certificate.

2. **Optional:** To configure a custom TLS certificate for the automation portal route, create a Secret containing the certificate and private key.


```terminal
$ oc create secret generic portal-tls \
--from-file=tls.crt=/path/to/tls.crt \
--from-file=tls.key=/path/to/tls.key \
-n automation-portal
```

If your certificate requires an intermediate CA certificate, you can include it as an optional `ca.crt` key:

```terminal
$ oc create secret generic portal-tls \
--from-file=tls.crt=/path/to/tls.crt \
--from-file=tls.key=/path/to/tls.key \
--from-file=ca.crt=/path/to/ca.crt \
-n automation-portal
```

Add the Secret reference to the `AutomationPortal` custom resource:



```yaml
spec:
backstage:
route:
tls:
secretRef: portal-tls
```

3. Apply the updated custom resource.


```terminal
$ oc apply -f portal.yaml -n automation-portal
```

The operator reconciles the configuration and restarts the automation portal pod. Monitor the deployment status:

```terminal
$ oc get automationportal portal -n automation-portal -w
```

Wait for `Phase: Running`. If the phase stays `Pending`, check the status conditions for certificate errors. See [Troubleshoot your portal operator deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_your_portal_operator_deployment#troubleshoot-portal-operator "Diagnose and resolve common issues when deploying or operating the automation portal operator on OpenShift, including status condition interpretation, log collection, and cleanup procedures.").

## Results

The automation portal uses the configured TLS certificates. If you provided a CA bundle, connections to internal services signed by your private CA are now trusted. If you provided a route TLS certificate, the automation portal serves traffic using your certificate.
