# 9. Patch releases
## 9.4. Ansible Automation Platform patch release January 21, 2026
### 9.4.7. Red Hat Ansible Lightspeed

#### 9.4.7.1. Enhancements

- Enabled chatbot authentication.(AAP-61015)
- Supports Red Hat Ansible Lightspeed chatbot authentication.(AAP-59478)
- Enabled chatbot authentication.(AAP-59476)
- The MCP service / endpoint now displays a banner that explains how to connect to the service, this banner replaces an error message.(AAP-59334)
- Implemented authentication between ansible-lightspeed and ansible-lightspeed-chatbot.(AAP-58796)
- Added chatbot authentication capabilities.(AAP-58794)
- Added Lightspeed chatbot TLS support.(AAP-54412)

#### 9.4.7.2. Bug Fixes

- Fixed an issue where there was an error on the cursor editor. When the error occurred, the MCP server configuration on the Cursor Settings panel and Output view displayed error messages.(AAP-62002)
- Fixed an issue where the Lightspeed Chatbot `PROVIDER_VECTOR_DB_ID` set to literal string caused degraded responses in production.(AAP-61118)
- Fixed bug where VS Code would throw a warning when connecting to Ansible Automation Platform MCP servers due to a period character being in the tool name.(AAP-59293)
- Fixed an issue where Ansible Lightspeed intelligent assistant showed raw tool_call output in answers.(AAP-57513)
- Fixed an issue where long tool names in the Ansible Automation Platform MCP server exceeding the 60-character limit in Cursor’s MCP server resulted in the MCP server tools to being hidden in Cursor, impacting tool usage. With this release, the MCP server now supports tool names exceeding 60 characters, resolving the visibility and usability issues for all tools in the Ansible Automation Platform MCP server.(AAP-61149)
- Fixed an issue where ALIA was experiencing Database or Disk is Full errors.(AAP-53081)
- Fixed an issue where the `CHATBOT_API_KEY` environment variable was not passed to the container when the provider was azure/openai.(AAP-63292)

#### 9.4.7.3. Deprecated

- Removed ansible-risk-insights dependency from ansible-ai-connect-service.(AAP-60336)

