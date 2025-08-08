# 10. Patch releases
## 10.4. Ansible Automation Platform patch release May 28, 2025
### 10.4.3. Enhancements




#### 10.4.3.1. Ansible Automation Platform




- Reduced the cognitive complexity level of `    validate_password()` method and reorganized the `    validate_authenticate_uid()` method to increase code readability.(AAP-45346)
- For clarity and to prevent misconfiguration, the SAML authenticator now requires both a permanent user ID and a username.(AAP-45333)
- Updated field names and help text in the System Settings UI to indicate client ID and client secret for service accounts, as well as client ID and client secret for analytics.(AAP-43119)
- Validation/enforcement of expected service types removed because service types are now dynamic.(AAP-40130)
- Enables configuration of control plane authentication for custom services. You should not modify it for pre-defined services.(AAP-40131)
- Custom service type support added. Arbitrary service types and services can be created rather than a fixed list.(AAP-39812)


#### 10.4.3.2. Red Hat Ansible Lightspeed




- It is now possible to disable SSL verification for Red Hat Ansible Lightspeed <→ Model Server communication.(AAP-45337)


#### 10.4.3.3. Automation controller




- Updated Azure Key Vault plugin to use managed identity when creating credentials.(AAP-43461)


