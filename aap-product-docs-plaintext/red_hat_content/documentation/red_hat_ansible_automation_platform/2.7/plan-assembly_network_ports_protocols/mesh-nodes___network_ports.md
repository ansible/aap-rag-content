# Network ports and protocols
## Automation mesh node requirements
### Network ports

Automation mesh uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 1. Network ports and protocols*

| Port number | Protocol       | Service      | Source                                   | Destination                                   |
| ----------- | -------------- | ------------ | ---------------------------------------- | --------------------------------------------- |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor | <br>Execution node                       | <br>OpenShift Container Platform mesh ingress |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor | <br>Hop node                             | <br>OpenShift Container Platform mesh ingress |
| <br>27199   | <br>TCP        | <br>Receptor | <br>OpenShift Container Platform cluster | <br>Execution node                            |
| <br>27199   | <br>TCP        | <br>Receptor | <br>OpenShift Container Platform cluster | <br>Hop node                                  |
