# Set up Red Hat Ansible Lightspeed for your organization

As a Red Hat customer portal administrator, you must configure Red Hat Ansible Lightspeed to connect to your IBM watsonx Code Assistant instance. This chapter provides information about configuring both the Red Hat Ansible Lightspeed cloud service and on-premise deployment.

## Configuration requirements

Ensure that you meet the licensing and setup requirements specified below before you begin setting up Red Hat Ansible Lightspeed.

### Licensing requirements

-  **Red Hat Ansible Lightspeed cloud service** To use the Red Hat Ansible Lightspeed cloud service, you must meet **one** of the following requirements:

* Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
* Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account. Note:
A Red Hat Ansible Lightspeed trial account does not require an IBM watsonx Code Assistant subscription.

-  **Red Hat Ansible Lightspeed on-premise deployment** To use an on-premise deployment of Red Hat Ansible Lightspeed, your organization must have the following subscriptions:

* A trial or paid subscription to the Red Hat Ansible Automation Platform
* An installation of IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data

### Setup requirements

To set up Red Hat Ansible Lightspeed for your organization, you need the following IBM watsonx Code Assistant information:

-  **API key** A unique API key authenticates all requests made from Red Hat Ansible Lightspeed to IBM watsonx Code Assistant. Each Red Hat organization with a valid Ansible Automation Platform subscription must have a configured API key. An authenticated RH-SSO user creating a task in Red Hat Ansible Lightspeed is authenticated to IBM watsonx Code Assistant through the user’s Red Hat organization API key.

-  **Model ID** A unique model ID identifies an IBM watsonx Code Assistant model in your IBM Cloud account. The model ID that you configure in the Ansible Lightspeed administrator portal is used as the default model, and can be accessed by all Ansible Lightspeed users within your organization.

Important:

You must configure both the API key and the model ID when you are initially configuring Red Hat Ansible Lightspeed.
