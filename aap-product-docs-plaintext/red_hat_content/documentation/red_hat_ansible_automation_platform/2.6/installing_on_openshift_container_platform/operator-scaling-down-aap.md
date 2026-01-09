# Chapter 8. Scaling down Red Hat Ansible Automation Platform Operator deployments




You can scale down all Ansible Automation Platform deployments and StatefulSets by using the `idle_aap` variable. This is useful for scenarios such as upgrades, migrations, or disaster recovery.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Go toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select **All Instances** and go to your **AnsibleAutomationPlatform** instance.
1. Click the **⋮** icon and then selectEdit AnsibleAutomationPlatform.
1. In the **YAML view** paste the following YAML code under the `    spec:` section:


```
idle_aap: true
```


1. ClickSave.


**Next steps**

Setting the `idle_aap` value to `true` scales down all active deployments. Setting the value to `false` scales the deployments back up.


