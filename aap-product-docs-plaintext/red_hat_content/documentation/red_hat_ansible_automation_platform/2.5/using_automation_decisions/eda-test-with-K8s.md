# 7. Rulebook activations
## 7.9. Testing with Kubernetes




With Kubernetes you can create an Ingress, or expose the port, but not for production.

**Procedure**

1. Run the following command to expose the port on the cluster for a given service:


```
kubectl port-forward svc/&lt;ACTIVATION_SVC_NAME&gt; 5000:5000
```


1. Make the HTTP requests against the `    localhost:5000` to trigger the rulebook:


```
curl -H "Content-Type: application/json" -X POST test-sync-bug-dynatrace.apps.aap-dt.ocp4.testing.ansible.com -d '{}'
```




