+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_configure_code_assistant"
title = "Set up Red Hat Ansible Lightspeed cloud service - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_configure_code_assistant/aem-page/develop-assembly_configure_code_assistant.html"
last_crumb = "Set up Red Hat Ansible Lightspeed cloud service"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Set up Red Hat Ansible Lightspeed cloud service"
oversized = "false"
page_slug = "develop-assembly_configure_code_assistant"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_configure_code_assistant"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_configure_code_assistant/toc/toc.json"
type = "aem-page"
+++

# Set up Red Hat Ansible Lightspeed cloud service

As a Red Hat customer portal administrator, you must configure Red Hat Ansible Lightspeed cloud service to connect to your IBM watsonx Code Assistant instance.

Note:

The IBM Cloud service instance of IBM watsonx Code Assistant is available in the following data centers:

- Dallas (`us-south`)
- Frankfurt (`eu-de`)
- Sydney (`au-syd`) (Essentials plan only)


Ansible Lightspeed cloud deployments are configured to connect exclusively to the US (Dallas) IBM data center. Attempts to connect from non-US data centers will result in connection failure. If you want to use a non-Dallas IBM data center, then you must set up Ansible Lightspeed in the hybrid deployment model.

## Log in to the Ansible Lightspeed administrator portal

Use the Ansible Lightspeed administrator portal to connect Red Hat Ansible Lightspeed to IBM watsonx Code Assistant.

### Before you begin

- You have organization administrator privileges to a Red Hat Customer Portal organization with a valid Red Hat Ansible Automation Platform subscription.

### Procedure

1.  Log in to the [Ansible Lightspeed portal](https://c.ai.ansible.redhat.com/) as an organization administrator.
2.  Click Log in> (and then)Log in with Red Hat.
3.  Enter your Red Hat account username and password. The Ansible Lightspeed Service uses Red Hat Single Sign-On (RH-SSO) for authentication. As part of the authentication process, the Ansible Lightspeed Service checks whether your organization has an active Ansible Automation Platform subscription. On successful authentication, the login screen is displayed along with your username and your assigned user role.

4.  From the login screen, click **Admin Portal**.

### Results

You are redirected to the Red Hat Ansible Lightspeed with IBM watsonx Code Assistant administrator portal where you can connect Red Hat Ansible Lightspeed to your IBM watsonx Code Assistant instance.

## Configure Red Hat Ansible Lightspeed cloud service

Use this procedure to configure the Red Hat Ansible Lightspeed cloud service.

### Before you begin

- You have obtained an API key and a model ID from IBM watsonx Code Assistant that you want to use in Red Hat Ansible Lightspeed. For information about how to obtain an API key and model ID from IBM watsonx Code Assistant, see the [IBM watsonx Code Assistant documentation](https://cloud.ibm.com/docs/watsonx-code-assistant).

### Procedure

1.  Log in to the [Ansible Lightspeed portal](https://c.ai.ansible.redhat.com/) as an organization administrator.
2.  From the login screen, click **Admin Portal**.
3.  Specify the API key of your IBM watsonx Code Assistant instance:
  1.  Under **IBM Cloud API Key**, click **Add API key**. A screen to enter the **API Key** is displayed.
  2.  Enter the API Key.
  3.  Optional: Click **Test** to validate the API key.
  4.  Click **Save**.
4.  Specify the model ID of the model that you want to use:
  1.  Click **Model Settings**.
  2.  Under **Model ID**, click **Add Model ID**. A screen to enter the **Model Id** is displayed.
  3.  Enter the **Model ID** that you obtained in the previous procedure as the default model for your organization.
  4.  Optional: Click **Test model ID** to validate the model ID.
  5.  Click **Save**. When the API key and model ID is successfully validated, Red Hat Ansible Lightspeed is connected to your IBM watsonx Code Assistant instance.
