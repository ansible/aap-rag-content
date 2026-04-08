# 3. API service performance
## 3.5. Considerations for scaling the Event-Driven Ansible APIs
### 3.5.2. Event-Driven Ansible EventStream service




The Event Stream API, which handles POST requests to `/api/eda-event-stream` , is a separate `Gunicorn` service designed to import events from external sources. If this service’s performance degrades, with high latency, low throughput, or availability issues, you must scale it. The platform gateway returns `503` errors for this service when a pod is too busy to respond to health checks in time.

Consider the following strategies to scale the Event-Driven Ansible EventStream service:

- OpenShift Container Platform: Horizontally scale up the dedicated `    eda-event-stream` worker deployment, because it is managed separately from the main `    eda-api deployment` .
- VM-based installation or container-based installation: Horizontally scale up this service by adding more hybrid nodes, which increases capacity for all Event-Driven Ansible components simultaneously.


