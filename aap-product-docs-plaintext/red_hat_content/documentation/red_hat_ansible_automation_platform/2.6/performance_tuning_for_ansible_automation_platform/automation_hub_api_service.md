# 3. API service performance
## 3.6. Considerations for scaling the automation hub APIs
### 3.6.1. Automation hub API service




The automation hub API service handles metadata-driven requests for the application, including UI interactions, searches, and remote repository configuration. Key performance indicators for the automation hub API service include:

- High API latency for requests under `    /api/galaxy`
- High CPU utilization on the API pods or nodes
- Platform gateway returning `    503` errors because the service is too busy to respond to health checks


Consider the following strategies to scale the automaton automation hub API service:

- OpenShift Container Platform: Horizontally scale the API pods by increasing the `    hub.api.replicas` attribute on the `    AnsibleAutomationPlatform` Custom Resource (CR).
- VM-based installation or container-based installation: Horizontally scale the API service by adding more automation hub nodes, which simultaneously scales all other automation hub services.


