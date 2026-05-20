# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.3. Configuring automation hub on Red Hat OpenShift Container Platform web console
### 5.3.6. Adding allowed registries to the automation controller image configuration

Before you can deploy a container image in automation hub, you must add the registry to the `allowedRegistries` in the automation controller image configuration. To do this you can copy and paste the following code into your automation controller image YAML.

**Procedure**

1. Log in to **Red Hat OpenShift Container Platform**.

2. Navigate to Home → Search.

3. Select the **Resources** drop-down list and type "Image".

4. Select **Image (config,openshift.io/v1)**.

5. Click Cluster under the **Name** heading.

6. Select the YAML tab.

7. Paste in the following under spec value:

spec:
registrySources:
allowedRegistries:
- quay.io
- registry.redhat.io
- image-registry.openshift-image-registry.svc:5000
- <OCP route for your automation hub>

8. Click Save.

