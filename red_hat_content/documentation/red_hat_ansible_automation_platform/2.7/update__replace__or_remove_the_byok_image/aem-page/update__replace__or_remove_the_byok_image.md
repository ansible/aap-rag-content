+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/update__replace__or_remove_the_byok_image"
template = "docs/aem-title.html"
title = "Update or replace the BYOK image - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/update__replace__or_remove_the_byok_image/aem-page/update__replace__or_remove_the_byok_image.html"
last_crumb = "Update or replace the BYOK image"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Update or replace the BYOK image"
oversized = "false"
page_slug = "update__replace__or_remove_the_byok_image"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/update__replace__or_remove_the_byok_image"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/update__replace__or_remove_the_byok_image/toc/toc.json"
type = "aem-page"
+++

# Update or replace the BYOK image

When your organization's documentation changes, you can update or replace the deployed BYOK image with the latest image, or remove it entirely.

## Before you begin

You have deployed a BYOK RAG image on a container-based or operator-based AAP 2.7 installation.

## Procedure

1.  Rebuild the BYOK RAG image using the latest version of your documentation by following the steps in [Build a searchable knowledge base image from your documentation](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-build_a_searchable_knowledge_base_image_from_your_documentation "The rag-content tool converts your documentation into a vector database that the intelligent assistant uses to retrieve relevant content when responding to queries. Use this procedure to download the tool version best suited to your system's hardware.").
2.  Publish the new version to your registry.
3.  Update the BYOK image reference in your Ansible configuration.
4.  Restart the intelligent assistant service (rerun the installer) to pick up the new image. The BYOK configuration persists and does not require reconfiguration after restarting.

## Remove the BYOK image

An administrator can remove the deployed BYOK RAG image. With this removal, the intelligent assistant reverts to using the default Ansible Automation Platform 2.7 documentation.

### Procedure

1.  Remove the BYOK image configuration from your installation variables.
2.  Re-run the installer, which restarts the service with the new configuration. The intelligent assistant resumes operating with only the default Ansible Automation Platform 2.7 documentation RAG pipeline.
