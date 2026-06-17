# Specify dedicated nodes for pods and job execution

A Kubernetes cluster runs on multiple nodes. Use the `topologySpreadConstraints` setting to control how pods are distributed across your nodes during scheduling. This ensures high availability and balanced workloads across your infrastructure.

Do not schedule your pods on a single node, because if that node fails, the services that those pods provide also fails.

Schedule the control plane nodes to run on different nodes to the automation job pods. If the control plane pods share nodes with the job pods, the control plane can become resource starved and degrade the performance of the whole application.

## Assign pods to specific nodes

You can constrain the automation controller pods created by the operator to run on a certain subset of nodes.

- `node_selector` and `postgres_selector` constrain the automation controller pods to run only on the nodes that match all the specified key, or value, pairs.
- `tolerations` and `postgres_tolerations` enable the automation controller pods to be scheduled onto nodes with matching taints. See [Taints and Toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) in the Kubernetes documentation for further details.


The following table shows the settings and fields that can be set on the automation controller’s specification section of the YAML (or using the OpenShift UI form).

| Name                               | Description                                              | Default      |
| ---------------------------------- | -------------------------------------------------------- | ------------ |
| <br> `postgres_image`              | <br>Path of the image to pull                            | <br>postgres |
| <br> `postgres_image_version`      | <br>Image version to pull                                | <br>15       |
| <br> `node_selector`               | <br>AutomationController pods’ nodeSelector              | <br>“”’’     |
| <br> `topology_spread_constraints` | <br>AutomationController pods’ topologySpreadConstraints | <br>“”’’     |
| <br> `tolerations`                 | <br>AutomationController pods’ tolerations               | <br>“”’’     |
| <br> `annotations`                 | <br>AutomationController pods’ annotations               | <br>“”’’     |
| <br> `postgres_selector`           | <br>Postgres pods’ nodeSelector                          | <br>“”’’     |
| <br> `postgres_tolerations`        | <br>Postgres pods’ tolerations                           | <br>“”’’     |


`topology_spread_constraints` can help optimize spreading your control plane pods across the compute nodes that match your node selector. For example, with the `maxSkew` parameter of this option set to `100`, this means maximally spread across available nodes. So if there are three matching compute nodes and three pods, one pod will be assigned to each compute node. This parameter helps prevent the control plane pods from competing for resources with each other.

**Example of a custom configuration for constraining controller pods to specific nodes**

```
spec:
...
node_selector: |
disktype: ssd
kubernetes.io/arch: amd64
kubernetes.io/os: linux
topology_spread_constraints: |
- maxSkew: 100
topologyKey: "topology.kubernetes.io/zone"
whenUnsatisfiable: "ScheduleAnyway"
labelSelector:
matchLabels:
app.kubernetes.io/name: "<resourcename>"
tolerations: |
- key: "dedicated"
operator: "Equal"
value: "AutomationController"
effect: "NoSchedule"
postgres_selector: |
disktype: ssd
kubernetes.io/arch: amd64
kubernetes.io/os: linux
postgres_tolerations: |
- key: "dedicated"
operator: "Equal"
value: "AutomationController"
effect: "NoSchedule"
```

## Specify nodes for job execution

You can add a node selector to the container group pod specification to ensure they only run against certain nodes. First add a label to the nodes you want to run jobs against.

### About this task

The following procedure adds a label to a node.

### Procedure

1.  List the nodes in your cluster, along with their labels:


```
kubectl get nodes --show-labels
```
The output is similar to this (shown here in a table):

| Name           | Status    | Roles      | Age    | Version     | Labels                                   |
| -------------- | --------- | ---------- | ------ | ----------- | ---------------------------------------- |
| <br> `worker0` | <br>Ready | <br><none> | <br>1d | <br>v1.13.0 | <br> `…​,kubernetes.io/hostname=worker0` |
| <br> `worker1` | <br>Ready | <br><none> | <br>1d | <br>v1.13.0 | <br> `…​,kubernetes.io/hostname=worker1` |
| <br> `worker2` | <br>Ready | <br><none> | <br>1d | <br>v1.13.0 | <br> `…​,kubernetes.io/hostname=worker2` |

2.  Choose one of your nodes, and add a label to it by using the following command:


```
kubectl label nodes <your-node-name> <aap_node_type>=<execution>
```
For example:

```
kubectl label nodes <your-node-name> disktype=ssd
```
where `<your-node-name>` is the name of your chosen node.

3.  Verify that your chosen node has a `disktype=ssd` label:


```
kubectl get nodes --show-labels
```

4.  The output is similar to this (shown here in a table):
| Name           | Status    | Roles      | Age    | Version     | Labels                                               |
| -------------- | --------- | ---------- | ------ | ----------- | ---------------------------------------------------- |
| <br> `worker0` | <br>Ready | <br><none> | <br>1d | <br>v1.13.0 | <br> `…​disktype=ssd,kubernetes.io/hostname=worker0` |
| <br> `worker1` | <br>Ready | <br><none> | <br>1d | <br>v1.13.0 | <br> `…​,kubernetes.io/hostname=worker1`             |
| <br> `worker2` | <br>Ready | <br><none> | <br>1d | <br>v1.13.0 | <br> `…​,kubernetes.io/hostname=worker2`             |
You can see that the `worker0` node now has a `disktype=ssd` label.

5.  In the automation controller UI, specify that label in the metadata section of your customized pod specification in the container group.

```
apiVersion: v1
kind: Pod
metadata:
disktype: ssd
namespace: ansible-automation-platform
spec:
serviceAccountName: default
automountServiceAccountToken: false
nodeSelector:
aap_node_type: execution
containers:
- image: >-
registry.redhat.io/ansible-automation-platform-22/ee-supported-rhel8@sha256:d134e198b179d1b21d3f067d745dd1a8e28167235c312cdc233860410ea3ec3e
name: worker
args:
- ansible-runner
- worker
- '--private-data-dir=/runner'
resources:
requests:
cpu: 250m
memory: 100Mi
```

## Extra settings

With `extra_settings`, you can pass many custom settings by using the awx-operator. The parameter `extra_settings` is appended to `/etc/tower/settings.py` and can be an alternative to the `extra_volumes` parameter.

| Name                  | Description        | Default |
| --------------------- | ------------------ | ------- |
| <br> `extra_settings` | <br>Extra settings | <br>‘’  |


**Example configuration of `extra_settings` parameter**

```
spec:
extra_settings:
- setting: MAX_PAGE_SIZE
value: "500"

- setting: AUTH_LDAP_BIND_DN
value: "cn=admin,dc=example,dc=com"

- setting: SYSTEM_TASK_ABS_MEM
value: "500"
```
**Custom pod timeouts**

A container group job in automation controller transitions to the `running` state just before you submit the pod to the Kubernetes API. Automation controller then expects the pod to enter the `Running` state before `AWX_CONTAINER_GROUP_POD_PENDING_TIMEOUT` seconds has elapsed. You can set `AWX_CONTAINER_GROUP_POD_PENDING_TIMEOUT` to a higher value if you want automation controller to wait for longer before canceling jobs that fail to enter the `Running` state. `AWX_CONTAINER_GROUP_POD_PENDING_TIMEOUT` is how long automation controller waits from creation of a pod until the Ansible work begins in the pod. You can also extend the time if the pod cannot be scheduled because of resource constraints. You can do this using `extra_settings` on the automation controller specification. The default value is two hours.

This is used if you are consistently launching many more jobs than Kubernetes can schedule, and jobs are spending periods longer than `AWX_CONTAINER_GROUP_POD_PENDING_TIMEOUT` in *pending*.

Jobs are not launched until control capacity is available. If many more jobs are being launched than the container group has capacity to run, consider scaling up your Kubernetes worker nodes.

## Jobs scheduled on the worker nodes

Both automation controller and Kubernetes play a role in scheduling a job.

When a job is launched, its dependencies are fulfilled, meaning any project updates or inventory updates are launched by automation controller as required by the job template, project, and inventory settings.

If the job is not blocked by other business logic in automation controller and there is control capacity in the control plane to start the job, the job is submitted to the dispatcher. The default settings of the "cost" to control a job is 1 *capacity*. So, a control pod with 100 capacity is able to control up to 100 jobs at a time. Given control capacity, the job transitions from *pending* to *waiting*.

The dispatcher, which is a background process in the control plan pod, starts a worker process to run the job. This communicates with the Kubernetes API using a service account associated with the container group and uses the pod specification as defined on the Container Group in automation controller to provision the pod. The job status in automation controller is shown as *running*.

Kubernetes now schedules the pod. A pod can remain in the *pending* state for `AWX_CONTAINER_GROUP_POD_PENDING_TIMEOUT`. If the pod is denied through a `ResourceQuota`, the job starts over at *pending*. You can configure a resource quota on a namespace to limit how many resources may be consumed by pods in the namespace. For further information about ResourceQuotas, see [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/).

## Minimize downtime during OpenShift Container Platform upgrade

Make the following configuration changes in automation controller to minimize downtime during the upgrade.

### Before you begin

- Ansible Automation Platform 2.4 or later
- Ansible automation controller 4.4 or later
- OpenShift Container Platform:
* Later than 4.10.42
* Later than 4.11.16
* Later than 4.12.0
- High availability (HA) deployment of Postgres
- Multiple worker nodes that automation controller pods can be scheduled on

### About this task

### Procedure

1.  Enable `RECEPTOR_KUBE_SUPPORT_RECONNECT` in AutomationController specification:


```
apiVersion: automationcontroller.ansible.com/v1beta1
kind: AutomationController
metadata:
...
spec:
...
ee_extra_env: |
- name: RECEPTOR_KUBE_SUPPORT_RECONNECT
value: enabled
```
```

2.  Enable the graceful termination feature in AutomationController specification:


```
termination_grace_period_seconds: <time to wait for job to finish>
```

3.  Configure `podAntiAffinity` for web and task the pod to spread out the deployment in AutomationController specification:


```
task_affinity:
podAntiAffinity:
preferredDuringSchedulingIgnoredDuringExecution:
- podAffinityTerm:
labelSelector:
matchExpressions:
- key: app.kubernetes.io/name
operator: In
values:
- awx-task
topologyKey: topology.kubernetes.io/zone
weight: 100
web_affinity:
podAntiAffinity:
preferredDuringSchedulingIgnoredDuringExecution:
- podAffinityTerm:
labelSelector:
matchExpressions:
- key: app.kubernetes.io/name
operator: In
values:
- awx-web
topologyKey: topology.kubernetes.io/zone
weight: 100
```

4.  Configure `PodDisruptionBudget` in OpenShift Container Platform:


```
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
name: automationcontroller-job-pods
spec:
maxUnavailable: 0
selector:
matchExpressions:
- key: ansible-awx-job-id
operator: Exists
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
name: automationcontroller-web-pods
spec:
minAvailable: 1
selector:
matchExpressions:
- key: app.kubernetes.io/name
operator: In
values:
- <automationcontroller_instance_name>-web
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
name: automationcontroller-task-pods
spec:
minAvailable: 1
selector:
matchExpressions:
- key: app.kubernetes.io/name
operator: In
values:
- <automationcontroller_instance_name>-task
```
