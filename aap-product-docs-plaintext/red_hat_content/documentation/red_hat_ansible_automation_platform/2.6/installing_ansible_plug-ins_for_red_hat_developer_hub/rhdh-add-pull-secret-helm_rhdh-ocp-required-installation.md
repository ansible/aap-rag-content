# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.4. Required configuration
### 2.4.2. Adding a pull secret to the Red Hat Developer Hub Helm configuration




You must add a pull secret to the Red Hat Developer Hub Helm configuration to enable the dynamic plug-ins to pull container images from authenticated registries.

**Prerequisite**

- You have a Red Hat Customer Portal account and Red Hat Service Registry account.


**Procedure**

1. Create a new [Red Hat Registry Service account](https://access.redhat.com/terms-based-registry/) , if required.
1. Click the token name under the **Account name** column.
1. Select the **OpenShift Secret** tab and follow the instructions to add the pull secret to your Red Hat Developer Hub OpenShift project.
1. Add the new secret to the Red Hat Developer Hub Helm configuration, replacing `    &lt;your-redhat-registry-pull-secret&gt;` with the name of the secret you generated on the Red Hat Registry Service Account website:


```
upstream:      backstage:        ...        image:          ...          pullSecrets:            - &lt;your-redhat-registry-pull-secret&gt;        ...
```




**Additional resources**

-  [Red Hat Container Registry documentation](https://access.redhat.com/RegistryAuthentication)


