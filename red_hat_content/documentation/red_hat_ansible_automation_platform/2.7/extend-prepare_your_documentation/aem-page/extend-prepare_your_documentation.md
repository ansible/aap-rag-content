+++
title = "Prepare your documentation - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-prepare_your_documentation"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/", "Extend the automation intelligent assistant with custom knowledge"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-prepare_your_documentation/aem-page/extend-prepare_your_documentation.html"
last_crumb = "Prepare your documentation"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Prepare your documentation"
oversized = "false"
page_slug = "extend-prepare_your_documentation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-prepare_your_documentation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-prepare_your_documentation/toc/toc.json"
type = "aem-page"
+++

# Prepare your documentation

Before creating a BYOK RAG image, collect and prepare your organization's documentation in supported file formats.

## Before you begin

- Access to your organization's documentation repository.
- The conversion tool that is appropriate for your file format is installed.
- Write permissions for a local directory to store the prepared documents.

## Procedure

1.  Collect your knowledge sources:
  1.  Identify all documents you want to include in the BYOK knowledge base.
  2.  Create a staging directory for your knowledge sources:
  

```
mkdir -p knowledge-sources/staging
```
  1.  Copy or download all source documents to the staging directory.

2.  If you have content that is not in Markdown (.md) and plain text (.txt) file format, convert them to Markdown or plain text format before uploading them to the BYOK RAG image:
  1.  PDF conversion: use a tool like [docling](https://github.com/docling-project/docling).
  2.  AsciiDoc conversion: Use [custom scripts](https://github.com/openshift/lightspeed-rag-content/blob/main/scripts/asciidoctor-text/convert-it-all.py) or the [Pandoc](https://pandoc.org/) tool.
  3.  HTML conversion: Use the [Pandoc](https://pandoc.org/) tool.
3.  Follow these guidelines when structuring your converted documents for optimal indexing. You can also find examples of each guideline in this [collections repository.](https://github.com/ansible/aap-rag-content/tree/main/byok/ansible-collection-docs)
  1.  **Use clear file names**: Name files descriptively to improve searchability.
  2.  **Organize by topic**: Group related documents in directories by subject area (for example, security-policies, deployment-procedures, compliance).
  3.  **Use consistent formatting**: Apply uniform heading structures and Markdown conventions across all documents.
  4.  **Include metadata**: Add document titles and source URLs when configuring the metadata processor.
  5.  **Remove sensitive information**: Exclude credentials, API keys, or proprietary details before creating the RAG image.
  6.  **Test document quality**: Verify that documents are readable and technically accurate.
  7.  **Optimize storage volume:** Keep the BYOK data between 1 Mi and 999 Mi for best performance. While the system supports larger allocations up to 2 Gi, smaller volumes are recommended.
4.  Copy the converted documents to a final directory for processing them with the `rag-content` tool.

## What to do next

After preparing your knowledge sources, use the `rag-content` tool to create a BYOK RAG image. The BYOK RAG image acts as a searchable knowledge base drawn from your documentation.
