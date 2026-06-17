+++
title = "View and manage Admin dashboard telemetry - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_managing_admin_dashboard_telemetry"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_managing_admin_dashboard_telemetry/aem-page/develop-assembly_managing_admin_dashboard_telemetry.html"
last_crumb = "View and manage Admin dashboard telemetry"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "View and manage Admin dashboard telemetry"
oversized = "false"
page_slug = "develop-assembly_managing_admin_dashboard_telemetry"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_managing_admin_dashboard_telemetry"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_managing_admin_dashboard_telemetry/toc/toc.json"
type = "aem-page"
+++

# View and manage Admin dashboard telemetry

Red Hat Ansible Lightspeed collects the following telemetry data by default:

-  **Operational telemetry data** This is the data that is required to operate and troubleshoot the Ansible Lightspeed service. For more information, refer the Enterprise Agreement. You cannot disable the collection of operational telemetry data.

     This includes the following data:

  * Organization you are logged into (Organization ID, account number)
  * Large language model (or models) that you are connected to

-  **Admin dashboard telemetry data** This is the data that provides insight into how your organization users are using the Ansible Lightspeed service, and the metrics are displayed on the Admin dashboard.

     This includes the following data:

  * Prompts and content suggestions, including accept or reject of the content suggestions

  * User sentiment feedback         You can also disable the Admin dashboard telemetry if you no longer want to collect and monitor the telemetry data.

Note:

Viewing telemetry data on the Admin dashboard is not yet supported on Red Hat Ansible Lightspeed on-premise deployments.

## Prerequisites

To view and manage the Admin dashboard telemetry data, ensure that you have the following:

- You have organization administrator privileges to a Red Hat Customer Portal organization with a valid Red Hat Ansible Automation Platform subscription.
- You have installed the Ansible VS Code extension v2.13.148 that is required to collect Admin dashboard telemetry.


Important:

Red Hat Ansible Lightspeed does not collect users' personal information, such as usernames or passwords. If any personal information is inadvertently received, the data is deleted. For more information about Red Hat Ansible Lightspeed’s privacy practices, see the Telemetry Data Collection Notice for the Admin dashboard.

## What telemetry data is collected?

Following is the list of telemetry data that Red Hat Ansible Lightspeed collects:

- Details of the organization that you are logged into, such as organization ID and account number
- Large language models that you are connected to
- Inline suggestions that were accepted, rejected, or ignored by your organization users
- User sentiment feedback
- Top 10 modules returned in code recommendations

## View the Admin dashboard telemetry

The Admin dashboard displays the analytics telemetry data that you can use to gain insight into how your organization users are using the Ansible Lightspeed service.

### About this task

The Admin dashboard displays the following charts:

-  **Inline suggestions accepted, rejected, or ignored by users** This graph tracks the number of inline suggestions that were accepted, rejected, or ignored by users in your organization. Use this graph to gain insight into how your organization users are using the Ansible Lightspeed service.

-  **User sentiment** This graph measures the users' feedback (feelings, opinions). Use this graph to gain insight into the overall user experience with Red Hat Ansible Lightspeed.

-  **Top 10 modules returned in code recommendations** This graph displays the top 10 modules returned in code recommendations. Use this metric to determine which modules are being suggested the most to your organization’s automation developers.

### Procedure

1.  Log in to the [Ansible Lightspeed with IBM watsonx Code Assistant Hybrid Cloud Console](https://console.redhat.com/preview/ansible/seats-administration) as an organization administrator.
2.  From the navigation panel, select **Ansible Lightspeed > Admin Dashboard**. The Admin dashboard displays a graphical representation of analytics telemetry data for the last 30 days by default.

3.  Use the following filters to refine your telemetry data:

  - To view the telemetry data for a specific time period or for a custom date range, select the date range from the **Quick Date Range** list.
  - To view the telemetry data for a specific IBM watsonx Code Assistant model only, select the model ID from the **Model Name** list. By default, the Admin dashboard displays telemetry data for all models.

## Disable the Admin dashboard telemetry

Red Hat Ansible Lightspeed collects Admin dashboard telemetry by default to gain insight into how your organization uses the service. You can disable this telemetry to stop collecting analytics data.

### Before you begin

- You have organization administrator privileges to a Red Hat Customer Portal organization with a valid Red Hat Ansible Automation Platform subscription.

### About this task

After you disable the Admin dashboard telemetry, the Ansible Lightspeed service no longer collects the analytics telemetry data for your organization. The earlier telemetry data is still available on the Admin dashboard, but no latest data is displayed. If you re-enable the Admin dashboard telemetry, the Ansible Lightspeed service starts collecting data for your organization, and the metrics are displayed on the Admin dashboard after 24 hours.

### Procedure

1.  Log in to the [Ansible Lightspeed portal](https://c.ai.ansible.redhat.com/) as an organization administrator.
2.  From the login screen, click **Admin Portal**.
3.  Under Admin Portal, click **Telemetry**.
4.  To disable the Admin dashboard telemetry, select **Operational telemetry data only**. Note:
      To re-enable the Admin dashboard telemetry, select **Admin dashboard telemetry data**.

5.  Click **Save**.
