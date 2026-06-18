+++
title = "Extend the automation intelligent assistant with custom knowledge - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/", "Extend the automation intelligent assistant with custom knowledge"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/aem-page/extend-extend_the_intelligent_assistant_with_custom_knowledge.html"
last_crumb = "Extend the automation intelligent assistant with custom knowledge"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Extend the automation intelligent assistant with custom knowledge"
oversized = "false"
page_slug = "extend-extend_the_intelligent_assistant_with_custom_knowledge"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/toc/toc.json"
type = "aem-page"
+++

# Extend the automation intelligent assistant with custom knowledge

The Bring Your Own Knowledge (BYOK) capability enables you to extend the automation intelligent assistant with your organization’s internal documentation.

By integrating custom knowledge sources into the assistant's Retrieval-Augmented Generation (RAG) pipeline, the intelligent assistant provides responses that reflect your organization’s specific Ansible policies, procedures, and best practices.

BYOK adds a second knowledge source to the intelligent assistant’s RAG pipeline:

- **Custom knowledge (BYOK)**: Store your organization's documentation in a custom RAG image that you create and deploy to Ansible Automation Platform 2.7. This custom knowledge is the highest priority or **primary** knowledge source.
- **Ansible documentation**: The default Ansible Automation Platform 2.7 documentation, which is the **secondary** knowledge source.
When users query the intelligent assistant, the system retrieves relevant context from both knowledge sources, prioritizing your custom content to provide organization-specific answers. If your BYOK documentation covers the topic, the intelligent assistant leads with your organization's guidance. If it doesn't, the intelligent assistant seamlessly falls back to standard Ansible documentation. The default Ansible documentation RAG database remains active at all times, and you cannot disable it.

Note:

The BYO Knowledge tool is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see the link to the Technology preview features support scope in the **Related Links** section below.

Note:

The BYOK RAG image is created outside your AAP deployment and then imported as an additional component in the intelligent assistant’s RAG pipeline. The default Ansible documentation RAG database remains active and cannot be disabled

## BYOK Benefits

Using BYOK with the intelligent assistant provides the following benefits:

- **Integrate custom knowledge sources**: Add your organization's internal documentation, policies, manuals, FAQs, or any text-based knowledge.
- **Improved accuracy**: Users receive contextual answers tailored to their environment and terminology.
- **Knowledge preservation**: Keep your knowledge sources within your infrastructure, and make internal documentation accessible through natural language queries.
- **Compliance support**: Incorporate compliance protocols and security requirements into the intelligent assistant’s responses.

Before you begin your BYOK implementation workflow, you will need:

- **Platform version**: An instance of Ansible Automation Platform 2.7 or later.
- **A deployment environment**:
  * **OpenShift:** Access to an OpenShift cluster with permissions to install operators.
  * **Containerized:** A supported container runtime.
- **Access credentials**: Administrator permissions to your containerized or operator-based installation of Ansible Automation Platform.
- **Existing integration:** An active intelligent assistant installation that is compatible with the Ansible-documentation-based RAG pipeline.
- **Custom data**: A collection of markdown (.md) or text (.txt) files containing the information you wish to add. Currently, the tool does not support other file formats.

*Table 1. BYOK Implementation Workflow*

| Step | Task                                                             | Description                                                                                                                                                                                                |
| ---- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Prepare your documentation                                       | An **administrator** collects and converts the organization's documents to Markdown or plain-text formats.                                                                                                 |
| 2    | Build a searchable knowledge base image from your documentation  | The **administrator** uses the rag-content tool to generate a vector database from the docs and packages it as a container image.                                                                          |
| 3    | Deploy your custom image                                         | The **administrator** imports the BYOK RAG image into your containerized or operator-based Ansible Automation Platform installation and configures the Ansible Lightspeed intelligent assistant to use it. |
| 4    | Get organization-specific answers from the intelligent assistant | <br>**Ansible Automation Platform users** ask the intelligent assistant questions and receive answers informed by their organization's custom documentation.                                               |
| 5    | Optional: Keep your custom knowledge current                     | <br>The **administrator** updates or replaces the BYOK image as the organization’s documentation evolves, or removes the image entirely if no longer needed.                                               |
