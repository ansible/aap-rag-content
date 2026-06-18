+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_horizontal_scaling"
title = "Horizontally scale in Event-Driven Ansible - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_horizontal_scaling/", "Horizontally scale in Event-Driven Ansible"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_horizontal_scaling/aem-page/optimize-assembly_horizontal_scaling.html"
last_crumb = "Horizontally scale in Event-Driven Ansible"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Horizontally scale in Event-Driven Ansible"
oversized = "false"
page_slug = "optimize-assembly_horizontal_scaling"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-assembly_horizontal_scaling"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_horizontal_scaling/toc/toc.json"
type = "aem-page"
+++

# Horizontally scale in Event-Driven Ansible

You can set up multi-node deployments for components across Ansible Automation Platform. Whether you require horizontal scaling for Automation Execution, Automation Decisions, or automation mesh, you can scale your deployments based on your organization’s needs.

## Horizontal scaling in Event-Driven Ansible controller

With Event-Driven Ansible controller, you can set up horizontal scaling for events automation. This multi-node deployment allows you to define as many nodes as preferred during installation. You can also increase or decrease the node count at any time to meet organizational needs.

The following node types are used in this deployment:

API node type
Responds to the HTTP REST API of Event-Driven Ansible controller.

Worker node type
Runs an Event-Driven Ansible worker, which is the component of Event-Driven Ansible that not only manages projects and activations, but also executes the activations themselves.

Hybrid node type
Is a combination of the API node and the worker node.

### Inventory file updates for RPM-based installations (VMs)

The following example shows how you can set up an inventory file for horizontal scaling of Event-Driven Ansible controller on Red Hat Enterprise Linux VMs using the host group name `[automationedacontroller]` and the node type variable `eda_node_type`:

```
[automationedacontroller]

3.88.116.111 routable_hostname=automationedacontroller-api.example.com eda_node_type=api

# worker node
3.88.116.112 routable_hostname=automationedacontroller-api.example.com eda_node_type=worker
```

### Inventory file updates for containerized installations

The following example shows how you can set up an inventory file for horizontal scaling of Event-Driven Ansible controller on Red Hat Enterprise Linux VMs using the host group name `[automationeda]` and the node type variable `eda_type`:

```
[automationeda]

3.88.116.111 routable_hostname=automationeda-api.example.com eda_type=api

# worker node
3.88.116.112 routable_hostname=automationeda-api.example.com eda_type=worker
```

## Sizing and scaling guidelines

Scaling guidelines for Event-Driven Ansible define how to properly size API nodes based on user requests and worker nodes based on automation activations. You can ensure independent scaling and optimized resource utilization for your environment by separating the node roles.

API nodes process user requests (interactions with the UI or API) while worker nodes process the activations and other background tasks required for Event-Driven Ansible to function properly. The number of API nodes you require correlates to the required number of users of the application and the number of worker nodes correlates to the required number of activations you want to run.

Since activations are variable and controlled by worker nodes, the supported approach for scaling is to use separate API and worker nodes instead of hybrid nodes due to the efficient allocation of hardware resources by worker nodes. By separating the nodes, you can scale each type independently based on specific needs, leading to better resource utilization and cost efficiency.

An example of an instance in which you might consider scaling up your node deployment is when you want to deploy Event-Driven Ansible for a small group of users who will run a large number of activations. In this case, one API node is adequate, but if you require more, you can scale up to three additional worker nodes.

## Set up horizontal scaling for Event-Driven Ansible controller

To scale up (add more nodes) or scale down (remove nodes), you must update the content of the inventory file to add or remove nodes and rerun the installation program.

### Procedure

1.  Update the inventory to add two more worker nodes:
  - For RPM-based installations:

```
[automationedacontroller]

        3.88.116.111 routable_hostname=automationedacontroller-api.example.com eda_node_type=api

        3.88.116.112 routable_hostname=automationedacontroller-api.example.com eda_node_type=worker

        # two more worker nodes
3.88.116.113 routable_hostname=automationedacontroller-api.example.com eda_node_type=worker

        3.88.116.114 routable_hostname=automationedacontroller-api.example.com eda_node_type=worker
```

  - For containerized installations:

```
[automationeda]

        3.88.116.111 routable_hostname=automationeda-api.example.com eda_type=api

        3.88.116.112 routable_hostname=automationeda-api.example.com eda_type=worker

        # two more worker nodes
3.88.116.113 routable_hostname=automationeda-api.example.com eda_type=worker

        3.88.116.114 routable_hostname=automationeda-api.example.com eda_type=worker
```

2.  Re-run the installer.

## Scale and manage by installation type

Considerations for scaling and managing each Ansible Automation Platform component differ based on the installation type. The following table provides information on scaling and management operations for each installation type, and other common operations to consider when planning your deployment:

Note:

Red Hat OpenShift Container Platform-based deployments provide the most flexibility and customizability, which enables you to adapt the deployment as needs change. OpenShift Container Platform also provides fine-grained observability through its built-in metrics capabilities and integrations, with log aggregation tools that capture all logs from all pods in the Ansible Automation Platform deployment.

*Table 1. Comparison of Scaling and Management Operations by installation Type*

| Task                                | OpenShift Container Platform                                                                                                                                                                                                                                                                                                    | VM-based installation                                                                                                                                                                                                                                                                                                                                                | Containerized Deployments (Podman based)                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Horizontally scale up           | <br>Scale control, execution, automation hub, and Event-Driven Ansible components independently by adjusting replicas. Expanding total capacity by adding worker nodes to OpenShift Container Platform does not disrupt Ansible Automation Platform operation.                                                                  | <br>Requires updating inventory file and re-running entire installation, which restarts and requires halting use of the platform.                                                                                                                                                                                                                                    | <br>Requires updating inventory file and re-running entire installation, which restarts and requires halting use of the platform.                                                                                                                                                                                                                                    |
| <br>Horizontally scale down         | <br>Reduces replicas handled by operator. For scaling down automation controller task pods, usage of `termination_grace_period_seconds` allows the scale down to occur after jobs are drained from the task pod.                                                                                                                | <br>Requires updating the inventory file and re-running the entire installation. This restarts the platform, halting use.                                                                                                                                                                                                                                            | <br>Requires updating the inventory file and re-running the entire installation. This restarts the platform, halting use.                                                                                                                                                                                                                                            |
| <br>Vertically scaling up or down   | <br>Increases or decreases requests and limits on individual deployment types. The operator deploys a new pod with these resources, and previous pods scale down. For automation controller task pods, usage of `termination_grace_period_seconds allows` the old replicas to scale down after jobs are drained from task pods. | <br>Depending on your virtualization provider, the virtual machine might require shutdown to resize. Attaining the full benefit of vertical scaling requires re-running the installation program, which restarts and halts use of the platform. Running the installation program adapts any settings that were tuned based on the number of available cores and RAM. | <br>Depending on your virtualization provider, the virtual machine might require shutdown to resize. Attaining the full benefit of vertical scaling requires re-running the installation program, which restarts and halts use of the platform. Running the installation program adapts any settings that were tuned based on the number of available cores and RAM. |
| <br>Installation                    | <br>Utilizes OpenShift Container Platform Operators for automated deployment and management.                                                                                                                                                                                                                                    | <br>Ansible Playbook-based installation program installs RPMs and configures the platform.                                                                                                                                                                                                                                                                           | <br>Ansible Playbook-based installation program that configures platform services in Podman containers, which are managed by `systemd`.                                                                                                                                                                                                                              |
| <br>Upgrade                         | <br>Handled by OpenShift Container Platform Operators with automated rolling updates. Usage of `termination_grace_period_seconds` allows upgrades without downtime and without halting job execution.                                                                                                                           | <br>Requires running the installation program and restarting services, which halts use of the platform.                                                                                                                                                                                                                                                              | <br>Requires running the installation program and restarting services, which halts use of the platform.                                                                                                                                                                                                                                                              |
| <br>Aggregating Application Logs    | <br>Centralized logging through OpenShift Container Platform’s built-in logging stack or integrations with external aggregators.                                                                                                                                                                                                | <br>Requires external log aggregation solutions (e.g., ELK stack, Splunk) to collect logs from individual nodes.                                                                                                                                                                                                                                                     | <br>Requires external log aggregation solutions (e.g., ELK stack, Splunk) to collect logs from container instances.                                                                                                                                                                                                                                                  |
| <br>Monitoring Resource Utilization | <br>Comprehensive monitoring with OpenShift Container Platform’s built-in Prometheus and Grafana dashboards, providing detailed pod and node metrics.                                                                                                                                                                           | <br>Requires external monitoring tools to collect and visualize resource metrics from nodes.                                                                                                                                                                                                                                                                         | <br>Requires external monitoring tools to collect and visualize resource metrics from nodes.                                                                                                                                                                                                                                                                         |
