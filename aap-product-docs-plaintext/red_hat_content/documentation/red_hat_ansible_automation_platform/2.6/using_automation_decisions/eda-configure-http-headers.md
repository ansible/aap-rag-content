# 10. Simplified event routing
## 10.4. HTTP headers
### 10.4.1. Configuring HTTP headers securely for event streams




To enhance event stream security, you must explicitly define which HTTP headers are passed. These headers carry the critical context and authentication data required for processing.

**Procedure**

1. To include all HTTP headers, enter an asterisk (*) in the Headers field. This allows all HTTP headers with the exception of a few headers:


-  **Excluded:** Headers that begin with `        X-Envoy` , `        X-Trusted-Proxy` , `        X-Forwarded-For` , and `        X-Real-Id`
-  **Redacted:** Authorization header (for example, `        Authorization: Redacted` )

Important
If the **Headers** field is empty, none of the HTTP headers will be added to the event payload in Production and Test mode.





1. To include a specific set of HTTP headers, enter the names of the desired headers as a comma-delimited string (for example, `    Host,Authorization,X-Request-ID` ).


