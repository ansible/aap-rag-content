# 2. Ansible Automation Platform containerized installation
## 2.7. Advanced configuration options
### 2.7.4. Configuring a HAProxy load balancer




To configure a HAProxy load balancer in front of platform gateway with a custom CA cert, set the following inventory file variables under the `[all:vars]` group:

```
custom_ca_cert=&lt;path_to_cert_crt&gt;
gateway_main_url=&lt;https://load_balancer_url&gt;
```

Note
HAProxy SSL passthrough mode is not supported with platform gateway.



