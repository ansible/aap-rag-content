# Scale down your Ansible Automation Platform Operator deployment

You can scale down all Ansible Automation Platform deployments and StatefulSets by using the `idle_aap` variable. This is useful for scenarios such as upgrades, migrations, or disaster recovery.

## About this task

## Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Go to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select **All Instances** and go to your **AnsibleAutomationPlatform** instance.
5.  Click the **⋮** icon and then select Edit AnsibleAutomationPlatform.
6.  In the **YAML view** paste the following YAML code under the `spec:` section:


```
idle_aap: true
```

7.  Click Save.

## What to do next

Setting the `idle_aap` value to `true` scales down all active deployments. Setting the value to `false` scales the deployments back up.
