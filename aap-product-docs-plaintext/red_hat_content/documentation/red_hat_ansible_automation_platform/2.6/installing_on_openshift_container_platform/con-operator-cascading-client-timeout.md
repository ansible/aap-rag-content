# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.1. Configuring platform gateway on Red Hat OpenShift Container Platform web console
### 5.1.7. Cascading client timeouts




Cascading timeouts ensure that if an outer layer of the system times out, inner processes also terminate to prevent resource exhaustion from orphaned requests.

Set the primary timeout at the Gateway level to allow Ansible Automation Platform to synchronize timeouts automatically across component applications.

#### 5.1.7.1. Timeout relationships




The `client_request_timeout` serves as the primary value. Internal layers follow this logic:

- The sum of the Envoy `    request_timeout` and the gRPC authentication timeout ( `    gateway_grpc_auth_service_timeout` ) must be less than the `    client_request_timeout` .
- The Nginx read timeout ( `    nginx_read_timeout` ) must be less than or equal to the Envoy `    request_timeout` .
- The Python web server timeout ( `    python_webserver_timeout` ) must be less than or equal to the `    nginx_read_timeout` .


#### 5.1.7.2. Timeout grace periods




At the uWSGI layer, the `uwsgi_timeout_grace_period` allows the application to attempt a graceful shutdown. During this period, the application displays a traceback of the current stack position. If the process does not exit within the grace period, Ansible Automation Platform terminates it.

