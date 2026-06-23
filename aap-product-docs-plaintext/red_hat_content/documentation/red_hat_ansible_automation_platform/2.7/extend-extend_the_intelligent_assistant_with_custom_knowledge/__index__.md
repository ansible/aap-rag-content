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

