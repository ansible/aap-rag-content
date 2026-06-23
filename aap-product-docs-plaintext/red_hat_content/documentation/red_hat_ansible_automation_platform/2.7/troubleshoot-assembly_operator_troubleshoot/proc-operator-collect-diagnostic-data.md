# Troubleshoot your Operator-based deployment of Ansible Automation Platform
## Collect diagnostic data

Use the `oc adm must-gather` command to collect comprehensive diagnostic data about your cluster and the Ansible Automation Platform components. This data is essential when contacting Red Hat Support.

### Procedure

1.  To start the `must-gather` tool, run:


```
oc adm must-gather --image=registry.redhat.io/ansible-automation-platform-25/aap-must-gather-rhel8
```
Note:
For version 2.6, the base image name changes to `registry.redhat.io/ansible-automation-platform-26/aap-must-gather-rhel9`.

2.  View the collected data, use the `omc` tool to query the `must-gather` tarball as if it were a live cluster.

```
omc use <path-to-must-gather>
omc get pods
```
