# Network ports and protocols
## Automation mesh node requirements
### Network ports

Automation mesh uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 1. Network ports and protocols*

| Port number | Protocol   | Service  | Source                               | Destination                               |
| ----------- | ---------- | -------- | ------------------------------------ | ----------------------------------------- |
| 80/443      | HTTP/HTTPS | Receptor | Execution node                       | OpenShift Container Platform mesh ingress |
| 80/443      | HTTP/HTTPS | Receptor | Hop node                             | OpenShift Container Platform mesh ingress |
| 27199       | TCP        | Receptor | OpenShift Container Platform cluster | Execution node                            |
| 27199       | TCP        | Receptor | OpenShift Container Platform cluster | Hop node                                  |
