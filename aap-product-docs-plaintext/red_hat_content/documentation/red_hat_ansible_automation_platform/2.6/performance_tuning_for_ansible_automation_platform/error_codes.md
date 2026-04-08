# 3. API service performance
## 3.2. Key performance indicators for scaling the API services
### 3.2.3. Error codes




Error codes in the platform gateway’s proxy container (on OpenShift Container Platform) or in the proxy logs (for VM-based and container-based installations) indicate the service must be scaled. They are often precipitated by the services being overloaded and unable to service requests in a timely manner, and are often preceded by periods of higher latency.

- Upstream Authentication Failures: `    502 UAEX` (Upstream Authentication Extension) responses in Envoy logs indicate issues during the authentication phase of a request. This suggests the authentication service is overloaded, timing out, or returning broken responses.
- Upstream Service Unhealthy: `    503 UH` (Upstream Service Unhealthy) responses for a specific service mean that Envoy has marked one or more of that service’s pods as unhealthy and is not sending traffic to it. This occurs when an upstream pod fails its health checks. Because health checks share the same request queue as client traffic, an overloaded pod that cannot respond to the health check in time will be temporarily removed from the load balancing pool.
- Upstream Connection Failure: `    503 UF` (Upstream Connection Failure) for a specific service’s requests indicates Envoy attempted to contact an upstream pod, but the connection failed. This can occur if the upstream service is overwhelmed and cannot accept new connections. For more information about Envoy Response Flags (the letter codes that follow the `    HTTP` response code), see [Access logging](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/usage) .


