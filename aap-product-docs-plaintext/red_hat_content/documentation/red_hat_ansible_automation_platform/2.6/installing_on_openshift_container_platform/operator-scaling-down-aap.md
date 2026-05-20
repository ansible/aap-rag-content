# Chapter 8. Scaling down Red Hat Ansible Automation Platform Operator deployments

You can scale down all Ansible Automation Platform deployments and StatefulSets by using the `idle_aap` variable. This is useful for scenarios such as upgrades, migrations, or disaster recovery.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.

2. Go to Operators → Installed Operators.

3. Select your Ansible Automation Platform Operator deployment.

4. Select **All Instances** and go to your **AnsibleAutomationPlatform** instance.

5. Click the **⋮** icon and then select Edit AnsibleAutomationPlatform.

6. In the **YAML view** paste the following YAML code under the `spec:` section:

idle_aap: true

7. Click Save.

**Next steps**

Setting the `idle_aap` value to `true` scales down all active deployments. Setting the value to `false` scales the deployments back up.

