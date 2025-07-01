# 7. Known issues
## 7.2. Event-Driven Ansible




- mTLS event stream creation should be disallowed on all installation methods by default. It is currently disallowed on OpenShift Container Platform installation, but not disallowed in the containerized installations or on RPM installations. (AAP-31337)
- If a primary Redis node enters a `    failed` state and a new primary node is promoted, Event-Driven Ansible workers and scheduler are unable to reconnect to the cluster. This causes activations to fail until the containers or pods are recycled. (AAP-30722)
For more information, see the KCS article [Redis failover causes Event-Driven Ansible activation failures](https://access.redhat.com/articles/7088545) .


