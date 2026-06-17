# 9. Patch releases
## 9.3. Ansible Automation Platform patch release February 25, 2026
### 9.3.5. Red Hat Ansible Lightspeed

#### 9.3.5.1. Bug Fixes

- Fixed an issue where Lightspeed timed out connecting to chatbot in Testing CI containerized installer. Added chatbot and mcp tools ports to `firewalld`.(AAP-65319)
- Fixed an issue where ChatGPT 5.1 produced blank ALIA responses while using a supported model provider. Added custom config variable to be added to the llama-stack agent configuration.(AAP-63538)
- Fixed an issue where navigating away from the chatbot while a request was in progress would interrupt the process, often resulting in errors like duplicated messages. This issue has been resolved this by ensuring that outstanding requests continue processing even when the browser focus changes.(AAP-62685)
- ChatGPT 5.1 produces blank ALIA responses, while using a supported model provider.

