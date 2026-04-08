# 2. Scaling the tested deployment models
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




