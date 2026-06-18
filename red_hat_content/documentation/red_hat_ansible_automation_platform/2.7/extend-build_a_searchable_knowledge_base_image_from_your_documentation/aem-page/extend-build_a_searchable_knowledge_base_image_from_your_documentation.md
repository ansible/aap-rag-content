+++
title = "Build a searchable knowledge base image from your documentation - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-build_a_searchable_knowledge_base_image_from_your_documentation"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/", "Extend the automation intelligent assistant with custom knowledge"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-build_a_searchable_knowledge_base_image_from_your_documentation/aem-page/extend-build_a_searchable_knowledge_base_image_from_your_documentation.html"
last_crumb = "Build a searchable knowledge base image from your documentation"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Build a searchable knowledge base image from your documentation"
oversized = "false"
page_slug = "extend-build_a_searchable_knowledge_base_image_from_your_documentation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-build_a_searchable_knowledge_base_image_from_your_documentation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-build_a_searchable_knowledge_base_image_from_your_documentation/toc/toc.json"
type = "aem-page"
+++

# Build a searchable knowledge base image from your documentation

The `rag-content` tool converts your documentation into a vector database that the intelligent assistant uses to retrieve relevant content when responding to queries. Use this procedure to download the tool version best suited to your system's hardware.

## Before you begin

Podman is installed and configured on your host system to manage container images.

## Procedure

 Run the following command to "pull" (download) the appropriate container image.

```
podman pull registry.redhat.io/lightspeed-core/rag-tool-rhel9:v0.5-latest
```

## Create a vector database from your documentation

Generate a vector database after you have prepared your organization's documentation and converted it to a Markdown or plain-text file.

### Before you begin

- You have prepared your data for BYOK and converted the documentation to a Markdown or plain-text file format.
- You have kept the BYOK data between 1 Mi and 999 Mi for best performance. While the system supports larger allocations up to 2 Gi, smaller volumes are recommended.
- You have installed and configured Podman on your host system to manage container images.

### Procedure

1.  Create a directory for your knowledge sources and outputs:
  

```
mkdir -p knowledge-sources/my-org-docs
mkdir -p output/vector_db
cp -r /path/to/your/prepared/files/* knowledge-sources/my-org-docs/
```

2.  Optional: Configure a metadata processor to add URL references (key="url") to indexed chunks. Use one of the following options:
  1.  Include the [YAML frontmatter](https://github.com/lightspeed-core/rag-content?tab=readme-ov-file#yaml-frontmatter-support) in the sources.
  2.  Write a custom data processor, as shown in the following example:
  

```
# custom_processor.py
def add_metadata(chunk, source_file):
     chunk.metadata['url'] = f"https://docs.example.com/{source_file}"  
     chunk.metadata['title'] = source_file.replace('-', ' ').title()
     return chunk
```

3.  Run the `rag-content` tool to generate the vector database:
  

```
podman run --rm \
-u 0 \
-v "$(pwd)/knowledge-sources/my-org-docs:/input:Z" \
-v "$(pwd)/output:/output:Z" \
registry.redhat.io/lightspeed-core/rag-tool-rhel9:v0.5-latest \
   python /rag-content/scripts/generate_embeddings.py \
    -f /input \
    -o /output/vector_db \
    -i my-docs-index \
     --exclude-model \
     --output-image /output/rag-content-output-latest.tar \
     --image-name rag-content-output \
     --image-tag latest
```

### Example

Replace the values in the command above with your own paths and names. Use the table below as a reference.

| Parameter                               | Description          | What to provide                                                                                                                                                            |
| --------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$(pwd)/knowledge-sources/my-org-docs`  | Source data path     | The full path to the folder containing your raw documents (PDFs, TXT, etc.).                                                                                               |
| `$(pwd)/output`                         | Local output path    | <br>The folder on your computer where you want the finished database to be saved.<br>**Note**: The HASH may differ depending on which container image was used previously. |
| `/output/vector_db`                     | Database folder Name | <br>The name of the subdirectory created inside your output folder to store the database.                                                                                  |
| <br>`my-docs-index`                     | Search index name    | A unique, descriptive name for this specific collection of data.                                                                                                           |
| `/output/rag-content-output-latest.tar` | Export filename      | The name of the compressed file (.tar) that contains your portable database.                                                                                               |
| `rag-content-output`                    | Internal image Name  | The name assigned to the container is used if you load this data into another system later.                                                                                |
| `latest`                                | Version tag          | A version label (for example, v1.0 or April-2026) to track your database updates.                                                                                          |


Note:

If you encounter the following error message, you can ignore it, as it does not affect vector database creation:

`AttributeError: 'SqliteKVStoreImpl' object has no attribute 'close'`
