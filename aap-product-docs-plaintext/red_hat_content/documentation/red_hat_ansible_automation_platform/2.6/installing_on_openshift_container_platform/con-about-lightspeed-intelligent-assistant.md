# 6. Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform
## 6.1. Overview




You can install and use Ansible Lightspeed intelligent assistant on Ansible Automation Platform 2.6 on OpenShift Container Platform. Ansible Lightspeed intelligent assistant is an intuitive chat interface embedded within the Ansible Automation Platform, using generative artificial intelligence (AI) to answer questions about the Ansible Automation Platform.

The Ansible Lightspeed intelligent assistant interacts with users in their natural language prompts in English, and uses Large Language Models (LLMs) to generate quick, accurate, and personalized responses. These responses empower Ansible users to work more efficiently, thereby improving productivity and the overall quality of their work.

Ansible Lightspeed intelligent assistant requires the following configurations:

- Installation of Ansible Automation Platform 2.6 on Red Hat OpenShift Container Platform
- Deployment of an LLM provider served by either a Red Hat AI platform or a third-party AI platform. To know the LLM providers that you can use, see [LLM providers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#LLMproviders) .


Important
Red Hat does not collect any telemetry data from your interactions with the Ansible Lightspeed intelligent assistant.



Upgrading from Ansible Automation Platform 2.5 to 2.6.1 or 2.6 to 2.6.1 enables HTTPS and TLS by default for internal communication between the Ansible Lightspeed API and the Ansible Lightspeed intelligent assistant pod. Following the upgrade to Ansible Automation Platform 2.6.1, the intelligent assistant will be unavailable for approximately 60 seconds while its pod restarts.

