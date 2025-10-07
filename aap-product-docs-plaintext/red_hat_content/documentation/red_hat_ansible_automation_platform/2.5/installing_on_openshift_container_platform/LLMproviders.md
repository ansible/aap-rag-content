# 5. Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform
## 5.3. Large Language Model (LLM) provider requirements




You must have configured an LLM provider that you will use before deploying the Ansible Lightspeed intelligent assistant.

An LLM is a type of machine learning model that can interpret and generate human-like language. When an LLM is used with the Ansible Lightspeed intelligent assistant, the LLM can interpret questions accurately and provide helpful answers in a conversational manner.

As part of the Technology Preview release, Ansible Lightspeed intelligent assistant can rely on the following Software as a Service (SaaS) LLM providers:

**Red Hat LLM providers**

- Red Hat Enterprise Linux AI

Red Hat Enterprise Linux AI is OpenAI API-compatible and is configured in a similar manner to the OpenAI provider. You can configure Red Hat Enterprise Linux AI as the LLM provider. For more information, see the [Red Hat Enterprise Linux AI](https://www.redhat.com/en/products/ai/enterprise-linux-ai) product page.


- Red Hat OpenShift AI

Red Hat OpenShift AI is OpenAI API-compatible and is configured in a similar manner to the OpenAI provider. You can configure Red Hat OpenShift AI as the LLM provider. For more information, see the [Red Hat OpenShift AI](https://www.redhat.com/en/products/ai/openshift-ai) product page.




Note
For configurations with Red Hat Enterprise Linux AI or Red Hat OpenShift AI, you must host your own LLM provider instead of using a SaaS LLM provider.



**Third-party LLM providers**

- IBM watsonx.ai

To use IBM watsonx with the Ansible Lightspeed intelligent assistant, you need an account with [IBM watsonx.ai](https://www.ibm.com/products/watsonx-ai) .


- OpenAI

To use OpenAI with the Ansible Lightspeed intelligent assistant, you need access the [OpenAI API platform](https://openai.com/api/) .


- Microsoft Azure OpenAI

To use Microsoft Azure with the Ansible Lightspeed intelligent assistant, you need access to [Microsoft Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) .

Note
Many self-hosted or self-managed model servers claim API compatibility with OpenAI. It is possible to configure the Ansible Lightspeed intelligent assistant OpenAI provider to point to an API-compatible model server. If the model server is truly API-compatible, especially with respect to authentication, then it might work. These configurations have not been tested by Red Hat, and issues related to their use are outside the scope of Technology Preview support.






