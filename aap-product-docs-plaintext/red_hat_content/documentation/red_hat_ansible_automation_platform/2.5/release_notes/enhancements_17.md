# 10. Patch releases
## 10.10. Ansible Automation Platform patch release February 25, 2025
### 10.10.1. Enhancements




#### 10.10.1.1. Platform gateway




- Previously `    gateway_proxy_url` was used for the proxy health check, but is no longer used in favor of the `    ENVOY_HOSTNAME` setting.(AAP-39907)


#### 10.10.1.2. Event-Driven Ansible




- In the credential type schema the format field can be set to binary_base64 to specify a file should be loaded as a binary file.(AAP-36581)


- Sample Credential Type Schema
- Inputs Configuration
- fields:


- id: keytab
- type: string
- label: Kerberos Keytab file
- format: binary_base64 secret: true
- help_text: Please select a Kerberos Keytab file
- multiline: true




