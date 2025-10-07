# 4. Configuring Ansible automation controller on OpenShift Container Platform
## 4.1. Minimizing downtime during OpenShift Container Platform upgrade




Make the following configuration changes in automation controller to minimize downtime during the upgrade.

**Prerequisites**

- Ansible Automation Platform 2.4 or later
- Ansible automation controller 4.4 or later
- OpenShift Container Platform:


- Later than 4.10.42
- Later than 4.11.16
- Later than 4.12.0

- High availability (HA) deployment of Postgres
- Multiple worker node that automation controller pods can be scheduled on


**Procedure**

1. Enable `    RECEPTOR_KUBE_SUPPORT_RECONNECT` in AutomationController specification:


```
apiVersion: automationcontroller.ansible.com/v1beta1    kind: AutomationController    metadata:      ...    spec:      ...      ee_extra_env: |        - name: RECEPTOR_KUBE_SUPPORT_RECONNECT          value: enabled        ```
```


1. Enable the graceful termination feature in AutomationController specification:


```
termination_grace_period_seconds: &lt;time to wait for job to finish&gt;
```


1. Configure `    podAntiAffinity` for web and task the pod to spread out the deployment in AutomationController specification:


```
task_affinity:        podAntiAffinity:          preferredDuringSchedulingIgnoredDuringExecution:          - podAffinityTerm:              labelSelector:                matchExpressions:                - key: app.kubernetes.io/name                  operator: In                  values:                  - awx-task              topologyKey: topology.kubernetes.io/zone            weight: 100      web_affinity:        podAntiAffinity:          preferredDuringSchedulingIgnoredDuringExecution:          - podAffinityTerm:              labelSelector:                matchExpressions:                - key: app.kubernetes.io/name                  operator: In                  values:                  - awx-web              topologyKey: topology.kubernetes.io/zone            weight: 100
```


1. Configure `    PodDisruptionBudget` in OpenShift Container Platform:


```
---    apiVersion: policy/v1    kind: PodDisruptionBudget    metadata:      name: automationcontroller-job-pods    spec:      maxUnavailable: 0      selector:        matchExpressions:          - key: ansible-awx-job-id            operator: Exists    ---    apiVersion: policy/v1    kind: PodDisruptionBudget    metadata:      name: automationcontroller-web-pods    spec:      minAvailable: 1      selector:        matchExpressions:          - key: app.kubernetes.io/name            operator: In            values:              - &lt;automationcontroller_instance_name&gt;-web    ---    apiVersion: policy/v1    kind: PodDisruptionBudget    metadata:      name: automationcontroller-task-pods    spec:      minAvailable: 1      selector:        matchExpressions:          - key: app.kubernetes.io/name            operator: In            values:              - &lt;automationcontroller_instance_name&gt;-task
```





<span id="idm140083191688608"></span>
