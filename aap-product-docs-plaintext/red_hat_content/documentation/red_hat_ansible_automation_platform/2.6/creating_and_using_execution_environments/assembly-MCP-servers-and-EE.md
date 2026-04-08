# Chapter 6. Using automation execution environments with Red Hat Model Context Protocol (MCP) servers




A _Model Context Protocol_ (MCP) Server is an external service that acts as a gateway between an _Artificial Intelligence_ (AI) model, specifically a _Large Language Model_ (LLM), and the outside world. An MCP eliminates the need for custom integrations by providing a universal "language" for AI models to access and interact with real-world systems, data, and tools.

The MCP operates using a client-server architecture:

| Component | Role | Description |
| --- | --- | --- |
| MCP Host | The application environment | This is where the user interacts with the AI, such as an AI-powered IDE like VS Code or a chatbot interface. |
| MCP Client | Connection manager | A component within the Host that translates LLM requests into the MCP format. |
| MCP Server | Resource provider | An external service that connects to underlying systems like databases or APIs. |


By using this standardized protocol, any LLM that implements the MCP Client can use any MCP Server.

