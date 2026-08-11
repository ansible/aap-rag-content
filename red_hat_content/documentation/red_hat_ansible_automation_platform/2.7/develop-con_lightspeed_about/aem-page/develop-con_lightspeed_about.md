+++
title = "Understand Red Hat Ansible Lightspeed with IBM watsonx Code Assistant - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_lightspeed_about"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-con_lightspeed_about/aem-page/develop-con_lightspeed_about.html"
last_crumb = "Understand Red Hat Ansible Lightspeed with IBM watsonx Code Assistant"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Understand Red Hat Ansible Lightspeed with IBM watsonx Code Assistant"
oversized = "false"
page_slug = "develop-con_lightspeed_about"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-con_lightspeed_about"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-con_lightspeed_about/toc/toc.json"
type = "aem-page"
+++

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

## Access Red Hat Ansible Lightspeed with IBM watsonx Code Assistant

This section contains information about accessing both Red Hat Ansible Lightspeed cloud service and on-premise deployment.

-  **Red Hat Ansible Lightspeed cloud service** To use the Red Hat Ansible Lightspeed cloud service, you must meet **one** of the following requirements:

  * Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
  * Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account. Note:
            A Red Hat Ansible Lightspeed trial account does not require an IBM watsonx Code Assistant subscription.

-  **Red Hat Ansible Lightspeed on-premise deployment** To use an on-premise deployment of Red Hat Ansible Lightspeed, your organization must have the following subscriptions:

  * A trial or paid subscription to the Red Hat Ansible Automation Platform
  * An installation of IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data

## Benefits of using Red Hat Ansible Lightspeed

Red Hat Ansible Lightspeed with IBM watsonx Code Assistant offers the following benefits:

-  **Reduces the onboarding learning period for Ansible developers** With just a basic understanding of YAML syntax, Ansible developers can use natural language prompts in English language to describe the automation goal. Red Hat Ansible Lightspeed then offers Ansible code recommendations to help achieve the automation goal more efficiently. This combination of content and best practice suggestions reduces the learning curve and offers a smoother onboarding experience for new Ansible users.

     For example, to get a multitask code recommendation, you can enter the prompt `Install postgresql-server & run postgresql-setup command`. The Ansible Lightspeed service reads the text, interacts with IBM watsonx Code Assistant, and generates code recommendations to automate a multitask that installs a PostgreSQL server and sets up a PostgreSQL database. You can then view and accept the code recommendations to create tasks in an Ansible YAML file.

-  **Increases productivity with quality content creation** Red Hat Ansible Lightspeed offers automation code recommendations that adhere to Ansible best practices, and IBM watsonx Code Assistant provides model fine-tuning features to improve the accuracy of suggested content based on your organization’s existing Ansible content. Therefore, the AI-generated code recommendations are more accurate, more reliable, and integrated with your existing automation development workflows.

-  **Extends trust with AI-generated code recommendations** The AI-generated code recommendations enable you to extend trust, with an automation code base that adheres to accepted Ansible best practices and significant data safeguards.

## Prerequisites

Review the following licensing and connectivity requirements for setting up Red Hat Ansible Lightspeed.

To use the Red Hat Ansible Lightspeed cloud service, you must meet **one** of the following requirements:

- Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
- Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account. Note:
      A Red Hat Ansible Lightspeed trial account does not require an IBM watsonx Code Assistant subscription.

To use an on-premise deployment of Red Hat Ansible Lightspeed, your organization must have the following subscriptions:

- A trial or paid subscription to Red Hat Ansible Automation Platform
- An installation of IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data

You must also install the following components:

- VS Code version 1.70.1 or later
- The Ansible extension for VS Code version 2.8 or later

### Connectivity requirements

To generate code recommendations, the Ansible Lightspeed service in Visual Studio (VS) Code editor requires access to the outbound domain https://c.ai.ansible.redhat.com. The outbound connections are encrypted on TCP protocol port 443.

## Data gathered to train the IBM watsonx Code Assistant models

This topic provides information about the data that is collected to train the IBM watsonx Code Assistant models.

### Models

Red Hat Ansible Lightspeed with IBM watsonx Code Assistant uses Ansible-specific IBM watsonx Granite models unique to your organization. These models are provided, managed, and maintained by IBM.

### Data sources

IBM watsonx Code Assistant models are trained on Ansible content from Ansible Galaxy, data from public Git repositories, and Red Hat Ansible subject matter expert examples.

If you publish content to Ansible Galaxy and want to restrict your Ansible Galaxy content from being used to train the models, you can opt out of sharing your Ansible Galaxy data in the Ansible Galaxy namespace configuration.

### Data telemetry

Red Hat Ansible Lightspeed collects the following telemetry data by default:

- Operational telemetry data
- Admin dashboard telemetry data

Note:

No telemetry data is collected in an Red Hat Ansible Lightspeed on-premise deployment.

## Telemetry data collection notice for the Admin dashboard

In connection with your use of this Red Hat offering, Red Hat may collect telemetry data about your use of the software. This data allows Red Hat to monitor the software and to improve Red Hat offerings and support, including identifying, troubleshooting, and responding to issues that impact users.

The telemetry data may also be used to enable you to track your entitlements to Red Hat subscriptions and take advantage of future Red Hat purchasing programs. It may also allow Red Hat to assist you in implementing upgrades to minimize service impact. The data may be shared internally within Red Hat to improve the user experience. If you are evaluating Red Hat software, the data will help Red Hat determine if you need assistance.

### What information does Red Hat collect?

Tools within the software monitor various metrics and this information is transmitted to Red Hat. The following metrics are monitored:

-  **Operational telemetry data** This is the data that is required to operate and troubleshoot the Ansible Lightspeed service. For more information, refer the Enterprise Agreement. You cannot disable the collection of operational telemetry data.

     This includes the following data:

  * Organization you are logged into (Organization ID, account number)
  * Large language model (or models) that you are connected to

-  **Admin dashboard telemetry data** This is the data that provides insight into how your organization users are using the Ansible Lightspeed service, and the metrics are displayed on the Admin dashboard.

     This includes the following data:

  * Prompts and content suggestions, including accept or reject of the content suggestions

  * User sentiment feedback         You can also disable the Admin dashboard telemetry if you no longer want to collect and monitor the telemetry data.

Note:

No telemetry data is collected in an Red Hat Ansible Lightspeed on-premise deployment.

### Personal Data

Red Hat does not intend to collect personal information. If Red Hat discovers that personal information has been inadvertently received, Red Hat will delete such information.

- Retention     Red Hat retains and stores telemetry data only for as long as it’s needed for the purposes described above or as otherwise required or permitted by law.

- Data security     Red Hat employs technical and organizational measures designed to protect the telemetry data. Data stored in the Red Hat cloud is being protected, where possible, through encryption. Data is also segmented, and therefore is not accessible across organizations.

- Data sharing     Red Hat may share telemetry data with its business partners in an aggregated form that does not identify customers. This data helps the partners better understand their markets and their customers' use of Red Hat offerings. The data also helps to ensure the successful integration of products jointly supported by those partners.

- Third Party Service Providers     Red Hat may engage certain service providers to assist in the collection and storage of the telemetry data.

- User control/ enabling and disabling Admin Dashboard telemetry collection     You cannot disable collection of operational telemetry data. Operational telemetry data includes only data that is necessary to operate and troubleshoot the service. However, you can disable the collection of Admin Dashboard telemetry data.
