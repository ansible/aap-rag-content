# 9. Patch releases
## 9.6. Ansible Automation Platform patch release December 10, 2025
### 9.6.8. Event-Driven Ansible

#### 9.6.8.1. Enhancements

- Added concise descriptions to API endpoints for Ansible Automation Platform MCP MVP endpoints (`x-ai-description`).(AAP-58431)

#### 9.6.8.2. Bug Fixes

- Fixed an issue where the OpenAPI specification for Event-Driven Ansible was not offering comprehensive documentation and detailed request/response schemas. Previously, developers integrating with Event-Driven Ansible via the MCP server had to manually explore APIs and format API calls without proper guidance, which impeded seamless integration. With this release, the OpenAPI specification for the Event-Driven Ansible REST API is now complete and well-documented. This enhancement enables seamless integration with the MCP server using Event-Driven Ansible.(AAP-53642)

