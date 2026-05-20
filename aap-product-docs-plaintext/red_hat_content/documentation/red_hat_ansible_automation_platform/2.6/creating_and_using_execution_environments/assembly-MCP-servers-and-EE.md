# Chapter 6. Create and integrate custom MCP Servers in execution environments

A *Model Context Protocol* (MCP) Server is an external service that acts as a gateway between an *Artificial Intelligence* (AI) model, specifically a *Large Language Model* (LLM), and the outside world.

An MCP eliminates the need for custom integrations by providing a universal "language" for AI models to access and interact with real-world systems, data, and tools.

The MCP operates using a client-server architecture:

| Component | Role | Description |
| --- | --- | --- |
| <br>  MCP Host | <br>  The application environment | <br>  This is where the user interacts with the AI, such as an AI-powered IDE like VS Code or a chatbot interface. |
| <br>  MCP Client | <br>  Connection manager | <br>  A component within the Host that translates LLM requests into the MCP format. |
| <br>  MCP Server | <br>  Resource provider | <br>  An external service that connects to underlying systems like databases or APIs. |

By using this standardized protocol, any LLM that implements the MCP Client can use any MCP Server.

