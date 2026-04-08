# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.2. Deploying an Ansible MCP server on a container-based installation




As an organization administrator, you can deploy and configure an Ansible MCP server on a container-based installation of Ansible Automation Platform 2.6. Use the following procedure to deploy and configure the Ansible MCP server.

**Prerequisites**

- You have a valid Ansible Automation Platform 2.6 subscription.


**Procedure**

1. Configure the Ansible MCP server variables in the inventory file:


1. Create an `        [ansiblemcp]` group and add a host for the Ansible MCP server.
1. Add the following installation variables to your inventory file under the `        [all:vars]` group:


-  `            mcp_allow_write_operations` : Use to grant read-only or read-write permissions to the external AI tool.
-  `            mcp_ignore_certificate_errors` : Use to bypass SSL/TLS certificate validation.

1. To make your system trust a self-signed custom certificate, add the following required variables to your inventory file:


-  `            mcp_tls_cert` : Path to TLS certificate
-  `            mcp_tls_key` : Path to TLS key

For information about using your own TLS certificates and keys, see [Configuring custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/advanced-configuration-containerized#using-custom-tls-certificates) . For information about required and optional variables, see [Appendix: Ansible MCP server variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#ansible-mcp-server-variables) .


```
# This is the list of inventory file variables required to deploy an Ansible MCP server on a container-based installation.                        # This section is for the Ansible MCP server host            # -------------------------------------------------            [ansiblemcp]            aap.example.com                        # This section is for Ansible MCP server permissions            # --------------------------------------------------            [all:vars]            mcp_allow_write_operations=false &lt;To enable read-write access, set the "mcp_allow_write_operations" variable to "true"&gt;            mcp_ignore_certificate_errors=false            mcp_tls_cert= &lt;path to tls certificate&gt;            mcp_tls_key= &lt;path to tls key&gt;
```




1.  [Run the install playbook to install containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#installing-containerized-aap) .


**Verification**

Check the pods after installation is complete. You should see an `ansiblemcp` pod running with the following command:


```
$ podman ps
```

**Next steps**

1. Obtain the location of the Ansible MCP server:


- The service is exposed on port 8448 of the host, and HTTPS is enabled.
- The example above deploys the MCP server on `        aap.example.com` , so the service base URL will be `        https://aap.example.com:8448` .

1.  [Create an API token for the Ansible MCP server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#proc-create-api-token-ansible-mcp-server_deploying-ansible-mcp-server) .


**Additional resources**

-  [Appendix: Ansible MCP server variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#ansible-mcp-server-variables)


