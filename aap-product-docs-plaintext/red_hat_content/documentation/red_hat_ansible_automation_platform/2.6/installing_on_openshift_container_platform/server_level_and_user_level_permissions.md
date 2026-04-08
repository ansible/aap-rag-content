# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.1. Overview
### 7.1.4. Server-level and user-level permissions




The Ansible MCP server employs a dual-layer security model to ensure safe integration between AI tools and your Ansible Automation Platform infrastructure. This approach combines a global administrative safeguard with the granular Role-Based Access Control (RBAC) of the Ansible Automation Platform.

You can grant the following access types to the Ansible MCP server:

-  **Server-level permissions** : Organization administrators assign a global-level permission while deploying the Ansible MCP server. Administrators can choose one of the following access levels:


- Read-only access: The default setting that enforces a strict "look but do not touch" policy. The AI agent can retrieve system data, such as logs and inventory, but the agent cannot launch jobs or modify configurations. This global safeguard overrides all individual user permissions to prevent unintended automation.
- Read-write access: This setting authorizes the AI agent to make changes in your Ansible Automation Platform, such as executing job templates, managing resources, and applying infrastructure changes. However, these actions are subject to the specific RBAC permissions of the user-provided API token.

-  **User-level permissions** : The AI agent’s specific capabilities are inherited from the user account that generated the authentication API token.


- Inherited permissions: The AI tool inherits the user’s permissions and performs only the actions the user is authorized to perform. For example, if the user’s token only has permissions to view the "network" inventory, the AI tool cannot access or modify the "database" inventory even if the user requests it.
- Rejection of unauthorized actions: If the AI tool attempts an action (like launching a job) that the user’s token is not authorized to perform, the Ansible Automation Platform API rejects the request.



Warning
Enabling read-write access for the Ansible MCP server grants the AI agent autonomy to directly make changes in your Ansible Automation Platform environment, for example, executing automation jobs. The AI agent can directly make changes in your Ansible Automation Platform environment only if the user has write permissions. Large Language Models (LLMs) can occasionally misinterpret prompts or hallucinate commands. Therefore, enabling read-write access may introduce a risk of unintended changes to your environment.



