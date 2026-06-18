# Scale up to an enterprise topology

Growth topologies are suited to proof-of-concept deployments, small-scale environments, or preliminary evaluations. Using a growth topology simplifies initial setup for your Ansible Automation Platform deployment, but they have inherent limitations.

## Inherent limitations of growth topologies

Growth topologies include single points of failure, such as a single platform gateway , and other critical components, such as the control plane, execution plane, and web services. These components often share resources on the same node, resulting in resource contention under increasing load. As workloads grow, specific services, such as job processing or API responsiveness, can become bottlenecks due to colocation or single node capacity limits. Consequently, growth topologies generally do not offer robust, high-availability capabilities. For VM-based installation and containerized deployments of Ansible Automation Platform, you can marginally increase possible workloads by vertically scaling the virtual machines or physical hosts within the growth deployment. However, vertical scaling capabilities within a growth topology are limited.

## Use cases for migrating to an enterprise topology

To scale beyond the limitations within growth topologies, you can migrate to an enterprise topology. Migrating to an enterprise topology might be relevant in the following use cases:

- Vertically scaling a growth topology becomes impractical due to cost or availability.
- The growth topology cannot satisfy high availability and disaster recovery requirements.
- You must scale Ansible Automation Platform services independently, such as API handling, job execution, and database capacity.
- Workload demands consistently overwhelm the capacity of vertically scaled growth topologies.
- You require more complex network architectures, such as segmented networks.

## Recommended enterprise topology

To maximize flexibility, resilience, and scalability, migrate to the OpenShift Container Platform-based enterprise topology. This migration includes integration with an externally managed, enterprise-grade PostgreSQL database. operator-based installation offers greater flexibility to scale individual services and adapt the deployment to specific requirements. They also enhance the ability to scale the deployment up and down with reduced downtime and customize workload placement with labels, taints, tolerations, and topology constraints. operator-based installation also benefits from resilience features, such as automatic service recreation if underlying worker nodes experience failure or resource exhaustion.

## Motivations for customizing enterprise topologies

Enterprise topologies provide a pattern for scalability and resilience. Organizations typically evolve the tested deployment models into custom deployments, tailoring service configurations and scaling to their specific workflows and performance needs within Red Hat Ansible Automation Platform.

An organization’s unique use of Ansible Automation Platform determines which components require scaling, moving from a generic enterprise topology to a workload-tuned deployment.

Workloads such as infrequent automation hub use or API-heavy integrations necessitate different scaling priorities. This includes components such as the API service or execution plane.

Motivations for customizing the documented enterprise deployment models include the following:

- Achieving high availability
- Enabling independent scaling of components, such as automation controller API compared to execution capacity
- Supporting workload growth or specific SLAs


This requires custom resource allocation and performance tuning based on identified needs, rather than adherence to a general pattern.

Before customizing and scaling, you must identify specific bottlenecks within your Ansible Automation Platform environment, such as:

- API response
- Job processing
- Database performance
- Event-Driven Ansible event handling.


Use platform monitoring tools and analytics to identify bottlenecks. After bottlenecks are identified, you can approach scaling each component vertically or horizontally.

## API request flow and latency sources for performance tuning

The Ansible Automation Platform API uses distributed services. Performance depends on the request path, with latency possible at each layer. The following table details each layer in the API request flow:

*Table 1. API Service architecture and performance considerations*

| Layer                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Performance Consideration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Client Request                               | <br>The request from the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | <br>The request from the client might have timeout parameters set. In the VM-based installation and containerized installation program, a variable `client_request_timeout` is used to inform downstream component timeouts. This value must match the timeout of the external load balancer. The size of the request body and headers can also impact performance.                                                                                                                                                                                                                                                                                                                                                                                                              |
| <br>Ingress Point                                | <br>The first point of entry into Ansible Automation Platform, typically an OpenShift Container Platform Route or a customer-provided Load Balancer, directing traffic to an available platform gateway pod/instance.                                                                                                                                                                                                                                                                                                             | <br>Performance is dependent on the configuration, capacity, and health of the load balancer or OpenShift Container Platform Route. Any timeout for the external load balancer must be greater than or equal to the `client_request_timeout` setting passed to the installation program. This layer is responsible for distributing traffic if there are multiple platform gateway nodes/pods.                                                                                                                                                                                                                                                                                                                                                                                   |
| <br>Envoy Proxy                                  | <br>Located within the platform gateway pod/instance, this proxy handles authorization, internal routing, and applies filters to the request. Authorization by the gRPC service is performed before the Envoy forwards the request to the destination service.                                                                                                                                                                                                                                                                    | <br>Introduces minimal latency, typically on the order of 10 milliseconds. Can handle hundreds of concurrent requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <br>Platform gateway gRPC Authentication Service | <br>A local gRPC service within the platform gateway container responsible for authenticating each request. This service can interact with external authentication services (LDAP/SAML) and the database for validation. Authentication with the gRPC service can be disabled for individual URL routes, notably requests to the platform gateway service itself are not authenticated by this gRPC service (for example, under `/api/gateway/v1/`). These requests are authenticated by the platform gateway API service itself. | <br>Potential source of latency. The service is multi-processed and multi-threaded, with capacity determined by `GRPC_SERVER_PROCESSES` and `GRPC_SERVER_MAX_THREADS_PER_PROCESS`. If all workers are busy, then requests queue, which adds to latency. In containerized or VM-based installation, its timeout is informed by the `client_request_timeout`. Slow database connections for session validation also negatively impact performance.                                                                                                                                                                                                                                                                                                                                 |
| <br>External Authentication Service (LDAP/SAML)  | <br>An optional external service invoked by the platform gateway gRPC Authentication Service for validating user credentials.                                                                                                                                                                                                                                                                                                                                                                                                     | <br>Potential source of latency. When external authentication services (e.g., LDAP or SAML) are configured, they are invoked during the gRPC authentication stage. Slow response times from these external systems can significantly increase the total latency for each request processed. It is the user’s responsibility to provide a low-latency, reliable external authentication service.                                                                                                                                                                                                                                                                                                                                                                                  |
| <br>API Service Nginx Proxy                      | <br>After authentication, Envoy forwards the request to the component API node or Service in OpenShift Container Platform. Nginx receives the request. Each distinct API service component has its own Nginx proxy that determines if the request is for a WSGI application, an ASGI-based WebSocket service, or static content.                                                                                                                                                                                                  | <br>Introduces minimal latency, typically on the order of 10 milliseconds. Can handle hundreds of concurrent requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <br>WSGI Server (`uWSGI` / `Gunicorn`)           | <br>Handles standard API requests forwarded by Nginx. These servers process requests, validate JWT tokens, run API operations, and frequently interact with the database.                                                                                                                                                                                                                                                                                                                                                         | <br>Primary source of latency. API requests are handled by each component’s web application served by a WSGI server (`uWSGI` for automation controller and platform gateway and `Gunicorn` for automation hub and Event-Driven Ansible), and their timeout is also informed by the `client_request_timeout` in VM-based installation and container-based installation. In OpenShift Container Platform, the timeout on the platform gateway Route is propagated to inform this same setting. The servers are configured with a maximum number of concurrent workers. If all workers are busy, the request is queued. After a worker picks up a request, it validates the authentication and executes the API operation, which typically involves further database communication. |
| <br>Databases                                    | <br>Almost every request requires interacting with the database to do activities such as validating sessions, storing data, and executing API operations.                                                                                                                                                                                                                                                                                                                                                                         | <br>Critical performance factor. Almost every request requires interacting with the database. The responsiveness of database connections remains a critical factor in API performance, impacting both the gRPC authentication service and the WSGI server processing. Responsiveness can be impacted by network latency between the database and components, as well as performance of the database itself.                                                                                                                                                                                                                                                                                                                                                                      |
| <br>Client Response                              | <br>The final response returned to the client after the request has been processed and traversed back through the system components (Nginx proxy, Envoy, and the initial load balancer/Route).                                                                                                                                                                                                                                                                                                                                    | <br>The final response returned to the client after the request has been processed and traversed back through the system components (Nginx proxy, Envoy, and the initial load balancer/Route).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Sources of latency and scaling strategies

The primary sources of latency across all layers are:

- Queueing delays while awaiting an available worker from either the gRPC authentication service or the WSGI server
- The authentication phase, particularly if external authentication systems exhibit slow response times
- The actual processing time and associated database interactions within the Python WSGI application


Scaling strategies include the following:

- Using more performant authentication methods, such as Session or Token
- Horizontally scaling platform gateway and API service pods to increase worker availability and minimize queue times


The following sections describe how to identify which of the Ansible Automation Platform services provide which APIs and provide considerations for scaling them. For more information on the performance of different authentication methods, see [Considerations for scaling the platform gateway proxy and authentication service](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_motivations_for_migrating_to_enterprise_topology#scaling-gateway-proxy-and-authentication "Scale the platform gateway proxy and authentication services if request volume exceeds capacity. Horizontal scaling is preferred. Vertical scaling does not automatically adjust worker pools for gRPC, Envoy, Nginx, and WSGI services.").

## Key performance indicators to guide scaling plans

Scaling adds resources to handle increased load. This is primarily achieved through horizontal scaling (adding more pods or instances) or vertical scaling (adding CPU or memory resources to pods or instances). Proper scaling ensures high availability and maintains performance under load.

Scale your services when key performance indicators suggest a component is reaching capacity. These indicators show the component cannot efficiently handle the current request load and include the following:

- High API latency
- High CPU utilization
- Errors that occur during periods of high traffic


### High API latency

Sustained high latency on API requests is a key performance indicator. All requests are made through the platform platform gateway, which acts as a proxy and forwards requests to the services in question. The request is sent to the destination service depending on which route is in the URL of the API request:

- platform gateway: `/api/gateway`
- automation controller: `/api/controller`
- Event-Driven Ansible: `/api/eda`
- Event-Driven Ansible Event Streams: `/eda-event-streams/api/eda/v1/external_event_stream/`
- automation hub: `/api/galaxy`


Monitoring latency on the different routes through the Envoy proxy logs helps you identify which service requires scaling. These routes are present in the proxy container of platform gateway pods in OpenShift Container Platform. For VM-based installation and container-based installation installations, check the proxy logs of the platform gateway nodes. Exceeding target API thresholds (for example, 99th percentile >1500ms) indicates a need to trigger alerts. You might also need to scale web services.

### High CPU utilization

When a service’s API pod shows consistently high CPU usage, it might be unable to process incoming requests promptly. This can lead to a backlog of requests. The following indicators suggest high CPU utilization:

- High total request time from the Envoy proxy logs with the processing time from the service’s WSGI logs
- High total Envoy latency
- Requests are waiting in a queue before being processed

### Error codes

Error codes indicate the service must be scaled. Find these codes in the platform gateway’s proxy container (on OpenShift Container Platform) or in the proxy logs (for VM-based and container-based installations). They are often precipitated by the services being overloaded and unable to service requests in a timely manner, and are often preceded by periods of higher latency.

- Upstream Authentication Failures: `502 UAEX` (Upstream Authentication Extension) indicates issues during the authentication phase of a request. This suggests the authentication service is overloaded, timing out, or returning broken responses.
- Upstream Service Unhealthy: A `503 UH` (Upstream Service Unhealthy) response means Envoy has marked one or more service pods as unhealthy. Traffic is not being sent to that unhealthy pod.
- Upstream Connection Failure: `503 UF` (Upstream Connection Failure) response indicates a connection failure. Envoy attempted to contact an upstream pod, but the connection failed. For more information about Envoy Response Flags (the letter codes that follow the `HTTP` response code), see *Access logging* in the Related Links section.

## Scale the platform gateway proxy and authentication service

Scale the platform gateway proxy and authentication services if request volume exceeds capacity. Horizontal scaling is preferred. Vertical scaling does not automatically adjust worker pools for gRPC, Envoy, Nginx, and WSGI services.

Note:

Additional platform gateway service pods or instances can increase the necessary database connections for WSGI web service workers and gRPC authentication service workers.

If you observe a bottleneck in CPU utilization, then scaling the gRPC authentication service can improve throughput. However, if external authentication providers are the source of high latency, then horizontal scaling of the gRPC service has minimal benefits. You can determine the gRPC authentication latency for requests by observing the difference between the upstream service time and the total request latency.

The most performant authentication methods are:

- Token authentication
- Session authentication
- Basic authentication must not be used for high-frequency API automation because CPU-intensive password hashing introduces significant request latency. If Basic authentication is used in combination with LDAP authentication, reaching out to the LDAP service can introduce significant latency, especially if the LDAP service has limited availability. For this reason, we recommend creating OAuth Tokens to perform automation against the API.


Horizontally scaling the platform gateway service pods also increases the number of health checks to each component’s API, because each Envoy tracks this separately. You can observe these in logs with the user agent `Envoy/HC`. Since health checks flow through the same services and queues as user-initiated requests, if overall request times slow due to overload, health checks can also timeout. When this occurs, Envoy stops forwarding requests to these service nodes until they pass their health check again.

### Special considerations for scaling the platform gateway proxy and authentication service on OpenShift Container Platform

It is particularly important that the service is horizontally scaled sufficiently in OpenShift Container Platform, because if more than 100 requests are backlogged, then these requests are then dropped by uWSGI. This results in clients receiving a timeout for dropped requests. The following log text provides the corresponding error for this event:

```
*** uWSGI listen queue of socket ":8000" (fd: 3) full !!! (101/100) ***
```
This error occurs due to a limitation of uWSGI tying its backlog length to the kernel parameter `somaxconn`. It is possible to raise this kernel parameter in OpenShift Container Platform, but doing so requires allowing “unsafe sysctls”.

## Scale the automation controller API service

The automation controller API service handles HTTP requests to the application, including information about user roles in automation controller, project creation, inventory creation or updates, job launches, and job result checks.

### Key performance indicators

Key performance indicators for the automation controller API service include the following:

- High API latency for requests under `/api/controller`
- High CPU utilization on the API pods or nodes
- Platform gateway returning `503` errors because the service is too busy to respond to health checks


The automation controller API service is located in web pods on operator-based installation and in control or hybrid nodes on VM-based installation or container-based installation.

### Scaling strategies by deployment type

Consider the following strategies to scale the automation controller API service:

- OpenShift Container Platform: Adjust the `web_replicas` attribute on the `AutomationController` CR. Scaling the `replicas` attribute scales task and web replicas.
- VM-based installation and container-based installation: Scale control or hybrid nodes, increasing the ability to control additional automation jobs.

### Database connection and architecture considerations

On OpenShift Container Platform, each web replica consumes database connections for WSGI web service workers and various background services facilitating task communication and WebSockets. The number of database connections used by the WSGI web server on VM-based installation and container-based installation scales with the machine’s CPU count.

Additionally, control and hybrid nodes manage the Dispatcher (tasking system) and the Callback Receiver (job event processing worker pool). These worker pools scale with CPU availability and necessitate database connections.

Provisioning additional control nodes demands more database connections than scaling out the web deployment on OpenShift Container Platform alone. This demand occurs because containerized and RPM control node scaling also expands the tasking system, which operates as a distinct deployment on OpenShift Container Platform. This separation of services on OpenShift Container Platform deployments is an important distinction that allows administrators to more finely tune the deployment and conserve limited resources, such as database connections.

### Special considerations for scaling on OpenShift Container Platform

It is particularly important that the service is horizontally scaled sufficiently in OpenShift Container Platform, because if more than 100 requests are backlogged, then these requests are then dropped by uWSGI. This results in clients receiving a timeout for dropped requests. The following log text provides the corresponding error for this event:

```
*** uWSGI listen queue of socket ":8000" (fd: 3) full !!! (101/100) ***
```
This error occurs due to a limitation of uWSGI tying its backlog length to the kernel parameter `somaxconn`. It is possible to raise this kernel parameter in OpenShift Container Platform, but doing so requires allowing “unsafe sysctls”.

## Scale the Event-Driven Ansible API service

Learn how to scale the Event-Driven Ansible API service.

Scaling Event-Driven Ansible involves considerations for each of its service types:

- API and WebSocket service
- EventStream service


API requests routed to `/api/eda` and `/api/eda-event-stream` are handled by two separate `Gunicorn` deployments. In OpenShift Container Platform, these services must be scaled independently. For VM-based installation and container-based installation, you can scale these services together by increasing the number of hybrid nodes.

### Event-Driven Ansible API and WebSocket service

The Event-Driven Ansible API service handles `HTTP` requests to the application, including information about user roles in Event-Driven Ansible, creating projects, creating activations, and checking results. Key performance indicators for the API service include the following:

- High API latency for requests under `/api/eda`
- High CPU utilization on the API pods/nodes
- Platform gateway returning `503` errors because the service is too busy to respond to health checks


A WebSocket service is deployed alongside the API service to manage the output of the rulebook activations. Each activation maintains a persistent WebSocket connection to this service to communicate status and receive instructions. A large number of activations or a large amount of output from activations can overwhelm the WebSocket server, leading to failures.

Consider the following strategies to scale the Event-Driven Ansible API and WebSocket service:

- OpenShift Container Platform: The WebSocket server (Daphne) runs within the `eda-api` pod. Horizontally scale the `eda-api` deployment to scale this service. Note:
Ensure that you scale the `eda-api` deployment in proportion to the number of activations being run.

- VM-based installation or container-based installation: Horizontally scale the WebSocket service alongside the API service by adding more hybrid nodes. This increases capacity for all Event-Driven Ansible components simultaneously.


To identify whether your deployment experienced a bottleneck in the WebSocket service, check the activation logs for the following errors:

```
ansible_rulebook.websocket - WARNING - websocket aborted by <class 'websockets.exceptions.InvalidMessage'>: did not receive a valid HTTP response
ansible_rulebook.cli - ERROR - Terminating: did not receive a valid HTTP response
```

### Event-Driven Ansible EventStream service

The Event Stream API, which handles POST requests to `/api/eda-event-stream`, is a separate `Gunicorn` service designed to import events from external sources. If this service’s performance degrades, with high latency, low throughput, or availability issues, you must scale it. The platform gateway returns `503` errors for this service when a pod is too busy to respond to health checks in time.

Consider the following strategies to scale the Event-Driven Ansible EventStream service:

- OpenShift Container Platform: Horizontally scale up the dedicated `eda-event-stream` worker deployment, because it is managed separately from the main `eda-api deployment`.
- VM-based installation or container-based installation: Horizontally scale up this service by adding more hybrid nodes, which increases capacity for all Event-Driven Ansible components simultaneously.

## Scale the automation hub API service

Learn about scaling the automation hub API service.

Scaling automation hub involves considerations for each of its service types:

- API service: manages `HTTP` requests through the API
- Pulp workers service: manages syncs and content uploads
- Content service: manages content delivery after content has been processed and stored


Separate `Gunicorn` deployments back these services and handle different types of requests. In OpenShift Container Platform, these services must be scaled independently. In VM-based installation and container-based installation, a standard automation hub node hosts all services, and scaling is achieved by adding more nodes.

### Automation hub API service

The automation hub API service handles metadata-driven requests for the application, including UI interactions, searches, and remote repository configuration. Key performance indicators for the automation hub API service include:

- High API latency for requests under `/api/galaxy`
- High CPU utilization on the API pods or nodes
- Platform gateway returning `503` errors because the service is too busy to respond to health checks


Consider the following strategies to scale the automaton automation hub API service:

- OpenShift Container Platform: Horizontally scale the API pods by increasing the `hub.api.replicas` attribute on the `AnsibleAutomationPlatform` Custom Resource (CR).
- VM-based installation or container-based installation: Horizontally scale the API service by adding more automation hub nodes, which simultaneously scales all other automation hub services.

### Automation hub Pulp worker and content services

The Pulp worker and content services manage all operations related to content syncs, uploads and downloads. Key performance indicators for the Pulp worker and content services include:

- High Content sync rates: Frequent or large synchronization operations from external repositories demanding significant worker processing.
- High Content upload or download rates: Frequent pushing or pulling of automation execution environments by automation controller, Event-Driven Ansible, or large Collection uploads or downloads by automation clients.
- Disk I/O bottlenecks: Performance issues related to read/write operations on the underlying content storage (`/var/lib/pulp`), often shown as high disk I/O wait times.
- Pulp worker saturation: High CPU utilization or queuing within pulp processes, indicating an inability to keep up with content processing and serving.


To scale your Pulp worker and content services, consider the following scaling strategies:

- In OpenShift Container Platform: Scale the deployment of these services by increasing the `hub.content.replicas` and `hub.worker.replicas` attributes on the `AnsibleAutomationPlatform` Custom Resource.
- For VM-based installation or container-based installation: Horizontally scale all services by adding more automation hub nodes.
