# 3. Operator topologies
## 3.2. Operator enterprise topology
### 3.2.5. Network ports




Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.


<span id="idm140186614855696"></span>
**Table 3.6. Network ports and protocols**

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | HTTP/HTTPS | Object storage | OpenShift Container Platform cluster | External object storage service |
| 80/443 | HTTP/HTTPS | Receptor | Execution node | OpenShift Container Platform ingress |
| 80/443 | HTTP/HTTPS | Receptor | Hop node | OpenShift Container Platform ingress |
| 5432 | TCP | PostgreSQL | OpenShift Container Platform cluster | External database service |
| 6379 | TCP | Redis | OpenShift Container Platform cluster | External Redis service |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Execution node |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Hop node |




