# 13. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 13.10. Debugging crashing pods




If a pod is failing or crashing, use the `oc debug` command. This command creates a new pod with the same configuration and mounts as the pod you specified, allowing you to access it for debugging.

**Procedure**

- To connect to the pod, run:


```
oc debug &lt;pod-name&gt;
```




