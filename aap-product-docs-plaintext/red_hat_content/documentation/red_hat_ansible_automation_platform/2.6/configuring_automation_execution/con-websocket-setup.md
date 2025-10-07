# 3. Performance tuning for automation controller
## 3.1. Websocket configuration for automation controller




You can configure automation controller to align the websocket configuration with your nginx or load balancer configuration.

Automation controller nodes are interconnected through websockets to distribute all websocket-emitted messages throughout your system. This configuration setup enables any browser client websocket to subscribe to any job that might be running on any automation controller node. Websocket clients are not routed to specific automation controller nodes. Instead, any automation controller node can handle any websocket request and each automation controller node must know about all websocket messages destined for all clients.

You can configure websockets at `/etc/tower/conf.d/websocket_config.py` in all of your automation controller nodes and the changes become effective after the service restarts.

Automation controller automatically handles discovery of other automation controller nodes through the Instance record in the database.

Important
Your automation controller nodes are designed to broadcast websocket traffic across a private, trusted subnet (and not the open Internet). Therefore, if you turn off HTTPS for websocket broadcasting, the websocket traffic, composed mostly of Ansible Playbook stdout, is sent unencrypted between automation controller nodes.



