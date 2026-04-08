# 3. API service performance
## 3.1. API request flow and latency sources
### 3.1.1. Sources of latency and scaling strategies




The primary sources of latency across all layers are:

- Queueing delays while awaiting an available worker from either the gRPC authentication service or the WSGI server
- The authentication phase, particularly if external authentication systems exhibit slow response times
- The actual processing time and associated database interactions within the Python WSGI application


Scaling strategies include the following:

- Using more performant authentication methods, such as Session or Token
- Horizontally scaling platform gateway and API service pods to increase worker availability and minimize queue times


The following sections describe how to identify which of the Ansible Automation Platform services provide which APIs and provide considerations for scaling them. For more information on the performance of different authentication methods, see [Considerations for scaling the platform gateway proxy and authentication service](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/performance_tuning_for_ansible_automation_platform/api_service_performance#scaling-gateway-proxy-and-authentication_aap-api-performance) .

