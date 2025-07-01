# 2. Red Hat Ansible Automation Platform Service on AWS PULL and PUSH models
## 2.2. PULL connectivity




Remote automation mesh nodes can access Ansible Automation Platform using a 'polling' or 'pull' model, which does not require opening ingress ports in your enterprise network. The pull model initiates a WebSocket from the remote execution node to the control plane hop node secured with mTLS for authentication and encryption. This model eliminates the need to deploy hop nodes into your demilitarized zone (DMZ) to establish connectivity to private networks if private networks have outbound internet connectivity. Proxy servers that terminate TLS are not supported and will disrupt automation mesh connectivity.

**Figure 1 Pull model**

![Pull model](https://access.redhat.com/webassets/avalon/d/Ansible_on_Clouds-2.x-Red_Hat_Ansible_Automation_Platform_Service_on_AWS-en-US/images/54104ceb343d4fa5ca7df794ddf477da/mesh_egress.png)



