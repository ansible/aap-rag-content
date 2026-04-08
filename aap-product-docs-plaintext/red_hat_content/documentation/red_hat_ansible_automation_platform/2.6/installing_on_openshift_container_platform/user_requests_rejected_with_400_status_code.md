# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.6. Troubleshooting Ansible MCP server errors
### 7.6.2. User requests rejected with 400 status code




**Issue** : The Ansible MCP server may reject user requests from the external AI tool with `400 Bad Request` status code. This error is encountered when the Ansible Automation Platform uses a self-signed certificate.

**Workaround** : Configure the Ansible MCP server to ignore certificate errors using the following steps:

- For container-based installation: Set the value of variable `    mcp_ignore_certificate_errors` to `    true` .
- For operator-based installation:

Add the `    IGNORE_CERTIFICATE_ERRORS` setting to the `    mcp:` section of **AnsibleAutomationPlatform** custom resource in the following format:


```
spec:        mcp:          extra_settings:            - setting: IGNORE_CERTIFICATE_ERRORS              value: true
```




