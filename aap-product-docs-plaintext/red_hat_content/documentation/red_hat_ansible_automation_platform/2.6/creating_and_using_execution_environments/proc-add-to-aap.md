# 6. Create and integrate custom MCP Servers in execution environments
## 6.10. Use your MCP-enabled execution environment in Ansible Automation Platform
### 6.10.2. Add your MCP-enabled execution environment to Ansible Automation Platform

To make your custom execution environment available for automation jobs, add it to Ansible Automation Platform by specifying the container image path and any necessary registry credentials.

**Procedure**

1. In the navigation panel, select Automation Content → Execution Environments.
2. Click Add.
3. Enter the image path (for example, `registry.example.com/ee/my-cfn-mcp-ee:latest`).
4. Configure registry credentials if required.
5. Save the execution environment.

