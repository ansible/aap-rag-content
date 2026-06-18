# Bring your own knowledge to the automation intelligent assistant

Bring your own, customized documentation and knowledge to the automation intelligent assistant.

Ansible’s automation intelligent assistant uses retrieval-augmented generation (RAG) to provide contextual answers grounded in Red Hat Ansible Automation Platform documentation. With the Bring Your Own Knowledge (BYOK) capability, administrators can extend the intelligent assistant’s knowledge by adding their organization's own internal Ansible documentation, such as policies, operational procedures, and best practices, into the RAG pipeline. When users ask the intelligent assistant a question, responses are informed by both the organization's custom content and Red Hat's Ansible Automation Platform documentation, with organizational content taking priority when relevant.

BYOK is designed for both OpenShift Operator and containerized installer deployments of the Ansible Automation Platform. Administrators build a custom knowledge image externally using provided tooling, import it into their Ansible environment, and configure the intelligent assistant to use it. The image can be updated or replaced over time as organizational documentation evolves.

For more information, see the section titled Extend the automation intelligent assistant with custom knowledge.
