+++
template = "docs/aem-title.html"
title = "Configure ANSIBLE_BASE_JWT_VALIDATE_CERT - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-configure_ansible_base_jwt_validate_cert"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-ansible_base_jwt_validate_cert_default_change/", "ANSIBLE_BASE_JWT_VALIDATE_CERT default change for Red Hat Ansible Lightspeed"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-configure_ansible_base_jwt_validate_cert/aem-page/extend-configure_ansible_base_jwt_validate_cert.html"
last_crumb = "Configure ANSIBLE_BASE_JWT_VALIDATE_CERT"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Configure ANSIBLE_BASE_JWT_VALIDATE_CERT"
oversized = "false"
page_slug = "extend-configure_ansible_base_jwt_validate_cert"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-configure_ansible_base_jwt_validate_cert"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-configure_ansible_base_jwt_validate_cert/toc/toc.json"
type = "aem-page"
+++

# Configure ANSIBLE_BASE_JWT_VALIDATE_CERT

Configure how Red Hat Ansible Lightspeed validates TLS certificates when authenticating with the Ansible Automation Platform gateway.

## Before you begin

- You have administrator access to your Ansible Automation Platform deployment.
- Your deployment uses self-signed or internally signed certificates.

## Procedure

**For operator-based deployments**

1. Choose one of the following options to configure certificate validation:
  - **Option 1: Add a CA certificate (recommended)**

        Create a secret containing your CA certificate and reference it in the `AnsibleAutomationPlatform` CR:

```
$ kubectl create secret generic <resourcename>-custom-certs \
     --from-file=bundle-ca.crt=<path/to/ca.crt>
```

        Then, add the secret reference to your `AnsibleAutomationPlatform` CR:

```
spec:
  bundle_cacert_secret: <resourcename>-custom-certs
```

  - **Option 2: Disable certificate validation**

        Add the setting to the `extra_settings` array in the `AnsibleAutomationPlatform` CR:

```
spec:
  extra_settings:
    - setting: ANSIBLE_BASE_JWT_VALIDATE_CERT
      value: "False"
```

    Important:
            Disabling TLS certificate validation exposes the authentication flow to potential man-in-the-middle attacks. Use only in development or testing environments.

**For containerized deployments**

2. Choose one of the following options to configure certificate validation:
  - **Option 1: Add a CA certificate (recommended)**

        Copy your CA certificate to the host and update the trust store:

```
$ sudo cp <path/to/ca.crt> /etc/pki/ca-trust/source/anchors/
$ sudo update-ca-trust
```

        Then, restart the Lightspeed service:

```
$ sudo systemctl restart automation-lightspeed
```

  - **Option 2: Disable certificate validation**

        Add the setting to `lightspeed_extra_settings` in your inventory file:

```
lightspeed_extra_settings:
  - setting: ANSIBLE_BASE_JWT_VALIDATE_CERT
    value: False
```

        Then, re-run the installer:

```
$ ansible-playbook -i <inventory_file_name> ansible.containerized_installer.install
```

    Important:
            Disabling TLS certificate validation exposes the authentication flow to potential man-in-the-middle attacks. Use only in development or testing environments.

## Results

Check the Lightspeed service logs for TLS-related warnings.

For a containerized deployment, run:

```
$ sudo podman logs lightspeed-api
```

For an operator-based deployment, run:

```
$ kubectl logs -l app.kubernetes.io/name=lightspeed -n <namespace>
```

If `ANSIBLE_BASE_JWT_VALIDATE_CERT` is set to `False`, the logs display the following CRITICAL warning:

```
CRITICAL: ANSIBLE_BASE_JWT_VALIDATE_CERT is disabled. JWT public key retrieval is not verifying TLS certificates. This is a security risk.
```

If no TLS warnings appear, certificate validation is active and the connection to the platform gateway is secured.
