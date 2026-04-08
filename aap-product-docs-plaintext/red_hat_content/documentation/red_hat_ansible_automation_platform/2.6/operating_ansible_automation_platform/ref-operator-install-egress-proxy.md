# 3. Configuring Ansible Automation Platform to use egress proxy
## 3.8. Configure operator-based Ansible Automation Platform to use egress proxy




When installing Ansible Automation Platform using the operator-based installation method, you can configure the platform to use an egress proxy.

When creating an `automationcontroller` instance, select the YAML view and add `extra_settings` in the spec definition as the `AWX_TASK_ENV` parameter for the proxy settings, as follows:

+

```
apiVersion: automationcontroller.ansible.com/v1beta1
kind: AutomationController
metadata:
name: example
namespace: ansible-automation-platform
spec:
create_preload_data: true
route_tls_termination_mechanism: Edge
garbage_collect_secrets: false
ingress_type: Route
loadbalancer_port: 80
no_log: true
image_pull_policy: IfNotPresent
projects_storage_size: 8Gi
auto_upgrade: true
task_privileged: false
projects_storage_access_mode: ReadWriteMany
set_self_labels: true
projects_persistence: false
replicas: 1
admin_user: admin
loadbalancer_protocol: http
nodeport_port: 30080
extra_settings:
- setting: AWX_TASK_ENV
value:
HTTPS_PROXY: 'https://192.168.0.XXX:3128'
HTTP_PROXY: 'https://192.168.0.XXX:3128'
NO_PROXY: 10.0.0.0/8
http_proxy: 'https://192.168.0.XXX:3128'
https_proxy: 'https://192.168.0.XXX:3128'
no_proxy: 10.0.0.0/8
```

