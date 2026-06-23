# Scale up to an enterprise topology
## Key performance indicators to guide scaling plans
### Error codes

Error codes indicate the service must be scaled. Find these codes in the platform gateway’s proxy container (on OpenShift Container Platform) or in the proxy logs (for VM-based and container-based installations). They are often precipitated by the services being overloaded and unable to service requests in a timely manner, and are often preceded by periods of higher latency.

- Upstream Authentication Failures: `502 UAEX` (Upstream Authentication Extension) indicates issues during the authentication phase of a request. This suggests the authentication service is overloaded, timing out, or returning broken responses.
- Upstream Service Unhealthy: A `503 UH` (Upstream Service Unhealthy) response means Envoy has marked one or more service pods as unhealthy. Traffic is not being sent to that unhealthy pod.
- Upstream Connection Failure: `503 UF` (Upstream Connection Failure) response indicates a connection failure. Envoy attempted to contact an upstream pod, but the connection failed. For more information about Envoy Response Flags (the letter codes that follow the `HTTP` response code), see *Access logging* in the Related Links section.

