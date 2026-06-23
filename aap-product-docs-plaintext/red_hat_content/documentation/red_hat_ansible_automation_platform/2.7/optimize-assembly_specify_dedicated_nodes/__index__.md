# Specify dedicated nodes for pods and job execution

A Kubernetes cluster runs on multiple nodes. Use the `topologySpreadConstraints` setting to control how pods are distributed across your nodes during scheduling. This ensures high availability and balanced workloads across your infrastructure.

Do not schedule your pods on a single node, because if that node fails, the services that those pods provide also fails.

Schedule the control plane nodes to run on different nodes to the automation job pods. If the control plane pods share nodes with the job pods, the control plane can become resource starved and degrade the performance of the whole application.

