+++
title = "Tune automation controller to improve performance - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_controller_improving_performance"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_controller_improving_performance/", "Tune automation controller to improve performance"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_controller_improving_performance/aem-page/optimize-assembly_controller_improving_performance.html"
last_crumb = "Tune automation controller to improve performance"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Tune automation controller to improve performance"
oversized = "false"
page_slug = "optimize-assembly_controller_improving_performance"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-assembly_controller_improving_performance"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_controller_improving_performance/toc/toc.json"
type = "aem-page"
+++

# Tune automation controller to improve performance

Tune your automation controller to optimize performance and scalability. When planning your workload, ensure that you identify your performance and scaling needs, adjust for any limitations, and monitor your deployment.

Automation controller is a distributed system with many components that you can tune, including the following:

- Task system in charge of scheduling jobs
- Control Plane in charge of controlling jobs and processing output
- Execution plane where jobs run
- Web server in charge of serving the API
- WebSocket system that serve and broadcast WebSocket connections and data
- Database used by many components

## Configure WebSocket load balancing

You can configure automation controller to align the WebSocket configuration with your nginx or load balancer configuration.

Automation controller nodes are interconnected through WebSockets to distribute all WebSocket-emitted messages throughout your system. This configuration setup enables any browser client WebsSocket to subscribe to any job that might be running on any automation controller node. WebSocket clients are not routed to specific automation controller nodes. Instead, any automation controller node can handle any WebSocket request and each automation controller node must know about all WebSocket messages destined for all clients.

You can configure WebSockets at `/etc/tower/conf.d/websocket_config.py` in all of your automation controller nodes and the changes become effective after the service restarts.

Automation controller automatically handles discovery of other automation controller nodes through the Instance record in the database.

Important:

Your automation controller nodes are designed to broadcast WebSocket traffic across a private, trusted subnet (and not the open Internet). Therefore, if you turn off HTTPS for WebSocket broadcasting, the WebSocket traffic, composed mostly of Ansible Playbook stdout, is sent unencrypted between automation controller nodes.

### Configure automatic discovery of other automation controller nodes

You can configure WebsSocket connections to enable automation controller to automatically handle discovery of other automation controller nodes through the Instance record in the database.

#### Procedure

1.  Edit automation controller WebSocket information for port and protocol, and confirm whether to verify certificates with `True` or `False` when establishing the WebSocket connections:
  

```
BROADCAST_WEBSOCKET_PROTOCOL = 'http'
BROADCAST_WEBSOCKET_PORT = 80
BROADCAST_WEBSOCKET_VERIFY_CERT = False
```

2.  Restart automation controller with the following command:
  

```
$ automation-controller-service restart
```
