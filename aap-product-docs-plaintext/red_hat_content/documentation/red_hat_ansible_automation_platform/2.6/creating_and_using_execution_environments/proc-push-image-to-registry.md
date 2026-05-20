# 6. Create and integrate custom MCP Servers in execution environments
## 6.10. Use your MCP-enabled execution environment in Ansible Automation Platform
### 6.10.1. Push the image to a registry

Tag and push your execution environment image to a container registry accessible by your Ansible Automation Platform instance:

`podman tag my-cfn-mcp-ee:latest registry.example.com/ee/my-cfn-mcp-ee:latest`

`podman push registry.example.com/ee/my-cfn-mcp-ee:latest`

If you are using the private automation hub included with Ansible Automation Platform, push to its registry.

