+++
template = "docs/aem-title.html"
title = "Configure custom SSL certificates for the Ansible automation portal - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_self_service_configure_custom_ssl"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_self_service_configure_custom_ssl/aem-page/install-proc_self_service_configure_custom_ssl.html"
last_crumb = "Configure custom SSL certificates for the Ansible automation portal"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure custom SSL certificates for the Ansible automation portal"
oversized = "false"
page_slug = "install-proc_self_service_configure_custom_ssl"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_self_service_configure_custom_ssl"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_self_service_configure_custom_ssl/toc/toc.json"
type = "aem-page"
+++

# Configure custom SSL certificates for the Ansible automation portal

If your Ansible Automation Platform instance uses custom or self-signed SSL certificates, configure the Ansible automation portal to trust those certificates to prevent authentication failures.

## Before you begin

- You have administrator access to your Red Hat OpenShift Container Platform cluster.
- You have the custom Certificate Authority (CA) certificate file used by your Ansible Automation Platform instance.
- The Ansible automation portal is installed in your Red Hat OpenShift Container Platform cluster.

## Procedure

1.  Obtain the CA certificate file from your Ansible Automation Platform instance.
      If you do not have the CA certificate file, you can extract it from your Ansible Automation Platform server:

```terminal
$ openssl s_client -showcerts -connect *aap-hostname*:443 </dev/null 2>/dev/null | openssl x509 -outform PEM > aap-ca-cert.pem
```
    Replace *aap-hostname* with your Ansible Automation Platform hostname.

2.  Log in to your Red Hat OpenShift Container Platform cluster with administrator privileges.
3.  Create a ConfigMap containing your custom CA certificate:
  

```terminal
$ oc create configmap custom-ca-bundle \
  --from-file=ca-bundle.crt=aap-ca-cert.pem \
  -n *namespace*
```
    Replace *namespace* with the namespace where the Ansible automation portal is installed.

4.  Update your Ansible automation portal Helm chart values to mount the custom CA certificate.
      Add the `custom-ca` volume and volume mount to your values file:

```yaml
upstream:
  backstage:
    extraVolumes:
      - name: custom-ca
        configMap:
          name: custom-ca-bundle
    extraVolumeMounts:
      - name: custom-ca
        mountPath: /etc/pki/ca-trust/source/anchors/
        readOnly: true
```

5.  Apply the updated configuration by upgrading the Ansible automation portal Helm chart:
  

```terminal
$ helm upgrade *release-name* *chart-name* \
  -f values.yaml \
  -n *namespace*
```
    Replace *release-name* with your Helm release name and *chart-name* with the Ansible automation portal chart name.

6.  Wait for the Ansible automation portal pods to restart with the new configuration.

## Results

1. Verify that the Ansible automation portal pods are running:

```terminal
$ oc get pods -n *namespace*
```
     All Ansible automation portal pods should show a status of `Running`.

2. Attempt to sign in to the Ansible automation portal using your Ansible Automation Platform credentials. If the SSL certificate configuration is correct, you can authenticate successfully without SSL verification errors.

3. Check the Ansible automation portal logs for SSL-related errors:

```terminal
$ oc logs -n *namespace* *pod-name* | grep -i ssl
```
     If you see no SSL verification errors, the custom CA certificate is trusted correctly.

If you continue to experience SSL verification errors after following this procedure:

- Verify that the CA certificate file contains the complete certificate chain.
- Ensure that the certificate file is in PEM format.
- Confirm that the Ansible Automation Platform hostname in your configuration matches the hostname in the SSL certificate.
- Check that the `checkSSL` parameter in your Helm values is set to `true` (the default). Setting it to `false` disables SSL verification entirely, which is not recommended for production environments.
