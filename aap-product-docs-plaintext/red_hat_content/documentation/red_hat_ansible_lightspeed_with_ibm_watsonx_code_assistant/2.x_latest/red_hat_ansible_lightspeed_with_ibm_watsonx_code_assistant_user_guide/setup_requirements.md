# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.1. Configuration requirements
### 3.1.2. Setup requirements




To set up Red Hat Ansible Lightspeed for your organization, you need the following IBM watsonx Code Assistant information:

-  **API key**

A unique API key authenticates all requests made from Red Hat Ansible Lightspeed to IBM watsonx Code Assistant. Each Red Hat organization with a valid Ansible Automation Platform subscription must have a configured API key. When an authenticated RH-SSO user creates a task request in Red Hat Ansible Lightspeed, the API key associated with the user’s Red Hat organization is used to authenticate the request to IBM watsonx Code Assistant.


-  **Model ID**

A unique model ID identifies an IBM watsonx Code Assistant model in your IBM Cloud account. The model ID that you configure in the Ansible Lightspeed administrator portal is used as the default model, and can be accessed by all Ansible Lightspeed users within your organization.




Important
You must configure both the API key and the model ID when you are initially configuring Red Hat Ansible Lightspeed.



