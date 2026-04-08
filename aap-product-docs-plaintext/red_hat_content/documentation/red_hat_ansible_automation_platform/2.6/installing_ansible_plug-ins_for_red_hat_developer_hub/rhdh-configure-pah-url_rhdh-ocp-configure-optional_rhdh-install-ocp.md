# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.5. Optional configuration for Ansible plug-ins
### 2.5.4. Configuring the private automation hub URL




Private automation hub provides a centralized, on-premise repository for certified Ansible collections, execution environments and any additional, vetted content provided by your organization.

If the private automation hub URL is not configured in the Ansible plug-ins, users are redirected to the [Red Hat Hybrid Cloud Console automation hub](https://console.redhat.com/ansible/automation-hub) .

Note
The private automation hub configuration is optional but recommended. The Ansible plug-ins will function without it.



**Prerequisites**

- You have a private automation hub instance. For more information, see [Ansible Automation Platform documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6) .


**Procedure**

1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.


```
data:      app-config-rhdh.yaml: |-        ansible:        ...          automationHub:            baseUrl: '&lt;https://MyOwnPAHUrl&gt;'        ...
```


1. Replace `    &lt;https://MyOwnPAHUrl/&gt;` with your private automation hub URL.
1. In the OpenShift Developer UI, select the `    Red Hat Developer Hub` pod.
1. Open **Actions** .
1. Click **Restart rollout** .


