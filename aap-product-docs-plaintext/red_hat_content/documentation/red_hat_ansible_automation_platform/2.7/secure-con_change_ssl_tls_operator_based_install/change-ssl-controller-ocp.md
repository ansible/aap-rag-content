# Operator-based installations
## Change the SSL/TLS certificate and key on automation controller on OpenShift Container Platform

The following procedure describes how to change the SSL/TLS certificate and key for automation controller running on OpenShift Container Platform.

### Procedure

1.  Copy the signed SSL/TLS certificate and key to a secure location.
2.  Create a TLS secret within OpenShift:


```
oc create secret tls controller-certs-$(date +%F) --cert=/path/to/ssl.crt --key=/path/to/ssl.key -n <namespace>
```

3.  Edit the Ansible Automation Platform custom resource to add `route_tls_secret` under the `controller` section:


```
oc edit ansibleautomationplatform <aap-instance-name> -n <namespace>
```

4.  Add or update the `route_tls_secret` parameter under `spec.controller`:


```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
namespace: ansible-automation-platform
spec:
controller:
route_tls_secret: controller-certs-2024-03-24
```

Note:
The name of the TLS secret is arbitrary. In this example, it is timestamped with the date that the secret is created, to differentiate it from other TLS secrets applied to the automation controller instance.

The operator automatically applies this configuration to the automation controllerinstance managed by this Ansible Automation Platform deployment.

5.  Wait a few minutes for the changes to be applied.
6.  Verify that new SSL/TLS certificate and key have been installed:


```
true | openssl s_client -showcerts -connect ${CONTROLLER_FQDN}:443
```

