# Migrate from HTTP plug-in registry to OCI container delivery
## Troubleshooting the migration
### Accessing init container logs

To view the logs of the `install-dynamic-plugins` init container:

```
$ oc get pods -n <namespace> -l app.kubernetes.io/component=backstage
$ oc logs <pod-name> -c install-dynamic-plugins -n <namespace>
```
If the pod has already completed (e.g., if the init container succeeded), you can view the previous logs:

```
$ oc logs <pod-name> -c install-dynamic-plugins --previous -n <namespace>
```
If the pod is still running, stream logs in real time:

```
$ oc logs -f <pod-name> -c install-dynamic-plugins -n <namespace>
```
