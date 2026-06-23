# Deploy the MCP server on Ansible Automation Platform
## Deploy the MCP server for Red Hat Ansible Automation Platform on a container-based installation

As an organization administrator, you can deploy and configure the MCP server on a container-based installation of Ansible Automation Platform. Use the following procedure to deploy and configure the MCP server.

### Before you begin

- You have a valid subscription for Ansible Automation Platform 2.6 or later.

### Procedure

Configure MCP server variables in the inventory file:

1.  Create an `[ansiblemcp]` group and add a host for the MCP server.
2.  Add the following installation variables to your inventory file under the `[all:vars]` group:

- `mcp_allow_write_operations`: Use to grant read-only or read-write permissions to the external AI tool.
- `mcp_ignore_certificate_errors`: Use to bypass SSL/TLS certificate validation.

3.  To make your system trust a self-signed custom certificate, add the following required variables to your inventory file:

- `mcp_tls_cert`: Path to TLS certificate

- `mcp_tls_key`: Path to TLS key         For information about using your own TLS certificates and keys, see [Configuring custom TLS certificates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_advanced_configuration_containerized "Configure external databases, custom TLS certificates, execution nodes, HAProxy load balancers, and hub storage for complex containerized Ansible Automation Platform deployments."). For information about required and optional variables, see [MCP server variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-mcp_server_variables "Inventory file variables for the MCP server for Red Hat Ansible Automation Platform.").



```
# This is the list of inventory file variables required to deploy an Ansible MCP server on a container-based installation.

# This section is for the MCP server host
# -------------------------------------------------
[ansiblemcp]
aap.example.com

# This section is for Ansible MCP server permissions
# --------------------------------------------------
[all:vars]
mcp_allow_write_operations=false <To enable read-write access, set the "mcp_allow_write_operations" variable to "true">
mcp_ignore_certificate_errors=false
mcp_tls_cert= <path to tls certificate>
mcp_tls_key= <path to tls key>

# Additional MCP server settings
mcp_extra_settings='[{"setting": "DEFAULT_PAGE_SIZE", "value": "25"}]' <Overrides the default page size for list-type API responses>
```

4.  Optional: add additional MCP server settings such as `DEFAULT_PAGE_SIZE` as in the example above.

### Results

Check the pods after installation is complete. You should see an `ansiblemcp` pod running with the following command:

```none
$ podman ps
```

### What to do next

1. Obtain the location of the MCP server:
- The service is exposed on port 8448 of the host, and HTTPS is enabled.
- The example above deploys the MCP server on `aap.example.com`, so the service base URL will be `https://aap.example.com:8448`.
2. [Create an API token for the MCP server](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server#proc-create-api-token-ansible-mcp-server "Create an API token for your Ansible Automation Platform instance, so you can use it to connect with your preferred AI agent. The AI tool will inherit the user’s permissions for API token-based authentication.").

