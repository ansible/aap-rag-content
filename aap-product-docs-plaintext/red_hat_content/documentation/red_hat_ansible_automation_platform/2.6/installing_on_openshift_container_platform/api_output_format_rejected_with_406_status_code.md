# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.6. Troubleshooting Ansible MCP server errors
### 7.6.1. API output format rejected with 406 Status Code




**Issue** : Ansible Automation Platform rejects an API request (for example, retrieving job stdout) with an HTTP `406` status code if the MCP server’s requested output is not in `JSON` format.

**Workaround** : To obtain the output in a specific format, instruct your AI tool to use `JSON` format first. You can then transform the `JSON` output into your desired format.

