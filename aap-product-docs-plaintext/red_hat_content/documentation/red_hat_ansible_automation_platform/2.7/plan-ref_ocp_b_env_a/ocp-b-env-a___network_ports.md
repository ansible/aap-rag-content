# Operator enterprise topology
## Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 5. Network ports and protocols*

| Port number | Protocol       | Service            | Source                                   | Destination                                                                                     |
| ----------- | -------------- | ------------------ | ---------------------------------------- | ----------------------------------------------------------------------------------------------- |
| <br>80/443  | <br>HTTP/HTTPS | <br>Object storage | <br>OpenShift Container Platform cluster | <br>External object storage service                                                             |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor       | <br>Execution node                       | <br>OpenShift Container Platform ingress                                                        |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor       | <br>Hop node                             | <br>OpenShift Container Platform ingress                                                        |
| <br>5432    | <br>TCP        | <br>PostgreSQL     | <br>OpenShift Container Platform cluster | <br>External database service                                                                   |
| <br>5432    | <br>TCP        | <br>PostgreSQL     | <br>OpenShift Container Platform cluster | <br>External database service (`metrics_service` database)                                      |
| <br>5432    | <br>TCP        | <br>PostgreSQL     | <br>OpenShift Container Platform cluster | <br>External database service (`automationcontroller` database - read-only for metrics service) |
| <br>6379    | <br>TCP        | <br>Redis          | <br>OpenShift Container Platform cluster | <br>External Redis service                                                                      |
| <br>27199   | <br>TCP        | <br>Receptor       | <br>OpenShift Container Platform cluster | <br>Execution node                                                                              |
| <br>27199   | <br>TCP        | <br>Receptor       | <br>OpenShift Container Platform cluster | <br>Hop node                                                                                    |


Note:

Metrics service pods communicate internally within the OpenShift cluster via the platform gateway. The `/api/metrics/` path is routed through the standard Ansible Automation Platform gateway and does not require a separate external ingress. Metrics service requires outbound connectivity on port 5432 to both the `metrics_service` database and the `automationcontroller` database (read-only).
