# Set up your development environment to use the MCP server

Use the Ansible AI assistant to query your environment to understand what tools you have installed, and to install `ansible-dev-tools` and set up your development environment.

## Before you begin

The latest version of Python is installed.

## About this task

First, run environment diagnostics. Use the AI assistant to assess your local environment to understand what tools, versions, and collections are currently installed.

## Procedure

1.  Open GitHub Copilot Chat.
2.  Enter a natural language prompt such as:
1.  `Check my Ansible environment and tell me what's installed.`
2.  `What collections are installed?`
The assistant will trigger the `ade_environment_info` tool.

3.  Review the output, which typically includes:
1.  Workspace path and Python version
2.  Virtual Environment status
3.  A list of Installed Collections.
4.  The installation status of Ansible Development Tools (ADT).
