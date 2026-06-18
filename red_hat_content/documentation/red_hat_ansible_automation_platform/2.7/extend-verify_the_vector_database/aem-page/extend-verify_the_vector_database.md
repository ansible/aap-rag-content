+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-verify_the_vector_database"
title = "Verify the vector database - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/", "Extend the automation intelligent assistant with custom knowledge"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-verify_the_vector_database/aem-page/extend-verify_the_vector_database.html"
last_crumb = "Verify the vector database"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Verify the vector database"
oversized = "false"
page_slug = "extend-verify_the_vector_database"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-verify_the_vector_database"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-verify_the_vector_database/toc/toc.json"
type = "aem-page"
+++

# Verify the vector database

Verify that you created a vector database of your documentation.

## Procedure

1.  Run the following command:
  

```
ls -lR output
```
  The tool generates an image archive (.tar), which contains the vector database files and metadata. The following shows the structure of the output directory:

```
output
├── rag-content-output-latest.tar
└── vector_db
    ├── faiss_store.db
    └── llama-stack.yaml
```
In the example above:
  - `rag-content-output-latest.tar`is the generated image archive.
  - `faiss_store.db`is the vector database file.
  - `llama-stack.yaml`is the Llama Stack configuration file.

2.  Verify that you get the expected results by querying the generated vector database using the following command:
  

```
podman run --rm \
    -u 0 \
    -v "$(pwd)/output/vector_db:/vector_db:Z" \
registry.redhat.io/lightspeed-core/rag-tool-rhel9:v0.5-latest
\python scripts/query_rag.py \
   -p /vector_db \
   -x index \ -m embeddings_model \
   -k 5 \
   -q "Prerequisites for installation"
```
  In the example above:
  - `-k` tells the AI tool to find the five most relevant matches from your documentation.
  - `-q` is your prompt; change the string according to your requirements.
    The command displays the top five query results, along with the scores. Verify that the results are expected.
