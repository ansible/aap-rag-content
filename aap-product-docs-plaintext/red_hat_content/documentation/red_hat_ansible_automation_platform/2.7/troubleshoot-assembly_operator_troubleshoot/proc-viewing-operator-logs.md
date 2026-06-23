# Troubleshoot your Operator-based deployment of Ansible Automation Platform
## View operator logs

The following procedure is an example of how to view the logs for an `automation-controller-operator` pod.

### Procedure

1.  To find the pod name, run:


```
oc get pods | grep operator
```

2.  To view the logs for the pod, run:


```
oc logs <operator-pod-name> -f
```
1.  Alternatively, to view the logs without first getting the pod name, run:


```
oc logs deployments/automation-controller-operator-controller-manager -c automation-controller-manager -f
```

