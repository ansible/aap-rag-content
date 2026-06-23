# Scale up to an enterprise topology
## Key performance indicators to guide scaling plans
### High API latency

Sustained high latency on API requests is a key performance indicator. All requests are made through the platform platform gateway, which acts as a proxy and forwards requests to the services in question. The request is sent to the destination service depending on which route is in the URL of the API request:

- platform gateway: `/api/gateway`
- automation controller: `/api/controller`
- Event-Driven Ansible: `/api/eda`
- Event-Driven Ansible Event Streams: `/eda-event-streams/api/eda/v1/external_event_stream/`
- automation hub: `/api/galaxy`


Monitoring latency on the different routes through the Envoy proxy logs helps you identify which service requires scaling. These routes are present in the proxy container of platform gateway pods in OpenShift Container Platform. For VM-based installation and container-based installation installations, check the proxy logs of the platform gateway nodes. Exceeding target API thresholds (for example, 99th percentile >1500ms) indicates a need to trigger alerts. You might also need to scale web services.

