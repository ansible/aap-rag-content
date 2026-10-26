+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-ref_lightspeed_variables"
title = "Red Hat Ansible Lightspeed variables - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_lightspeed_containerized_install/", "Deploy the automation intelligent assistant on containerized Ansible Automation Platform"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-ref_lightspeed_variables/aem-page/extend-ref_lightspeed_variables.html"
last_crumb = "Red Hat Ansible Lightspeed variables"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Red Hat Ansible Lightspeed variables"
oversized = "false"
page_slug = "extend-ref_lightspeed_variables"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-ref_lightspeed_variables"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-ref_lightspeed_variables/toc/toc.json"
type = "aem-page"
+++

# Red Hat Ansible Lightspeed variables

Configure Red Hat Ansible Lightspeed by setting inventory file variables during installation. Use this reference to determine which variables to set for your deployment requirements.

## Red Hat Ansible Lightspeed variables

Inventory file variables for Red Hat Ansible Lightspeed.

| Variable name                           | Description                                                                                                                                                                                              | Required or optional | Default              |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------- |
| `lightspeed_admin_password`             | Red Hat Ansible Lightspeed administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/`, `"`, or `@`.               | Required             |                      |
| `lightspeed_admin_user`                 | Username used to identify and create the Red Hat Ansible Lightspeed admin user.                                                                                                                          | Optional             | `admin`              |
| `lightspeed_chat_rate_throttle`         | Chat rate throttle.                                                                                                                                                                                      | Optional             | `10/minute`          |
| `lightspeed_nginx_client_max_body_size` | Maximum allowed size for data sent to Red Hat Ansible Lightspeed through NGINX.                                                                                                                          | Optional             | `5m`                 |
| `lightspeed_nginx_disable_hsts`         | Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for Red Hat Ansible Lightspeed. Set this variable to `true` to disable HSTS.                                               | Optional             | `false`              |
| `lightspeed_nginx_disable_https`        | Controls whether HTTPS is enabled or disabled for Red Hat Ansible Lightspeed. Set this variable to `true` to disable HTTPS.                                                                              | Optional             | `false`              |
| `lightspeed_nginx_hsts_max_age`         | Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for Red Hat Ansible Lightspeed.                                                                                     | Optional             | `63072000`           |
| `lightspeed_nginx_http_port`            | Port number that Red Hat Ansible Lightspeed listens on for HTTP requests.                                                                                                                                | Optional             | `8084`               |
| `lightspeed_nginx_https_port`           | Port number that Red Hat Ansible Lightspeed listens on for HTTPS requests.                                                                                                                               | Optional             | `8447`               |
| `lightspeed_nginx_https_protocols`      | Protocols that Red Hat Ansible Lightspeed will support when handling HTTPS traffic.                                                                                                                      | Optional             | `[TLSv1.2, TLSv1.3]` |
| `lightspeed_nginx_user_headers`         | Custom Nginx headers. List of additional NGINX headers to add to Red Hat Ansible Lightspeed’s NGINX configuration.                                                                                       | Optional             | []                   |
| `lightspeed_nginx_read_timeout`         | Sets the HTTP timeout for end-user requests. The minimum value is `10` seconds.                                                                                                                          | Optional             | `3600`               |
| `lightspeed_pg_cert_auth`               | Controls whether client certificate authentication is enabled or disabled on the Red Hat Ansible Lightspeed PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | Optional             | `false`              |
| `lightspeed_pg_database`                | Name of the PostgreSQL database used by Red Hat Ansible Lightspeed.                                                                                                                                      | Optional             | `lightspeed`         |
| `lightspeed_pg_host`                    | Hostname of the PostgreSQL database used by Red Hat Ansible Lightspeed.                                                                                                                                  | Required             |                      |
| `lightspeed_pg_password`                | Password for the Red Hat Ansible Lightspeed PostgreSQL database user. Use of special characters for this variable is limited. The `!`, `#`, `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | Optional             |                      |
| `lightspeed_pg_port`                    | Port number for the PostgreSQL database used by Red Hat Ansible Lightspeed.                                                                                                                              | Optional             | `5432`               |
| `lightspeed_pg_sslmode`                 | Controls the SSL mode to use when platform gateway connects to the PostgreSQL database. Valid options include `verify-full`, `verify-ca`, `require`, `prefer`, `allow`, `disable`.                       | Optional             | `prefer`             |
| `lightspeed_pg_tls_cert`                | Path to the PostgreSQL SSL/TLS certificate file for Red Hat Ansible Lightspeed.                                                                                                                          | Optional             |                      |
| `lightspeed_pg_tls_key`                 | Path to the PostgreSQL SSL/TLS key file for Red Hat Ansible Lightspeed.                                                                                                                                  | Optional             |                      |
| `lightspeed_pg_username`                | Username for the Red Hat Ansible Lightspeed PostgreSQL database user.                                                                                                                                    | Optional             | `lightspeed`         |
| `lightspeed_secret_key`                 | Secret key value used by Red Hat Ansible Lightspeed to sign and encrypt data.                                                                                                                            | Optional             |                      |
| `lightspeed_tls_cert`                   | Path to the SSL/TLS certificate file for Red Hat Ansible Lightspeed.                                                                                                                                     | Optional             |                      |
| `lightspeed_tls_key`                    | Path to the SSL/TLS key file for Red Hat Ansible Lightspeed.                                                                                                                                             | Optional             |                      |
| `lightspeed_tls_remote`                 | Denote whether the Red Hat Ansible Lightspeed provided certificate files are local to the installation program (`false`) or on the remote component server (`true`).                                     | Optional             | `false`              |
| `lightspeed_use_archive_compression`    | Controls whether archive compression is enabled or disabled for Red Hat Ansible Lightspeed. You can control this functionality globally by using `use_archive_compression`.                              | Optional             | `true`               |
| `lightspeed_use_db_compression`         | Controls whether database compression is enabled or disabled for Red Hat Ansible Lightspeed. You can control this functionality globally by using `use_db_compression`.                                  | Optional             | `false`              |

## Coding assistant variables

Inventory file variables for the coding assistant.

| Variable name                               | Description                                                                                                                                                                                              | Required or optional | Default |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------- |
| `lightspeed_wca_model_type`                 | IBM watsonx Code Assistant model deployment mode, cloud (`wca`) or on-premise (`wca-onprem`).                                                                                                            | Optional             | `wca`   |
| `lightspeed_wca_model_url`                  | URL of the IBM watsonx Code Assistant model. For cloud deployment, the URL could be `https://api.dataplatform.test.cloud.ibm.com`.                                                                       | Optional             |         |
| `lightspeed_wca_model_api_key`              | API key of the IBM watsonx Code Assistant model that was generated during the model installation.                                                                                                        | Required             |         |
| `lightspeed_wca_model_id`                   | ID of the IBM watsonx Code Assistant model.                                                                                                                                                              | Optional             |         |
| `lightspeed_wca_model_verify_ssl`           | Denotes whether or not to verify IBM watsonx Code Assistant’s web certificates when making calls from Red Hat Ansible Lightspeed to itself during installation. Set to `false` to disable web certificate verification. | Optional             | `true`  |
| `lightspeed_wca_model_enable_anonymization` | Controls whether the anonymization of Personally Identifiable Information (PII) is enabled. PII information includes passwords, IP addresses, email addresses, and other sensitive data.<br>When PII anonymization is enabled, users' personal information is modified to some generic values to protect their data and reduce the risk of data leaks.<br>You can turn off the anonymization by specifying the value as `false` if you want to retain all original information as entered by users and improve the quality of the answers.<br>If you set the value to `false` and the Ansible administrator is using Red Hat Ansible Lightspeed in hybrid mode (where the model is in IBM watsonx Code Assistant in IBM Cloud) then their users' PII is sent to IBM Cloud. | Optional             | `true`  |
| `lightspeed_wca_model_username`             | For on-premise deployment only. The username you use to connect to an IBM Cloud Pak for Data deployment.                                                                                                 | Optional             |         |
| `lightspeed_wca_health_check`               | Enables or disables IBM watsonx Code Assistant health check.                                                                                                                                             | Optional             | `true`  |
| `lightspeed_wca_idp_url`                    | For cloud deployment only. The IBM watsonx Code Assistant Identity Provider (IdP) URL.                                                                                                                   | Optional             |         |
| `lightspeed_wca_idp_login`                  | For cloud deployment only. The IBM watsonx Code Assistant Identity Provider (IdP) username.                                                                                                              | Optional             |         |
| `lightspeed_wca_idp_password`               | For cloud deployment only. The IBM watsonx Code Assistant Identity Provider (IdP) password.                                                                                                              | Optional             |         |

## Automation intelligent assistant variables

Inventory file variables for the intelligent assistant.

| Variable name                             | Description                                                                                                                                                                                              | Required or optional | Default |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------- |
| `lightspeed_chatbot_model_url`            | The inference API base URL on your LLM setup. For example, `https://your_inference_api/v1`.If you are using Microsoft Azure OpenAI, then set the base URL to `https://your_inference_api/openai/v1`.     | Optional             |         |
| `lightspeed_chatbot_model_verify_ssl`     | Controls whether SSL/TLS certificate verification is enabled or disabled when making HTTPS requests.                                                                                                     | Optional             | `true`  |
| `lightspeed_chatbot_default_provider`     | The provider type of your LLM setup by using one of the following values:<br>Red Hat Enterprise Linux AI: `rhelai`Red Hat OpenShift AI: `rhoai`OpenAI: `openai`Microsoft Azure OpenAI: `azure`           | Optional             | `rhoai` |
| `lightspeed_chatbot_model_extra_settings` | Use this parameter to pass a JSON dictionary of extra parameters to pass directly to the model provider, for settings not covered by other standard fields.<br>If you want to use Microsoft Azure OpenAI as the LLM provider, specify the value as `'{"api_type": ""}'`. | Optional             | `{}`    |
| `lightspeed_chatbot_agent_extra_settings` | Use this parameter to customize agent behavior, such as controlling the temperature of the LLM. For example, <br>`'{"chatbot_temperature_override": 1}'`.                                                | Optional             | `{}`    |
| `lightspeed_chatbot_chatbot_max_tokens`   | Maximum number of tokens to generate a chat response.                                                                                                                                                    | Optional             | `4096`  |
| `lightspeed_chatbot_http_port`            | Port number that Ansible Lightspeed intelligent assistant listens on for HTTP requests.                                                                                                                  | Optional             | `8085`  |
| `lightspeed_chatbot_model_id`             | The ID of the LLM model that is configured on your LLM setup.                                                                                                                                            | Optional             |         |
| `lightspeed_chatbot_model_api_key`        | The API token or the API key of your LLM setup. This token is sent along with the authorization header when an inference API is called.                                                                  | Optional             |         |

## Automation intelligent assistant integration with MCP server variables

Inventory file variables for automation intelligent assistant integration with the Model Context Protocol (MCP) server for Red Hat Ansible Automation Platform.

| Variable name                       | Description                                                                    | Required or optional | Default |
| ----------------------------------- | ------------------------------------------------------------------------------ | -------------------- | ------- |
| `lightspeed_mcp_controller_enabled` | Controls whether the Ansible Lightspeed MCP controller is enabled or disabled. | Optional             | `false` |
| `lightspeed_mcp_controller_port`    | Ansible Lightspeed MCP controller port.                                        | Optional             | `8004`  |
| `lightspeed_mcp_lightspeed_enabled` | Ansible Lightspeed MCP lightspeed enabled.                                     | Optional             | `false` |
| `lightspeed_mcp_lightspeed_port`    | Ansible Lightspeed MCP lightspeed port.                                        | Optional             | `8005`  |

## Bring your own Knowledge for automation intelligent assistant variables

Inventory file variables for the automation intelligent assistant with BYOK.

| Variable name                              | Description                                                                                                                  | Default value |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `lightspeed_chatbot_byok_image`            | The full registry path to your RAG image. For example,`lightspeed_chatbot_byok_image: quay.io/my-custom-image/my-rag`        | n/a           |
| `lightspeed_chatbot_byok_score_multiplier` | The score multiplier for BYOK content priority. It adjusts how heavily the AI weighs your custom data versus base knowledge. | `1.2`         |
