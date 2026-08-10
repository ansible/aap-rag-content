+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-proc_update_aap_operator_yaml_chatbot"
template = "docs/aem-title.html"
title = "Update the YAML file of the Ansible Automation Platform operator - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_chatbot_operator/", "Deploy the automation intelligent assistant on OpenShift Container Platform"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-proc_update_aap_operator_yaml_chatbot/aem-page/extend-proc_update_aap_operator_yaml_chatbot.html"
last_crumb = "Update the YAML file of the Ansible Automation Platform operator"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Update the YAML file of the Ansible Automation Platform operator"
oversized = "false"
page_slug = "extend-proc_update_aap_operator_yaml_chatbot"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-proc_update_aap_operator_yaml_chatbot"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-proc_update_aap_operator_yaml_chatbot/toc/toc.json"
type = "aem-page"
+++

# Update the YAML file of the Ansible Automation Platform operator

After you create the chatbot authorization secret, you must update the YAML file of the Ansible Automation Platform operator to use the secret.

## Procedure

1.  Log in to Red Hat OpenShift Container Platform as an administrator.
2.  Navigate to Operators> (and then)Installed Operators.
3.  From the list of installed operators, select the **Ansible Automation Platform** operator.
4.  Locate and select the **Ansible Automation Platform** custom resource, and then click the required app.
5.  Select the **YAML** tab.
6.  Scroll the text to find the `spec:` section, and add the following details under the `spec:` section:
  

```
spec:
  lightspeed:
    disabled: false
    chatbot_config_secret_name: <name of your chatbot configuration secret>
```

7.  Click **Save**. The intelligent assistant service takes a few minutes to set up.  Note:
      Upgrading from Ansible Automation Platform 2.5 to 2.6.1 enables HTTPS and enables TLS by default for internal communication between the Ansible Lightspeed API and the intelligent assistant pod. Following the upgrade to Ansible Automation Platform 2.6.1, the intelligent assistant will be unavailable for approximately 60 seconds while its pod restarts.

## Results

1. Verify that the chat interface service is running successfully:
  1. Navigate to Workloads> (and then)Pods.
  2. Filter with the term **api** and ensure that the following APIs are displayed in **Running** status:
    - `myaap-lightspeed-api-<version number>`
    - `myaap-lightspeed-chatbot-api-<version number>`
2. Verify the MCP server configuration if you specified either `aap_gateway_url` or `aap_controller_url` parameter:
  - Open the `lightspeed-chatbot-api` pod and click the **Containers** section.     * If the `ansible-mcp-lightspeed` container is displayed, the Ansible Lightspeed MCP server is running.
    * If the `ansible-mcp-controller` container is displayed, the Ansible Automation Platform Controller Service MCP server is running.
3. Verify that the chat interface is displayed on the Ansible Automation Platform:
  1. Access the Ansible Automation Platform:
    1. Navigate to Operators> (and then)Installed Operators.
    2. From the list of installed operators, click **Ansible Automation Platform**.
    3. Locate and select the **Ansible Automation Platform** custom resource, and then click the app that you created.
    4. From the **Details** tab, record the information available in the following fields:
      - **URL**: This is the URL of your Ansible Automation Platform instance.
      - **Gateway Admin User**: This is the username to log into your Ansible Automation Platform instance.
      - **Gateway Admin password**: This is the password to log into your Ansible Automation Platform instance.
    5. Log in to the Ansible Automation Platform using the URL, username, and password that you recorded earlier.
  2. Access the intelligent assistant:
    1. Click the intelligent assistant icon ![intelligent assistant icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/chatbot-icon.png) that is displayed at the top right corner of the taskbar.

    2. Verify that the chat interface is displayed, as shown in the following image:             ![Intelligent assistant](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/aap-ansible-lightspeed-intelligent-assistant.png).
