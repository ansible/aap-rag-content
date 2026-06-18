+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-get_organization_specific_answers_from_the_intelligent_assistant"
title = "Get organization-specific answers from the intelligent assistant - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/", "Extend the automation intelligent assistant with custom knowledge"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-get_organization_specific_answers_from_the_intelligent_assistant/aem-page/extend-get_organization_specific_answers_from_the_intelligent_assistant.html"
last_crumb = "Get organization-specific answers from the intelligent assistant"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Get organization-specific answers from the intelligent assistant"
oversized = "false"
page_slug = "extend-get_organization_specific_answers_from_the_intelligent_assistant"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-get_organization_specific_answers_from_the_intelligent_assistant"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-get_organization_specific_answers_from_the_intelligent_assistant/toc/toc.json"
type = "aem-page"
+++

# Get organization-specific answers from the intelligent assistant

Once your administrator has deployed a BYOK image in your Ansible Automation Platform environment, you can continue using the intelligent assistant chatbot without changing your workflow.

Use the intelligent assistant as usual for all your Ansible automation needs, including asking questions, requesting guidance, and seeking help. No additional steps are required to access your organization’s data.

While the user interface remains the same, the quality and relevance of the answers are significantly improved. With BYOK active, the intelligent assistant integrates your organization's internal documentation with standard Ansible knowledge. This integration allows responses to automatically incorporate information specific to your team, including:

- Naming conventions and internal terminology.
- Approval workflows and compliance requirements.
- Escalation paths and support structures.
- Proprietary tooling and internal best practices.

By using the RAG image, the intelligent assistant provides context-aware guidance tailored to your specific environment without requiring you to define those constraints in every query manually.

**Key considerations for end users**

To optimize your experience with the enhanced chatbot, keep the following principles in mind:

- **Zero configuration required**: The BYOK integration is configured and managed entirely by your Ansible administrator. You can access the enhanced knowledge base immediately through the intelligent assistant’s chat interface without adjusting any settings or preferences.
- **Seamless interaction**: Continue to use the same natural language queries you always have. The intelligent assistant automatically determines when to incorporate your organization's documentation based on the context of your question.
- **Prioritized knowledge sources**: The intelligent assistant synthesizes information from two sources. It prioritizes internal organizational documentation for proprietary topics while utilizing standard Ansible Automation Platform 2.7 documentation for general automation guidance.
- **Actionable, context-aware results:** By using internal data, the intelligent assistant delivers more precise, specific answers. You receive higher-quality guidance regarding internal workflows, custom policies, and organization-specific tooling.
