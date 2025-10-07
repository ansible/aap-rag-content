# 3. Installing the Ansible plug-ins with the Operator on OpenShift Container Platform
## 3.12. Optional configuration for Ansible plug-ins
### 3.12.2. Configuring Ansible plug-ins optional integrations




The Ansible plug-ins provide integrations with Ansible Automation Platform and other optional Red Hat products.

To edit your custom ConfigMap, log in to the OpenShift UI and navigate toSelect Project ( developerHubProj )→ConfigMaps→{developer-hub}-app-config-rhdh→app-config-rhdh.

#### 3.12.2.1. Configuring OpenShift Dev Spaces




When OpenShift Dev Spaces is configured for the Ansible plug-ins, users can click a link from the catalog item view in Red Hat Developer Hub and edit their provisioned Ansible Git projects using Dev Spaces.

Note
OpenShift Dev Spaces is a separate product and it is optional. The plug-ins will function without it.

It is a separate Red Hat product and is not included in the Ansible Automation Platform or Red Hat Developer Hub subscription.



If the OpenShift Dev Spaces link is not configured in the Ansible plug-ins, the **Go to OpenShift Dev Spaces dashboard** link in the **DEVELOP** section of the Ansible plug-ins landing page redirects users to the [Ansible development tools home page](https://www.redhat.com/en/technologies/management/ansible/development-tools) .

**Prerequisites**

- A Dev Spaces installation. Refer to the [Installing Dev Spaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.14/html-single/administration_guide/installing-devspaces) section of the _Red Hat OpenShift Dev Spaces Administration guide_ .


**Procedure**

1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.


```
data:      app-config-rhdh.yaml: |-        ansible:          devSpaces:            baseUrl: &gt;-              https://&lt;Your OpenShift Dev Spaces URL&gt;
```


1. Replace `    &lt;Your OpenShft Dev Spaces URL&gt;` with your OpenShift Dev Spaces URL.
1. In the OpenShift Developer UI, select the `    Red Hat Developer Hub` pod.
1. Open **Actions** .
1. Click **Restart rollout** .


#### 3.12.2.2. Configuring the private automation hub URL




Private automation hub provides a centralized, on-premise repository for certified Ansible collections, execution environments and any additional, vetted content provided by your organization.

If the private automation hub URL is not configured in the Ansible plug-ins, users are redirected to the [Red Hat Hybrid Cloud Console automation hub](https://console.redhat.com/ansible/automation-hub) .

Note
The private automation hub configuration is optional but recommended. The Ansible plug-ins will function without it.



**Prerequisites**

- A private automation hub instance.

For more information on installing private automation hub, refer to the installation guides in the [Ansible Automation Platform documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5) .




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


