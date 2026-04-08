# 5. Advanced containerized deployment
## 5.4. Configuring a HAProxy load balancer




To configure a HAProxy load balancer in front of platform gateway with a custom CA cert, set the following inventory file variables under the `[all:vars]` group:

```
custom_ca_cert=&lt;path_to_cert_crt&gt;
gateway_main_url=&lt;https://load_balancer_url&gt;
```

Important
- Ensure your load balancer is configured to use HTTP/1.1 when communicating with platform gateway. HTTP/2 is not supported.
- HAProxy SSL passthrough mode is not supported with platform gateway.




