# 2. Scaling the tested deployment models
## 2.5. Motivations for customizing enterprise topologies




Enterprise topologies provide a pattern for scalability and resilience. Organizations typically evolve the tested deployment models into custom deployments, tailoring service configurations and scaling to their specific workflows and performance needs within Red Hat Ansible Automation Platform.

An organization’s unique use of Ansible Automation Platform determines which components require scaling, moving from a generic enterprise topology to a workload-tuned deployment. For example, infrequent automation hub use, numerous small jobs across distributed regions, or API-heavy integrations necessitate different scaling priorities for each component, such as the API service or execution plane. Motivations for customizing the documented enterprise deployment models include achieving high availability, enabling independent scaling of components, such as automation controller API compared to execution capacity, to match actual demand, and supporting workload growth or specific SLAs. This requires custom resource allocation and performance tuning based on identified needs, rather than adherence to a general pattern. Before customizing and scaling, you must identify specific bottlenecks within your Ansible Automation Platform environment (for example, in API response, job processing, database performance, or Event-Driven Ansible event handling). Use platform monitoring tools and analytics to identify bottlenecks. After bottlenecks are identified, you can approach scaling each component vertically or horizontally.

