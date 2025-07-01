# 7. Troubleshooting
## 7.2. Troubleshooting Red Hat Ansible Lightspeed on-premise deployment errors
### 7.2.1. Cannot log in to the Ansible Lightspeed portal




After you configure a Red Hat Ansible Lightspeed on-premise deployment and try to log in to the Ansible Lightspeed portal, the log-in attempt fails. The following scenarios are possible:

- The log-in attempt fails with the following error message:

`    Error: invalid_request`

`    Mismatching redirect URL`

This error indicates an incorrect configuration of the login redirect URI. The redirect URI parameter must contain the URL of the Red Hat Ansible Lightspeed instance along with `    /complete/aap/` suffix. The following is an example of the login redirect URI:

`    <a class="link" href="https://lightspeed-on-prem-web-service.com/complete/aap/">https://lightspeed-on-prem-web-service.com/complete/aap/</a>`

For more information, see [Updating the Redirect URIs](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#update-redirect-uri_configuring-lightspeed-onpremise) .


- The log-in attempt fails with the following error message:

`    Error: invalid_request`

`    Invalid client_id parameter value`

This error indicates that the authorization connection secret contains an incorrect **client ID** value. To resolve this error, ensure that you have not accidentally added any whitespace characters (extra line, space, and so on) to the `    auth_api_key` parameter in the authorization connection secret. For more information, see [Creating connection secrets](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise) .


- The log-in attempt fails with the following error message:

`    ERROR: Your credentials aren’t allowed`

`    You currently do not have access to.`

This error indicates that the authorization connection secret contains an incorrect **client secret** value. To resolve this error, ensure that you have not accidentally added any whitespace characters (extra line, space, and so on) to the `    auth_api_secret` parameter in the authorization connection secret. For more information, see [Creating connection secrets](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise) .


- The log-in attempt fails with the following error message:

`    Not Found`

`    The requested resource could not be found.`

This error indicates that an incorrect **API URL** value was used to create an authorization connection secret. To resolve this error, ensure that the `    auth_api_url` parameter contains the prefix `    https://` and suffix `    /api/` . For more information, see [Creating connection secrets](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise) .


- The log-in attempt fails with the following error message:

`    Server Not Found`

This error indicates that the **API URL** value in the authorization connection secret does not contain the suffix `    /api/` . To resolve this error, ensure that the `    auth_api_url` parameter contains the suffix `    /api/` . For more information, see [Creating connection secrets](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise) .


- The log-in attempt fails with the following error message:

`    Server Error (500)`

This error message indicates the service has internal errors or that the authorization connection secret contains incorrect **API URL** value. To resolve this error, ensure that the `    auth_api_url` parameter contains the prefix `    https://` and not `    http://` . For more information, see [Creating connection secrets](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise) .


- The log-in attempt fails with the following error message:

`    Bad Request (400)`

To resolve this error, check the `    auth_allowed_hosts` parameter in the authorization secret. For test diagnosis, use the asterisk (*) sign. For more information, see [Creating connection secrets](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise) .




