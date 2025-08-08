# 4. Troubleshooting
## 4.1. Automation controller custom resource has the same name as an existing deployment




The name specified for the new AutomationController custom resource must not match an existing deployment or the recovery process will fail.

If your AutomationController customer resource matches an existing deployment, perform the following steps to resolve the issue.

**Procedure**

1. Delete the existing AutomationController and the associated postgres PVC:


```
oc delete automationcontroller &lt;YOUR_DEPLOYMENT_NAME&gt; -n &lt;YOUR_NAMESPACE&gt;        oc delete pvc postgres-13-&lt;YOUR_DEPLOYMENT_NAME&gt;-13-0 -n &lt;YOUR_NAMESPACE&gt;
```


1. Use AutomationControllerRestore with the same deployment_name in it:


```
oc apply -f restore.yaml
```





<span id="idm139856908708624"></span>
