# 9. Patch releases
## 9.9. Ansible Automation Platform patch release October 28, 2025
### 9.9.4. Red Hat Ansible Lightspeed

#### 9.9.4.1. Features

**Ability to deploy Red Hat Ansible Lightspeed on new containerized installations of Ansible Automation Platform 2.6**

You can deploy and use Red Hat Ansible Lightspeed when you install or upgrade to a containerized installation of Ansible Automation Platform 2.6.

Red Hat Ansible Lightspeed includes two main components that enhance your automation experience with generative artificial intelligence (AI):

**Ansible Lightspeed intelligent assistant**, which is an AI-powered, intuitive chat interface embedded within the Ansible Automation Platform.

The integration of Red Hat Ansible Lightspeed intelligent assistant with the Model Context Protocol (MCP) server is available as a Technology Preview release. This integration enhances the user experience by delivering relevant, dynamically sourced data results to your queries.

Note

Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Ansible Lightspeed coding assistant**, which is a generative AI service that works with IBM watsonx Code Assistant to help developers create and maintain Ansible content more efficiently.

For more information, see [Deploying Red Hat Ansible Lightspeed on containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/deploying-lightspeed-containerized-install) in the containerized install user guide.

#### 9.9.4.2. Enhancements

- Added `postgres_extra_settings` to Ansible Automation Platform operators to apply PostgreSQL configuration file level changes to managed postgres.(AAP-55053)

