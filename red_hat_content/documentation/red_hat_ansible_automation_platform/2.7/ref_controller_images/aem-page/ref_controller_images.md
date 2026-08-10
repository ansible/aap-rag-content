+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/ref_controller_images"
title = "Images - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/ref_controller_images/aem-page/ref_controller_images.html"
last_crumb = "Images"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Images"
oversized = "false"
page_slug = "ref_controller_images"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/ref_controller_images"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/ref_controller_images/toc/toc.json"
type = "aem-page"
+++

# Images

Use the **images** dictionary to define container images for your execution environment. Each key represents a unique image name, while the corresponding value is a dictionary defining that image's properties.

At a minimum you must specify a source, image, and tag for the base image. The base image provides the operating system and can also provide some packages. Use the standard `host/namespace/container:tag` syntax to specify images. You can use Podman or Docker shortcut syntax instead, but the full definition is more reliable and portable.

Valid keys for this section are:

| <br> **base\_image** | <br>A dictionary defining the parent image for the execution environment.<br>A `name` key must be supplied with the container image to use. Use the `signature_original_name` key if the image is mirrored within your repository, but signed with the original image’s signature key. |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
