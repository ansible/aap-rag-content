# 6. Create and integrate custom MCP Servers in execution environments
## 6.8. Secure your custom MCP servers

Apply essential security configurations and best practices to safeguard your custom MCP servers, manage credentials securely, and harden your execution environments.

**Manage credentials and secrets**

MCP servers frequently require credentials to interact with cloud providers or external services. Follow these practices:

- **Never embed credentials into the execution environment image**: Credentials embedded during build time persist in the container image layers and can be extracted. Instead, pass credentials at runtime using environment variables or mounted files.
- **Use runtime environment variables**: Pass credentials when launching the execution environment:

podman run --rm \
-e AWS_PROFILE=my-profile \
-e GITHUB_PERSONAL_ACCESS_TOKEN="$GITHUB_TOKEN" \
my-mcp-ee:latest …

- **Mount credential files as read-only**: For providers that use credential files (such as AWS), mount them read-only:

`-v ~/.aws:/home/runner/.aws:ro`

- **In Ansible Automation Platform, use credential types**: When running MCP-enabled execution environments through Ansible Automation Platform, configure credentials through the automation controller credential management system rather than embedding them in playbooks or job templates.

