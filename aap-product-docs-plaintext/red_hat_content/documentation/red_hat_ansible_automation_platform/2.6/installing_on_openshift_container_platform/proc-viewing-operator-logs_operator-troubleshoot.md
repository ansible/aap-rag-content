# 12. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 12.3. Viewing operator logs




The following procedure is an example of how to view the logs for an `automation-controller-operator` pod.

**Procedure**

1. To find the pod name, run:


```
oc get pods | grep operator
```


1. to view the logs for the pod, run:


```
oc logs &lt;operator-pod-name&gt; -f
```


1. Alternatively, to view the logs without first getting the pod name, run:


```
oc logs deployments/automation-controller-operator-controller-manager -c automation-controller-manager -f
```





