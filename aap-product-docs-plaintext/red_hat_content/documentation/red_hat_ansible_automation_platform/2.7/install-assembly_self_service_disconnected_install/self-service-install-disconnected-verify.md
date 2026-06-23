# Install Ansible automation portal in air-gapped OpenShift Container Platform environments
## Verify the disconnected installation

Verify the successful installation of the Helm chart in the disconnected environment. Check the Helm release status, monitor the pods, and verify that the application routes are accessible.

### Procedure

1.  Check the Helm release status:


```
$ helm list -n ${MY_NAMESPACE}
```

2.  Monitor the pods in your namespace to ensure they are running:


```
$ oc get pods -n ${MY_NAMESPACE}
```

3.  Check for `ImagePullBackOff` or other errors in pod events:


```
$ oc describe pod <pod_name> -n ${MY_NAMESPACE}
```

4.  If the chart uses routes to expose services, verify that the routes are created and accessible:


```
$ oc get route -n ${MY_NAMESPACE}
```

