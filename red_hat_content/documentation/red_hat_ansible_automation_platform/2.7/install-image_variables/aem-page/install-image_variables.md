+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-image_variables"
template = "docs/aem-title.html"
title = "Image variables - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_inventory_file_vars/", "Inventory file variables"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-image_variables/aem-page/install-image_variables.html"
last_crumb = "Image variables"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Image variables"
oversized = "false"
page_slug = "install-image_variables"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-image_variables"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-image_variables/toc/toc.json"
type = "aem-page"
+++

# Image variables

Reference information for the inventory file variables used to configure images.

| Variable name             | Description                                                                                                             | Required or optional | Default                              |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------ |
| <br>`controller_image`    | <br>Container image for automation controller.                                                                          | <br>Optional         | <br>`controller-rhel9:latest`        |
| <br>`de_extra_images`     | <br>Additional decision environment container images to pull from the configured container registry during deployment.  | <br>Optional         | <br>`[]`                             |
| <br>`de_supported_image`  | <br>Supported decision environment container image.                                                                     | <br>Optional         | <br>`de-supported-rhel9:latest`      |
| <br>`eda_image`           | <br>Backend container image for Event-Driven Ansible.                                                                   | <br>Optional         | <br>`eda-controller-rhel9:latest`    |
| <br>`eda_web_image`       | <br>Front-end container image for Event-Driven Ansible.                                                                 | <br>Optional         | <br>`eda-controller-ui-rhel9:latest` |
| <br>`ee_extra_images`     | <br>Additional execution environment container images to pull from the configured container registry during deployment. | <br>Optional         | <br>`[]`                             |
| <br>`ee_minimal_image`    | <br>Minimal execution environment container image.                                                                      | <br>Optional         | <br>`ee-minimal-rhel9:latest`        |
| <br>`ee_supported_image`  | <br>Supported execution environment container image.                                                                    | <br>Optional         | <br>`ee-supported-rhel9:latest`      |
| <br>`gateway_image`       | <br>Container image for platform gateway.                                                                               | <br>Optional         | <br>`gateway-rhel9:latest`           |
| <br>`gateway_proxy_image` | <br>Container image for platform gateway proxy.                                                                         | <br>Optional         | <br>`gateway-proxy-rhel9:latest`     |
| <br>`hub_image`           | <br>Backend container image for automation hub.                                                                         | <br>Optional         | <br>`hub-rhel9:latest`               |
| <br>`hub_web_image`       | <br>Front-end container image for automation hub.                                                                       | <br>Optional         | <br>`hub-web-rhel9:latest`           |
| <br>`pcp_image`           | <br>Container image for Performance Co-Pilot.                                                                           | <br>Optional         | <br>`pcp:latest`                     |
| <br>`postgresql_image`    | <br>Container image for PostgreSQL.                                                                                     | <br>Optional         | <br>`postgresql-15:latest`           |
| <br>`receptor_image`      | <br>Container image for receptor.                                                                                       | <br>Optional         | <br>`receptor-rhel9:latest`          |
| <br>`redis_image`         | <br>Container image for Redis.                                                                                          | <br>Optional         | <br>`redis-6:latest`                 |
