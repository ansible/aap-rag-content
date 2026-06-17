# Activate webhook-based automation in Openshift

In Openshift environments, you can activate webhooks by creating a route to expose the activation’s service, enabling external systems to send events and trigger automation.

## Before you begin

- You have created a rulebook activation.


Note:

The following is an example of rulebook with a given webhook:

```
- name: Listen for storage-monitor events
hosts: all
sources:
- ansible.eda.webhook:
host: 0.0.0.0
port: 5000
rules:
- name: Rule - Print event information
condition: event.meta.headers is defined
action:
run_job_template:
name: StorageRemediation
organization: Default
job_args:
extra_vars:
message: from eda
sleep: 1
```

## Procedure

1.  Create a Route (on OpenShift Container Platform) to expose the service. The following is an example Route for an ansible-rulebook source that expects POST’s on port 5000 on the decision environment pod:


```
kind: Route
apiVersion: route.openshift.io/v1
metadata:
name: test-sync-bug
namespace: dynatrace
labels:
app: eda
job-name: activation-job-1-5000
spec:
host: test-sync-bug-dynatrace.apps.aap-dt.ocp4.testing.ansible.com
to:
kind: Service
name: activation-job-1-5000
weight: 100
port:
targetPort: 5000
tls:
termination: edge
insecureEdgeTerminationPolicy: Redirect
wildcardPolicy: None
```

2.  When you create the Route, test it with a **Post to the Route URL**:

Note:
You do not need the port as it is specified on the Route (targetPort).

```
curl -H "Content-Type: application/json" -X POST
test-sync-bug-dynatrace.apps.aap-dt.ocp4.testing.ansible.com -d
'{}'
```

## Testing with OpenShift (Kubernetes)

Configure Kubernetes networking (for example, Ingress) to temporarily expose activation webhooks for non-production testing and debugging.

### Procedure

1.  Run the following command to expose the port on the cluster for a given service:


```
kubectl port-forward svc/<ACTIVATION_SVC_NAME> 5000:5000
```

2.  Make the HTTP requests against the `localhost:5000` to trigger the rulebook:


```
curl -H "Content-Type: application/json" -X POST test-sync-bug-dynatrace.apps.aap-dt.ocp4.testing.ansible.com -d '{}'
```
