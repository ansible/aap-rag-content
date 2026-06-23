# Operator-based installations
## Change the SSL/TLS certificate and key for automation hub on OpenShift Container Platform

The following procedure describes how to change the SSL/TLS certificate and key for your operator-based Ansible Automation Platform installation of automation hub running on OpenShift Container Platform.

### Procedure

1.  Copy the signed SSL/TLS certificate and key to a secure location.
2.  Create a TLS secret within OpenShift:


```
oc create secret tls hub-certs-$(date +%F) --cert=/path/to/ssl.crt --key=/path/to/ssl.key -n <namespace>
```

3.  Edit the Ansible Automation Platform custom resource to add `route_tls_secret` under the `hub` section:


```
oc edit ansibleautomationplatform <aap-instance-name> -n <namespace>
```

4.  Add or update the `route_tls_secret` parameter under `spec.hub`:


```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
namespace: ansible-automation-platform
spec:
hub:
route_tls_secret: hub-certs-2024-03-24
```
Note:
The name of the TLS secret is arbitrary. In this example, it is timestamped with the date that the secret is created, to differentiate it from other TLS secrets applied to the automation hub instance.

The operator automatically applies this configuration to the automation hub instance managed by this Ansible Automation Platform deployment.

5.  Wait a few minutes for the changes to be applied.
6.  Verify that new SSL/TLS certificate and key have been installed:


```
true | openssl s_client -showcerts -connect ${HUB_FQDN}:443
```
