# New features and enhancements
## Bring-Your-Own-Knowledge with the Ansible Lightspeed intelligent assistant

Ansible Lightspeed intelligent assistant uses retrieval-augmented generation (RAG) to provide contextual answers grounded in Red Hat Ansible Automation Platform (AAP) documentation. With the upcoming Bring Your Own Knowledge (BYOK) capability, administrators can extend the intelligent assistant’s knowledge by adding their organization’s own documentation, such as internal AAP policies, operational procedures, and best practices, into the RAG pipeline. When users ask the intelligent assistant a question, responses are informed by both the organization’s custom content and Red Hat’s AAP documentation, with organizational content taking priority when relevant.

BYOK is designed for both OpenShift Operator and containerized installer deployments of Ansible Automation Platform. Administrators build a custom knowledge image externally using provided tooling, import it into their AAP environment, and configure the intelligent assistant to use it. The image can be updated or replaced over time as organizational documentation evolves.
