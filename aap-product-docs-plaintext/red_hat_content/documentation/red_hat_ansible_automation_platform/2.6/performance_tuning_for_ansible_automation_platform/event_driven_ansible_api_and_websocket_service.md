# 3. API service performance
## 3.5. Considerations for scaling the Event-Driven Ansible APIs
### 3.5.1. Event-Driven Ansible API and WebSocket service




The Event-Driven Ansible API service handles `HTTP` requests to the application, including information about user roles in Event-Driven Ansible, creating projects, creating activations, and checking results. Key performance indicators for the API service include the following:

- High API latency for requests under `    /api/eda`
- High CPU utilization on the API pods/nodes
- Platform gateway returning `    503` errors because the service is too busy to respond to health checks


A WebSocket service is deployed alongside the API service to manage the output of the rulebook activations. Each activation maintains a persistent WebSocket connection to this service to communicate status and receive instructions. A large number of activations or a large amount of output from activations can overwhelm the WebSocket server, leading to failures.

Consider the following strategies to scale the Event-Driven Ansible API and WebSocket service:

- OpenShift Container Platform: The WebSocket server (Daphne) runs within the `    eda-api` pod. Horizontally scale the `    eda-api` deployment to scale this service.


Ensure that you scale the `eda-api` deployment in proportion to the number of activations being run.


- VM-based installation or container-based installation: Horizontally scale the WebSocket service alongside the API service by adding more hybrid nodes. This increases capacity for all Event-Driven Ansible components simultaneously.


To identify whether your deployment experienced a bottleneck in the WebSocket service, check the activation logs for the following errors:

```
ansible_rulebook.websocket - WARNING - websocket aborted by &lt;class 'websockets.exceptions.InvalidMessage'&gt;: did not receive a valid HTTP response
ansible_rulebook.cli - ERROR - Terminating: did not receive a valid HTTP response
```

