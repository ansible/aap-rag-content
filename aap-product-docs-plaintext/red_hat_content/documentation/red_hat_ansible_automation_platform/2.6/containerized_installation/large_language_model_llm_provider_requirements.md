# 6. Deploying Red Hat Ansible Lightspeed on containerized Ansible Automation Platform
## 6.1. Overview
### 6.1.6. Large Language Model (LLM) provider requirements




You must have configured an LLM provider that you will use before deploying the Ansible Lightspeed intelligent assistant. An LLM is a type of machine learning model that can interpret and generate human-like language. When an LLM is used with the Ansible Lightspeed intelligent assistant, the LLM can interpret questions accurately and provide helpful answers in a conversational manner.

Ansible Lightspeed intelligent assistant can rely on the following LLM providers:

-  **Red Hat LLM providers:**


-  **Red Hat Enterprise Linux AI**

You can configure Red Hat Enterprise Linux AI as the LLM provider. As the Red Hat Enterprise Linux is in a different environment than the Ansible Lightspeed deployment, the model deployment must allow access using a secure connection. For more information, see [Optional: Allowing access to a model from a secure endpoint](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_ai/1.5#creating_secure_endpoint) .

Ansible Lightspeed intelligent assistant supports vLLM Server. When self-hosting an LLM with Red Hat Enterprise Linux AI, you can use vLLM Server as the inference engine.


-  **Red Hat OpenShift AI**

You must deploy an LLM on the Red Hat OpenShift AI single-model serving platform that uses the Virtual Large Language Model (vLLM) runtime. If the model deployment lives in a different OpenShift environment than the Ansible Lightspeed deployment, include a route to expose the model deployment outside the cluster. For more information, see [About the single-model serving platform](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/2.23#about-the-single-model-serving-platform_serving-large-models) .

Ansible Lightspeed intelligent assistant supports vLLM Server. When self-hosting an LLM with Red Hat OpenShift AI, you can use vLLM Server as the inference engine.

Note
For configurations with Red Hat Enterprise Linux AI or Red Hat OpenShift AI, you must host your own LLM provider instead of using a SaaS LLM provider.




-  **Red Hat AI Inference Server**

You can deploy an LLM by using Red Hat AI Inference Server as your inference runtime. Red Hat AI Inference Server supports vLLM runtimes for efficient model serving and can be configured to work with Ansible Lightspeed intelligent assistant. For more information, see [Red Hat AI Inference Server documentation](http://docs.redhat.com/en/documentation/red_hat_ai_inference_server/3.2/html/getting_started/rhaiis-getting-started-overview_getting-started) .

If the Red Hat AI Inference Server deployment is in a different environment than the Ansible Lightspeed deployment, ensure the model deployment allows access by using a secure connection and configure appropriate network routing.

Ansible Lightspeed intelligent assistant supports vLLM Server when self-hosting an LLM with Red Hat AI Inference Server as the inference engine.



-  **Third-party LLM providers:**


-  **OpenAI**

To use OpenAI with the Ansible Lightspeed intelligent assistant, you need access to the [OpenAI API platform](https://openai.com/api/) .


-  **Microsoft Azure OpenAI**

To use Microsoft Azure with the Ansible Lightspeed intelligent assistant, you need access to [Microsoft Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-foundry/models/openai/) product page.





