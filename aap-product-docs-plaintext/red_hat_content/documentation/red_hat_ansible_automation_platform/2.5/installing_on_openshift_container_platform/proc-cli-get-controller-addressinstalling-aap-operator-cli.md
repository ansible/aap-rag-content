# 1. Installing Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 1.4. Installing Red Hat Ansible Automation Platform Operator from the Red Hat OpenShift Container Platform CLI
### 1.4.4. Fetching the platform gateway web address




A Red Hat OpenShift Container Platform route exposes a service at a host name, so that external clients can reach it by name. When you created the platform gateway instance, a route was created for it. The route inherits the name that you assigned to the platform gateway object in the YAML file.

**Procedure**

- Use the following command to fetch the routes:


```
oc get routes -n<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;platform_namespace&gt;</span></em></span>
```

**Verification**

You can see in the following example, the `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">example</span></em></span>` platform gateway is running in the `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">ansible-automation-platform</span></em></span>` namespace.





```
$ oc get routes -n ansible-automation-platform

NAME      HOST/PORT                                              PATH   SERVICES          PORT   TERMINATION     WILDCARD
example   example-ansible-automation-platform.apps-crc.testing          example-service   http   edge/Redirect   None
```

The address for the platform gateway instance is `example-ansible-automation-platform.apps-crc.testing` .

