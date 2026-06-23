# Configure custom TLS certificates
## Considerations for certificates provided per service

When providing custom TLS certificates for each individual service, consider the following:

- Each service has its own `_tls_cert` and `_tls_key` variables. You can provide unique certificates for each service, or use the same certificate across multiple services if they share a fully qualified domain name (FQDN). If you do not define a certificate for a service, the installation program generates a self-signed certificate for that service.
- For services deployed across many nodes (for example, when following the enterprise topology), the provided certificate for that service must include the FQDN of all associated nodes in its Subject Alternative Name (SAN) field.
- If an external-facing service (such as automation controller or platform gateway) is deployed behind a load balancer that performs SSL/TLS offloading, the service’s certificate must include the load balancer’s FQDN in its SAN field, in addition to the FQDNs of the individual service nodes.
- Metrics service requires TLS certificates for both the service itself (`automationmetrics_tls_cert`) and its database connection (`automationmetrics_pg_tls_cert`). In enterprise topology, metrics service runs on a dedicated host and requires a unique certificate with the metrics service host FQDN in the SAN field.

