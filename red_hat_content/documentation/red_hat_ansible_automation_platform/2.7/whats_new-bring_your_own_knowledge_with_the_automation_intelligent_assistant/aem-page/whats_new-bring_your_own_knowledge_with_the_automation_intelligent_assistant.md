+++
title = "Bring your own knowledge to the automation intelligent assistant - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-bring_your_own_knowledge_with_the_automation_intelligent_assistant"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-bring_your_own_knowledge_with_the_automation_intelligent_assistant/aem-page/whats_new-bring_your_own_knowledge_with_the_automation_intelligent_assistant.html"
last_crumb = "Bring your own knowledge to the automation intelligent assistant"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Bring your own knowledge to the automation intelligent assistant"
oversized = "false"
page_slug = "whats_new-bring_your_own_knowledge_with_the_automation_intelligent_assistant"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-bring_your_own_knowledge_with_the_automation_intelligent_assistant"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-bring_your_own_knowledge_with_the_automation_intelligent_assistant/toc/toc.json"
type = "aem-page"
+++

# Bring your own knowledge to the automation intelligent assistant

Bring your own, customized documentation and knowledge to the automation intelligent assistant.

Ansible’s automation intelligent assistant uses retrieval-augmented generation (RAG) to provide contextual answers grounded in Red Hat Ansible Automation Platform documentation. With the Bring Your Own Knowledge (BYOK) capability, administrators can extend the intelligent assistant’s knowledge by adding their organization's own internal Ansible documentation, such as policies, operational procedures, and best practices, into the RAG pipeline. When users ask the intelligent assistant a question, responses are informed by both the organization's custom content and Red Hat's Ansible Automation Platform documentation, with organizational content taking priority when relevant.

BYOK is designed for both OpenShift Operator and containerized installer deployments of the Ansible Automation Platform. Administrators build a custom knowledge image externally using provided tooling, import it into their Ansible environment, and configure the intelligent assistant to use it. The image can be updated or replaced over time as organizational documentation evolves.

For more information, see the section titled Extend the automation intelligent assistant with custom knowledge.
