# Optimize platform performance

Optimizing platform performance ensures your deployment responds efficiently to workload demands and maintains availability under load. Scale services appropriately and tune configurations to support your automation capacity requirements.

Optimizing platform performance helps you to:

- **Maintain system responsiveness**: Scale services and adjust capacity to handle workload demands and prevent request queueing or timeouts.
- **Support growing automation workloads**: Plan deployment capacity based on your workload characteristics and add resources to accommodate increased managed hosts or concurrent jobs.
- **Resolve performance bottlenecks**: Monitor key performance indicators to identify services that require scaling and adjust configurations to improve throughput.

## How Ansible Automation Platform supports performance optimization

You can use multiple optimization approaches based on your deployment type and workload characteristics:

- **Scaling strategies** include horizontal scaling (adding more replicas) and vertical scaling (adding CPU, memory, or other resources). Scale services for platform gateway, automation controller, Event-Driven Ansible, and automation hub independently based on performance indicators.
- **Database tuning** includes configuring PostgreSQL parameters for memory allocation and maintenance operations to improve query performance and data management.
- **Capacity planning** involves characterizing workload based on managed hosts, concurrent jobs, and API request rates, then planning control and execution capacity.

## Automation execution settings

You can configure the following automation execution settings through the UI, API, or file settings:

- Live events in the automation controller UI
- Job event processing and scheduling
- Control and execution node capacity
- Instance and container groups capacity
- Internal cluster routing
- Web server tuning
