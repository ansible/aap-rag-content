# Chapter 10. Metrics




A metrics endpoint, `/api/controller/v2/metrics/` is available in the API that produces instantaneous metrics about automation controller, which can be consumed by system monitoring software such as the open source project Prometheus.

The types of data shown at the `metrics/` endpoint are `Content-type: text/plain` and `application/json` .

This endpoint has useful information, such as counts of how many active user sessions there are, or how many jobs are actively running on each automation controller node.

You can configure Prometheus to scrape these metrics from automation controller by hitting the automation controller metrics endpoint and storing this data in a time-series database.

Clients can later use Prometheus in conjunction with other software such as Grafana or Metricbeat to visualize that data and set up alerts.

