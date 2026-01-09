# 8. Troubleshooting
## 8.3. Troubleshooting Ansible Visual Studio Code extension errors
### 8.3.4. Cannot connect to Ansible VS code extension due to network issues




If you encounter network issues, use the **Network Proxy Test** extension to test the connection:

1. Install the VS code extension [Network Proxy Test](https://marketplace.visualstudio.com/items?itemName=chrmarti.network-proxy-test) .
1. Use the **Network Proxy Test: Test Connection** action to target the server and the endpoint using the parameter `    /check/status end-point` .

For example:

`    https://c.ai.ansible.redhat.com/check/status/` to test the connection to Red Hat Ansible Lightspeed cloud service.




