# 3. API service performance
## 3.2. Key performance indicators for scaling the API services
### 3.2.1. High API latency




Sustained high latency on API requests is a key performance indicator. All requests are made through the platform platform gateway, which acts as a proxy and forwards requests to the services in question. The request is sent to the destination service depending on which route is in the URL of the API request:

- platform gateway: `    /api/gateway`
- automation controller: `    /api/controller`
- Event-Driven Ansible: `    /api/eda`
- Event-Driven Ansible Event Streams: `    /eda-event-streams/api/eda/v1/external_event_stream/`
- automation hub: `    /api/galaxy`


Monitoring latency on the different routes through the Envoy proxy logs enables you to identify which service requires scaling. These routes are present in the proxy container of platform gateway pods in OpenShift Container Platform or in the proxy logs of the platform gateway nodes in VM-based installation and container-based installation. Latency exceeding target API thresholds (for example, 99th percentile >1500ms) indicates a need to trigger alerts or scale web services.

