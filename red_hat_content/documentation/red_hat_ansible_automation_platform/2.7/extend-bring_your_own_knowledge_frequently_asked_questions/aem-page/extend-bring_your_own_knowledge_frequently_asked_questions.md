+++
title = "Bring your own knowledge frequently asked questions - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-bring_your_own_knowledge_frequently_asked_questions"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/", "Extend the automation intelligent assistant with custom knowledge"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-bring_your_own_knowledge_frequently_asked_questions/aem-page/extend-bring_your_own_knowledge_frequently_asked_questions.html"
last_crumb = "Bring your own knowledge frequently asked questions"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Bring your own knowledge frequently asked questions"
oversized = "false"
page_slug = "extend-bring_your_own_knowledge_frequently_asked_questions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-bring_your_own_knowledge_frequently_asked_questions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-bring_your_own_knowledge_frequently_asked_questions/toc/toc.json"
type = "aem-page"
+++

# Bring your own knowledge frequently asked questions

Below, find some frequently-asked questions about the BYOK to the automation assistant feature.

**Does BYOK replace the default Ansible documentation in the intelligent assistant?** No. BYOK adds a second knowledge source alongside the default Ansible documentation. Both sources remain active. The Ansible documentation RAG cannot be disabled.

**Do end users need to do anything differently once BYOK is deployed?** No. Users interact with the intelligent assistant the same way they always have. The intelligent assistant automatically incorporates BYOK content into its responses when relevant.

**How does the intelligent assistant decide whether to use BYOK content or Ansible docs?** The intelligent assistant queries both sources for every question. BYOK content receives a higher priority score (controlled by the `score_multiplier` parameter). When BYOK content is relevant, it takes precedence. When it isn't, Ansible documentation fills the gap. For questions that span both, the intelligent assistant blends the sources into a single coherent answer.

**What happens if the BYOK image becomes unavailable?** The intelligent assistant falls back gracefully to the Ansible documentation RAG and continues serving users without interruption. The issue is logged for administrator visibility.

**What file formats can I include in a BYOK image?** Only Markdown (.md) and plain text (.txt) files are supported. Content in other formats (PDF, AsciiDoc, HTML) must be converted before creating the BYOK image.

**Can I have multiple BYOK images active at the same time?** No. Only one BYOK image can be active at a time. To combine multiple documentation sets, merge them into a single image during the build process.

**How do I update the BYOK content when our documentation changes?**See the section titled **Keep your custom documentation current** for instructions on updating the BYOK image.

**Does BYOK work on both OpenShift and containerized deployments?** Yes. BYOK provides full feature parity across both operator-based (OpenShift) and containerized AAP deployments.

**Does BYOK affect response times?** BYOK's dual-source retrieval is designed to maintain response times comparable to single-source operation. Response times remain comparable.

**Does my data leave my infrastructure?** No. The BYOK image is built on your infrastructure using open source tooling, stored in your container registry, and deployed within your Ansible Automation Platform environment. For on-premise deployments, your documentation never leaves your control.
