+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_change_ssl_tls_operator_based_install"
title = "Operator-based installations - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_changing_ssl_certs_keys/", "Renew and change SSL/TLS certificates"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_change_ssl_tls_operator_based_install/aem-page/secure-con_change_ssl_tls_operator_based_install.html"
last_crumb = "Operator-based installations"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Operator-based installations"
oversized = "false"
page_slug = "secure-con_change_ssl_tls_operator_based_install"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_change_ssl_tls_operator_based_install"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_change_ssl_tls_operator_based_install/toc/toc.json"
type = "aem-page"
+++

# Operator-based installations

You can change the TLS certificates and keys for your operator-based Ansible Automation Platform installation.

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
