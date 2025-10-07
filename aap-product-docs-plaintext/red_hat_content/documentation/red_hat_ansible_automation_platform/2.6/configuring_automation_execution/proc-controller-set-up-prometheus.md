# 10. Metrics
## 10.1. Setting up Prometheus




To set up and use Prometheus, you must install Prometheus on a virtual machine or container.

For more information, see the [First steps with Prometheus](https://prometheus.io/docs/introduction/first_steps/) documentation.

**Procedure**

1. In the Prometheus configuration file (typically `    prometheus.yml` ), specify a `    &lt;token_value&gt;` , a valid username and password for an automation controller user that you have created, and a `    &lt;controller_host&gt;` .

Note
Alternatively, you can provide an OAuth2 token (which can be generated at `    /api/v2/users/N/personal_tokens/` ). By default, the configuration assumes a user with username= `    admin` and password= `    password` .



Using an OAuth2 Token, created at the `    /api/v2/tokens` endpoint to authenticate Prometheus with automation controller, the following example provides a valid scrape configuration if the URL for your automation controller’s metrics endpoint is `    /https://controller_host:443/metrics` .


```
scrape_configs          - job_name: 'controller'        tls_config:            insecure_skip_verify: True        metrics_path: /api/v2/metrics        scrape_interval: 5s        scheme: https        bearer_token: &lt;token_value&gt;        # basic_auth:        #   username: admin        #   password: password        static_configs:            - targets:                - &lt;controller_host&gt;
```

For help configuring other aspects of Prometheus, such as alerts and service discovery configurations, see the [Prometheus configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/) documentation.

If Prometheus is already running, you must restart it to apply the configuration changes by making a **POST** to the reload endpoint, or by killing the Prometheus process or service.


1. Use a browser to navigate to your graph in the Prometheus UI at `    /http://&lt;your_prometheus&gt;:9090/graph` and test out some queries. For example, you can query the current number of active automation controller user sessions by executing: `    awx_sessions_total{type="user"}` .

![Prometheus queries](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/8e53f42bb637438071625b985c2b9a67/metrics-prometheus-ui-query-example.png)





**Next steps**

Refer to the metrics endpoint in the automation controller API for your instance ( `api/v2/metrics` ) for more ways to query.


