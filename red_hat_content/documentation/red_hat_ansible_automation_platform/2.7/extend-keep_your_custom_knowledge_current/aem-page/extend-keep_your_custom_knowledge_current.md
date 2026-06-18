+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-keep_your_custom_knowledge_current"
title = "Keep your custom knowledge current - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/", "Extend the automation intelligent assistant with custom knowledge"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-keep_your_custom_knowledge_current/aem-page/extend-keep_your_custom_knowledge_current.html"
last_crumb = "Keep your custom knowledge current"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Keep your custom knowledge current"
oversized = "false"
page_slug = "extend-keep_your_custom_knowledge_current"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-keep_your_custom_knowledge_current"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-keep_your_custom_knowledge_current/toc/toc.json"
type = "aem-page"
+++

# Keep your custom knowledge current

Administrators can update BYOK images to reflect their organization’s latest documentation changes. You can also remove the BYOK image entirely.

Note:

Updating your custom knowledge is optional.

**Identify the BYOK image in use**

When BYOK is enabled, at the beginning of the chatbot container log file, look for the BYOK logs section similar to the following:

```
BYOK_IMAGE is set: quay.io/<repository>/<byok-image-name>:<label>
Checking BYOK vector DB files...
BYOK FAISS DB file exists: /.llama/data/byok/distributions/ansible-chatbot/faiss_store.db
BYOK FAISS DB file size: 4.50 MB
BYOK FAISS DB file date/time: Apr 22 08:51
BYOK provider vector DB ID file exists:
/.llama/data/byok/distributions/ansible-chatbot/provider_vector_db_id.ind
BYOK provider vector DB ID: vs_88af3cff-aeb2-4159-bc12-cef9e8e8fccd
BYOK_PROVIDER_VECTOR_DB_ID already set: vs_88af3cff-aeb2-4159-bc12-cef9e8e8fccd
```
