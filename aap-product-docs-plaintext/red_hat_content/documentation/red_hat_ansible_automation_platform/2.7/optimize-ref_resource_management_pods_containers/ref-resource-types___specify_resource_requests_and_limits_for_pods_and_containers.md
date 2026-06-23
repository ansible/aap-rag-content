# Manage resources for pods and containers
## Resource types
### Specify resource requests and limits for pods and containers

For each container, you can specify resource limits and requests, including the following:

```
spec.containers[].resources.limits.cpu
spec.containers[].resources.limits.memory
spec.containers[].resources.requests.cpu
spec.containers[].resources.requests.memory
```
Although you can only specify requests and limits for individual containers, it is also useful to think about the overall resource requests and limits for a pod. For a particular resource, a pod resource request or limit is the sum of the resource requests or limits of that type for each container in the pod.

