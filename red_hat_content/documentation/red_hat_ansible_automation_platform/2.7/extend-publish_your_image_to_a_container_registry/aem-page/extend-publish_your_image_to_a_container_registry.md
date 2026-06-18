+++
title = "Publish your image to a container registry - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-publish_your_image_to_a_container_registry"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/", "Extend the automation intelligent assistant with custom knowledge"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-publish_your_image_to_a_container_registry/aem-page/extend-publish_your_image_to_a_container_registry.html"
last_crumb = "Publish your image to a container registry"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Publish your image to a container registry"
oversized = "false"
page_slug = "extend-publish_your_image_to_a_container_registry"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-publish_your_image_to_a_container_registry"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-publish_your_image_to_a_container_registry/toc/toc.json"
type = "aem-page"
+++

# Publish your image to a container registry

Publish your BYOK RAG image to a container registry accessible from your Ansible Automation Platform deployment.

## Before you begin

- You have created the RAG image (vector database .tar file).
- You have the necessary permissions and credentials to write to your target registry.

## About this task

After building your custom RAG container image, upload it to a central container registry to make it accessible for deployment. Publishing the image ensures that your organization’s AI services can securely pull and use the vector database from any authorized environment.

## Procedure

1.  Load the image archive:
  

```
$ podman load < output/rag-content-output-latest.tar
```

2.  Tag the image for your registry:
  

```
$ podman tag localhost/rag-content-output:latest registry.example.com/aap/my-org-byok-rag:1.0
```

3.  Log in to your container registry:
  

```
$ podman login registry.example.com
```

4.  **For containerized Ansible deployments only:** Manually pull the image in the containerized installer Ansible Lightspeed instance VM:
  

```
$ podman pull registry.example.com/aap/my-org-byok-rag:1.0
```

5.  Push the image:
  

```
$ podman push registry.example.com/aap/my-org-byok-rag:1.0
```

## What to do next

Verify that the image is available:

```
podman search registry.example.com/aap/my-org-byok-rag --list-tags
```


The command outputs a list of all available versions, as in the following example output:

```
NAME                                            TAG
registry.example.com/aap/my-org-byok-rag        1.0
```
