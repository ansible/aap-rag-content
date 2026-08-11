# Understand Red Hat Ansible Lightspeed with IBM watsonx Code Assistant

Learn about the coding assistant feature of Red Hat Ansible Lightspeed, its benefits, key features, supported model providers, and data gathered to train the IBM watsonx Code Assistant models.

Red Hat Ansible Lightspeed provides two AI-powered features that serve different purposes. Use the following table to identify the feature that meets your needs and find the correct setup guide.

*Table 1. Ansible Lightspeed AI features*

|                           | Coding assistant                                                                              | Intelligent assistant                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Purpose                   | Generates Ansible content, such as tasks, playbooks, and roles, from natural language prompts | Provides conversational answers to Ansible automation questions                                                |
| Interface                 | IDE (VS Code with the Ansible extension)                                                      | Ansible Automation Platform web interface                                                                      |
| Supported model providers | IBM watsonx Code Assistant, Google Gemini, Red Hat AI platforms                               | Red Hat Enterprise Linux AI, Red Hat OpenShift AI, Red Hat AI Inference Server, OpenAI, Microsoft Azure OpenAI |
| Deployment types          | Cloud service or on-premise deployment                                                        | Operator-based (OpenShift) or containerized installation                                                       |
| Setup guide               | Set up Red Hat Ansible Lightspeed for your organization (this section)                        | Deploy the intelligent assistant (Extend section)                                                              |

Red Hat Ansible Lightspeed is the cloud service that enables integration of generative AI into Ansible Automation Platform. This document specifically describes the integration of Red Hat Ansible Lightspeed with IBM watsonx Code Assistant.

Red Hat Ansible Lightspeed uses IBM watsonx Code Assistant models trained on subject matter expertise across the Ansible ecosystem, which includes Galaxy, GitHub, and Ansible certified and validated content. For ease of use, Red Hat Ansible Lightspeed is integrated with your existing Ansible developer workflows. For example, you can use your existing Git repositories (both public and private) to train your IBM watsonx Code Assistant models. You can also access Lightspeed content suggestions in VS Code through the Ansible VS code extension.

