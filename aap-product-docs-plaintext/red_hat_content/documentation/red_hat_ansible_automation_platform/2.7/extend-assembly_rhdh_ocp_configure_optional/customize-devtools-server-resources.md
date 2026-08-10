# Optional configuration
## Customize Ansible Developer Tools server resources

Ansible Developer Tools sidecar container ships with default CPU and memory resource requests and limits. Customize these values if your namespace enforces a `LimitRange` with lower values or if you want to tune resources for your workload.

### About this task

The following table lists the default resource requests and limits for the `ansible-devtools-server` container in the Helm chart:

*Table 1. Default resource requests and limits*

| Resource type | CPU   | Memory |
| ------------- | ----- | ------ |
| Requests      | 1     | 1Gi    |
| Limits        | 2500m | 2.5Gi  |

Important:

If the target namespace has a `LimitRange` resource configured without default values, Kubernetes rejects any pod that does not specify resource requests and limits. The `ansible-devtools-server` container includes explicit defaults to pass `LimitRange` validation. If your `LimitRange` enforces values lower than the chart defaults, you must override the resources to match your namespace constraints.

The `ansible-devtools-server` runs as an `extraContainers` entry in the Helm chart. Due to Helm array replacement behavior, overriding a single field inside an array item requires duplicating the full container spec. You cannot set only the `resources` block. You must include the `command`, `image`, `name`, and `ports` fields as well.

### Procedure

1.  Log in to the OpenShift Container Platform web console.
2.  Open the Helm chart configuration for your portal deployment.

- For a new deployment, select Ecosystem> (and then)Helm, click Create, and select **Helm Release**.
- For an existing deployment, select Workloads> (and then)Deployments, click your portal deployment, and click the **YAML** tab.

3.  Switch to the YAML view and find the `extraContainers` section. Set your desired resource values:


```yaml
upstream:
backstage:
extraContainers:
- command:
- adt
- server
image: >-
registry.redhat.io/ansible-automation-platform-2.7/ansible-dev-tools-rhel9:latest
imagePullPolicy: IfNotPresent
name: ansible-devtools-server
ports:
- containerPort: 8000
resources:
requests:
cpu: 500m
memory: 512Mi
limits:
cpu: 1250m
memory: 1.25Gi
```

Replace the `cpu` and `memory` values under `requests` and `limits` with values that match your namespace constraints.

4.  Apply the changes.

- For a new deployment, click Create.
- For an existing deployment, click Save. The pod restarts automatically with the updated resource values.
