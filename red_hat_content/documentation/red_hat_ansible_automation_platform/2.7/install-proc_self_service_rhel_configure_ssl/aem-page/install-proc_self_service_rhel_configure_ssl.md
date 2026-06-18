+++
title = "Replace self-signed SSL certificates - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_ssl"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_ssl/aem-page/install-proc_self_service_rhel_configure_ssl.html"
last_crumb = "Replace self-signed SSL certificates"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Replace self-signed SSL certificates"
oversized = "false"
page_slug = "install-proc_self_service_rhel_configure_ssl"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_ssl"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_ssl/toc/toc.json"
type = "aem-page"
+++

# Replace self-signed SSL certificates

The Ansible automation portal RHEL appliance generates self-signed SSL certificates at first boot and stores them at /etc/portal/ssl/. Replace these certificates with certificates from a trusted certificate authority for production use.

## Replace the SSL certificates

Prerequisites:

- A TLS certificate and private key in PEM format, issued by a certificate authority trusted by your organization.
- SSH access to the appliance.


Procedure:

1. Copy your certificates to the appliance:

```terminal
$ sudo cp *certificate-file*.pem /etc/portal/ssl/cert.pem
$ sudo cp *private-key-file*.pem /etc/portal/ssl/key.pem
$ sudo chmod 644 /etc/portal/ssl/cert.pem
$ sudo chmod 600 /etc/portal/ssl/key.pem
```

2. Restart the Ansible automation portal service:

```terminal
$ sudo systemctl restart portal
```

Verification:

- Verify that the Ansible automation portal is using the new certificate:

```terminal
$ curl -vk https://localhost 2>&1 | grep -i "issuer"
```
     The output displays the issuer from your certificate, not the self-signed issuer.

## Trust a custom certificate authority

If your organization uses a custom certificate authority (CA) or a self-signed certificate for your Ansible Automation Platform instance, configure the Ansible automation portal RHEL appliance to trust it.

Prerequisites:

- The CA certificate or self-signed certificate in PEM format.
- SSH access to the appliance.


Procedure:

1. Copy the CA certificate or self-signed certificate to the appliance:

```terminal
$ sudo cp *ca-certificate-file*.pem /etc/portal/ssl/ca-bundle.crt
```
     If you have multiple CA certificates to trust, concatenate them into a single bundle file before copying it to the appliance.

2. Create a Quadlet drop-in to set the `NODE_EXTRA_CA_CERTS` environment variable:

```terminal
$ sudo mkdir -p /etc/containers/systemd/portal.container.d
$ echo -e '[Container]\nEnvironment=NODE_EXTRA_CA_CERTS=/etc/portal/ssl/ca-bundle.crt' \
  | sudo tee /etc/containers/systemd/portal.container.d/ca-certs.conf
```

3. Reload systemd and restart the Ansible automation portal service:

```terminal
$ sudo systemctl daemon-reload
$ sudo systemctl restart portal
```

Verification:

- Verify that the environment variable is set in the portal container:

```terminal
$ sudo podman exec portal env | grep NODE_EXTRA_CA_CERTS
```
     The output displays `NODE_EXTRA_CA_CERTS=/etc/portal/ssl/ca-bundle.crt`.
