# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.5. Required configuration
### 2.5.2. Adding the Ansible Development Tools sidecar container




After the plug-ins are loaded, add the Ansible Development Container ( `ansible-devtools-server` ) in the Red Hat Developer Hub pod as a sidecar container.

#### 2.5.2.1. Adding a pull secret to the Red Hat Developer Hub Helm configuration




**Prerequisite**

The Ansible Development Container download requires a Red Hat Customer Portal account and Red Hat Service Registry account.


**Procedure**

1. Create a new [Red Hat Registry Service account](https://access.redhat.com/terms-based-registry/) , if required.
1. Click the token name under the **Account name** column.
1. Select the **OpenShift Secret** tab and follow the instructions to add the pull secret to your Red Hat Developer Hub OpenShift project.
1. Add the new secret to the Red Hat Developer Hub Helm configuration, replacing `    &lt;your-redhat-registry-pull-secret&gt;` with the name of the secret you generated on the Red Hat Registry Service Account website:


```
upstream:      backstage:        ...        image:          ...          pullSecrets:            - &lt;your-redhat-registry-pull-secret&gt;        ...
```




For more information, refer to the [Red Hat Container Registry documentation](https://access.redhat.com/RegistryAuthentication) .

#### 2.5.2.2. Adding the Ansible Developer Tools container




You must update the Helm chart configuration to add an extra container.

**Procedure**

1. Log in to the OpenShift UI.
1. Navigate toHelm→developer-hub→Actions→upgrade→Yaml viewto open the Helm chart.
1. Update the `    extraContainers` section in the YAML file.

Add the following code:


```
upstream:      backstage:        ...        extraContainers:          - command:              - adt              - server            image: &gt;-              registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest            imagePullPolicy: IfNotPresent            name: ansible-devtools-server            ports:              - containerPort: 8000        ...
```

Note
The image pull policy is `    imagePullPolicy: IfNotPresent` . The image is pulled only if it does not already exist on the node. Update it to `    imagePullPolicy: Always` if you always want to use the latest image.




1. ClickUpgrade.


**Verification**

To verify that the container is running, check the container log:


![View container log](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_Ansible_plug-ins_for_Red_Hat_Developer_Hub-en-US/images/6abd3ad41671a23156c96a0710df0fe8/rhdh-check-devtools-container.png)


