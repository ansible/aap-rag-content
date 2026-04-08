# 10. Simplified event routing
## 10.4. HTTP headers




In the context of Event-Driven Ansible and event streams, HTTP headers play a significant role because they carry the necessary context and security information about the incoming event from a third-party source (for example, GitHub, a monitoring tool, or a proprietary webhook).

They include the following capabilities:

Headers are essential for all HTTP communication, serving several distinct purposes:

-  **Context and metadata:** Describe the data being sent (for example, `    Content-Type: application/json, Content-Length: 1024` ).
-  **Client/Server Capabilities:** Inform the receiving party of the sender’s capabilities or preferences (for example, `    Accept-Language: en-US` ).
-  **Authentication/Authorization:** Carry security credentials (for example, `    Authorization: Bearer &lt;token&gt;` ).
-  **Caching:** Controls how content should be cached by clients and proxies (for example, `    Cache-Control: max-age=3600` ).
-  **Routing and Tracking:** They facilitate network routing and transaction tracking, often via custom headers (for example, `    X-Request-ID` ).


