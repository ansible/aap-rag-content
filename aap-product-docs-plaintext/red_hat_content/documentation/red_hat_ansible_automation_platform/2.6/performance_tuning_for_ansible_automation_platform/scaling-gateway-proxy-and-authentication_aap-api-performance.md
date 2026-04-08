# 3. API service performance
## 3.3. Considerations for scaling the platform gateway proxy and authentication service




Scaling the platform gateway proxy and authentication service might be appropriate if the volume of requests to proxy or authenticate exceeds existing platform gateway service capabilities. Horizontal scaling is preferred in this case, as vertical scaling does not automatically adjust all worker pool values for the gRPC, Envoy, Nginx, and WSGI services.

Note
Additional platform gateway service pods or instances can increase the necessary database connections for WSGI web service workers and gRPC authentication service workers.



If you observe a bottleneck in CPU utilization, then scaling the gRPC authentication service can improve throughput. However, if external authentication providers are the source of high latency, then horizontal scaling of the gRPC service has minimal benefits. You can determine the gRPC authentication latency for requests by observing the difference between the upstream service time and the total request latency.

The most performant authentication methods are:

- Token authentication
- Session authentication
- Basic authentication must not be used for high-frequency API automation because CPU-intensive password hashing introduces significant request latency. If Basic authentication is used in combination with LDAP authentication, reaching out to the LDAP service can introduce significant latency, especially if the LDAP service has limited availability. For this reason, we recommend creating OAuth Tokens to perform automation against the API.


Horizontally scaling the platform gateway service pods also increases the number of health checks to each component’s API, because each Envoy tracks this separately. You can observe these in logs with the user agent `Envoy/HC` . Since health checks flow through the same services and queues as user-initiated requests, if overall request times slow due to overload, health checks can also timeout. When this occurs, Envoy stops forwarding requests to these service nodes until they pass their health check again.

