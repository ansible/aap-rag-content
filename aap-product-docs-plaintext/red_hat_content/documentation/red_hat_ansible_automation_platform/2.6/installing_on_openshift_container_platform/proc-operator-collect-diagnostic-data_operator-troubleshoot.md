# 14. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 14.9. Collecting Diagnostic Data




Use the `oc adm must-gather` command to collect comprehensive diagnostic data about your cluster and the Ansible Automation Platform components. This data is essential when contacting Red Hat Support.

**Procedure**

1. To start the `    must-gather` tool, run:


```
oc adm must-gather --image=registry.redhat.io/ansible-automation-platform-26/aap-must-gather-rhel9
```

Note
For version 2.6, the base image name changes to `    registry.redhat.io/ansible-automation-platform-26/aap-must-gather-rhel9` .




1. View the collected data, use the `    omc` tool to query the `    must-gather` tarball as if it were a live cluster.


```
omc use &lt;path-to-must-gather&gt;    omc get pods
```




**Additional resources**

-  [How to collect diagnostics data from Ansible Automation Platform running on OpenShift?](https://access.redhat.com/solutions/6997224)
-  [How to generate a sos report within nodes without SSH in OpenShift Container Platform 4](https://access.redhat.com/solutions/4387261)


