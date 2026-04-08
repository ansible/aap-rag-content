# 2. Configuring the Ansible VS Code extension MCP server
## 2.3. Enable the MCP server through the VS Code settings menu




Take the following steps to enable the MCP server through the VS Code settings menu.

**Procedure**

1. In VS Code, select the **Extensions** icon in the left menu.
1. Find the Ansible VS Code extension and click the settings wheel.
1. Select **Settings** from the menu that appears.
1. In the Settings window, select **Extensions** > **Ansible** > **MCP Server** .
1. Click the checkbox next to **Enable the Ansible development tools MCP server for AI integration** .

A message confirms that the MCP server is enabled.


1. Find and select **Ansible: Enable Ansible development tools MCP Server** .

A message confirms that you have successfully enabled the MCP server and that it is now available for AI assistants that support MCP.


1. Find and select **MCP: List servers** in the command palette at the top of the window. In the list that appears you should see an entry for **Ansible development tools MCP Server** .
1. Select **Ansible development tools MCP Server** to start the server.


**Verification**

Verify that the server has started by looking for `Discovered 10 tools` in your VS Code output window.


