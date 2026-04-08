# 6. Configuring Ansible Automation Platform
## 6.3. Understanding the platform gateway OpenAPI specification
### 6.3.1. Downloading the platform gateway OpenAPI specification




You can download the OpenAPI specification by using the `curl` command from the schema endpoint.

**Prerequisites**

Token authentication is the recommended method for programmatic API use.


1. Create a Personal Access Token (PAT): From the navigation panel, selectAccess Management→Users, select your user, go to the **Tokens** tab, and clickCreate token.
1. Copy the generated token value. Use this value as the `    &lt;OAUTH2_TOKEN_VALUE&gt;` in the following commands.


**Procedure**

- Retrieve the OpenAPI specification from the schema endpoint located at `    <a class="link" href="https://$AAP_INSTANCE/api/gateway/v1/docs/schema/">https://$AAP_INSTANCE/api/gateway/v1/docs/schema/</a>` , using one of the following methods:


- Get the YAML specification (Default format): To download the specification as a YAML file, run the following command:


```
curl -o "gateway_openapi_spec.yaml" "https://$AAP_INSTANCE/api/gateway/v1/docs/schema/"
```


- Get the JSON specification (Optional format): To explicitly request the specification in JSON format, append `        ?format=json` to the URL path and run the following command:


```
curl -o "gateway_openapi_spec.json" "https://$AAP_INSTANCE/api/gateway/v1/docs/schema/?format=json"
```

Important
Replace `        $AAP_INSTANCE` with your Ansible Automation Platform hostname in the commands.







