# Scale up to an enterprise topology
## Scale the automation controller API service
### Key performance indicators

Key performance indicators for the automation controller API service include the following:

- High API latency for requests under `/api/controller`
- High CPU utilization on the API pods or nodes
- Platform gateway returning `503` errors because the service is too busy to respond to health checks


The automation controller API service is located in web pods on operator-based installation and in control or hybrid nodes on VM-based installation or container-based installation.

