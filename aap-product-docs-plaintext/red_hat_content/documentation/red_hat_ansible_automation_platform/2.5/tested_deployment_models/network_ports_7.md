# 4. Operator topologies
## 4.1. Operator growth topology
### 4.1.5. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server for it to work. Ensure that these ports are available and are not blocked by the server firewall.


<span id="idm139891621644112"></span>
**Table 4.3. Network ports and protocols**

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | HTTP/HTTPS | Receptor | Execution node | OpenShift Container Platform ingress |
| 80/443 | HTTP/HTTPS | Receptor | Hop node | OpenShift Container Platform ingress |
| 80/443 | HTTP/HTTPS | Platform | Customer clients | OpenShift Container Platform ingress |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Execution node |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Hop node |




