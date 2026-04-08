# 3. Configuring Ansible Automation Platform to use egress proxy
## 3.8. Configure operator-based Ansible Automation Platform to use egress proxy
### 3.8.1. Modification for a deployed instance




The configuration is stored as a ConfigMap resource. See it in the **OCP console > ConfigMaps > <instancename>-automationcontroller-configmap** .

To modify the settings after deployment, use the Operator.

After editing `extra_settings` , perform the deployment again. Go to **OCP console > Deployments > your instance > Decrease the Pod count > Increase the Pod count** . You can also redeploy it in the command line utility as follows:

```
$ oc scale --replicas=0 deployment.apps/&lt;instancename&gt; -n ansible-automation-platform deployment.apps/&lt;instancename&gt; scaled
$ oc scale --replicas=1 deployment.apps/&lt;instancename&gt; -n ansible-automation-platform deployment.apps/&lt;instancename&gt; scaled
```

**Verification**

See the settings in the Web UI at **Settings > Jobs settings > Extra Environment Variables** . If you need to set another value, you can define it in the same way. `extra_settings` settings is stored statically in the `/etc/tower/settings.py` file in the `automationcontroller` instance


