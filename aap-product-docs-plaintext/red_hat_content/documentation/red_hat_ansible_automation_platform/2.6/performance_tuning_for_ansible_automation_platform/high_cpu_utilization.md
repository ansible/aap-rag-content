# 3. API service performance
## 3.2. Key performance indicators for scaling the API services
### 3.2.2. High CPU utilization




When a service’s API pod shows consistently high CPU usage, it might be unable to process incoming requests in a timely manner, leading to a backlog of requests. The following indicators suggest high CPU utilization:

- High total request time from the Envoy proxy logs with the processing time from the service’s WSGI logs
- High total Envoy latency
- Requests are waiting in a queue before being processed


