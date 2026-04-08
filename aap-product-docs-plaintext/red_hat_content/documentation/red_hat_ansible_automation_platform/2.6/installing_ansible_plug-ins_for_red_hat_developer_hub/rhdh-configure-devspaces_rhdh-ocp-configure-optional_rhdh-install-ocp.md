# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.5. Optional configuration for Ansible plug-ins
### 2.5.3. Configuring OpenShift Dev Spaces




When OpenShift Dev Spaces is configured for the Ansible plug-ins, users can click a link from the catalog item view in Red Hat Developer Hub and edit their provisioned Ansible Git projects using Dev Spaces.

Note
OpenShift Dev Spaces is a separate product and it is optional. The plug-ins will function without it.

It is a separate Red Hat product and is not included in the Ansible Automation Platform or Red Hat Developer Hub subscription.



If the OpenShift Dev Spaces link is not configured in the Ansible plug-ins, the **Go to OpenShift Dev Spaces dashboard** link in the **DEVELOP** section of the Ansible plug-ins landing page redirects users to the [Ansible development tools home page](https://www.redhat.com/en/technologies/management/ansible/development-tools) .

**Prerequisites**

- You have a Dev Spaces installation. For more details, see [Installing Dev Spaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.14/html-single/administration_guide/installing-devspaces) .


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


