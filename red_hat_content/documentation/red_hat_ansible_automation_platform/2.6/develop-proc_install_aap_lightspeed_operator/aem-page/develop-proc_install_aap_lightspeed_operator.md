+++
title = "Install the Red Hat Ansible Automation Platform operator - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-proc_install_aap_lightspeed_operator"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-proc_install_aap_lightspeed_operator/aem-page/develop-proc_install_aap_lightspeed_operator.html"
last_crumb = "Install the Red Hat Ansible Automation Platform operator"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Install the Red Hat Ansible Automation Platform operator"
oversized = "false"
page_slug = "develop-proc_install_aap_lightspeed_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-proc_install_aap_lightspeed_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-proc_install_aap_lightspeed_operator/toc/toc.json"
type = "aem-page"
+++

# Install the Red Hat Ansible Automation Platform operator

Use this procedure to install the Ansible Automation Platform operator on the Red Hat OpenShift Container Platform.

## Before you begin

- You have installed and configured automation controller.

## Procedure

1.  Log in to the Red Hat OpenShift Container Platform as an administrator.
2.  Create a namespace:
  1.  Go to Administration> (and then)Namespaces.
  2.  Click **Create Namespace**.
  3.  Enter a unique name for the namespace.
  4.  Click **Create**.
3.  Install the operator:
  1.  Go to Operators> (and then)OperatorHub.
  2.  Select the namespace where you want to install the Red Hat Ansible Automation Platform operator.
  3.  Search for the Ansible Automation Platform operator.
  4.  From the search results, select the Ansible Automation Platform (provided by Red Hat) tile.
  5.  Select an **Update Channel**. You can select either **stable-2.x** or **stable-2.x-cluster-scoped** as the channel.
  6.  Select the destination namespace if you selected “stable-2.x” as the update channel.
  7.  Select **Install**. It takes a few minutes for the operator to be installed.
4.  Click **View Operator** to see the details of your newly installed Red Hat Ansible Automation Platform operator.

## Create a model configuration secret

You must create a configuration secret to connect to an IBM watsonx Code Assistant model, which can be either an on-premise deployment or a cloud deployment.

### Before you begin

- You have installed the Ansible Automation Platform operator 2.5.0-0.1753402603 or later on the Red Hat OpenShift Container Platform.

- You have created an OAuth application in the automation controller.

- You have obtained an API key and a model ID from IBM watsonx Code Assistant. For information about obtaining an API key and model ID from IBM watsonx Code Assistant, see the [IBM watsonx Code Assistant documentation](https://cloud.ibm.com/docs/watsonx-code-assistant). For information about installing IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data, see the [watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data documentation](https://www.ibm.com/docs/en/software-hub/5.1.x?topic=services-watsonx-code-assistant-red-hat-ansible-lightspeed).

### Procedure

1.  Go to the Red Hat OpenShift Container Platform.
2.  Select Workloads> (and then)Secrets.
3.  Click Create> (and then)Key/value secret.
4.  From the **Projects** list, select the namespace that you created when you installed the Red Hat Ansible Automation Platform operator.
5.  Click Create> (and then)Key/value secret.
6.  In **Secret name**, enter a unique name for the secret. For example, `model-aiconnect`.
7.  Add the following keys and their associated values individually:
    | Key                               | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
    | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | <br> `username`                   | <br>  *For on-premise deployment only*<br> Enter the username you use to connect to an IBM Cloud Pak for Data deployment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | <br> `model_type`                 | <br>Enter one of the following values per your IBM watsonx Code Assistant model:<br>  For on-premise deployment (IBM Cloud Pak for Data): `wca-onprem`  For cloud deployment (IBM Cloud): `wca`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | <br> `model_url`                  | <br>Enter the URL of the IBM watsonx Code Assistant model. For cloud deployment, the model URL could be `https://api.dataplatform.cloud.ibm.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | <br> `model_api_key`              | <br>Enter the API key of your IBM watsonx Code Assistant model that was generated during the model installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | <br> `model_id`                   | <br>Enter the ID of your IBM watsonx Code Assistant model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | <br> `model_verify_ssl`           | <br>  *Optional, and supported on Ansible Automation Platform 2.5 and later*<br> This key controls whether the SSL certificate of the IBM watsonx Code Assistant model is verified.<br> Default = `true`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | <br> `model_enable_anonymization` | <br>  *Optional and supported on Ansible Automation Platform 2.5.250730 and later*<br> This key controls whether the anonymization of Personally Identifiable Information (PII) is enabled. PII information includes passwords, IP addresses, email addresses, and other sensitive data. When is enabled, users' personal information is modified to some generic values to protect their data and reduce the risk of data leaks.<br> You can turn off anonymization by setting the value to `false` to retain all original information entered by users and improve the quality of the answers. Disabling anonymization for Ansible Lightspeed hybrid deployments (the model is in IBM watsonx Code Assistant on IBM Cloud) results in users' PII being sent to IBM Cloud.<br> Default = `true` |
  Important:
      Ensure that you do not accidentally add any whitespace characters (extra line, space, and so on) to the value fields. If there are any extra or erroneous characters in the secret, the connection to IBM watsonx Code Assistant fails.

8.  Click **Create**. After you create the model configuration secret, you must update the YAML file of the Ansible Automation Platform operator.

## Update the YAML file of the Ansible Automation Platform operator

After you create the model configuration secret, you must update the YAML file of the Ansible Automation Platform operator to use the secret.

### Procedure

1.  Go to the Red Hat OpenShift Container Platform.
2.  Select Operators> (and then)Installed Operators.
3.  From the list of installed operators, select the **Ansible Automation Platform** operator.
4.  Locate and select the **Ansible Automation Platform** custom resource, and then click the required app.
5.  Select the **YAML** tab.
6.  Scroll the text to find the `Lightspeed` category, and add the following details under the `spec:` section:
  

```
spec:
  lightspeed:
    disabled: false
    model_config_secret_name: <Name of the model configuration secret that you recently created.>
```

7.  Click **Save**. The Ansible Lightspeed service takes a few minutes to set up.
