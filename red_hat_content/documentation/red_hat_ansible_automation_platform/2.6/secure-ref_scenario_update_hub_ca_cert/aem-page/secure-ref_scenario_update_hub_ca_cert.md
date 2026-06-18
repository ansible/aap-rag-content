+++
title = "Configure a CA file - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_scenario_update_hub_ca_cert"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_changing_ssl_certs_keys/", "Renew and change SSL/TLS certificates"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-ref_scenario_update_hub_ca_cert/aem-page/secure-ref_scenario_update_hub_ca_cert.html"
last_crumb = "Configure a CA file"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure a CA file"
oversized = "false"
page_slug = "secure-ref_scenario_update_hub_ca_cert"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-ref_scenario_update_hub_ca_cert"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-ref_scenario_update_hub_ca_cert/toc/toc.json"
type = "aem-page"
+++

# Configure a CA file

Use this example to customize the default definition file to include a CA certificate to the `additional-build-files` section, move the file to the appropriate directory and, run the command to update the dynamic configuration of CA certificates to allow the system to trust this certificate.

 **Prerequisites**

- A custom CA certificate, for example `rootCA.crt`.


Note:

Customizing the CA certificate using `prepend_base` means that the resulting CA configuration is displayed in all other build stages and the final image, because all other build stages inherit from the base image.

```
additional_build_files:
  # copy the CA public key into the build context, we will copy and use it in the base image later
  - src: files/rootCA.crt
    dest: configs

additional_build_steps:
  prepend_base:
    # copy a custom CA cert into the base image and recompute the trust database
    # because this is in "base", all stages will inherit (including the final EE)
    - COPY _build/configs/rootCA.crt /usr/share/pki/ca-trust-source/anchors
    - RUN update-ca-trust

options:
  package_manager_path: /usr/bin/microdnf  # downstream images use non-standard package manager

[galaxy]
server_list = automation_hub
```
