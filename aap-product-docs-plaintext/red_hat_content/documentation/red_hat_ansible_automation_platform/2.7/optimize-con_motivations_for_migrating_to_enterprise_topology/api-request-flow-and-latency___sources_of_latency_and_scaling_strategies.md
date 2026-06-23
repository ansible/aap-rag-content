# Scale up to an enterprise topology
## API request flow and latency sources for performance tuning
### Sources of latency and scaling strategies

The primary sources of latency across all layers are:

- Queueing delays while awaiting an available worker from either the gRPC authentication service or the WSGI server
- The authentication phase, particularly if external authentication systems exhibit slow response times
- The actual processing time and associated database interactions within the Python WSGI application


Scaling strategies include the following:

- Using more performant authentication methods, such as Session or Token
- Horizontally scaling platform gateway and API service pods to increase worker availability and minimize queue times


The following sections describe how to identify which of the Ansible Automation Platform services provide which APIs and provide considerations for scaling them. For more information on the performance of different authentication methods, see [Considerations for scaling the platform gateway proxy and authentication service](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_motivations_for_migrating_to_enterprise_topology#scaling-gateway-proxy-and-authentication "Scale the platform gateway proxy and authentication services if request volume exceeds capacity. Horizontal scaling is preferred. Vertical scaling does not automatically adjust worker pools for gRPC, Envoy, Nginx, and WSGI services.").

