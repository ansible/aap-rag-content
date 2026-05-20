# 2. Logging in to self-service automation portal
## 2.2. Configuring custom SSL certificates for self-service automation portal

If your Ansible Automation Platform instance uses custom or self-signed SSL certificates, you must configure self-service automation portal to trust those certificates. Without this configuration, authentication between self-service automation portal and Ansible Automation Platform fails with SSL verification errors.

**Prerequisites**

- You have administrator access to your OpenShift Container Platform cluster.
- You have the custom Certificate Authority (CA) certificate file used by your Ansible Automation Platform instance.
- self-service automation portal is installed in your OpenShift Container Platform cluster.

**Procedure**

1. Obtain the CA certificate file from your Ansible Automation Platform instance.

If you do not have the CA certificate file, you can extract it from your Ansible Automation Platform server:

openssl s_client -showcerts -connect <aap-hostname>:443 </dev/null 2>/dev/null | openssl x509 -outform PEM > aap-ca-cert.pem

Replace `<aap-hostname>` with your Ansible Automation Platform hostname.

2. Log in to your OpenShift Container Platform cluster with administrator privileges.

3. Create a ConfigMap containing your custom CA certificate:

oc create configmap custom-ca-bundle \
--from-file=ca-bundle.crt=aap-ca-cert.pem \
-n <namespace>

Replace `<namespace>` with the namespace where self-service automation portal is installed.

4. Update your self-service automation portal Helm chart values to mount the custom CA certificate:

upstream:
backstage:
extraEnvVarsSecrets:
- custom-ca-bundle
extraVolumes:
- name: custom-ca
configMap:
name: custom-ca-bundle
extraVolumeMounts:
- name: custom-ca
mountPath: /etc/pki/ca-trust/source/anchors/
readOnly: true

5. Apply the updated configuration by upgrading the self-service automation portal Helm chart:

helm upgrade <release-name> <chart-name> \
-f values.yaml \
-n <namespace>

Replace `<release-name>` with your Helm release name and `<chart-name>` with the self-service automation portal chart name.

6. Wait for the self-service automation portal pods to restart with the new configuration.

**Verification**

1. Verify that the self-service automation portal pods are running:

oc get pods -n <namespace>

All self-service automation portal pods should show a status of `Running`.

2. Attempt to sign in to self-service automation portal using your Ansible Automation Platform credentials.

If the SSL certificate configuration is correct, you can authenticate successfully without SSL verification errors.

3. Check the self-service automation portal logs for SSL-related errors:

oc logs -n <namespace> <pod-name> | grep -i ssl

If you see no SSL verification errors, the custom CA certificate is trusted correctly.

**Troubleshooting**

If you continue to experience SSL verification errors after following this procedure:

- Verify that the CA certificate file contains the complete certificate chain.
- Ensure that the certificate file is in PEM format.
- Confirm that the Ansible Automation Platform hostname in your configuration matches the hostname in the SSL certificate.
- Check that the `checkSSL` parameter in your Helm values is set to `true` (the default). Setting it to `false` disables SSL verification entirely, which is not recommended for production environments.

