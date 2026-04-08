+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/html-single/performance_tuning_for_ansible_automation_platform/index"
title = "Performance tuning for Ansible Automation Platform - Red Hat Ansible Automation Platform 2.6"

[extra]
category = "Configure and Operate"
category_description = ""
document_kind = "documentation"
modified = "2025-11-12T20:26:04.000Z"
multi_page_path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/html/performance_tuning_for_ansible_automation_platform/index/"
name = "Performance tuning for Ansible Automation Platform"
page_slug = "performance_tuning_for_ansible_automation_platform"
product = "Red Hat Ansible Automation Platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/performance_tuning_for_ansible_automation_platform/index"
type = "single-page"
+++


<span id="idm139687044106368"></span>
Red Hat Ansible Automation Platform2.6
## Tune your Ansible Automation Platform for optimal performance.


Red Hat Customer Content Services

 [Legal Notice](#idm139687041685328) 
 **Abstract** 

This guide provides recommended practices for various processes needed to tune your Ansible Automation Platform deployments.




---

# Preface




This guide provides recommended practices for various processes needed to tune your Ansible Automation Platform deployments.

# Providing feedback on Red Hat documentation




If you have a suggestion to improve this documentation, or find an error, you can contact technical support at [https://access.redhat.com](https://access.redhat.com) to open a request.

# Chapter 1. Types of workloads




This guide offers insights on enabling performance tuning for your Ansible Automation Platform deployment. It covers the following topics:

- The types of workloads and the components these workloads rely on to perform well
- The services each workload uses
- Reference workloads supported by the tested deployment models
- Reasons for scaling each service beyond the base configurations of the tested deployment models


## 1.1. UI authentication and platform load




Users can access the Ansible Automation Platform UI by using enterprise authentication methods. UI clients apply load to the platform gateway proxy and the gRPC authentication service, the web servers of all components, and the database, because most UI-driven API requests interact with the database.

The login performance with enterprise authentication is dependent on the performance of the external authentication provider and the complexity of the mapping of the external authentication attributes to RBAC attributes in Ansible Automation Platform. After successful login, the browser uses session authentication for subsequent requests, which is generally a faster authentication method as some session data is cached.

The Ansible Automation Platform UI receives live updates through WebSockets and periodically requests updates from all components to properly render options and update on-screen information. Users can configure the frequency of these periodically maintained update requests by adjusting the "Refresh Interval" setting in the UI **User Preferences** tab. This action affects the load that an open browser tab with the Ansible Automation Platform UI generates on backend services.

Through WebSockets in the user interface, the browser receives real-time job updates. The browser can subscribe to any job running on any automation controller node, because events are accessible everywhere. However, live streaming updates to the job detail page might increase the load on the automation controller service. To disable these updates, set `UI_LIVE_UPDATES_ENABLED` to false in the automation controller configuration.

Note
Disabling updates prevents the job detail page from automatically updating when events are received. In this case, you must manually refresh the page to access the most recent details.



## 1.2. REST API access and client load




The Red Hat Ansible Automation Platform provides a REST API, offering access to all its functionalities. You can access this API by using various clients, including cURL, Python, Ansible Automation Platform configuration collections, or the Ansible URI module.

You can use the API to automate the following tasks:

- launching jobs
- updating inventories
- checking automation status
- pushing events into an Event Stream for Event-Driven Ansible
- automating the upload or publication of collections in automation hub
- managing automation execution environments in the automation hub container registry using a Podman client that connects to automation hub over its registry API


API clients apply load to the platform gateway proxy, the gRPC service for authentication, the web server of the targeted component, and the database, because most API client queries interact with the database.

To access the API, you can use the following common authentication methods: Basic authentication (using a username and password) and Token authentication (your chosen authentication method). We recommend Token authentication for better performance. Use the platform gateway to create tokens and link them to an OAuth application or your account. The platform gateway’s gRPC service authenticates each request and directs it to the appropriate application server based on the specified route. For more information, see [Authenticating in the API](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/automation_execution_api_overview/controller-api-auth-methods) .

## 1.3. Primary workloads for automation controller




The primary workloads for automation controller include the following:

- Managing automation content through automation controller projects
- Initiating automation by executing jobs


### 1.3.1. Automation controller project synchronization




Users define the source of automation content within the automation controller projects, such as Ansible Playbooks. The primary workload for these projects is synchronization. Project update jobs in the API manage synchronization. These jobs are also known as source control updates in the UI.

These project update jobs run only on the control plane and in task pods within the OpenShift Container Platform. Their role is to update the automation controller with the latest automation content from its defined source, such as a Git repository.

Updating projects is not performance-sensitive, provided that they store only playbooks and Ansible-related text files. However, issues might arise when projects become excessively large. Do not store large volumes of binary data within a project. If jobs require access to additional data, retrieve this data from object storage or file storage within the playbook’s scope.

### 1.3.2. Jobs and automation workloads




Jobs are the primary workload for automation controller and are run on the execution plane. They include the following job types:

- Standard jobs
- Workflow, sliced, and bulk jobs
- System jobs


#### 1.3.2.1. Standard jobs




Standard jobs involve the execution of an Ansible Playbook from a Project against a set of hosts from an Inventory. Jobs are initiated by a control node, which then streams, processes, and stores job results.

A performance sensitive part of this is the processing of the playbook output. The output is captured and serialized into job events by the automation controller. A single Ansible task running against a host typically produces multiple job events (for example: task start, host-specific details, and task completion).

Event volume varies significantly with the playbook’s configured verbosity level. For example, a simple debug task that prints `Hello World` on one host might produce 6 job events at verbosity 1, increasing to 34 job events at verbosity 3.

The dispatcher and the callback receiver collaborate to process, transmit, and store job events. These actions contribute to the platform’s storage and processing usage. Job events are processed on the control plane and stored in the database. The dispatcher processes job events, and the callback receiver stores them.

#### 1.3.2.2. Workflow, Sliced and Bulk jobs




To enable complex automation and orchestration, use the following job types to extend standard jobs:

- Sliced jobs: Split jobs to run against slices of the inventory in parallel
- Bulk jobs: Launch multiple jobs in a single request
- Workflow jobs: Coordinate multiple job templates


These job types coordinate the launch and management of multiple underlying standard jobs. They impact job scheduling, which occurs in the control plane, but otherwise do not have significant impact on their services.

#### 1.3.2.3. System jobs




System jobs involve internal maintenance tasks, such as clean up of old job event data. The execution frequency of system jobs is managed by schedules. System jobs run on the control plane, because they run management commands that interact with the database. These workloads involve key platform activities. Reducing the frequency of system jobs or increasing the number of days of data for jobs to retain can degrade database performance. In general, we recommend retaining as few days of data as possible and leveraging the external logging features for long term audit data storage. Storing more data in the database can make expensive queries that scan large tables more costly for the database.

## 1.4. Event-Driven Ansible activations




Activations are used by Event-Driven Ansible to run instances of `ansible-rulebook` . These activations can either connect to external event sources or listen to an event stream for incoming payloads.

Activation and output management uses Event-Driven Ansible hybrid nodes, the platform gateway for event stream handling, the WebSocket server in each API node or pod, and the database for audit event storage.

Activations process discrete payloads called events. The activation’s resource usage is affected by the event arrival rate and the complexity of the rulebook’s rules. When events match rules, they trigger actions, which launch jobs in automation controller. Event auditing stores audit events in the database and is enabled by default.

Each event is sent from the activation to the WebSocket server to be serialized and written to the database. This process stresses the server and can cause performance issues. Selecting **Skip audit events** in the UI for a given activation eliminates this workload. When **Skip audit events** is selected, rules are still fired, but the fire count in the API and UI is updated at a periodic interval (default 300 seconds) rather than immediately.

## 1.5. Collection synchronization




Private automation hub can synchronize collections from remote `ansible-galaxy` repositories, such as `galaxy.ansible.com` or automation hub on `console.redhat.com` .

Pulp content worker and the database sync repositories. The automation controller can download these collections during project updates, or use them to build automation execution environments. Collections are also available for any other client by using the `ansible-galaxy` CLI to download and use.

The performance of syncing collections is relative to the number of collections listed in the `requirements.yml` , the number of versions synced, and the number of versions retained. Specifically, synchronization uses memory in proportion to the number of collections and versions synchronized. Using a targeted `requirements.yml` with specific versions can limit this impact. Hosting collections uses storage space. Manage the storage space that collections use by specifying the retained number of versions on the repository.

## 1.6. Container image hosting and performance




Private automation hub has the capability to host container images for automation execution environments and decision environments. Event-Driven Ansible or automation controller can pull these container images when running activations or jobs. The frequency of job starts and the pull policy configured for the automation execution environments and decision environments in Event-Driven Ansible or automation controller determine how often they pull these containers.

The performance of pushing and pulling container images from automation hub depends on the disk performance of the underlying storage. This is because Pulp content workers store and fetch the layers of the container image from disk. The size of layers can impact the memory used by the pulp workers, because they serve entire layers in a single operation. The pull policy on jobs and activations, the frequency of job or activation starts, and the node or Container Group’s existing image status determine the frequency of container image pulls.

## 1.7. Reference workloads for growth topologies




The following table provides reference data for typical workloads, performance metrics, and capacity planning for the tested Ansible Automation Platform growth topologies.


<span id="idm139687045633696"></span>
 **Table 1.1. Reference workloads for growth topologies** 

| Component / Feature | Metric |
| --- | --- |
| REST API | 8 requests per second (RPS) |
| REST API 50 percentile latency at 8 RPS | 500 milliseconds |
| REST API 99 percentile latency at 8 RPS | 1.5 seconds |
| Hosts in automation controller inventory | 1,000 hosts |
| Job start rate in automation controller (max burst rate with standard launch) | 20 jobs started per second |
| Concurrent jobs in automation controller | 10 concurrent jobs with default forks (5 forks is default) + 100 with forks=1 |
| Callback receiver event processing rate | 10,000 job events per second at peak |
| Job History with 30 days retention | 2kb event; 500 events per playbook run; 500 jobs a day + Less than 60Gb (as specified as minimum required disk on Database node) |
| (Certified) Sync time | Less than 30 minutes |
| (Validated) Sync time | Less than 5 minutes |
| Activation processing events with skip audit events enabled (6 activation) with events incoming via Event Stream and execution strategy set to sequential (default) in the rulebook | 1 actionable event/minute with minimal payload with job template action on local automation controller where each job completes in 1 minute |




## 1.8. Reference workloads for enterprise topologies




The following table provides reference data for typical workloads, performance metrics, and capacity planning for the tested Ansible Automation Platform enterprise topologies.


<span id="idm139687045228800"></span>
 **Table 1.2. Reference workloads for enterprise topologies** 

| Component / Feature | Metric |
| --- | --- |
| REST API | 16 requests per second (RPS) |
| REST API 50 percentile latency at 16 RPS | 500 milliseconds |
| REST API 99 percentile latency at 16 RPS | 1.5 seconds |
| Hosts in automation controller inventory | 10,000 hosts |
| Job start rate in automation controller | 80 jobs started per second |
| Concurrent jobs in automation controller | 40 with default forks (5 forks is default) + 400 with forks=1 |
| Callback receiver event rate | 40,000 events per second at peak |
| Job History with 7 days retention | 2kb event; 500 events per playbook run; 2000 jobs a day + Less than 60Gb (as specified as minimum required disk on Database node) |
| (Certified) Sync time | Less than 30 minutes |
| (Validated) Sync time | Less than 5 minutes |
| Processing events with skip audit events enabled (6 activations) with events incoming via Event Stream and execution strategy set to sequential (default) in the rulebook | 3 actionable event/minute with minimal payload with job template action on local automation controller where each job completes in 1 minute |




# Chapter 2. Scaling the tested deployment models




You can scale your Ansible Automation Platform tested deployment models to meet your workload requirements. This document refers to the following scaling methods:

- Vertical scaling
- Horizontal scaling


## 2.1. Vertical scaling for performance




Vertical scaling increases the physical resources available to a service, including the CPU, memory, disk volume, and disk Input/Output Operations per Second (IOPS). Use vertical scaling for deployments with high resource utilization or workload demand.

### 2.1.1. Benefits of vertical scaling




- Relieves resource contention: Applications have access to more resources and this can relieve resource contention or exhaustion.


### 2.1.2. Drawbacks and other considerations for vertical scaling




- Extensive testing required: The installation program attempts to tune application and system configurations to use additional resources, but not all components of the application automatically scale in relation to machine size. Manually tuning each variable requires extensive testing. For this reason, after an instance size has been verified for an environment, horizontal scaling by adding more instances of the same size is recommended.
- Application-level limitations: For VM-based installation or Containerized deployments, instances with more than 64 CPU cores and 128 GB of RAM might not scale linearly due to system and application-level limits.
- Resource overcommit: Overcommitting virtual machine resources (for example, allocating more virtual CPU/RAM to guests than is physically available on the host) leads to unpredictable performance.
- CPU throttling: In OpenShift Container Platform, setting a CPU `    limit` without an equivalent `    request` can lead to CPU throttling, even if the node has spare CPU capacity. This throttling negatively impacts API latency.
    
    
    - To mitigate this, always set CPU `        requests` equal to CPU `        limits` .
    - Monitor CPU throttling using the `        container_cpu_cfs_throttled_seconds_total` metric.
    
- Database limitations: Scaling the application increases the maximum potential number of database connections from worker processes and the overall memory, I/O, and CPU utilization of the PostgreSQL instance. As you scale past the tested deployment models, deploy your separate Postgres instances per component (platform gateway, Event-Driven Ansible, automation controller, automation hub).


## 2.2. Horizontal scaling for performance




Horizontal scaling involves increasing the number of replicas (pods or virtual machines) for a given service. Similar to vertical scaling, this approach is useful for high resource utilization or workload scaling.

### 2.2.1. Benefits of horizontal scaling




- Improved availability: Distributes load across more instances to reduce the impact of a single slow or failing node.
- Redundancy: Provides extra capacity, allowing individual service nodes to recover or cool-off without impacting overall availability.
- Increased authentication capacity: Each platform gateway pod includes its own authentication service, so scaling the platform gateway directly increases the platform’s authentication throughput.
- Repeatable scaling procedure: After the instance size and configuration are verified for your environment, deploy identical instances to scale.


### 2.2.2. Drawbacks and other considerations for horizontal scaling




- Database limitations: Scaling the application increases the maximum potential number of database connections from worker processes, and the overall memory, I/O, and CPU utilization of the PostgreSQL instance. As you scale past the tested deployment models, deploy your separate Postgres instances per component (platform gateway, Event-Driven Ansible, automation controller, automation hub).
- Health Check Overhead: In a mesh architecture, each Envoy proxy sends health checks to every other cluster member. Horizontal scaling increases this baseline traffic, adding to system usage.


## 2.3. Scaling and management considerations by installation type




Considerations for scaling and managing each Ansible Automation Platform component differ based on the installation type. The following table provides information on scaling and management operations for each installation type, and other common operations to consider when planning your deployment:

Note
Red Hat OpenShift Container Platform-based deployments provide the most flexibility and customizability, which enables you to adapt the deployment as needs change. OpenShift Container Platform also provides fine-grained observability through its built-in metrics capabilities and integrations, with log aggregation tools that capture all logs from all pods in the Ansible Automation Platform deployment.




<span id="idm139687045466736"></span>
 **Table 2.1. Comparison of Scaling and Management Operations by installation Type** 

| Task | OpenShift Container Platform | VM-based installation | Containerized Deployments (Podman based) |
| --- | --- | --- | --- |
| Horizontally scale up | Scale control, execution, automation hub, and Event-Driven Ansible components independently by adjusting replicas. Expanding total capacity by adding worker nodes to OpenShift Container Platform does not disrupt Ansible Automation Platform operation. | Requires updating inventory file and re-running entire installation, which restarts and requires halting use of the platform. | Requires updating inventory file and re-running entire installation, which restarts and requires halting use of the platform. |
| Horizontally scale down | Reduces replicas handled by operator. For scaling down automation controller task pods, usage of `termination_grace_period_seconds` allows the scale down to occur after jobs are drained from the task pod. | Requires updating the inventory file and re-running the entire installation. This restarts the platform, halting use. | Requires updating the inventory file and re-running the entire installation. This restarts the platform, halting use. |
| Vertically scaling up or down | Increases or decreases requests and limits on individual deployment types. The operator deploys a new pod with these resources, and previous pods scale down. For automation controller task pods, usage of `termination_grace_period_seconds allows` the old replicas to scale down after jobs are drained from task pods. | Depending on your virtualization provider, the virtual machine might require shutdown to resize. Attaining the full benefit of vertical scaling requires re-running the installation program, which restarts and halts use of the platform. Running the installation program adapts any settings that were tuned based on the number of available cores and RAM. | Depending on your virtualization provider, the virtual machine might require shutdown to resize. Attaining the full benefit of vertical scaling requires re-running the installation program, which restarts and halts use of the platform. Running the installation program adapts any settings that were tuned based on the number of available cores and RAM. |
| Installation | Utilizes OpenShift Container Platform Operators for automated deployment and management. | Ansible Playbook-based installation program installs RPMs and configures the platform. | Ansible Playbook-based installation program that configures platform services in Podman containers, which are managed by `systemd` . |
| Upgrade | Handled by OpenShift Container Platform Operators with automated rolling updates. Usage of `termination_grace_period_seconds` allows upgrades without downtime and without halting job execution. | Requires running the installation program and restarting services, which halts use of the platform. | Requires running the installation program and restarting services, which halts use of the platform. |
| Aggregating Application Logs | Centralized logging through OpenShift Container Platform’s built-in logging stack or integrations with external aggregators. | Requires external log aggregation solutions (e.g., ELK stack, Splunk) to collect logs from individual nodes. | Requires external log aggregation solutions (e.g., ELK stack, Splunk) to collect logs from container instances. |
| Monitoring Resource Utilization | Comprehensive monitoring with OpenShift Container Platform’s built-in Prometheus and Grafana dashboards, providing detailed pod and node metrics. | Requires external monitoring tools to collect and visualize resource metrics from nodes. | Requires external monitoring tools to collect and visualize resource metrics from nodes. |




## 2.4. Motivations for migrating to an enterprise topology




Growth topologies model a minimal Ansible Automation Platform installation. Growth topologies are suited to proof-of-concept deployments, small-scale environments, or preliminary evaluations. Using a growth topology simplifies initial setup for your Ansible Automation Platform deployment, but they have inherent limitations.

### 2.4.1. Inherent limitations of growth topologies




Growth topologies include single points of failure, such as a single platform gateway , and other critical components, such as the control plane, execution plane, and web services. These components often share resources on the same node, resulting in resource contention under increasing load. As workloads grow, specific services, such as job processing or API responsiveness, can become bottlenecks due to colocation or single node capacity limits. Consequently, growth topologies generally do not offer robust, high-availability capabilities. For VM-based installation and containerized deployments of Ansible Automation Platform, you can marginally increase possible workloads by vertically scaling the virtual machines or physical hosts within the growth deployment. However, vertical scaling capabilities within a growth topology are limited.

### 2.4.2. Use cases for migrating to an enterprise topology




To scale beyond the limitations within growth topologies, you can migrate to an enterprise topology. Migrating to an enterprise topology might be relevant in the following use cases:

- Vertically scaling a growth topology becomes impractical due to cost or availability.
- The growth topology cannot satisfy high availability and disaster recovery requirements.
- You must scale Ansible Automation Platform services independently, such as API handling, job execution, and database capacity.
- Workload demands consistently overwhelm the capacity of vertically scaled growth topologies.
- You require more complex network architectures, such as segmented networks.


### 2.4.3. Recommended enterprise topology




To maximize flexibility, resilience, and scalability, migrate to the OpenShift Container Platform-based enterprise topology. This migration includes integration with an externally managed, enterprise-grade PostgreSQL database. operator-based installation offers greater flexibility to scale individual services and adapt the deployment to specific requirements. They also enhance the ability to scale the deployment up and down with reduced downtime and customize workload placement with labels, taints, tolerations, and topology constraints. operator-based installation also benefits from resilience features, such as automatic service recreation if underlying worker nodes experience failure or resource exhaustion.

## 2.5. Motivations for customizing enterprise topologies




Enterprise topologies provide a pattern for scalability and resilience. Organizations typically evolve the tested deployment models into custom deployments, tailoring service configurations and scaling to their specific workflows and performance needs within Red Hat Ansible Automation Platform.

An organization’s unique use of Ansible Automation Platform determines which components require scaling, moving from a generic enterprise topology to a workload-tuned deployment. For example, infrequent automation hub use, numerous small jobs across distributed regions, or API-heavy integrations necessitate different scaling priorities for each component, such as the API service or execution plane. Motivations for customizing the documented enterprise deployment models include achieving high availability, enabling independent scaling of components, such as automation controller API compared to execution capacity, to match actual demand, and supporting workload growth or specific SLAs. This requires custom resource allocation and performance tuning based on identified needs, rather than adherence to a general pattern. Before customizing and scaling, you must identify specific bottlenecks within your Ansible Automation Platform environment (for example, in API response, job processing, database performance, or Event-Driven Ansible event handling). Use platform monitoring tools and analytics to identify bottlenecks. After bottlenecks are identified, you can approach scaling each component vertically or horizontally.

# Chapter 3. API service performance




The API service for each Ansible Automation Platform component affects the overall performance of your Ansible Automation Platform deployment. This document describes the following:

- API service architecture and scalable components
- Key performance indicators for scaling the API services
- Considerations for scaling the API service for each Ansible Automation Platform component


## 3.1. API request flow and latency sources




The Ansible Automation Platform API is provided by a distributed set of services. Overall platform performance is affected by the path that each request takes through the platform and the multiple potential sources of latency and performance considerations at each layer. The following table describes each layer in the API request flow through Ansible Automation Platform:


<span id="idm139687043835488"></span>
 **Table 3.1. API Service architecture and performance considerations** 

| Layer | Description | Performance Consideration |
| --- | --- | --- |
| Client Request | The request from the client. | The request from the client might have timeout parameters set. In the VM-based installation and containerized installation program, a variable `client_request_timeout` is used to inform downstream component timeouts. This value must match the timeout of the external load balancer. The size of the request body and headers can also impact performance. |
| Ingress Point | The first point of entry into Ansible Automation Platform, typically an OpenShift Container Platform Route or a customer-provided Load Balancer, directing traffic to an available platform gateway pod/instance. | Performance is dependent on the configuration, capacity, and health of the load balancer or OpenShift Container Platform Route. Any timeout for the external load balancer must be greater than or equal to the `client_request_timeout` setting passed to the installation program. This layer is responsible for distributing traffic if there are multiple platform gateway nodes/pods. |
| Envoy Proxy | Located within the platform gateway pod/instance, this proxy handles authorization, internal routing, and applies filters to the request. Authorization by the gRPC service is performed before the Envoy forwards the request to the destination service. | Introduces minimal latency, typically on the order of 10 milliseconds. Can handle hundreds of concurrent requests. |
| Platform gateway gRPC Authentication Service | A local gRPC service within the platform gateway container responsible for authenticating each request. This service can interact with external authentication services (LDAP/SAML) and the database for validation. Authentication with the gRPC service can be disabled for individual URL routes, notably requests to the platform gateway service itself are not authenticated by this gRPC service (for example, under `/api/gateway/v1/` ). These requests are authenticated by the platform gateway API service itself. | Potential source of latency. The service is multi-processed and multi-threaded, with capacity determined by `GRPC_SERVER_PROCESSES` and `GRPC_SERVER_MAX_THREADS_PER_PROCESS` . If all workers are busy, then requests queue, which adds to latency. In containerized or VM-based installation, its timeout is informed by the `client_request_timeout` . Slow database connections for session validation also negatively impact performance. |
| External Authentication Service (LDAP/SAML) | An optional external service invoked by the platform gateway gRPC Authentication Service for validating user credentials. | Potential source of latency. When external authentication services (e.g., LDAP or SAML) are configured, they are invoked during the gRPC authentication stage. Slow response times from these external systems can significantly increase the total latency for each request processed. It is the user’s responsibility to provide a low-latency, reliable external authentication service. |
| API Service Nginx Proxy | After authentication, Envoy forwards the request to the component API node or Service in OpenShift Container Platform. Nginx receives the request. Each distinct API service component has its own Nginx proxy that determines if the request is for a WSGI application, an ASGI-based WebSocket service, or static content. | Introduces minimal latency, typically on the order of 10 milliseconds. Can handle hundreds of concurrent requests. |
| WSGI Server ( `uWSGI` / `Gunicorn` ) | Handles standard API requests forwarded by Nginx. These servers process requests, validate JWT tokens, run API operations, and frequently interact with the database. | Primary source of latency. API requests are handled by each component’s web application served by a WSGI server ( `uWSGI` for automation controller and platform gateway and `Gunicorn` for automation hub and Event-Driven Ansible), and their timeout is also informed by the `client_request_timeout` in VM-based installation and container-based installation. In OpenShift Container Platform, the timeout on the platform gateway Route is propagated to inform this same setting. The servers are configured with a maximum number of concurrent workers. If all workers are busy, the request is queued. After a worker picks up a request, it validates the authentication and executes the API operation, which typically involves further database communication. |
| Databases | Almost every request requires interacting with the database to do activities such as validating sessions, storing data, and executing API operations. | Critical performance factor. Almost every request requires interacting with the database. The responsiveness of database connections remains a critical factor in API performance, impacting both the gRPC authentication service and the WSGI server processing. Responsiveness can be impacted by network latency between the database and components, as well as performance of the database itself. |
| Client Response | The final response returned to the client after the request has been processed and traversed back through the system components (Nginx proxy, Envoy, and the initial load balancer/Route). | The final response returned to the client after the request has been processed and traversed back through the system components (Nginx proxy, Envoy, and the initial load balancer/Route). |




### 3.1.1. Sources of latency and scaling strategies




The primary sources of latency across all layers are:

- Queueing delays while awaiting an available worker from either the gRPC authentication service or the WSGI server
- The authentication phase, particularly if external authentication systems exhibit slow response times
- The actual processing time and associated database interactions within the Python WSGI application


Scaling strategies include the following:

- Using more performant authentication methods, such as Session or Token
- Horizontally scaling platform gateway and API service pods to increase worker availability and minimize queue times


The following sections describe how to identify which of the Ansible Automation Platform services provide which APIs and provide considerations for scaling them. For more information on the performance of different authentication methods, see [Considerations for scaling the platform gateway proxy and authentication service](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/performance_tuning_for_ansible_automation_platform/api_service_performance#scaling-gateway-proxy-and-authentication_aap-api-performance) .

## 3.2. Key performance indicators for scaling the API services




Scaling adds resources to handle increased load. This is primarily achieved through horizontal scaling (adding more pods or instances) or vertical scaling (adding CPU or memory resources to pods or instances). Proper scaling ensures high availability and maintains performance under load.

Consider scaling your services when you observe one or more of the following key performance indicators, which suggest a component is reaching its capacity and cannot efficiently handle the current request load:

- High API latency
- High CPU utilization
- Errors that occur during periods of high traffic


### 3.2.1. High API latency




Sustained high latency on API requests is a key performance indicator. All requests are made through the platform platform gateway, which acts as a proxy and forwards requests to the services in question. The request is sent to the destination service depending on which route is in the URL of the API request:

- platform gateway: `    /api/gateway` 
- automation controller: `    /api/controller` 
- Event-Driven Ansible: `    /api/eda` 
- Event-Driven Ansible Event Streams: `    /eda-event-streams/api/eda/v1/external_event_stream/` 
- automation hub: `    /api/galaxy` 


Monitoring latency on the different routes through the Envoy proxy logs enables you to identify which service requires scaling. These routes are present in the proxy container of platform gateway pods in OpenShift Container Platform or in the proxy logs of the platform gateway nodes in VM-based installation and container-based installation. Latency exceeding target API thresholds (for example, 99th percentile >1500ms) indicates a need to trigger alerts or scale web services.

### 3.2.2. High CPU utilization




When a service’s API pod shows consistently high CPU usage, it might be unable to process incoming requests in a timely manner, leading to a backlog of requests. The following indicators suggest high CPU utilization:

- High total request time from the Envoy proxy logs with the processing time from the service’s WSGI logs
- High total Envoy latency
- Requests are waiting in a queue before being processed


### 3.2.3. Error codes




Error codes in the platform gateway’s proxy container (on OpenShift Container Platform) or in the proxy logs (for VM-based and container-based installations) indicate the service must be scaled. They are often precipitated by the services being overloaded and unable to service requests in a timely manner, and are often preceded by periods of higher latency.

- Upstream Authentication Failures: `    502 UAEX` (Upstream Authentication Extension) responses in Envoy logs indicate issues during the authentication phase of a request. This suggests the authentication service is overloaded, timing out, or returning broken responses.
- Upstream Service Unhealthy: `    503 UH` (Upstream Service Unhealthy) responses for a specific service mean that Envoy has marked one or more of that service’s pods as unhealthy and is not sending traffic to it. This occurs when an upstream pod fails its health checks. Because health checks share the same request queue as client traffic, an overloaded pod that cannot respond to the health check in time will be temporarily removed from the load balancing pool.
- Upstream Connection Failure: `    503 UF` (Upstream Connection Failure) for a specific service’s requests indicates Envoy attempted to contact an upstream pod, but the connection failed. This can occur if the upstream service is overwhelmed and cannot accept new connections. For more information about Envoy Response Flags (the letter codes that follow the `    HTTP` response code), see [Access logging](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/usage) .


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

### 3.3.1. Special considerations for scaling the platform gateway proxy and authentication service on OpenShift Container Platform




It is particularly important that the service is horizontally scaled sufficiently in OpenShift Container Platform, because if more than 100 requests are backlogged, then these requests are then dropped by uWSGI. This results in clients receiving a timeout for dropped requests. The following log text provides the corresponding error for this event:

```
*** uWSGI listen queue of socket ":8000" (fd: 3) full !!! (101/100) ***
```

This error occurs due to a limitation of uWSGI tying its backlog length to the kernel parameter `somaxconn` . It is possible to raise this kernel parameter in OpenShift Container Platform, but doing so requires allowing “unsafe sysctls”.

## 3.4. Considerations for scaling the automation controller API service




The automation controller API service handles HTTP requests to the application, including information about user roles in automation controller, project creation, inventory creation or updates, job launches, and job result checks.

### 3.4.1. Key performance indicators




Key performance indicators for the automation controller API service include the following:

- High API latency for requests under `    /api/controller` 
- High CPU utilization on the API pods or nodes
- Platform gateway returning `    503` errors because the service is too busy to respond to health checks


The automation controller API service is located in web pods on operator-based installation and in control or hybrid nodes on VM-based installation or container-based installation.

### 3.4.2. Scaling strategies by deployment type




Consider the following strategies to scale the automation controller API service:

- OpenShift Container Platform: Adjust the `    web_replicas` attribute on the `    AutomationController` CR. Scaling the `    replicas` attribute scales task and web replicas.
- VM-based installation and container-based installation: Scale control or hybrid nodes, increasing the ability to control additional automation jobs.


### 3.4.3. Database connection and architecture considerations




On OpenShift Container Platform, each web replica consumes database connections for WSGI web service workers and various background services facilitating task communication and WebSockets. The number of database connections used by the WSGI web server on VM-based installation and container-based installation scales with the machine’s CPU count. Additionally, control and hybrid nodes manage the Dispatcher (tasking system) and the Callback Receiver (job event processing worker pool). These worker pools scale with CPU availability and necessitate database connections.

Provisioning additional control nodes demands more database connections than solely scaling out the web deployment on OpenShift Container Platform. This demand occurs because containerized and RPM control node scaling also expands the tasking system, which operates as a distinct deployment on OpenShift Container Platform. This separation of services on OpenShift Container Platform deployments is an important distinction that allows administrators to more finely tune the deployment and conserve limited resources, such as database connections.

### 3.4.4. Special considerations for scaling on OpenShift Container Platform




It is particularly important that the service is horizontally scaled sufficiently in OpenShift Container Platform, because if more than 100 requests are backlogged, then these requests are then dropped by uWSGI. This results in clients receiving a timeout for dropped requests. The following log text provides the corresponding error for this event:

```
*** uWSGI listen queue of socket ":8000" (fd: 3) full !!! (101/100) ***
```

This error occurs due to a limitation of uWSGI tying its backlog length to the kernel parameter `somaxconn` . It is possible to raise this kernel parameter in OpenShift Container Platform, but doing so requires allowing “unsafe sysctls”.

## 3.5. Considerations for scaling the Event-Driven Ansible APIs




Scaling Event-Driven Ansible involves considerations for each of its service types:

- API and WebSocket service
- EventStream service


API requests routed to `/api/eda` and `/api/eda-event-stream` are handled by two separate `Gunicorn` deployments. In OpenShift Container Platform, these services must be scaled independently. For VM-based installation and container-based installation, you can scale these services together by increasing the number of hybrid nodes.

### 3.5.1. Event-Driven Ansible API and WebSocket service




The Event-Driven Ansible API service handles `HTTP` requests to the application, including information about user roles in Event-Driven Ansible, creating projects, creating activations, and checking results. Key performance indicators for the API service include the following:

- High API latency for requests under `    /api/eda` 
- High CPU utilization on the API pods/nodes
- Platform gateway returning `    503` errors because the service is too busy to respond to health checks


A WebSocket service is deployed alongside the API service to manage the output of the rulebook activations. Each activation maintains a persistent WebSocket connection to this service to communicate status and receive instructions. A large number of activations or a large amount of output from activations can overwhelm the WebSocket server, leading to failures.

Consider the following strategies to scale the Event-Driven Ansible API and WebSocket service:

- OpenShift Container Platform: The WebSocket server (Daphne) runs within the `    eda-api` pod. Horizontally scale the `    eda-api` deployment to scale this service.


Ensure that you scale the `eda-api` deployment in proportion to the number of activations being run.


- VM-based installation or container-based installation: Horizontally scale the WebSocket service alongside the API service by adding more hybrid nodes. This increases capacity for all Event-Driven Ansible components simultaneously.


To identify whether your deployment experienced a bottleneck in the WebSocket service, check the activation logs for the following errors:

```
ansible_rulebook.websocket - WARNING - websocket aborted by &lt;class 'websockets.exceptions.InvalidMessage'&gt;: did not receive a valid HTTP response
ansible_rulebook.cli - ERROR - Terminating: did not receive a valid HTTP response
```

### 3.5.2. Event-Driven Ansible EventStream service




The Event Stream API, which handles POST requests to `/api/eda-event-stream` , is a separate `Gunicorn` service designed to import events from external sources. If this service’s performance degrades, with high latency, low throughput, or availability issues, you must scale it. The platform gateway returns `503` errors for this service when a pod is too busy to respond to health checks in time.

Consider the following strategies to scale the Event-Driven Ansible EventStream service:

- OpenShift Container Platform: Horizontally scale up the dedicated `    eda-event-stream` worker deployment, because it is managed separately from the main `    eda-api deployment` .
- VM-based installation or container-based installation: Horizontally scale up this service by adding more hybrid nodes, which increases capacity for all Event-Driven Ansible components simultaneously.


## 3.6. Considerations for scaling the automation hub APIs




Scaling automation hub involves considerations for each of its service types:

- API service: manages `    HTTP` requests through the API
- Pulp workers service: manages syncs and content uploads
- Content service: manages content delivery after content has been processed and stored


Separate `Gunicorn` deployments back these services and handle different types of requests. In OpenShift Container Platform, these services must be scaled independently. In VM-based installation and container-based installation, a standard automation hub node hosts all services, and scaling is achieved by adding more nodes.

### 3.6.1. Automation hub API service




The automation hub API service handles metadata-driven requests for the application, including UI interactions, searches, and remote repository configuration. Key performance indicators for the automation hub API service include:

- High API latency for requests under `    /api/galaxy` 
- High CPU utilization on the API pods or nodes
- Platform gateway returning `    503` errors because the service is too busy to respond to health checks


Consider the following strategies to scale the automaton automation hub API service:

- OpenShift Container Platform: Horizontally scale the API pods by increasing the `    hub.api.replicas` attribute on the `    AnsibleAutomationPlatform` Custom Resource (CR).
- VM-based installation or container-based installation: Horizontally scale the API service by adding more automation hub nodes, which simultaneously scales all other automation hub services.


### 3.6.2. Automation hub Pulp worker and content services




The Pulp worker and content services manage all operations related to content syncs, uploads and downloads. Key performance indicators for the Pulp worker and content services include:

- High Content sync rates: Frequent or large synchronization operations from external repositories demanding significant pulp-content worker processing.
- High Content upload or download rates: Frequent pushing or pulling of automation execution environments by automation controller, Event-Driven Ansible, or large Collection uploads or downloads by automation clients.
- Disk I/O bottlenecks: Performance issues related to read/write operations on the underlying content storage ( `    /var/lib/pulp` ), often shown as high disk I/O wait times.
- Pulp worker saturation: High CPU utilization or queuing within pulp processes, indicating an inability to keep up with content processing and serving.


To scale your Pulp worker and content services, consider the following scaling strategies:

- In OpenShift Container Platform: Scale the deployment of these services by increasing the `    hub.content.replicas` and `    hub.worker.replicas` attributes on the `    AnsibleAutomationPlatform` Custom Resource.
- For VM-based installation or container-based installation: Horizontally scale all services by adding more automation hub nodes.



<span id="idm139687041685328"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





