# Scale up to an enterprise topology
## Key performance indicators to guide scaling plans
### High CPU utilization

When a service’s API pod shows consistently high CPU usage, it might be unable to process incoming requests promptly. This can lead to a backlog of requests. The following indicators suggest high CPU utilization:

- High total request time from the Envoy proxy logs with the processing time from the service’s WSGI logs
- High total Envoy latency
- Requests are waiting in a queue before being processed

