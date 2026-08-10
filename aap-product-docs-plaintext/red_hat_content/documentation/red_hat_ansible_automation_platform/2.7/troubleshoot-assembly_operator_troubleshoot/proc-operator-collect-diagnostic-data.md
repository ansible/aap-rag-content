# Troubleshoot your Operator-based deployment of Ansible Automation Platform
## Collect diagnostic data

Use the `oc adm must-gather` command to collect comprehensive diagnostic data about your cluster and the Ansible Automation Platform components. This data is essential when contacting Red Hat Support.

### Procedure

1.  To start the `must-gather` tool, run:


```
oc adm must-gather --image=registry.redhat.io/<platform-version>/aap-must-gather-rhel<rhel-version>
```

2.  View the collected data, use the `omc` tool to query the `must-gather` tarball as if it were a live cluster.

```
omc use <path-to-must-gather>
omc get pods
```
